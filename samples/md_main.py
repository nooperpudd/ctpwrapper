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
import json
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

    def __init__(self, broker_id, investor_id, password, request_id=100):
        """
        """
        self.login = False
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.password = password
        self._request_id = request_id

    @property
    def request_id(self):
        self._request_id += 1
        return self._request_id

    def OnRspError(self, pRspInfo, nRequestID, bIsLast):
        print("OnRspError:")
        print("requestID:", nRequestID)
        print(pRspInfo)
        print(bIsLast)

    def OnFrontConnected(self):
        """
        :return:
        """
        user_login = ApiStructure.ReqUserLoginField(BrokerID=self.broker_id, UserID=self.investor_id, Password=self.password)
        self.ReqUserLogin(user_login, self.request_id)

    def OnFrontDisconnected(self, nReason):
        print("Md OnFrontDisconnected {0}".format(nReason))
        sys.exit()

    def OnHeartBeatWarning(self, nTimeLapse):
        """心跳超时警告。当长时间未收到报文时，该方法被调用。
        @param nTimeLapse 距离上次接收报文的时间
        """
        print('Md OnHeartBeatWarning, time = {0}'.format(nTimeLapse))

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        """
        用户登录应答
        :param pRspUserLogin:
        :param pRspInfo:
        :param nRequestID:
        :param bIsLast:
        :return:
        """
        print("OnRspUserLogin")
        print("requestID:", nRequestID)
        print("RspInfo:", pRspInfo)

        if pRspInfo.ErrorID != 0:
            print("RspInfo:", pRspInfo)
        else:
            print("user login successfully")
            print("RspUserLogin:", pRspUserLogin)
            self.login = True

    def OnRtnDepthMarketData(self, pDepthMarketData):
        """
        行情订阅推送信息
        :param pDepthMarketData:
        :return:
        """
        print("OnRtnDepthMarketData")
        print("DepthMarketData:", pDepthMarketData)

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
        print("RequestId:", nRequestID)
        print("isLast:", bIsLast)
        print("pRspInfo:", pRspInfo)
        print("pSpecificInstrument:", pSpecificInstrument)

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
        print("RequestId:", nRequestID)
        print("isLast:", bIsLast)
        print("pRspInfo:", pRspInfo)
        print("pSpecificInstrument:", pSpecificInstrument)


def main():
    json_file = open("config.json")
    config = json.load(json_file)
    json_file.close()

    investor_id = config["investor_id"]
    broker_id = config["broker_id"]
    password = config["password"]
    server = config["md_server"]

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
        time.sleep(6)

        day = md.GetTradingDay()
        print("trading day:", day)
        print("md login:", md.login)

        if md.login:
            md.SubscribeMarketData(["ru2101"])
        time.sleep(30)
        md.UnSubscribeMarketData(["ru2101"])
        md.Join()
    else:
        print("md server is down")


if __name__ == "__main__":
    main()
