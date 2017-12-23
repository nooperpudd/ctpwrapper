# encoding:utf-8

class TraderClass(object):
    def __init__(self):
        pass

    def GetApiVersion(self):
        """
        获取到的版本号
        :return:
        """

    def GetTradingDay(self):
        """
        获取当前交易日
        @retrun 获取到的交易日
        @remark 只有登录成功后,才能得到正确的交易日
        """
        pass

    def RegisterFront(self, pszFrontAddress):
        """
        注册前置机网络地址
        @param pszFrontAddress：前置机网络地址。
        @remark 网络地址的格式为：“protocol:
        ipaddress:port”，如：”tcp:
        127.0.0.1:17001”。
        @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
        """
        pass

    def RegisterNameServer(self, pszNsAddress):
        """
        注册名字服务器网络地址
        @param pszNsAddress：名字服务器网络地址。
        @remark 网络地址的格式为：“protocol:
        ipaddress:port”，如：”tcp:
        127.0.0.1:12001”。
        @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”12001”代表服务器端口号。
        @remark RegisterNameServer优先于RegisterFront
        """
        pass

    def RegisterFensUserInfo(self, pFensUserInfo):
        """
        注册名字服务器用户信息
        @param pFensUserInfo：用户信息。
        """
        pass

    def SubscribePrivateTopic(self, nResumeType):
        """
        订阅私有流。
        @param nResumeType 私有流重传方式
                THOST_TERT_RESTART:从本交易日开始重传
                THOST_TERT_RESUME:从上次收到的续传
                THOST_TERT_QUICK:只传送登录后私有流的内容
        @remark 该方法要在Init方法前调用。若不调用则不会收到私有流的数据。
        """
        pass

    def SubscribePublicTopic(self, nResumeType):
        """
        订阅公共流。
        @param nResumeType 公共流重传方式
                THOST_TERT_RESTART:从本交易日开始重传
                THOST_TERT_RESUME:从上次收到的续传
                THOST_TERT_QUICK:只传送登录后公共流的内容
        @remark 该方法要在Init方法前调用。若不调用则不会收到公共流的数据。
        """
        pass

    def ReqAuthenticate(self, pReqAuthenticate, nRequestID):
        """
        客户端认证请求
        """
        pass

    def ReqUserLogin(self, pReqUserLogin, nRequestID):
        """
        用户登录请求
        """
        pass

    def ReqUserLogout(self, pUserLogout, nRequestID):
        """
        登出请求
        """
        pass

    def ReqUserPasswordUpdate(self, pUserPasswordUpdate, nRequestID):
        """
        用户口令更新请求
        """
        pass

    def ReqTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, nRequestID):
        """资金账户口令更新请求"""
        pass

    def ReqOrderInsert(self, pInputOrder, nRequestID):
        """报单录入请求"""
        pass

    def ReqParkedOrderInsert(self, pParkedOrder, nRequestID):
        """预埋单录入请求"""
        pass

    def ReqParkedOrderAction(self, pParkedOrderAction, nRequestID):
        """预埋撤单录入请求"""
        pass

    def ReqOrderAction(self, pInputOrderAction, nRequestID):
        """报单操作请求"""
        pass

    def ReqQueryMaxOrderVolume(self, pQueryMaxOrderVolume, nRequestID):
        """查询最大报单数量请求"""
        pass

    def ReqSettlementInfoConfirm(self, pSettlementInfoConfirm, nRequestID):
        """投资者结算结果确认"""
        pass

    def ReqRemoveParkedOrder(self, pRemoveParkedOrder, nRequestID):
        """请求删除预埋单"""
        pass

    def ReqRemoveParkedOrderAction(self, pRemoveParkedOrderAction, nRequestID):
        """请求删除预埋撤单"""
        pass

    def ReqExecOrderInsert(self, pInputExecOrder, nRequestID):
        """执行宣告录入请求"""
        pass

    def ReqExecOrderAction(self, pInputExecOrderAction, nRequestID):
        """执行宣告操作请求"""
        pass

    def ReqForQuoteInsert(self, pInputForQuote, nRequestID):
        """询价录入请求"""
        pass

    def ReqQuoteInsert(self, pInputQuote, nRequestID):
        """报价录入请求"""
        pass

    def ReqQuoteAction(self, pInputQuoteAction, nRequestID):
        """报价操作请求"""
        pass

    def ReqBatchOrderAction(self, pInputBatchOrderAction, nRequestID):
        """
        批量报单操作请求
        :param pInputBatchOrderAction:
        :param nRequestID:
        :return:
        """
        pass

    def ReqCombActionInsert(self, pInputCombAction, nRequestID):
        """申请组合录入请求"""
        pass

    def ReqQryOrder(self, pQryOrder, nRequestID):
        """请求查询报单"""
        pass

    def ReqQryTrade(self, pQryTrade, nRequestID):
        """请求查询成交"""
        pass

    def ReqQryInvestorPosition(self, pQryInvestorPosition, nRequestID):
        """请求查询投资者持仓"""
        pass

    def ReqQryTradingAccount(self, pQryTradingAccount, nRequestID):
        """请求查询资金账户"""
        pass

    def ReqQryInvestor(self, pQryInvestor, nRequestID):
        """请求查询投资者"""
        pass

    def ReqQryTradingCode(self, pQryTradingCode, nRequestID):
        """请求查询交易编码"""
        pass

    def ReqQryInstrumentMarginRate(self, pQryInstrumentMarginRate, nRequestID):
        """请求查询合约保证金率"""
        pass

    def ReqQryInstrumentCommissionRate(self, pQryInstrumentCommissionRate, nRequestID):
        """请求查询合约手续费率"""
        pass

    def ReqQryExchange(self, pQryExchange, nRequestID):
        """请求查询交易所"""
        pass

    def ReqQryProduct(self, pQryProduct, nRequestID):
        """请求查询产品"""
        pass

    def ReqQryInstrument(self, pQryInstrument, nRequestID):
        """请求查询合约"""
        pass

    def ReqQryDepthMarketData(self, pQryDepthMarketData, nRequestID):
        """请求查询行情"""
        pass

    def ReqQrySettlementInfo(self, pQrySettlementInfo, nRequestID):
        """请求查询投资者结算结果"""
        pass

    def ReqQryTransferBank(self, pQryTransferBank, nRequestID):
        """请求查询转帐银行"""
        pass

    def ReqQryInvestorPositionDetail(self, pQryInvestorPositionDetail, nRequestID):
        """请求查询投资者持仓明细"""
        pass

    def ReqQryNotice(self, pQryNotice, nRequestID):
        """请求查询客户通知"""
        pass

    def ReqQrySettlementInfoConfirm(self, pQrySettlementInfoConfirm, nRequestID):
        """请求查询结算信息确认"""
        pass

    def ReqQryInvestorPositionCombineDetail(self, pQryInvestorPositionCombineDetail, nRequestID):
        """请求查询投资者持仓明细"""
        pass

    def ReqQryCFMMCTradingAccountKey(self, pQryCFMMCTradingAccountKey, nRequestID):
        """请求查询保证金监管系统经纪公司资金账户密钥"""
        pass

    def ReqQryEWarrantOffset(self, pQryEWarrantOffset, nRequestID):
        """请求查询仓单折抵信息"""
        pass

    def ReqQryInvestorProductGroupMargin(self, pQryInvestorProductGroupMargin, nRequestID):
        """请求查询投资者品种/跨品种保证金"""
        pass

    def ReqQryExchangeMarginRate(self, pQryExchangeMarginRate, nRequestID):
        """请求查询交易所保证金率"""
        pass

    def ReqQryExchangeMarginRateAdjust(self, pQryExchangeMarginRateAdjust, nRequestID):
        """请求查询交易所调整保证金率"""
        pass

    def ReqQryExchangeRate(self, pQryExchangeRate, nRequestID):
        """请求查询汇率"""
        pass

    def ReqQrySecAgentACIDMap(self, pQrySecAgentACIDMap, nRequestID):
        """请求查询二级代理操作员银期权限"""
        pass

    def ReqQryProductExchRate(self, pQryProductExchRate, nRequestID):
        """请求查询产品报价汇率"""
        pass

    def ReqQryProductGroup(self, pQryProductGroup, nRequestID):
        """
        请求查询产品组
        :param pQryProductGroup:
        :param nRequestID:
        :return:
        """
        pass

    def ReqQryMMInstrumentCommissionRate(self, pQryMMInstrumentCommissionRate, nRequestID):
        """
        请求查询做市商合约手续费率
        :param pQryMMInstrumentCommissionRate:
        :param nRequestID:
        :return:
        """

    def ReqQryMMOptionInstrCommRate(self, pQryMMOptionInstrCommRate, nRequestID):
        """
        请求查询做市商期权合约手续费
        :param pQryMMOptionInstrCommRate:
        :param nRequestID:
        :return:
        """
        pass

    def ReqQryInstrumentOrderCommRate(self, pQryInstrumentOrderCommRate, nRequestID):
        """
        请求查询报单手续费
        """
        pass

    def ReqQryOptionInstrTradeCost(self, pQryOptionInstrTradeCost, nRequestID):
        """请求查询期权交易成本"""
        pass

    def ReqQryOptionInstrCommRate(self, pQryOptionInstrCommRate, nRequestID):
        """请求查询期权合约手续费"""
        pass

    def ReqQryExecOrder(self, pQryExecOrder, nRequestID):
        """请求查询执行宣告"""
        pass

    def ReqQryForQuote(self, pQryForQuote, nRequestID):
        """请求查询询价"""
        pass

    def ReqQryQuote(self, pQryQuote, nRequestID):
        """请求查询报价"""
        pass

    def ReqQryCombInstrumentGuard(self, pQryCombInstrumentGuard, nRequestID):
        """请求查询组合合约安全系数"""
        pass

    def ReqQryCombAction(self, pQryCombAction, nRequestID):
        """请求查询申请组合"""
        pass

    def ReqQryTransferSerial(self, pQryTransferSerial, nRequestID):
        """请求查询转帐流水"""
        pass

    def ReqQryAccountregister(self, pQryAccountregister, nRequestID):
        """请求查询银期签约关系"""
        pass

    def ReqQryContractBank(self, pQryContractBank, nRequestID):
        """请求查询签约银行"""
        pass

    def ReqQryParkedOrder(self, pQryParkedOrder, nRequestID):
        """请求查询预埋单"""
        pass

    def ReqQryParkedOrderAction(self, pQryParkedOrderAction, nRequestID):
        """请求查询预埋撤单"""
        pass

    def ReqQryTradingNotice(self, pQryTradingNotice, nRequestID):
        """请求查询交易通知"""
        pass

    def ReqQryBrokerTradingParams(self, pQryBrokerTradingParams, nRequestID):
        """请求查询经纪公司交易参数"""
        pass

    def ReqQryBrokerTradingAlgos(self, pQryBrokerTradingAlgos, nRequestID):
        """请求查询经纪公司交易算法"""
        pass

    def ReqQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken, nRequestID):
        """请求查询监控中心用户令牌"""
        pass

    def ReqFromBankToFutureByFuture(self, pReqTransfer, nRequestID):
        """
        期货发起银行资金转期货请求
        """
        pass

    def ReqFromFutureToBankByFuture(self, pReqTransfer, nRequestID):
        """
        期货发起期货资金转银行请求
        """
        pass

    def ReqQueryBankAccountMoneyByFuture(self, pReqQueryAccount, nRequestID):
        """
        期货发起查询银行余额请求
        """
        pass
