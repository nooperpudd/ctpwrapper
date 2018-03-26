# encoding:utf-8

from ctpwrapper.MdApi import MdApiWrapper


# class MdSpiPy(object):
#
#     # 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
#     def OnFrontConnected(self):
#         pass
#
#     # 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
#     # @param nReason 错误原因
#     #         0x1001 网络读失败
#     #         0x1002 网络写失败
#     #         0x2001 接收心跳超时
#     #         0x2002 发送心跳失败
#     #         0x2003 收到错误报文
#
#     # 4097 0x1001 网络读失败
#     # 4098 0x1002 网络写失败
#     # 8193 0x2001 读心跳超时
#     # 8194 0x2002 发送心跳超时
#     # 8195 0x2003 收到不能识别的错误消息
#     # 客户端与服务端的连接断开有两种情况：
#     #  网络原因导致连接断开
#     #  服务端主动断开连接
#     # 服务器主动断开连接有两种可能：
#     #  客户端长时间没有从服务端接收报文，时间超时
#     #  客户端建立的连接数超过限制
#     def OnFrontDisconnected(self, nReason):
#         pass
#
#     # 心跳超时警告。当长时间未收到报文时，该方法被调用。
#     # @param nTimeLapse 距离上次接收报文的时间
#     def OnHeartBeatWarning(self, nTimeLapse):
#         pass
#
#     # 登录请求响应
#     def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
#         pass
#
#     # 登出请求响应
#     def OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast):
#         pass
#
#     # 错误应答
#     def OnRspError(self, pRspInfo, nRequestID, bIsLast):
#         pass
#
#     # 订阅行情应答
#     def OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
#         pass
#
#     # 取消订阅行情应答
#     def OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
#         pass
#
#     # 订阅询价应答
#     def OnRspSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
#         pass
#
#     # 取消订阅询价应答
#     def OnRspUnSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
#         pass
#
#     # 深度行情通知
#     def OnRtnDepthMarketData(self, pDepthMarketData):
#         pass
#
#     # 询价通知
#     def OnRtnForQuoteRsp(self, pForQuoteRsp):
#         pass


class MdApiPy(MdApiWrapper):
    #     def __init__(self, pszFlowPath="", bIsUsingUdp=False, bIsMulticast=False):

    # self.Create(pszFlowPath, bIsUsingUdp, bIsMulticast)
    #     # super(MdApiPy, self).__init__(pszFlowPath.encode(), bIsUsingUdp, bIsMulticast)

    def Create(self, pszFlowPath="", bIsUsingUdp=False, bIsMulticast=False):
        """创建MdApi
        @param pszFlowPath 存贮订阅信息文件的目录，默认为当前目录
        @return 创建出的UserApi
        modify for udp marketdata
        """
        super(MdApiPy,self).Create(pszFlowPath.encode(),bIsUsingUdp,bIsMulticast)

    def Init(self):
        super(MdApiPy,self).Init()

    def Join(self) -> int:
        return super(MdApiPy,self).Join()

    def ReqUserLogin(self, pReqUserLoginField, nRequestID):
        """
        用户登录请求
        :return:
        """
        return super(MdApiPy, self).ReqUserLogin(pReqUserLoginField, nRequestID)

    def ReqUserLogout(self, pUserLogout, nRequestID):
        """
         登出请求
        :return:
        """
        return super(MdApiPy, self).ReqUserLogout(pUserLogout, nRequestID)

    def GetTradingDay(self):
        """
        获取当前交易日
        @retrun 获取到的交易日
        @remark 只有登录成功后,才能得到正确的交易日
        :return:
        """
        return super(MdApiPy, self).GetTradingDay()

    def RegisterFront(self, pszFrontAddress: str):
        """
        注册前置机网络地址
        @param pszFrontAddress：前置机网络地址。
        @remark 网络地址的格式为：“protocol:# ipaddress:port”，如：”tcp:# 127.0.0.1:17001”。
        @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
        :return:
        """
        super(MdApiPy, self).RegisterFront(pszFrontAddress.encode())

    def RegisterNameServer(self, pszNsAddress: str):
        """
        注册名字服务器网络地址
        @param pszNsAddress：名字服务器网络地址。
        @remark 网络地址的格式为：“protocol:# ipaddress:port”，如：”tcp:# 127.0.0.1:12001”。
        @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”12001”代表服务器端口号。
        @remark RegisterNameServer优先于RegisterFront
        :return:
        """
        super(MdApiPy, self).RegisterNameServer(pszNsAddress.encode())

    def RegisterFensUserInfo(self, pFensUserInfo):
        """
        注册名字服务器用户信息
        @param pFensUserInfo：用户信息。
        :return:
        """
        super(MdApiPy, self).RegisterFensUserInfo(pFensUserInfo)

    def SubscribeMarketData(self, pInstrumentID: list):
        """
         订阅行情。
        @param ppInstrumentID 合约ID
        :return:
        """
        return super(MdApiPy, self).SubscribeMarketData(pInstrumentID)

    def UnSubscribeMarketData(self, pInstrumentID: list):
        """
        退订行情。
        @param ppInstrumentID 合约ID
        :return:
        """
        return super(MdApiPy, self).UnSubscribeMarketData(pInstrumentID)

    def SubscribeForQuoteRsp(self, pInstrumentID: list):
        """
        订阅询价。
        :param pInstrumentID: 合约ID list
        :return:
        """
        return super(MdApiPy, self).SubscribeForQuoteRsp(pInstrumentID)

    def UnSubscribeForQuoteRsp(self, pInstrumentID: list):
        """
        退订询价。
        :param pInstrumentID: 合约ID list
        :return:
        """
        return super(MdApiPy, self).UnSubscribeForQuoteRsp(pInstrumentID)

    # for receive message

    # 当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。

    def OnFrontConnected(self):
        pass

        # 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
        # @param nReason 错误原因
        #         0x1001 网络读失败
        #         0x1002 网络写失败
        #         0x2001 接收心跳超时
        #         0x2002 发送心跳失败
        #         0x2003 收到错误报文

        # 4097 0x1001 网络读失败
        # 4098 0x1002 网络写失败
        # 8193 0x2001 读心跳超时
        # 8194 0x2002 发送心跳超时
        # 8195 0x2003 收到不能识别的错误消息
        # 客户端与服务端的连接断开有两种情况：
        #  网络原因导致连接断开
        #  服务端主动断开连接
        # 服务器主动断开连接有两种可能：
        #  客户端长时间没有从服务端接收报文，时间超时
        #  客户端建立的连接数超过限制

    def OnFrontDisconnected(self, nReason):
        pass

        # 心跳超时警告。当长时间未收到报文时，该方法被调用。
        # @param nTimeLapse 距离上次接收报文的时间

    def OnHeartBeatWarning(self, nTimeLapse):
        pass

        # 登录请求响应

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        pass

        # 登出请求响应

    def OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast):
        pass

        # 错误应答

    def OnRspError(self, pRspInfo, nRequestID, bIsLast):
        pass

        # 订阅行情应答

    def OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        pass

        # 取消订阅行情应答

    def OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        pass

        # 订阅询价应答

    def OnRspSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        pass

        # 取消订阅询价应答

    def OnRspUnSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast):
        pass

        # 深度行情通知

    def OnRtnDepthMarketData(self, pDepthMarketData):
        pass

        # 询价通知

    def OnRtnForQuoteRsp(self, pForQuoteRsp):
        pass
