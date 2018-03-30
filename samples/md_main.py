#!/usr/bin/env python3
# encoding:utf-8

import socket
import sys
import urllib.parse
from contextlib import closing

from ctpwrapper import ApiStructure
from ctpwrapper import MdApiPy


def check_address_port(tcp):
    """
    :param tcp:
    :return:
    """
    host_schema = urllib.parse.urlparse(tcp)

    ip = host_schema.hostname
    port = host_schema.port

    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
        if sock.connect_ex((ip, port)) == 0:
            return True  # OPEN
        else:
            return False  # closed


class Md(MdApiPy):
    """
    """

    def __init__(self, broker_id, investor_id, password, request_id=1):

        self.broker_id = broker_id
        self.investor_id = investor_id
        self.password = password
        self.request_id = request_id

    def OnRspError(self, pRspInfo, nRequestID, bIsLast):

        self.ErrorRspInfo(pRspInfo, nRequestID)

    def ErrorRspInfo(self, info, request_id):
        """
        :param info:
        :return:
        """
        if info.ErrorID != 0:
            print('request_id=%s ErrorID=%d, ErrorMsg=%s',
                  request_id, info.ErrorID, info.ErrorMsg.decode('gbk'))
        return info.ErrorID != 0

    def OnFrontConnected(self):
        """
        :return:
        """

        user_login = ApiStructure.ReqUserLoginField(BrokerID=self.broker_id,
                                                    UserID=self.investor_id,
                                                    Password=self.password)
        self.ReqUserLogin(user_login, self.request_id)

    def OnFrontDisconnected(self, nReason):

        print("Md OnFrontDisconnected %s", nReason)
        sys.exit()

    def OnHeartBeatWarning(self, nTimeLapse):
        """心跳超时警告。当长时间未收到报文时，该方法被调用。
        @param nTimeLapse 距离上次接收报文的时间
        """
        print('Md OnHeartBeatWarning, time = %s', nTimeLapse)

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        """
        用户登录应答
        :param pRspUserLogin:
        :param pRspInfo:
        :param nRequestID:
        :param bIsLast:
        :return:
        """
        if pRspInfo.ErrorID != 0:
            print("Md OnRspUserLogin failed error_id=%s msg:%s",
                  pRspInfo.ErrorID, pRspInfo.ErrorMsg.decode('gbk'))
        else:
            print("Md user login successfully")
            print(pRspUserLogin)
            print(pRspInfo)

    def OnRtnDepthMarketData(self, pDepthMarketData):
        """
        行情订阅推送信息
        :param pDepthMarketData:
        :return:
        """
        market_data = pDepthMarketData.to_dict()
        print(market_data)

    def OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        """
        订阅行情应答
        :param pSpecificInstrument:
        :param pRspInfo:
        :param nRequestID:
        :param bIsLast:
        :return:
        """
        print("OnRspSubMarketData")
        print(pSpecificInstrument)
        print(pRspInfo)

    def OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        """
        取消订阅行情应答
        :param pSpecificInstrument:
        :param pRspInfo:
        :param nRequestID:
        :param bIsLast:
        :return:
        """
        print("OnRspUnSubMarketData")
        print(pSpecificInstrument)
        print(pRspInfo)


def main():
    investor_id = "089303"
    broker_id = "9999"
    password = "198759"
    server = "tcp://180.168.146.187:10011"

    if check_address_port(server):

        md = Md(broker_id, investor_id, password)
        md.Create()
        md.RegisterFront(server)
        md.Init()
        day = md.GetTradingDay()
        print(day)

        print("md_start")

        md.SubscribeMarketData(["rb1810"])
        md.Join()

    else:
        print("md server down")


if __name__ == "__main__":
    main()
