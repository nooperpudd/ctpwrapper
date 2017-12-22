# encoding:utf-8

class TraderClass(object):
    def __init__(self):
        pass
    def GetApiVersion(self):
        pass

    def GetTradingDay(self):
        """获取当前交易日
        @retrun 获取到的交易日
        @remark 只有登录成功后,才能得到正确的交易日
        """
        return ''

    def RegisterFront(self, pszFrontAddress):
        """注册前置机网络地址
        @param pszFrontAddress：前置机网络地址。
        @remark 网络地址的格式为：“protocol:
        ipaddress:port”，如：”tcp:
        127.0.0.1:17001”。
        @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
        """

    def RegisterNameServer(self, pszNsAddress):
        """注册名字服务器网络地址
        @param pszNsAddress：名字服务器网络地址。
        @remark 网络地址的格式为：“protocol:
        ipaddress:port”，如：”tcp:
        127.0.0.1:12001”。
        @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”12001”代表服务器端口号。
        @remark RegisterNameServer优先于RegisterFront
        """

    def RegisterFensUserInfo(self, pFensUserInfo):
        """注册名字服务器用户信息
        @param pFensUserInfo：用户信息。
        """

    def SubscribePrivateTopic(self, nResumeType):
        """订阅私有流。
        @param nResumeType 私有流重传方式
                THOST_TERT_RESTART:从本交易日开始重传
                THOST_TERT_RESUME:从上次收到的续传
                THOST_TERT_QUICK:只传送登录后私有流的内容
        @remark 该方法要在Init方法前调用。若不调用则不会收到私有流的数据。
        """

    def SubscribePublicTopic(self, nResumeType):
        """订阅公共流。
        @param nResumeType 公共流重传方式
                THOST_TERT_RESTART:从本交易日开始重传
                THOST_TERT_RESUME:从上次收到的续传
                THOST_TERT_QUICK:只传送登录后公共流的内容
        @remark 该方法要在Init方法前调用。若不调用则不会收到公共流的数据。
        """

    def ReqAuthenticate(self, pReqAuthenticate, nRequestID):
        """客户端认证请求"""
        return 0

    def ReqUserLogin(self, pReqUserLogin, nRequestID):
        """用户登录请求"""
        return 0

    def ReqUserLogout(self, pUserLogout, nRequestID):
        """登出请求"""
        return 0

    def ReqUserPasswordUpdate(self, pUserPasswordUpdate, nRequestID):
        """用户口令更新请求"""
        return 0

    def ReqTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, nRequestID):
        """资金账户口令更新请求"""
        return 0

    def ReqOrderInsert(self, pInputOrder, nRequestID):
        """报单录入请求"""
        return 0

    def ReqParkedOrderInsert(self, pParkedOrder, nRequestID):
        """预埋单录入请求"""
        return 0

    def ReqParkedOrderAction(self, pParkedOrderAction, nRequestID):
        """预埋撤单录入请求"""
        return 0

    def ReqOrderAction(self, pInputOrderAction, nRequestID):
        """报单操作请求"""
        return 0

    def ReqQueryMaxOrderVolume(self, pQueryMaxOrderVolume, nRequestID):
        """查询最大报单数量请求"""
        return 0

    def ReqSettlementInfoConfirm(self, pSettlementInfoConfirm, nRequestID):
        """投资者结算结果确认"""
        return 0

    def ReqRemoveParkedOrder(self, pRemoveParkedOrder, nRequestID):
        """请求删除预埋单"""
        return 0

    def ReqRemoveParkedOrderAction(self, pRemoveParkedOrderAction, nRequestID):
        """请求删除预埋撤单"""
        return 0

    def ReqExecOrderInsert(self, pInputExecOrder, nRequestID):
        """执行宣告录入请求"""
        return 0

    def ReqExecOrderAction(self, pInputExecOrderAction, nRequestID):
        """执行宣告操作请求"""
        return 0

    def ReqForQuoteInsert(self, pInputForQuote, nRequestID):
        """询价录入请求"""
        return 0

    def ReqQuoteInsert(self, pInputQuote, nRequestID):
        """报价录入请求"""
        return 0

    def ReqQuoteAction(self, pInputQuoteAction, nRequestID):
        """报价操作请求"""
        return 0

    def ReqCombActionInsert(self, pInputCombAction, nRequestID):
        """申请组合录入请求"""
        return 0

    def ReqQryOrder(self, pQryOrder, nRequestID):
        """请求查询报单"""
        return 0

    def ReqQryTrade(self, pQryTrade, nRequestID):
        """请求查询成交"""
        return 0

    def ReqQryInvestorPosition(self, pQryInvestorPosition, nRequestID):
        """请求查询投资者持仓"""
        return 0

    def ReqQryTradingAccount(self, pQryTradingAccount, nRequestID):
        """请求查询资金账户"""
        return 0

    def ReqQryInvestor(self, pQryInvestor, nRequestID):
        """请求查询投资者"""
        return 0

    def ReqQryTradingCode(self, pQryTradingCode, nRequestID):
        """请求查询交易编码"""
        return 0

    def ReqQryInstrumentMarginRate(self, pQryInstrumentMarginRate, nRequestID):
        """请求查询合约保证金率"""
        return 0

    def ReqQryInstrumentCommissionRate(self, pQryInstrumentCommissionRate, nRequestID):
        """请求查询合约手续费率"""
        return 0

    def ReqQryExchange(self, pQryExchange, nRequestID):
        """请求查询交易所"""
        return 0

    def ReqQryProduct(self, pQryProduct, nRequestID):
        """请求查询产品"""
        return 0

    def ReqQryInstrument(self, pQryInstrument, nRequestID):
        """请求查询合约"""
        return 0

    def ReqQryDepthMarketData(self, pQryDepthMarketData, nRequestID):
        """请求查询行情"""
        return 0

    def ReqQrySettlementInfo(self, pQrySettlementInfo, nRequestID):
        """请求查询投资者结算结果"""
        return 0

    def ReqQryTransferBank(self, pQryTransferBank, nRequestID):
        """请求查询转帐银行"""
        return 0

    def ReqQryInvestorPositionDetail(self, pQryInvestorPositionDetail, nRequestID):
        """请求查询投资者持仓明细"""
        return 0

    def ReqQryNotice(self, pQryNotice, nRequestID):
        """请求查询客户通知"""
        return 0

    def ReqQrySettlementInfoConfirm(self, pQrySettlementInfoConfirm, nRequestID):
        """请求查询结算信息确认"""
        return 0

    def ReqQryInvestorPositionCombineDetail(self, pQryInvestorPositionCombineDetail, nRequestID):
        """请求查询投资者持仓明细"""
        return 0

    def ReqQryCFMMCTradingAccountKey(self, pQryCFMMCTradingAccountKey, nRequestID):
        """请求查询保证金监管系统经纪公司资金账户密钥"""
        return 0

    def ReqQryEWarrantOffset(self, pQryEWarrantOffset, nRequestID):
        """请求查询仓单折抵信息"""
        return 0

    def ReqQryInvestorProductGroupMargin(self, pQryInvestorProductGroupMargin, nRequestID):
        """请求查询投资者品种/跨品种保证金"""
        return 0

    def ReqQryExchangeMarginRate(self, pQryExchangeMarginRate, nRequestID):
        """请求查询交易所保证金率"""
        return 0

    def ReqQryExchangeMarginRateAdjust(self, pQryExchangeMarginRateAdjust, nRequestID):
        """请求查询交易所调整保证金率"""
        return 0

    def ReqQryExchangeRate(self, pQryExchangeRate, nRequestID):
        """请求查询汇率"""
        return 0

    def ReqQrySecAgentACIDMap(self, pQrySecAgentACIDMap, nRequestID):
        """请求查询二级代理操作员银期权限"""
        return 0

    def ReqQryProductExchRate(self, pQryProductExchRate, nRequestID):
        """请求查询产品报价汇率"""
        return 0

    def ReqQryOptionInstrTradeCost(self, pQryOptionInstrTradeCost, nRequestID):
        """请求查询期权交易成本"""
        return 0

    def ReqQryOptionInstrCommRate(self, pQryOptionInstrCommRate, nRequestID):
        """请求查询期权合约手续费"""
        return 0

    def ReqQryExecOrder(self, pQryExecOrder, nRequestID):
        """请求查询执行宣告"""
        return 0

    def ReqQryForQuote(self, pQryForQuote, nRequestID):
        """请求查询询价"""
        return 0

    def ReqQryQuote(self, pQryQuote, nRequestID):
        """请求查询报价"""
        return 0

    def ReqQryCombInstrumentGuard(self, pQryCombInstrumentGuard, nRequestID):
        """请求查询组合合约安全系数"""
        return 0

    def ReqQryCombAction(self, pQryCombAction, nRequestID):
        """请求查询申请组合"""
        return 0

    def ReqQryTransferSerial(self, pQryTransferSerial, nRequestID):
        """请求查询转帐流水"""
        return 0

    def ReqQryAccountregister(self, pQryAccountregister, nRequestID):
        """请求查询银期签约关系"""
        return 0

    def ReqQryContractBank(self, pQryContractBank, nRequestID):
        """请求查询签约银行"""
        return 0

    def ReqQryParkedOrder(self, pQryParkedOrder, nRequestID):
        """请求查询预埋单"""
        return 0

    def ReqQryParkedOrderAction(self, pQryParkedOrderAction, nRequestID):
        """请求查询预埋撤单"""
        return 0

    def ReqQryTradingNotice(self, pQryTradingNotice, nRequestID):
        """请求查询交易通知"""
        return 0

    def ReqQryBrokerTradingParams(self, pQryBrokerTradingParams, nRequestID):
        """请求查询经纪公司交易参数"""
        return 0

    def ReqQryBrokerTradingAlgos(self, pQryBrokerTradingAlgos, nRequestID):
        """请求查询经纪公司交易算法"""
        return 0

    def ReqQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken, nRequestID):
        """请求查询监控中心用户令牌"""
        return 0

    def ReqFromBankToFutureByFuture(self, pReqTransfer, nRequestID):
        """期货发起银行资金转期货请求"""
        return 0

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

    """
        static CThostFtdcTraderApi *CreateFtdcTraderApi(const char *pszFlowPath = "");

    ///获取API的版本信息
    ///@retrun 获取到的版本号
    static const char *GetApiVersion();

    ///删除接口对象本身
    ///@remark 不再使用本接口对象时,调用该函数删除接口对象
    virtual void Release() = 0;

    ///初始化
    ///@remark 初始化运行环境,只有调用后,接口才开始工作
    virtual void Init() = 0;

    ///等待接口线程结束运行
    ///@return 线程退出代码
    virtual int Join() = 0;

    ///获取当前交易日
    ///@retrun 获取到的交易日
    ///@remark 只有登录成功后,才能得到正确的交易日
    virtual const char *GetTradingDay() = 0;

    ///注册前置机网络地址
    ///@param pszFrontAddress：前置机网络地址。
    ///@remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。
    ///@remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
    virtual void RegisterFront(char *pszFrontAddress) = 0;

    ///注册名字服务器网络地址
    ///@param pszNsAddress：名字服务器网络地址。
    ///@remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:12001”。
    ///@remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”12001”代表服务器端口号。
    ///@remark RegisterNameServer优先于RegisterFront
    virtual void RegisterNameServer(char *pszNsAddress) = 0;

    ///注册名字服务器用户信息
    ///@param pFensUserInfo：用户信息。
    virtual void RegisterFensUserInfo(CThostFtdcFensUserInfoField *pFensUserInfo) = 0;

    ///注册回调接口
    ///@param pSpi 派生自回调接口类的实例
    virtual void RegisterSpi(CThostFtdcTraderSpi *pSpi) = 0;

    ///订阅私有流。
    ///@param nResumeType 私有流重传方式
    ///        THOST_TERT_RESTART:从本交易日开始重传
    ///        THOST_TERT_RESUME:从上次收到的续传
    ///        THOST_TERT_QUICK:只传送登录后私有流的内容
    ///@remark 该方法要在Init方法前调用。若不调用则不会收到私有流的数据。
    virtual void SubscribePrivateTopic(THOST_TE_RESUME_TYPE nResumeType) = 0;

    ///订阅公共流。
    ///@param nResumeType 公共流重传方式
    ///        THOST_TERT_RESTART:从本交易日开始重传
    ///        THOST_TERT_RESUME:从上次收到的续传
    ///        THOST_TERT_QUICK:只传送登录后公共流的内容
    ///@remark 该方法要在Init方法前调用。若不调用则不会收到公共流的数据。
    virtual void SubscribePublicTopic(THOST_TE_RESUME_TYPE nResumeType) = 0;

    ///客户端认证请求
    virtual int ReqAuthenticate(CThostFtdcReqAuthenticateField *pReqAuthenticateField, int nRequestID) = 0;

    ///用户登录请求
    virtual int ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID) = 0;


    ///登出请求
    virtual int ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) = 0;

    ///用户口令更新请求
    virtual int ReqUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, int nRequestID) = 0;

    ///资金账户口令更新请求
    virtual int
    ReqTradingAccountPasswordUpdate(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate,
                                    int nRequestID) = 0;

    ///报单录入请求
    virtual int ReqOrderInsert(CThostFtdcInputOrderField *pInputOrder, int nRequestID) = 0;

    ///预埋单录入请求
    virtual int ReqParkedOrderInsert(CThostFtdcParkedOrderField *pParkedOrder, int nRequestID) = 0;

    ///预埋撤单录入请求
    virtual int ReqParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, int nRequestID) = 0;

    ///报单操作请求
    virtual int ReqOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, int nRequestID) = 0;

    ///查询最大报单数量请求
    virtual int ReqQueryMaxOrderVolume(CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, int nRequestID) = 0;

    ///投资者结算结果确认
    virtual int
    ReqSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, int nRequestID) = 0;

    ///请求删除预埋单
    virtual int ReqRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, int nRequestID) = 0;

    ///请求删除预埋撤单
    virtual int
    ReqRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, int nRequestID) = 0;

    ///执行宣告录入请求
    virtual int ReqExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, int nRequestID) = 0;

    ///执行宣告操作请求
    virtual int ReqExecOrderAction(CThostFtdcInputExecOrderActionField *pInputExecOrderAction, int nRequestID) = 0;

    ///询价录入请求
    virtual int ReqForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, int nRequestID) = 0;

    ///报价录入请求
    virtual int ReqQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, int nRequestID) = 0;

    ///报价操作请求
    virtual int ReqQuoteAction(CThostFtdcInputQuoteActionField *pInputQuoteAction, int nRequestID) = 0;

    ///批量报单操作请求
    virtual int ReqBatchOrderAction(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, int nRequestID) = 0;

    ///申请组合录入请求
    virtual int ReqCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, int nRequestID) = 0;

    ///请求查询报单
    virtual int ReqQryOrder(CThostFtdcQryOrderField *pQryOrder, int nRequestID) = 0;

    ///请求查询成交
    virtual int ReqQryTrade(CThostFtdcQryTradeField *pQryTrade, int nRequestID) = 0;

    ///请求查询投资者持仓
    virtual int ReqQryInvestorPosition(CThostFtdcQryInvestorPositionField *pQryInvestorPosition, int nRequestID) = 0;

    ///请求查询资金账户
    virtual int ReqQryTradingAccount(CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID) = 0;

    ///请求查询投资者
    virtual int ReqQryInvestor(CThostFtdcQryInvestorField *pQryInvestor, int nRequestID) = 0;

    ///请求查询交易编码
    virtual int ReqQryTradingCode(CThostFtdcQryTradingCodeField *pQryTradingCode, int nRequestID) = 0;

    ///请求查询合约保证金率
    virtual int
    ReqQryInstrumentMarginRate(CThostFtdcQryInstrumentMarginRateField *pQryInstrumentMarginRate, int nRequestID) = 0;

    ///请求查询合约手续费率
    virtual int ReqQryInstrumentCommissionRate(CThostFtdcQryInstrumentCommissionRateField *pQryInstrumentCommissionRate,
                                               int nRequestID) = 0;

    ///请求查询交易所
    virtual int ReqQryExchange(CThostFtdcQryExchangeField *pQryExchange, int nRequestID) = 0;

    ///请求查询产品
    virtual int ReqQryProduct(CThostFtdcQryProductField *pQryProduct, int nRequestID) = 0;

    ///请求查询合约
    virtual int ReqQryInstrument(CThostFtdcQryInstrumentField *pQryInstrument, int nRequestID) = 0;

    ///请求查询行情
    virtual int ReqQryDepthMarketData(CThostFtdcQryDepthMarketDataField *pQryDepthMarketData, int nRequestID) = 0;

    ///请求查询投资者结算结果
    virtual int ReqQrySettlementInfo(CThostFtdcQrySettlementInfoField *pQrySettlementInfo, int nRequestID) = 0;

    ///请求查询转帐银行
    virtual int ReqQryTransferBank(CThostFtdcQryTransferBankField *pQryTransferBank, int nRequestID) = 0;

    ///请求查询投资者持仓明细
    virtual int ReqQryInvestorPositionDetail(CThostFtdcQryInvestorPositionDetailField *pQryInvestorPositionDetail,
                                             int nRequestID) = 0;

    ///请求查询客户通知
    virtual int ReqQryNotice(CThostFtdcQryNoticeField *pQryNotice, int nRequestID) = 0;

    ///请求查询结算信息确认
    virtual int
    ReqQrySettlementInfoConfirm(CThostFtdcQrySettlementInfoConfirmField *pQrySettlementInfoConfirm, int nRequestID) = 0;

    ///请求查询投资者持仓明细
    virtual int ReqQryInvestorPositionCombineDetail(
            CThostFtdcQryInvestorPositionCombineDetailField *pQryInvestorPositionCombineDetail, int nRequestID) = 0;

    ///请求查询保证金监管系统经纪公司资金账户密钥
    virtual int ReqQryCFMMCTradingAccountKey(CThostFtdcQryCFMMCTradingAccountKeyField *pQryCFMMCTradingAccountKey,
                                             int nRequestID) = 0;

    ///请求查询仓单折抵信息
    virtual int ReqQryEWarrantOffset(CThostFtdcQryEWarrantOffsetField *pQryEWarrantOffset, int nRequestID) = 0;

    ///请求查询投资者品种/跨品种保证金
    virtual int
    ReqQryInvestorProductGroupMargin(CThostFtdcQryInvestorProductGroupMarginField *pQryInvestorProductGroupMargin,
                                     int nRequestID) = 0;

    ///请求查询交易所保证金率
    virtual int
    ReqQryExchangeMarginRate(CThostFtdcQryExchangeMarginRateField *pQryExchangeMarginRate, int nRequestID) = 0;

    ///请求查询交易所调整保证金率
    virtual int ReqQryExchangeMarginRateAdjust(CThostFtdcQryExchangeMarginRateAdjustField *pQryExchangeMarginRateAdjust,
                                               int nRequestID) = 0;

    ///请求查询汇率
    virtual int ReqQryExchangeRate(CThostFtdcQryExchangeRateField *pQryExchangeRate, int nRequestID) = 0;

    ///请求查询二级代理操作员银期权限
    virtual int ReqQrySecAgentACIDMap(CThostFtdcQrySecAgentACIDMapField *pQrySecAgentACIDMap, int nRequestID) = 0;

    ///请求查询产品报价汇率
    virtual int ReqQryProductExchRate(CThostFtdcQryProductExchRateField *pQryProductExchRate, int nRequestID) = 0;

    ///请求查询产品组
    virtual int ReqQryProductGroup(CThostFtdcQryProductGroupField *pQryProductGroup, int nRequestID) = 0;

    ///请求查询做市商合约手续费率
    virtual int
    ReqQryMMInstrumentCommissionRate(CThostFtdcQryMMInstrumentCommissionRateField *pQryMMInstrumentCommissionRate,
                                     int nRequestID) = 0;

    ///请求查询做市商期权合约手续费
    virtual int
    ReqQryMMOptionInstrCommRate(CThostFtdcQryMMOptionInstrCommRateField *pQryMMOptionInstrCommRate, int nRequestID) = 0;

    ///请求查询报单手续费
    virtual int ReqQryInstrumentOrderCommRate(CThostFtdcQryInstrumentOrderCommRateField *pQryInstrumentOrderCommRate,
                                              int nRequestID) = 0;

    ///请求查询期权交易成本
    virtual int
    ReqQryOptionInstrTradeCost(CThostFtdcQryOptionInstrTradeCostField *pQryOptionInstrTradeCost, int nRequestID) = 0;

    ///请求查询期权合约手续费
    virtual int
    ReqQryOptionInstrCommRate(CThostFtdcQryOptionInstrCommRateField *pQryOptionInstrCommRate, int nRequestID) = 0;

    ///请求查询执行宣告
    virtual int ReqQryExecOrder(CThostFtdcQryExecOrderField *pQryExecOrder, int nRequestID) = 0;

    ///请求查询询价
    virtual int ReqQryForQuote(CThostFtdcQryForQuoteField *pQryForQuote, int nRequestID) = 0;

    ///请求查询报价
    virtual int ReqQryQuote(CThostFtdcQryQuoteField *pQryQuote, int nRequestID) = 0;

    ///请求查询组合合约安全系数
    virtual int
    ReqQryCombInstrumentGuard(CThostFtdcQryCombInstrumentGuardField *pQryCombInstrumentGuard, int nRequestID) = 0;

    ///请求查询申请组合
    virtual int ReqQryCombAction(CThostFtdcQryCombActionField *pQryCombAction, int nRequestID) = 0;

    ///请求查询转帐流水
    virtual int ReqQryTransferSerial(CThostFtdcQryTransferSerialField *pQryTransferSerial, int nRequestID) = 0;

    ///请求查询银期签约关系
    virtual int ReqQryAccountregister(CThostFtdcQryAccountregisterField *pQryAccountregister, int nRequestID) = 0;

    ///请求查询签约银行
    virtual int ReqQryContractBank(CThostFtdcQryContractBankField *pQryContractBank, int nRequestID) = 0;

    ///请求查询预埋单
    virtual int ReqQryParkedOrder(CThostFtdcQryParkedOrderField *pQryParkedOrder, int nRequestID) = 0;

    ///请求查询预埋撤单
    virtual int ReqQryParkedOrderAction(CThostFtdcQryParkedOrderActionField *pQryParkedOrderAction, int nRequestID) = 0;

    ///请求查询交易通知
    virtual int ReqQryTradingNotice(CThostFtdcQryTradingNoticeField *pQryTradingNotice, int nRequestID) = 0;

    ///请求查询经纪公司交易参数
    virtual int
    ReqQryBrokerTradingParams(CThostFtdcQryBrokerTradingParamsField *pQryBrokerTradingParams, int nRequestID) = 0;

    ///请求查询经纪公司交易算法
    virtual int
    ReqQryBrokerTradingAlgos(CThostFtdcQryBrokerTradingAlgosField *pQryBrokerTradingAlgos, int nRequestID) = 0;

    ///请求查询监控中心用户令牌
    virtual int
    ReqQueryCFMMCTradingAccountToken(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken,
                                     int nRequestID) = 0;

    ///期货发起银行资金转期货请求
    virtual int ReqFromBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, int nRequestID) = 0;

    ///期货发起期货资金转银行请求
    virtual int ReqFromFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, int nRequestID) = 0;

    ///期货发起查询银行余额请求
    virtual int ReqQueryBankAccountMoneyByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, int nRequestID) = 0;
    """