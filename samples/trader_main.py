#!/usr/bin/env python3
# encoding:utf-8

import socket
import urllib.parse
from contextlib import closing

from ctpwrapper import ApiStructure
from ctpwrapper import TraderApiPy


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


class Trader(TraderApiPy):

    def __init__(self, broker_id, investor_id, password, request_id=1):
        self.request_id = request_id
        self.broker_id = broker_id.encode()
        self.investor_id = investor_id.encode()
        self.password = password.encode()

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

    def OnHeartBeatWarning(self, nTimeLapse):
        """心跳超时警告。当长时间未收到报文时，该方法被调用。
        @param nTimeLapse 距离上次接收报文的时间
        """
        print("on OnHeartBeatWarning time: ", nTimeLapse)

    def OnFrontDisconnected(self, nReason):
        print("on FrontDisConnected disconnected", nReason)

    def OnFrontConnected(self):

        req = ApiStructure.ReqUserLoginField(BrokerID=self.broker_id,
                                             UserID=self.investor_id,
                                             Password=self.password)
        self.ReqUserLogin(req, self.request_id)
        print("trader on front connection")

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):

        if pRspInfo.ErrorID != 0:
            print("Md OnRspUserLogin failed error_id=%s msg:%s",
                  pRspInfo.ErrorID, pRspInfo.ErrorMsg.decode('gbk'))
        else:
            print("Md user login successfully")

            inv = ApiStructure.QryInvestorField(BrokerID=self.broker_id, InvestorID=self.investor_id)

            self.ReqQryInvestor(inv, self.inc_request_id())
            req = ApiStructure.SettlementInfoConfirmField.from_dict({"BrokerID": self.broker_id,
                                                                     "InvestorID": self.investor_id})

            self.ReqSettlementInfoConfirm(req, self.inc_request_id())

    def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
        print(pSettlementInfoConfirm, pRspInfo)
        print(pRspInfo.ErrorMsg.decode("GBK"))

    def inc_request_id(self):
        self.request_id += 1
        return self.request_id

    def OnRspQryInvestor(self, pInvestor, pRspInfo, nRequestID, bIsLast):
        print(pInvestor, pRspInfo)


def main():

    investor_id = "089303"
    broker_id = "9999"
    password = "198759"

    server = "tcp://180.168.146.187:10001"

    if check_address_port(server):

        user_trader = Trader(broker_id=broker_id, investor_id=investor_id, password=password)

        user_trader.Create()
        user_trader.RegisterFront(server)
        user_trader.SubscribePrivateTopic(2) # 只传送登录后的流内容
        user_trader.SubscribePrivateTopic(2) # 只传送登录后的流内容

        user_trader.Init()

        print("trader started")
        print(user_trader.GetTradingDay())

        user_trader.Join()

    else:
        print("trader server down")


if __name__ == "__main__":
    main()
