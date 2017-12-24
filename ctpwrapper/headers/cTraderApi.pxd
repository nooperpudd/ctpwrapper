# encoding:utf-8

from ThostFtdcUserApiStruct cimport *

from libc.string cimport const_char
from libcpp cimport bool

cdef extern from "ThostFtdcTraderApi.h":
    cdef cppclass CTraderSpi "CThostFtdcTraderSpi":
        void OnFrontConnected() nogil except +

        #当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
        #@param nReason 错误原因
        #        0x1001 网络读失败
        #        0x1002 网络写失败
        #        0x2001 接收心跳超时
        #        0x2002 发送心跳失败
        #        0x2003 收到错误报文
        void OnFrontDisconnected(int nReason) nogil except +

        #心跳超时警告。当长时间未收到报文时，该方法被调用。
        #@param nTimeLapse 距离上次接收报文的时间
        void OnHeartBeatWarning(int nTimeLapse) nogil except +

        #客户端认证响应
        void OnRspAuthenticate(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo,
                               int nRequestID, bool bIsLast) nogil except +

        #登录请求响应
        void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo,
                            int nRequestID,
                            bool bIsLast) nogil except +

        #登出请求响应
        void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                             bool bIsLast) nogil except +

        #用户口令更新请求响应
        void OnRspUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate,
                                     CThostFtdcRspInfoField *pRspInfo,
                                     int nRequestID, bool bIsLast) nogil except +

        #资金账户口令更新请求响应
        void OnRspTradingAccountPasswordUpdate(
                CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate,
                CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) nogil except +

        #报单录入请求响应
        void OnRspOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                              bool bIsLast) nogil except +

        #预埋单录入请求响应
        void OnRspParkedOrderInsert(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo,
                                    int nRequestID,
                                    bool bIsLast) nogil except +

        #预埋撤单录入请求响应
        void OnRspParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction,
                                    CThostFtdcRspInfoField *pRspInfo,
                                    int nRequestID, bool bIsLast) nogil except +

        #报单操作请求响应
        void OnRspOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo,
                              int nRequestID, bool bIsLast) nogil except +

        #查询最大报单数量响应
        void OnRspQueryMaxOrderVolume(CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume,
                                      CThostFtdcRspInfoField *pRspInfo,
                                      int nRequestID, bool bIsLast) nogil except +

        #投资者结算结果确认响应
        void OnRspSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm,
                                        CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) nogil except +

        #删除预埋单响应
        void OnRspRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder,
                                    CThostFtdcRspInfoField *pRspInfo,
                                    int nRequestID, bool bIsLast) nogil except +

        #删除预埋撤单响应
        void OnRspRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction,
                                          CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) nogil except +

        #执行宣告录入请求响应
        void OnRspExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo,
                                  int nRequestID, bool bIsLast) nogil except +

        #执行宣告操作请求响应
        void OnRspExecOrderAction(CThostFtdcInputExecOrderActionField *pInputExecOrderAction,
                                  CThostFtdcRspInfoField *pRspInfo,
                                  int nRequestID, bool bIsLast) nogil except +

        #询价录入请求响应
        void OnRspForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo,
                                 int nRequestID,
                                 bool bIsLast) nogil except +

        #报价录入请求响应
        void OnRspQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                              bool bIsLast) nogil except +

        #报价操作请求响应
        void OnRspQuoteAction(CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo,
                              int nRequestID, bool bIsLast) nogil except +

        #批量报单操作请求响应
        void OnRspBatchOrderAction(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction,
                                   CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) nogil except +

        #申请组合录入请求响应
        void OnRspCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo,
                                   int nRequestID, bool bIsLast) nogil except +

        #请求查询报单响应
        void OnRspQryOrder(CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                           bool bIsLast) nogil except +

        #请求查询成交响应
        void OnRspQryTrade(CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                           bool bIsLast) nogil except +

        #请求查询投资者持仓响应
        void OnRspQryInvestorPosition(CThostFtdcInvestorPositionField *pInvestorPosition,
                                      CThostFtdcRspInfoField *pRspInfo,
                                      int nRequestID, bool bIsLast) nogil except +

        #请求查询资金账户响应
        void OnRspQryTradingAccount(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo,
                                    int nRequestID, bool bIsLast) nogil except +

        #请求查询投资者响应
        void OnRspQryInvestor(CThostFtdcInvestorField *pInvestor, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                              bool bIsLast) nogil except +

        #请求查询交易编码响应
        void OnRspQryTradingCode(CThostFtdcTradingCodeField *pTradingCode, CThostFtdcRspInfoField *pRspInfo,
                                 int nRequestID,
                                 bool bIsLast) nogil except +

        #请求查询合约保证金率响应
        void OnRspQryInstrumentMarginRate(CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate,
                                          CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) nogil except +

        #请求查询合约手续费率响应
        void OnRspQryInstrumentCommissionRate(CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate,
                                              CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                              bool bIsLast) nogil except +

        #请求查询交易所响应
        void OnRspQryExchange(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                              bool bIsLast) nogil except +

        #请求查询产品响应
        void OnRspQryProduct(CThostFtdcProductField *pProduct, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                             bool bIsLast) nogil except +

        #请求查询合约响应
        void OnRspQryInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo,
                                int nRequestID,
                                bool bIsLast) nogil except +

        #请求查询行情响应
        void OnRspQryDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo,
                                     int nRequestID, bool bIsLast) nogil except +

        #请求查询投资者结算结果响应
        void OnRspQrySettlementInfo(CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo,
                                    int nRequestID, bool bIsLast) nogil except +

        #请求查询转帐银行响应
        void OnRspQryTransferBank(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo,
                                  int nRequestID,
                                  bool bIsLast) nogil except +

        #请求查询投资者持仓明细响应
        void OnRspQryInvestorPositionDetail(CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail,
                                            CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                            bool bIsLast) nogil except +

        #请求查询客户通知响应
        void OnRspQryNotice(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                            bool bIsLast) nogil except +

        #请求查询结算信息确认响应
        void OnRspQrySettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm,
                                           CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                           bool bIsLast) nogil except +

        #请求查询投资者持仓明细响应
        void OnRspQryInvestorPositionCombineDetail(
                CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail,
                CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) nogil except +

        #查询保证金监管系统经纪公司资金账户密钥响应
        void OnRspQryCFMMCTradingAccountKey(CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey,
                                            CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                            bool bIsLast) nogil except +

        #请求查询仓单折抵信息响应
        void OnRspQryEWarrantOffset(CThostFtdcEWarrantOffsetField *pEWarrantOffset, CThostFtdcRspInfoField *pRspInfo,
                                    int nRequestID, bool bIsLast) nogil except +

        #请求查询投资者品种/跨品种保证金响应
        void OnRspQryInvestorProductGroupMargin(CThostFtdcInvestorProductGroupMarginField *pInvestorProductGroupMargin,
                                                CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                bool bIsLast) nogil except +

        #请求查询交易所保证金率响应
        void OnRspQryExchangeMarginRate(CThostFtdcExchangeMarginRateField *pExchangeMarginRate,
                                        CThostFtdcRspInfoField *pRspInfo,
                                        int nRequestID, bool bIsLast) nogil except +

        #请求查询交易所调整保证金率响应
        void OnRspQryExchangeMarginRateAdjust(CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust,
                                              CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                              bool bIsLast) nogil except +

        #请求查询汇率响应
        void OnRspQryExchangeRate(CThostFtdcExchangeRateField *pExchangeRate, CThostFtdcRspInfoField *pRspInfo,
                                  int nRequestID,
                                  bool bIsLast) nogil except +

        #请求查询二级代理操作员银期权限响应
        void OnRspQrySecAgentACIDMap(CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap, CThostFtdcRspInfoField *pRspInfo,
                                     int nRequestID, bool bIsLast) nogil except +

        #请求查询产品报价汇率
        void OnRspQryProductExchRate(CThostFtdcProductExchRateField *pProductExchRate, CThostFtdcRspInfoField *pRspInfo,
                                     int nRequestID, bool bIsLast) nogil except +

        #请求查询产品组
        void OnRspQryProductGroup(CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo,
                                  int nRequestID,
                                  bool bIsLast) nogil except +

        #请求查询做市商合约手续费率响应
        void OnRspQryMMInstrumentCommissionRate(CThostFtdcMMInstrumentCommissionRateField *pMMInstrumentCommissionRate,
                                                CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                bool bIsLast) nogil except +

        #请求查询做市商期权合约手续费响应
        void OnRspQryMMOptionInstrCommRate(CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate,
                                           CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                           bool bIsLast) nogil except +

        #请求查询报单手续费响应
        void OnRspQryInstrumentOrderCommRate(CThostFtdcInstrumentOrderCommRateField *pInstrumentOrderCommRate,
                                             CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                             bool bIsLast) nogil except +

        #请求查询期权交易成本响应
        void OnRspQryOptionInstrTradeCost(CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost,
                                          CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) nogil except +

        #请求查询期权合约手续费响应
        void OnRspQryOptionInstrCommRate(CThostFtdcOptionInstrCommRateField *pOptionInstrCommRate,
                                         CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) nogil except +

        #请求查询执行宣告响应
        void OnRspQryExecOrder(CThostFtdcExecOrderField *pExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                               bool bIsLast) nogil except +

        #请求查询询价响应
        void OnRspQryForQuote(CThostFtdcForQuoteField *pForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                              bool bIsLast) nogil except +

        #请求查询报价响应
        void OnRspQryQuote(CThostFtdcQuoteField *pQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                           bool bIsLast) nogil except +

        #请求查询组合合约安全系数响应
        void OnRspQryCombInstrumentGuard(CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard,
                                         CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) nogil except +

        #请求查询申请组合响应
        void OnRspQryCombAction(CThostFtdcCombActionField *pCombAction, CThostFtdcRspInfoField *pRspInfo,
                                int nRequestID,
                                bool bIsLast) nogil except +

        #请求查询转帐流水响应
        void OnRspQryTransferSerial(CThostFtdcTransferSerialField *pTransferSerial, CThostFtdcRspInfoField *pRspInfo,
                                    int nRequestID, bool bIsLast) nogil except +

        #请求查询银期签约关系响应
        void OnRspQryAccountregister(CThostFtdcAccountregisterField *pAccountregister, CThostFtdcRspInfoField *pRspInfo,
                                     int nRequestID, bool bIsLast) nogil except +

        #错误应答
        void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) nogil except +

        #报单通知
        void OnRtnOrder(CThostFtdcOrderField *pOrder) nogil except +

        #成交通知
        void OnRtnTrade(CThostFtdcTradeField *pTrade) nogil except +

        #报单录入错误回报
        void OnErrRtnOrderInsert(CThostFtdcInputOrderField *pInputOrder,
                                 CThostFtdcRspInfoField *pRspInfo) nogil except +

        #报单操作错误回报
        void OnErrRtnOrderAction(CThostFtdcOrderActionField *pOrderAction,
                                 CThostFtdcRspInfoField *pRspInfo) nogil except +

        #合约交易状态通知
        void OnRtnInstrumentStatus(CThostFtdcInstrumentStatusField *pInstrumentStatus) nogil except +

        #交易所公告通知
        void OnRtnBulletin(CThostFtdcBulletinField *pBulletin) nogil except +

        #交易通知
        void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) nogil except +

        #提示条件单校验错误
        void OnRtnErrorConditionalOrder(CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder) nogil except +

        #执行宣告通知
        void OnRtnExecOrder(CThostFtdcExecOrderField *pExecOrder) nogil except +

        #执行宣告录入错误回报
        void OnErrRtnExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder,
                                     CThostFtdcRspInfoField *pRspInfo) nogil except +

        #执行宣告操作错误回报
        void OnErrRtnExecOrderAction(CThostFtdcExecOrderActionField *pExecOrderAction,
                                     CThostFtdcRspInfoField *pRspInfo) nogil except +

        #询价录入错误回报
        void OnErrRtnForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote,
                                    CThostFtdcRspInfoField *pRspInfo) nogil except +

        #报价通知
        void OnRtnQuote(CThostFtdcQuoteField *pQuote) nogil except +

        #报价录入错误回报
        void OnErrRtnQuoteInsert(CThostFtdcInputQuoteField *pInputQuote,
                                 CThostFtdcRspInfoField *pRspInfo) nogil except +

        #报价操作错误回报
        void OnErrRtnQuoteAction(CThostFtdcQuoteActionField *pQuoteAction,
                                 CThostFtdcRspInfoField *pRspInfo) nogil except +

        #询价通知
        void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) nogil except +

        #保证金监控中心用户令牌
        void OnRtnCFMMCTradingAccountToken(
                CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken) nogil except +

        #批量报单操作错误回报
        void OnErrRtnBatchOrderAction(CThostFtdcBatchOrderActionField *pBatchOrderAction,
                                      CThostFtdcRspInfoField *pRspInfo) nogil except +

        #申请组合通知
        void OnRtnCombAction(CThostFtdcCombActionField *pCombAction) nogil except +

        #申请组合录入错误回报
        void OnErrRtnCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction,
                                      CThostFtdcRspInfoField *pRspInfo) nogil except +

        #请求查询签约银行响应
        void OnRspQryContractBank(CThostFtdcContractBankField *pContractBank, CThostFtdcRspInfoField *pRspInfo,
                                  int nRequestID,
                                  bool bIsLast) nogil except +

        #请求查询预埋单响应
        void OnRspQryParkedOrder(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo,
                                 int nRequestID,
                                 bool bIsLast) nogil except +

        #请求查询预埋撤单响应
        void OnRspQryParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction,
                                       CThostFtdcRspInfoField *pRspInfo,
                                       int nRequestID, bool bIsLast) nogil except +

        #请求查询交易通知响应
        void OnRspQryTradingNotice(CThostFtdcTradingNoticeField *pTradingNotice, CThostFtdcRspInfoField *pRspInfo,
                                   int nRequestID, bool bIsLast) nogil except +

        #请求查询经纪公司交易参数响应
        void OnRspQryBrokerTradingParams(CThostFtdcBrokerTradingParamsField *pBrokerTradingParams,
                                         CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) nogil except +

        #请求查询经纪公司交易算法响应
        void OnRspQryBrokerTradingAlgos(CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos,
                                        CThostFtdcRspInfoField *pRspInfo,
                                        int nRequestID, bool bIsLast) nogil except +

        #请求查询监控中心用户令牌
        void OnRspQueryCFMMCTradingAccountToken(
                CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken,
                CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) nogil except +

        #银行发起银行资金转期货通知
        void OnRtnFromBankToFutureByBank(CThostFtdcRspTransferField *pRspTransfer) nogil except +

        #银行发起期货资金转银行通知
        void OnRtnFromFutureToBankByBank(CThostFtdcRspTransferField *pRspTransfer) nogil except +

        #银行发起冲正银行转期货通知
        void OnRtnRepealFromBankToFutureByBank(CThostFtdcRspRepealField *pRspRepeal) nogil except +

        #银行发起冲正期货转银行通知
        void OnRtnRepealFromFutureToBankByBank(CThostFtdcRspRepealField *pRspRepeal) nogil except +

        #期货发起银行资金转期货通知
        void OnRtnFromBankToFutureByFuture(CThostFtdcRspTransferField *pRspTransfer) nogil except +

        #期货发起期货资金转银行通知
        void OnRtnFromFutureToBankByFuture(CThostFtdcRspTransferField *pRspTransfer) nogil except +

        #系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
        void OnRtnRepealFromBankToFutureByFutureManual(CThostFtdcRspRepealField *pRspRepeal) nogil except +

        #系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
        void OnRtnRepealFromFutureToBankByFutureManual(CThostFtdcRspRepealField *pRspRepeal) nogil except +

        #期货发起查询银行余额通知
        void OnRtnQueryBankBalanceByFuture(CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount) nogil except +

        #期货发起银行资金转期货错误回报
        void OnErrRtnBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer,
                                          CThostFtdcRspInfoField *pRspInfo) nogil except +

        #期货发起期货资金转银行错误回报
        void OnErrRtnFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer,
                                          CThostFtdcRspInfoField *pRspInfo) nogil except +

        #系统运行时期货端手工发起冲正银行转期货错误回报
        void OnErrRtnRepealBankToFutureByFutureManual(CThostFtdcReqRepealField *pReqRepeal,
                                                      CThostFtdcRspInfoField *pRspInfo) nogil except +

        #系统运行时期货端手工发起冲正期货转银行错误回报
        void OnErrRtnRepealFutureToBankByFutureManual(CThostFtdcReqRepealField *pReqRepeal,
                                                      CThostFtdcRspInfoField *pRspInfo) nogil except +

        #期货发起查询银行余额错误回报
        void OnErrRtnQueryBankBalanceByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount,
                                              CThostFtdcRspInfoField *pRspInfo) nogil except +

        #期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
        void OnRtnRepealFromBankToFutureByFuture(CThostFtdcRspRepealField *pRspRepeal) nogil except +

        #期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
        void OnRtnRepealFromFutureToBankByFuture(CThostFtdcRspRepealField *pRspRepeal) nogil except +

        #期货发起银行资金转期货应答
        void OnRspFromBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo,
                                           int nRequestID, bool bIsLast) nogil except +

        #期货发起期货资金转银行应答
        void OnRspFromFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo,
                                           int nRequestID, bool bIsLast) nogil except +

        #期货发起查询银行余额应答
        void OnRspQueryBankAccountMoneyByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount,
                                                CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                bool bIsLast) nogil except +

        #银行发起银期开户通知
        void OnRtnOpenAccountByBank(CThostFtdcOpenAccountField *pOpenAccount) nogil except +

        #银行发起银期销户通知
        void OnRtnCancelAccountByBank(CThostFtdcCancelAccountField *pCancelAccount) nogil except +

        #银行发起变更银行账号通知
        void OnRtnChangeAccountByBank(CThostFtdcChangeAccountField *pChangeAccount) nogil except +

    cdef cppclass CTraderApi "CThostFtdcTraderApi":
        # 删除接口对象本身
        #@remark 不再使用本接口对象时,调用该函数删除接口对象
        void Release() nogil

        #初始化
        #@remark 初始化运行环境,只有调用后,接口才开始工作
        void Init() nogil

        #等待接口线程结束运行
        #@return 线程退出代码
        int Join() nogil

        #获取当前交易日
        #@retrun 获取到的交易日
        #@remark 只有登录成功后,才能得到正确的交易日
        const_char *GetTradingDay() nogil except +

        #注册前置机网络地址
        #@param pszFrontAddress：前置机网络地址。
        #@remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。
        #@remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
        void RegisterFront(char *pszFrontAddress) nogil except +

        #注册名字服务器网络地址
        #@param pszNsAddress：名字服务器网络地址。
        #@remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:12001”。
        #@remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”12001”代表服务器端口号。
        #@remark RegisterNameServer优先于RegisterFront
        void RegisterNameServer(char *pszNsAddress) nogil except +

        #注册名字服务器用户信息
        #@param pFensUserInfo：用户信息。
        void RegisterFensUserInfo(CThostFtdcFensUserInfoField *pFensUserInfo) nogil except +

        #注册回调接口
        #@param pSpi 派生自回调接口类的实例
        # todo
        # void RegisterSpi(CThostFtdcTraderSpi *pSpi) nogil except +

        #订阅私有流。
        #@param nResumeType 私有流重传方式
        #        THOST_TERT_RESTART:从本交易日开始重传
        #        THOST_TERT_RESUME:从上次收到的续传
        #        THOST_TERT_QUICK:只传送登录后私有流的内容
        #@remark 该方法要在Init方法前调用。若不调用则不会收到私有流的数据。
        void SubscribePrivateTopic(THOST_TE_RESUME_TYPE nResumeType) nogil except +

        #订阅公共流。
        #@param nResumeType 公共流重传方式
        #        THOST_TERT_RESTART:从本交易日开始重传
        #        THOST_TERT_RESUME:从上次收到的续传
        #        THOST_TERT_QUICK:只传送登录后公共流的内容
        #@remark 该方法要在Init方法前调用。若不调用则不会收到公共流的数据。
        void SubscribePublicTopic(THOST_TE_RESUME_TYPE nResumeType) nogil except +

        #客户端认证请求
        int ReqAuthenticate(CThostFtdcReqAuthenticateField *pReqAuthenticateField, int nRequestID) nogil except +

        #用户登录请求
        int ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLoginField, int nRequestID) nogil except +

        #登出请求
        int ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout, int nRequestID) nogil except +

        #用户口令更新请求
        int ReqUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, int nRequestID) nogil except +

        #资金账户口令更新请求
        int ReqTradingAccountPasswordUpdate(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate,
                                            int nRequestID) nogil except +

        #报单录入请求
        int ReqOrderInsert(CThostFtdcInputOrderField *pInputOrder, int nRequestID) nogil except +

        #预埋单录入请求
        int ReqParkedOrderInsert(CThostFtdcParkedOrderField *pParkedOrder, int nRequestID) nogil except +

        #预埋撤单录入请求
        int ReqParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, int nRequestID) nogil except +

        #报单操作请求
        int ReqOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, int nRequestID) nogil except +

        #查询最大报单数量请求
        int ReqQueryMaxOrderVolume(CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume,
                                   int nRequestID) nogil except +

        #投资者结算结果确认
        int ReqSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm,
                                     int nRequestID) nogil except +

        #请求删除预埋单
        int ReqRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, int nRequestID) nogil except +

        #请求删除预埋撤单
        int ReqRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction,
                                       int nRequestID) nogil except +

        #执行宣告录入请求
        int ReqExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, int nRequestID) nogil except +

        #执行宣告操作请求
        int ReqExecOrderAction(CThostFtdcInputExecOrderActionField *pInputExecOrderAction,
                               int nRequestID) nogil except +

        #询价录入请求
        int ReqForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, int nRequestID) nogil except +

        #报价录入请求
        int ReqQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, int nRequestID) nogil except +

        #报价操作请求
        int ReqQuoteAction(CThostFtdcInputQuoteActionField *pInputQuoteAction, int nRequestID) nogil except +

        #批量报单操作请求
        int ReqBatchOrderAction(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction,
                                int nRequestID) nogil except +

        #申请组合录入请求
        int ReqCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, int nRequestID) nogil except +

        #请求查询报单
        int ReqQryOrder(CThostFtdcQryOrderField *pQryOrder, int nRequestID) nogil except +

        #请求查询成交
        int ReqQryTrade(CThostFtdcQryTradeField *pQryTrade, int nRequestID) nogil except +

        #请求查询投资者持仓
        int ReqQryInvestorPosition(CThostFtdcQryInvestorPositionField *pQryInvestorPosition,
                                   int nRequestID) nogil except +

        #请求查询资金账户
        int ReqQryTradingAccount(CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID) nogil except +

        #请求查询投资者
        int ReqQryInvestor(CThostFtdcQryInvestorField *pQryInvestor, int nRequestID) nogil except +

        #请求查询交易编码
        int ReqQryTradingCode(CThostFtdcQryTradingCodeField *pQryTradingCode, int nRequestID) nogil except +

        #请求查询合约保证金率
        int ReqQryInstrumentMarginRate(CThostFtdcQryInstrumentMarginRateField *pQryInstrumentMarginRate,
                                       int nRequestID) nogil except +

        #请求查询合约手续费率
        int ReqQryInstrumentCommissionRate(CThostFtdcQryInstrumentCommissionRateField *pQryInstrumentCommissionRate,
                                           int nRequestID) nogil except +

        #请求查询交易所
        int ReqQryExchange(CThostFtdcQryExchangeField *pQryExchange, int nRequestID) nogil except +

        #请求查询产品
        int ReqQryProduct(CThostFtdcQryProductField *pQryProduct, int nRequestID) nogil except +

        #请求查询合约
        int ReqQryInstrument(CThostFtdcQryInstrumentField *pQryInstrument, int nRequestID) nogil except +

        #请求查询行情
        int ReqQryDepthMarketData(CThostFtdcQryDepthMarketDataField *pQryDepthMarketData, int nRequestID) nogil except +

        #请求查询投资者结算结果
        int ReqQrySettlementInfo(CThostFtdcQrySettlementInfoField *pQrySettlementInfo, int nRequestID) nogil except +

        #请求查询转帐银行
        int ReqQryTransferBank(CThostFtdcQryTransferBankField *pQryTransferBank, int nRequestID) nogil except +

        #请求查询投资者持仓明细
        int ReqQryInvestorPositionDetail(CThostFtdcQryInvestorPositionDetailField *pQryInvestorPositionDetail,
                                         int nRequestID) nogil except +

        #请求查询客户通知
        int ReqQryNotice(CThostFtdcQryNoticeField *pQryNotice, int nRequestID) nogil except +

        #请求查询结算信息确认
        int ReqQrySettlementInfoConfirm(CThostFtdcQrySettlementInfoConfirmField *pQrySettlementInfoConfirm,
                                        int nRequestID) nogil except +

        #请求查询投资者持仓明细
        int ReqQryInvestorPositionCombineDetail(
                CThostFtdcQryInvestorPositionCombineDetailField *pQryInvestorPositionCombineDetail,
                int nRequestID) nogil except +

        #请求查询保证金监管系统经纪公司资金账户密钥
        int ReqQryCFMMCTradingAccountKey(CThostFtdcQryCFMMCTradingAccountKeyField *pQryCFMMCTradingAccountKey,
                                         int nRequestID) nogil except +

        #请求查询仓单折抵信息
        int ReqQryEWarrantOffset(CThostFtdcQryEWarrantOffsetField *pQryEWarrantOffset, int nRequestID) nogil except +

        #请求查询投资者品种/跨品种保证金
        int ReqQryInvestorProductGroupMargin(
                CThostFtdcQryInvestorProductGroupMarginField *pQryInvestorProductGroupMargin,
                int nRequestID) nogil except +

        #请求查询交易所保证金率
        int ReqQryExchangeMarginRate(CThostFtdcQryExchangeMarginRateField *pQryExchangeMarginRate,
                                     int nRequestID) nogil except +

        #请求查询交易所调整保证金率
        int ReqQryExchangeMarginRateAdjust(CThostFtdcQryExchangeMarginRateAdjustField *pQryExchangeMarginRateAdjust,
                                           int nRequestID) nogil except +

        #请求查询汇率
        int ReqQryExchangeRate(CThostFtdcQryExchangeRateField *pQryExchangeRate, int nRequestID) nogil except +

        #请求查询二级代理操作员银期权限
        int ReqQrySecAgentACIDMap(CThostFtdcQrySecAgentACIDMapField *pQrySecAgentACIDMap, int nRequestID) nogil except +

        #请求查询产品报价汇率
        int ReqQryProductExchRate(CThostFtdcQryProductExchRateField *pQryProductExchRate, int nRequestID) nogil except +

        #请求查询产品组
        int ReqQryProductGroup(CThostFtdcQryProductGroupField *pQryProductGroup, int nRequestID) nogil except +

        #请求查询做市商合约手续费率
        int ReqQryMMInstrumentCommissionRate(
                CThostFtdcQryMMInstrumentCommissionRateField *pQryMMInstrumentCommissionRate,
                int nRequestID) nogil except +

        #请求查询做市商期权合约手续费
        int ReqQryMMOptionInstrCommRate(CThostFtdcQryMMOptionInstrCommRateField *pQryMMOptionInstrCommRate,
                                        int nRequestID) nogil except +

        #请求查询报单手续费
        int ReqQryInstrumentOrderCommRate(CThostFtdcQryInstrumentOrderCommRateField *pQryInstrumentOrderCommRate,
                                          int nRequestID) nogil except +

        #请求查询期权交易成本
        int ReqQryOptionInstrTradeCost(CThostFtdcQryOptionInstrTradeCostField *pQryOptionInstrTradeCost,
                                       int nRequestID) nogil except +

        #请求查询期权合约手续费
        int ReqQryOptionInstrCommRate(CThostFtdcQryOptionInstrCommRateField *pQryOptionInstrCommRate,
                                      int nRequestID) nogil except +

        #请求查询执行宣告
        int ReqQryExecOrder(CThostFtdcQryExecOrderField *pQryExecOrder, int nRequestID) nogil except +

        #请求查询询价
        int ReqQryForQuote(CThostFtdcQryForQuoteField *pQryForQuote, int nRequestID) nogil except +

        #请求查询报价
        int ReqQryQuote(CThostFtdcQryQuoteField *pQryQuote, int nRequestID) nogil except +

        #请求查询组合合约安全系数
        int ReqQryCombInstrumentGuard(CThostFtdcQryCombInstrumentGuardField *pQryCombInstrumentGuard,
                                      int nRequestID) nogil except +

        #请求查询申请组合
        int ReqQryCombAction(CThostFtdcQryCombActionField *pQryCombAction, int nRequestID) nogil except +

        #请求查询转帐流水
        int ReqQryTransferSerial(CThostFtdcQryTransferSerialField *pQryTransferSerial, int nRequestID) nogil except +

        #请求查询银期签约关系
        int ReqQryAccountregister(CThostFtdcQryAccountregisterField *pQryAccountregister, int nRequestID) nogil except +

        #请求查询签约银行
        int ReqQryContractBank(CThostFtdcQryContractBankField *pQryContractBank, int nRequestID) nogil except +

        #请求查询预埋单
        int ReqQryParkedOrder(CThostFtdcQryParkedOrderField *pQryParkedOrder, int nRequestID) nogil except +

        #请求查询预埋撤单
        int ReqQryParkedOrderAction(CThostFtdcQryParkedOrderActionField *pQryParkedOrderAction,
                                    int nRequestID) nogil except +

        #请求查询交易通知
        int ReqQryTradingNotice(CThostFtdcQryTradingNoticeField *pQryTradingNotice, int nRequestID) nogil except +

        #请求查询经纪公司交易参数
        int ReqQryBrokerTradingParams(CThostFtdcQryBrokerTradingParamsField *pQryBrokerTradingParams,
                                      int nRequestID) nogil except +

        #请求查询经纪公司交易算法
        int ReqQryBrokerTradingAlgos(CThostFtdcQryBrokerTradingAlgosField *pQryBrokerTradingAlgos,
                                     int nRequestID) nogil except +

        #请求查询监控中心用户令牌
        int ReqQueryCFMMCTradingAccountToken(
                CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken,
                int nRequestID) nogil except +

        #期货发起银行资金转期货请求
        int ReqFromBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, int nRequestID) nogil except +

        #期货发起期货资金转银行请求
        int ReqFromFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, int nRequestID) nogil except +

        #期货发起查询银行余额请求
        int ReqQueryBankAccountMoneyByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount,
                                             int nRequestID) nogil except +
