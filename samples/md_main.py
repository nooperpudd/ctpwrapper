#!/usr/bin/env python3
# encoding:utf-8

"""
(Copyright) 2018, Winton Wang <365504029@qq.com>

ctpwrapper is free software: you can redistribute it and/or modify
it under the terms of the GNU LGPLv3 as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ctpwrapper.  If not, see <http://www.gnu.org/licenses/>.

"""

import socket
import sys
import urllib.parse
from contextlib import closing
import time
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
        self.is_login = False

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
        result = self.ReqUserLogin(user_login, self.request_id)
        if result == 0:
            self.is_login = True

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
            print("OnRspUserLogin failed error_id=%s msg:%s",
                  pRspInfo.ErrorID, pRspInfo.ErrorMsg.decode('gbk'))
        else:
            print("user login successfully")
            print(pRspUserLogin)
            print(pRspInfo)
            result = self.SubscribeMarketData(["v2104"])

    def OnRtnDepthMarketData(self, pDepthMarketData):
        """
        行情订阅推送信息
        :param pDepthMarketData:
        :return:
        """
        print("OnRtnDepthMarketData")
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
    server = "tcp://180.168.146.187:10131"
    app_id = "simnow_client_test"
    verify_code = "0000000000000000"

    if check_address_port(server):
        print("connect to md sever successfully")
        # 1 create
        # 2 register
        # 3 register front
        # 4 init
        md = Md(broker_id, investor_id, password)
        md.Create()

        md.Init()
        md.RegisterFront(server)
        # time.sleep(1)
        day = md.GetTradingDay()
        print(day)
        # md.ReqUserLogin()
        # md.ReqQryMulticastInstrument()

        # if result == 0:
        #     print("SubscribeMarketData success")
        # else:
        #     print("SubscribeMarketData failed")
        while True:
            print("haha")
            time.sleep(1)
        # md.Join()
        # print("join")

    else:
        print("md server is down")


if __name__ == "__main__":
    main()
