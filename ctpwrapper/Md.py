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
import time
import typing
from typing import Optional

from ctpwrapper.ApiStructure import (FensUserInfoField, UserLogoutField,
                                     ReqUserLoginField, QryMulticastInstrumentField)
from ctpwrapper.MdApi import MdApiWrapper


class MdApiPy(MdApiWrapper):

    def Create(self, pszFlowPath: Optional[str] = "",
               bIsUsingUdp: Optional[bool] = False,
               bIsMulticast: Optional[bool] = False) -> None:
        """
        创建MdApi
        :param pszFlowPath: 存贮订阅信息文件的目录，默认为当前目录
        :param bIsUsingUdp:
        :param bIsMulticast:
        """
        super(MdApiPy, self).Create(pszFlowPath.encode(), bIsUsingUdp, bIsMulticast)

    def Init(self) -> None:
        """
        初始化运行环境,只有调用后,接口才开始工作
        """
        super(MdApiPy, self).Init()
        time.sleep(1)  # wait for c++ init

    def Join(self) -> int:
        """
        等待接口线程结束运行
        @return 线程退出代码
        """
        return super(MdApiPy, self).Join()

    def ReqUserLogin(self, pReqUserLogin: "ReqUserLoginField", nRequestID: int) -> int:
        """
        用户登录请求
        """
        return super(MdApiPy, self).ReqUserLogin(pReqUserLogin, nRequestID)

    def ReqUserLogout(self, pUserLogout: "UserLogoutField", nRequestID: int) -> int:
        """
         登出请求
        """
        return super(MdApiPy, self).ReqUserLogout(pUserLogout, nRequestID)

    def ReqQryMulticastInstrument(self, pQryMulticastInstrument: "QryMulticastInstrumentField", nRequestID: int) -> int:
        """
        请求查询组播合约
        """
        return super(MdApiPy, self).ReqQryMulticastInstrument(pQryMulticastInstrument, nRequestID)

    def GetTradingDay(self) -> str:
        """
        获取当前交易日
        @retrun 获取到的交易日
        @remark 只有登录成功后,才能得到正确的交易日
        :return:
        """
        day = super(MdApiPy, self).GetTradingDay()
        return day.decode()

    def RegisterFront(self, pszFrontAddress: str) -> None:
        """
        注册前置机网络地址
        @param pszFrontAddress：前置机网络地址。
        @remark 网络地址的格式为：“protocol:# ipaddress:port”，如：”tcp:# 127.0.0.1:17001”。
        @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
        """
        super(MdApiPy, self).RegisterFront(pszFrontAddress.encode())

    def RegisterNameServer(self, pszNsAddress: str) -> None:
        """
        注册名字服务器网络地址
        @param pszNsAddress：名字服务器网络地址。
        @remark 网络地址的格式为：“protocol:# ipaddress:port”，如：”tcp:# 127.0.0.1:12001”。
        @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”12001”代表服务器端口号。
        @remark RegisterNameServer优先于RegisterFront
        """
        super(MdApiPy, self).RegisterNameServer(pszNsAddress.encode())

    def RegisterFensUserInfo(self, pFensUserInfo: "FensUserInfoField") -> None:
        """
        注册名字服务器用户信息
        @param pFensUserInfo：用户信息。
        """
        super(MdApiPy, self).RegisterFensUserInfo(pFensUserInfo)

    def SubscribeMarketData(self, pInstrumentID: typing.List[str]) -> int:
        """
         订阅行情。
        @param pInstrumentID 合约ID
        :return: int
        """
        ids = [bytes(item, encoding="utf-8") for item in pInstrumentID]
        return super(MdApiPy, self).SubscribeMarketData(ids)

    def UnSubscribeMarketData(self, pInstrumentID: typing.List[str]) -> int:
        """
        退订行情。
        @param pInstrumentID 合约ID
        :return: int
        """
        ids = [bytes(item, encoding="utf-8") for item in pInstrumentID]

        return super(MdApiPy, self).UnSubscribeMarketData(ids)

    def SubscribeForQuoteRsp(self, pInstrumentID: typing.List[str]) -> int:
        """
        订阅询价。
        :param pInstrumentID: 合约ID list
        :return: int
        """
        ids = [bytes(item, encoding="utf-8") for item in pInstrumentID]

        return super(MdApiPy, self).SubscribeForQuoteRsp(ids)

    def UnSubscribeForQuoteRsp(self, pInstrumentID: typing.List[str]) -> int:
        """
        退订询价。
        :param pInstrumentID: 合约ID list
        :return: int
        """
        ids = [bytes(item, encoding="utf-8") for item in pInstrumentID]

        return super(MdApiPy, self).UnSubscribeForQuoteRsp(ids)

    # for receive message
    def OnFrontConnected(self) -> None:
        """
        当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
        :return:
        """
        pass

    def OnFrontDisconnected(self, nReason) -> None:
        """
        当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
        @param nReason 错误原因
            4097 0x1001 网络读失败
            4098 0x1002 网络写失败
            8193 0x2001 读心跳超时
            8194 0x2002 发送心跳超时
            8195 0x2003 收到不能识别的错误消息
        客户端与服务端的连接断开有两种情况：
            网络原因导致连接断开
            服务端主动断开连接
        服务器主动断开连接有两种可能：
            客户端长时间没有从服务端接收报文，时间超时
            客户端建立的连接数超过限制
        :param nReason:
        """
        pass

    def OnHeartBeatWarning(self, nTimeLapse) -> None:
        """
        心跳超时警告。当长时间未收到报文时，该方法被调用。

        :param nTimeLapse: 距离上次接收报文的时间
        :return:
        """
        pass

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast) -> None:
        """
        登录请求响应
        :param pRspUserLogin:
        :param pRspInfo:
        :param nRequestID:
        :param bIsLast:
        :return:
        """
        pass

    def OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast) -> None:
        """
        登出请求响应
        :param pUserLogout:
        :param pRspInfo:
        :param nRequestID:
        :param bIsLast:
        :return:
        """
        pass

    def OnRspQryMulticastInstrument(self, pMulticastInstrument, pRspInfo, nRequestID, bIsLast) -> None:
        """
        请求查询组播合约响应
        :param pMulticastInstrument:
        :param pRspInfo:
        :param nRequestID:
        :param bIsLast:
        :return:
        """
        pass

    def OnRspError(self, pRspInfo, nRequestID, bIsLast) -> None:
        """
        错误应答
        :param pRspInfo:
        :param nRequestID:
        :param bIsLast:
        :return:
        """
        pass

    def OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast) -> None:
        """
        订阅行情应答
        :param pSpecificInstrument:
        :param pRspInfo:
        :param nRequestID:
        :param bIsLast:
        :return:
        """
        pass

    def OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast) -> None:
        """
        取消订阅行情应答
        :param pSpecificInstrument:
        :param pRspInfo:
        :param nRequestID:
        :param bIsLast:
        :return:
        """
        pass

    def OnRspSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast) -> None:
        """
        订阅询价应答
        :param pSpecificInstrument:
        :param pRspInfo:
        :param nRequestID:
        :param bIsLast:
        :return:
        """
        pass

    def OnRspUnSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast) -> None:
        """
        取消订阅询价应答
        :param pSpecificInstrument:
        :param pRspInfo:
        :param nRequestID:
        :param bIsLast:
        :return:
        """
        pass

    def OnRtnDepthMarketData(self, pDepthMarketData) -> None:
        """
        深度行情通知
        :param pDepthMarketData:
        :return:
        """
        pass

    def OnRtnForQuoteRsp(self, pForQuoteRsp) -> None:
        """
        询价通知
        :param pForQuoteRsp:
        :return:
        """
        pass
