# encoding:utf-8

from ctpwrapper.MdApi import MdApiWrapper



class MdApiPy(MdApiWrapper):
    def __init__(self, pszFlowPath="", bIsUsingUdp=False, bIsMulticast=False):

        super(MdApiPy, self).__init__(pszFlowPath, bIsUsingUdp, bIsMulticast)

    def ReqUserLogin(self, pReqUserLoginField, nRequestID):
        """
        用户登录请求
        :return:
        """
        return super(MdApiPy,self).ReqUserLogin(pReqUserLoginField,nRequestID)

    def ReqUserLogout(self, pUserLogout, nRequestID):
        """
         登出请求
        :return:
        """
        return super(MdApiPy,self).ReqUserLogout(pUserLogout, nRequestID)


    def GetTradingDay(self):
        """
        获取当前交易日
        @retrun 获取到的交易日
        @remark 只有登录成功后,才能得到正确的交易日
        :return:
        """
        return super(MdApiPy, self).GetTradingDay()

    def RegisterFront(self, pszFrontAddress):
        """
        注册前置机网络地址
        @param pszFrontAddress：前置机网络地址。
        @remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。
        @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
        :return:
        """
        return super(MdApiPy, self).RegisterFront(pszFrontAddress)


    def RegisterNameServer(self, pszNsAddress):
        """
        注册名字服务器网络地址
        @param pszNsAddress：名字服务器网络地址。
        @remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:12001”。
        @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”12001”代表服务器端口号。
        @remark RegisterNameServer优先于RegisterFront
        :return:
        """
        return super(MdApiPy, self).RegisterNameServer(pszNsAddress)


    def RegisterFensUserInfo(self, pFensUserInfo):
        """
        注册名字服务器用户信息
        @param pFensUserInfo：用户信息。
        :return:
        """
        return super(MdApiPy, self).RegisterFensUserInfo(pFensUserInfo)

    def SubscribeMarketData(self, pInstrumentID):
        """
         订阅行情。
        @param ppInstrumentID 合约ID
        :return:
        """
        return super(MdApiPy, self).SubscribeMarketData(pInstrumentID)

    def UnSubscribeMarketData(self, pInstrumentID):
        """
        退订行情。
        @param ppInstrumentID 合约ID
        :return:
        """
        return super(MdApiPy, self).UnSubscribeMarketData(pInstrumentID)

    def SubscribeForQuoteRsp(self, pInstrumentID):
        """
        订阅询价。
        :param pInstrumentID: 合约ID list
        :return:
        """
        return super(MdApiPy, self).SubscribeForQuoteRsp(pInstrumentID)


    def UnSubscribeForQuoteRsp(self, pInstrumentID):
        """
        退订询价。
        :param pInstrumentID: 合约ID list
        :return:
        """
        return super(MdApiPy, self).UnSubscribeForQuoteRsp(pInstrumentID)

