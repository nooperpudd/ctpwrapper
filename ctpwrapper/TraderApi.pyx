# encoding:utf-8
# distutils: language = c++
# cython: nonecheck=True
# cython: profile=False
# cython: binding=True

import ctypes

from cpython cimport PyObject
from libc.string cimport const_char
# from libc cimport stdlib

from headers.cTraderApi cimport CTraderSpi, CTraderApi, CreateFtdcTraderApi
from headers.ThostFtdcUserApiStruct cimport *


class TraderApiWrapper:
    cdef CTraderApi *_api
    cdef CTraderSpi *_spi

    def __cinit__(self):
        self._api = NULL
        self._spi = NULL

    def __dealloc__(self):
        self.Release()

    def Create(self, const_char *pszFlowPath):

        self._api = CreateFtdcTraderApi(pszFlowPath)

        if not self._api:
            raise MemoryError()

    @staticmethod
    def GetApiVersion():
        return CTraderApi.GetApiVersion()

    def Release(self):

        if self._api is not NULL:
            self._api.RegisterSpi(NULL)
            self._api.Release()
            self._api = NULL
            self._spi = NULL

    def Init(self):
        if self._api is not NULL:
            self._spi = new CTraderSpi(<PyObject *> self)

            with nogil:
                self._api.RegisterSpi(self._spi)
                self._api.Init()

    def Join(self):

        cdef int result
        if self._spi is not NULL:
            with nogil:
                result = self._api.Join()
            return result

    def GetTradingDay(self):

        cdef const_char *result

        if self._spi is not NULL:
            result = self._api.GetTradingDay()
            return result

    def RegisterFront(self, char *pszFrontAddress):

        if self._api is not NULL:
            with nogil:
                self._api.RegisterFront(pszFrontAddress)

    def RegisterNameServer(self, char *pszNsAddress):
        if self._api is not NULL:
            with nogil:
                self._api.RegisterNameServer(pszNsAddress)

    def RegisterFensUserInfo(self, pFensUserInfo):
        if self._api is not NULL:
            with nogil:
                self._api.RegisterFensUserInfo(<CThostFtdcFensUserInfoField *> <size_t> ctypes.addressof(pFensUserInfo))

    def SubscribePrivateTopic(self, THOST_TE_RESUME_TYPE nResumeType):
        if self._api is not NULL:
            with nogil:
                self._api.SubscribePrivateTopic(nResumeType)
    #订阅公共流。
    #@param nResumeType 公共流重传方式
    #        THOST_TERT_RESTART:从本交易日开始重传
    #        THOST_TERT_RESUME:从上次收到的续传
    #        THOST_TERT_QUICK:只传送登录后公共流的内容
    #@remark 该方法要在Init方法前调用。若不调用则不会收到公共流的数据。
    def SubscribePublicTopic(self, THOST_TE_RESUME_TYPE nResumeType):
        if self._api is not NULL:
            with nogil:
                self._api.SubscribePublicTopic(nResumeType)
            
    #客户端认证请求
    def ReqAuthenticate(self, pReqAuthenticateField, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqAuthenticate(<CThostFtdcReqAuthenticateField *> <size_t> ctypes.addressof(pReqAuthenticateField), nRequestID)
            return result

    #用户登录请求
    def ReqUserLogin(self, pReqUserLoginField, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqUserLogin(<CThostFtdcReqUserLoginField *> <size_t> ctypes.addressof(pReqUserLoginField), nRequestID)
            return result
    #登出请求
    def ReqUserLogout(self, pUserLogout, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqUserLogout(<CThostFtdcUserLogoutField *> <size_t> ctypes.addressof(pUserLogout),nRequestID)
            return result
    #用户口令更新请求
    def ReqUserPasswordUpdate(self, pUserPasswordUpdate, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqUserPasswordUpdate(<CThostFtdcUserPasswordUpdateField *> <size_t> ctypes.addressof(pUserPasswordUpdate), nRequestID)
            return result
    #资金账户口令更新请求
    def ReqTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqTradingAccountPasswordUpdate(<CThostFtdcTradingAccountPasswordUpdateField *> <size_t> ctypes.addressof(pTradingAccountPasswordUpdate), nRequestID)
            return result
        #报单录入请求
    def ReqOrderInsert(self, pInputOrder, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqOrderInsert(<CThostFtdcInputOrderField *> <size_t> ctypes.addressof(pInputOrder),nRequestID)
            return result
        #预埋单录入请求
    def ReqParkedOrderInsert(self, pParkedOrder, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqParkedOrderInsert(<CThostFtdcParkedOrderField *> <size_t> ctypes.addressof(pParkedOrder), nRequestID)
            return result
        #预埋撤单录入请求
    def ReqParkedOrderAction(self, pParkedOrderAction, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqParkedOrderAction(<CThostFtdcParkedOrderActionField *> <size_t> ctypes.addressof(pParkedOrderAction), nRequestID)
            return result
        #报单操作请求
    def ReqOrderAction(self, pInputOrderAction, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqOrderAction(<CThostFtdcInputOrderActionField *> <size_t> ctypes.addressof(pInputOrderAction), nRequestID)
            return result
        #查询最大报单数量请求
    def ReqQueryMaxOrderVolume(self, pQueryMaxOrderVolume,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQueryMaxOrderVolume(<CThostFtdcQueryMaxOrderVolumeField *> <size_t> ctypes.addressof(pQueryMaxOrderVolume), nRequestID)
            return result
        #投资者结算结果确认
    def ReqSettlementInfoConfirm(self, pSettlementInfoConfirm,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqSettlementInfoConfirm(<CThostFtdcSettlementInfoConfirmField *> <size_t> ctypes.addressof(pSettlementInfoConfirm), nRequestID)
            return result
        #请求删除预埋单
    def ReqRemoveParkedOrder(self, pRemoveParkedOrder, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqRemoveParkedOrder(<CThostFtdcRemoveParkedOrderField *> <size_t> ctypes.addressof(pRemoveParkedOrder), nRequestID)
            return result
        #请求删除预埋撤单
    def ReqRemoveParkedOrderAction(self, pRemoveParkedOrderAction,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqRemoveParkedOrderAction(<CThostFtdcRemoveParkedOrderActionField *> <size_t> ctypes.addressof(pRemoveParkedOrderAction),nRequestID)
            return result
        #执行宣告录入请求
    def ReqExecOrderInsert(self, pInputExecOrder, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqExecOrderInsert(<CThostFtdcInputExecOrderField *> <size_t> ctypes.addressof(pInputExecOrder), nRequestID)
            return result
        #执行宣告操作请求
    def ReqExecOrderAction(self, pInputExecOrderAction,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqExecOrderAction(<CThostFtdcInputExecOrderActionField *> <size_t> ctypes.addressof(pInputExecOrderAction), nRequestID)
            return result
        #询价录入请求
    def ReqForQuoteInsert(self, pInputForQuote, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqForQuoteInsert(<CThostFtdcInputForQuoteField *> <size_t> ctypes.addressof(pInputForQuote), nRequestID)
            return result
        #报价录入请求
    def ReqQuoteInsert(self, pInputQuote, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQuoteInsert(<CThostFtdcInputQuoteField *> <size_t> ctypes.addressof(pInputQuote),nRequestID)
            return result
        #报价操作请求
    def ReqQuoteAction(self, pInputQuoteAction, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQuoteAction(<CThostFtdcInputQuoteActionField *> <size_t> ctypes.addressof(pInputQuoteAction), nRequestID)
            return result
        #批量报单操作请求
    def ReqBatchOrderAction(self, pInputBatchOrderAction,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqBatchOrderAction(<CThostFtdcInputBatchOrderActionField *> <size_t> ctypes.addressof(pInputBatchOrderAction), nRequestID)
            return result
        #申请组合录入请求
    def ReqCombActionInsert(self, pInputCombAction, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqCombActionInsert(<CThostFtdcInputCombActionField *> <size_t> ctypes.addressof(pInputCombAction), nRequestID)
            return result
        #请求查询报单
    def ReqQryOrder(self, pQryOrder, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryOrder(<CThostFtdcQryOrderField *> <size_t> ctypes.addressof(pQryOrder), nRequestID)
            return result
        #请求查询成交
    def ReqQryTrade(self, pQryTrade, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryTrade(<CThostFtdcQryTradeField *> <size_t> ctypes.addressof(pQryTrade), nRequestID)
            return result
        #请求查询投资者持仓
    def ReqQryInvestorPosition(self, pQryInvestorPosition,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryInvestorPosition(<CThostFtdcQryInvestorPositionField *> <size_t> ctypes.addressof(pQryInvestorPosition), nRequestID)
            return result
        #请求查询资金账户
    def ReqQryTradingAccount(self, pQryTradingAccount, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryTradingAccount(<CThostFtdcQryTradingAccountField *> <size_t> ctypes.addressof(pQryTradingAccount), nRequestID)
            return result
        #请求查询投资者
    def ReqQryInvestor(self, pQryInvestor, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryInvestor(<CThostFtdcQryInvestorField *> <size_t> ctypes.addressof(pQryInvestor),nRequestID)
            return result
        #请求查询交易编码
    def ReqQryTradingCode(self, pQryTradingCode, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryTradingCode(<CThostFtdcQryTradingCodeField *> <size_t> ctypes.addressof(pQryTradingCode), nRequestID)
            return result
        #请求查询合约保证金率
    def ReqQryInstrumentMarginRate(self, pQryInstrumentMarginRate,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryInstrumentMarginRate(<CThostFtdcQryInstrumentMarginRateField *> <size_t> ctypes.addressof(pQryInstrumentMarginRate),nRequestID)
            return result
        #请求查询合约手续费率
    def ReqQryInstrumentCommissionRate(self, pQryInstrumentCommissionRate,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryInstrumentCommissionRate(<CThostFtdcQryInstrumentCommissionRateField *> <size_t> ctypes.addressof(pQryInstrumentCommissionRate), nRequestID)
            return result
        #请求查询交易所
    def ReqQryExchange(self, pQryExchange, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryExchange(<CThostFtdcQryExchangeField *> <size_t> ctypes.addressof(pQryExchange), nRequestID)
            return result
        #请求查询产品
    def ReqQryProduct(self, pQryProduct, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryProduct(<CThostFtdcQryProductField *> <size_t> ctypes.addressof(pQryProduct), nRequestID)
            return result
        #请求查询合约
    def ReqQryInstrument(self, pQryInstrument, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryInstrument(<CThostFtdcQryInstrumentField *> <size_t> ctypes.addressof(pQryInstrument), nRequestID)
            return result
        #请求查询行情
    def ReqQryDepthMarketData(self, pQryDepthMarketData, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryDepthMarketData(<CThostFtdcQryDepthMarketDataField *> <size_t> ctypes.addressof(pQryDepthMarketData), nRequestID)
            return result
        #请求查询投资者结算结果
    def ReqQrySettlementInfo(self, pQrySettlementInfo, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQrySettlementInfo(<CThostFtdcQrySettlementInfoField *> <size_t> ctypes.addressof(pQrySettlementInfo), nRequestID)
            return result
        #请求查询转帐银行
    def ReqQryTransferBank(self, pQryTransferBank, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryTransferBank(<CThostFtdcQryTransferBankField *> <size_t> ctypes.addressof(pQryTransferBank), nRequestID)
            return result
        #请求查询投资者持仓明细
    def ReqQryInvestorPositionDetail(self, pQryInvestorPositionDetail,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryInvestorPositionDetail(<CThostFtdcQryInvestorPositionDetailField *> <size_t> ctypes.addressof(pQryInvestorPositionDetail),nRequestID)
            return result
        #请求查询客户通知
    def ReqQryNotice(self, pQryNotice, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryNotice(<CThostFtdcQryNoticeField *> <size_t> ctypes.addressof(pQryNotice), nRequestID)
            return result
        #请求查询结算信息确认
    def ReqQrySettlementInfoConfirm(self, pQrySettlementInfoConfirm,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQrySettlementInfoConfirm(<CThostFtdcQrySettlementInfoConfirmField *> <size_t> ctypes.addressof(pQrySettlementInfoConfirm),nRequestID)
            return result
        #请求查询投资者持仓明细
    def ReqQryInvestorPositionCombineDetail(self, pQryInvestorPositionCombineDetail,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryInvestorPositionCombineDetail(<CThostFtdcQryInvestorPositionCombineDetailField *> <size_t> ctypes.addressof(pQryInvestorPositionCombineDetail), nRequestID)
            return result
        #请求查询保证金监管系统经纪公司资金账户密钥
    def ReqQryCFMMCTradingAccountKey(self, pQryCFMMCTradingAccountKey,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryCFMMCTradingAccountKey(<CThostFtdcQryCFMMCTradingAccountKeyField *> <size_t> ctypes.addressof(pQryCFMMCTradingAccountKey),nRequestID)
            return result
        #请求查询仓单折抵信息
    def ReqQryEWarrantOffset(self, pQryEWarrantOffset, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryEWarrantOffset(<CThostFtdcQryEWarrantOffsetField *> <size_t> ctypes.addressof(pQryEWarrantOffset), nRequestID)
            return result
        #请求查询投资者品种/跨品种保证金
    def ReqQryInvestorProductGroupMargin(self, pQryInvestorProductGroupMargin,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryInvestorProductGroupMargin(<CThostFtdcQryInvestorProductGroupMarginField *> <size_t> ctypes.addressof(pQryInvestorProductGroupMargin), nRequestID)
            return result
        #请求查询交易所保证金率
    def ReqQryExchangeMarginRate(self, pQryExchangeMarginRate,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryExchangeMarginRate(<CThostFtdcQryExchangeMarginRateField *> <size_t> ctypes.addressof(pQryExchangeMarginRate),nRequestID)
            return result
        #请求查询交易所调整保证金率
    def ReqQryExchangeMarginRateAdjust(self, pQryExchangeMarginRateAdjust,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryExchangeMarginRateAdjust(<CThostFtdcQryExchangeMarginRateAdjustField *> <size_t> ctypes.addressof(pQryExchangeMarginRateAdjust), nRequestID)
            return result
        #请求查询汇率
    def ReqQryExchangeRate(self, pQryExchangeRate, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryExchangeRate(<CThostFtdcQryExchangeRateField *> <size_t> ctypes.addressof(pQryExchangeRate), nRequestID)
            return result
        #请求查询二级代理操作员银期权限
    def ReqQrySecAgentACIDMap(self, pQrySecAgentACIDMap, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQrySecAgentACIDMap(<CThostFtdcQrySecAgentACIDMapField *> <size_t> ctypes.addressof(pQrySecAgentACIDMap), nRequestID)
            return result
        #请求查询产品报价汇率
    def ReqQryProductExchRate(self, pQryProductExchRate, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryProductExchRate(<CThostFtdcQryProductExchRateField *> <size_t> ctypes.addressof(pQryProductExchRate), nRequestID)
            return result
        #请求查询产品组
    def ReqQryProductGroup(self, pQryProductGroup, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryProductGroup(<CThostFtdcQryProductGroupField *> <size_t> ctypes.addressof(pQryProductGroup), nRequestID)
            return result
        #请求查询做市商合约手续费率
    def ReqQryMMInstrumentCommissionRate(self, pQryMMInstrumentCommissionRate,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryMMInstrumentCommissionRate(<CThostFtdcQryMMInstrumentCommissionRateField *> <size_t> ctypes.addressof(pQryMMInstrumentCommissionRate), nRequestID)
            return result
        #请求查询做市商期权合约手续费
    def ReqQryMMOptionInstrCommRate(self, pQryMMOptionInstrCommRate,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryMMOptionInstrCommRate(<CThostFtdcQryMMOptionInstrCommRateField *> <size_t> ctypes.addressof(pQryMMOptionInstrCommRate),nRequestID)
            return result
        #请求查询报单手续费
    def ReqQryInstrumentOrderCommRate(self, pQryInstrumentOrderCommRate,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryInstrumentOrderCommRate(<CThostFtdcQryInstrumentOrderCommRateField *> <size_t> ctypes.addressof(pQryInstrumentOrderCommRate),nRequestID)
            return result
        #请求查询期权交易成本
    def ReqQryOptionInstrTradeCost(self, pQryOptionInstrTradeCost,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryOptionInstrTradeCost(<CThostFtdcQryOptionInstrTradeCostField *> <size_t> ctypes.addressof(pQryOptionInstrTradeCost),nRequestID)
            return result
        #请求查询期权合约手续费
    def ReqQryOptionInstrCommRate(self, pQryOptionInstrCommRate,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryOptionInstrCommRate(<CThostFtdcQryOptionInstrCommRateField *> <size_t> ctypes.addressof(pQryOptionInstrCommRate),nRequestID)
            return result
        #请求查询执行宣告
    def ReqQryExecOrder(self, pQryExecOrder, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryExecOrder(<CThostFtdcQryExecOrderField *> <size_t> ctypes.addressof(pQryExecOrder), nRequestID)
            return result
        #请求查询询价
    def ReqQryForQuote(self, pQryForQuote, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryForQuote(<CThostFtdcQryForQuoteField *> <size_t> ctypes.addressof(pQryForQuote), nRequestID)
            return result
        #请求查询报价
    def ReqQryQuote(self, pQryQuote, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryQuote(<CThostFtdcQryQuoteField *> <size_t> ctypes.addressof(pQryQuote), nRequestID)
            return result
        #请求查询组合合约安全系数
    def ReqQryCombInstrumentGuard(self, pQryCombInstrumentGuard,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryCombInstrumentGuard(<CThostFtdcQryCombInstrumentGuardField *> <size_t> ctypes.addressof(pQryCombInstrumentGuard),nRequestID)
            return result
        #请求查询申请组合
    def ReqQryCombAction(self, pQryCombAction, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryCombAction(<CThostFtdcQryCombActionField *> <size_t> ctypes.addressof(pQryCombAction), nRequestID)
            return result
        #请求查询转帐流水
    def ReqQryTransferSerial(self, pQryTransferSerial, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryTransferSerial(<CThostFtdcQryTransferSerialField *> <size_t> ctypes.addressof(pQryTransferSerial), nRequestID)
            return result
        #请求查询银期签约关系
    def ReqQryAccountregister(self, pQryAccountregister, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryAccountregister(<CThostFtdcQryAccountregisterField *> <size_t> ctypes.addressof(pQryAccountregister), nRequestID)
            return result
        #请求查询签约银行
    def ReqQryContractBank(self, pQryContractBank, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryContractBank(<CThostFtdcQryContractBankField *> <size_t> ctypes.addressof(pQryContractBank), nRequestID)
            return result
        #请求查询预埋单
    def ReqQryParkedOrder(self, pQryParkedOrder, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryParkedOrder(<CThostFtdcQryParkedOrderField *> <size_t> ctypes.addressof(pQryParkedOrder), nRequestID)
            return result
        #请求查询预埋撤单
    def ReqQryParkedOrderAction(self, pQryParkedOrderAction,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryParkedOrderAction(<CThostFtdcQryParkedOrderActionField *> <size_t> ctypes.addressof(pQryParkedOrderAction), nRequestID)
            return result
        #请求查询交易通知
    def ReqQryTradingNotice(self, pQryTradingNotice, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryTradingNotice(<CThostFtdcQryTradingNoticeField *> <size_t> ctypes.addressof(pQryTradingNotice), nRequestID)
            return result
        #请求查询经纪公司交易参数
    def ReqQryBrokerTradingParams(self, pQryBrokerTradingParams,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryBrokerTradingParams(<CThostFtdcQryBrokerTradingParamsField *> <size_t> ctypes.addressof(pQryBrokerTradingParams),nRequestID)
            return result
        #请求查询经纪公司交易算法
    def ReqQryBrokerTradingAlgos(self, pQryBrokerTradingAlgos,int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQryBrokerTradingAlgos(<CThostFtdcQryBrokerTradingAlgosField *> <size_t> ctypes.addressof(pQryBrokerTradingAlgos),nRequestID)
            return result
        #请求查询监控中心用户令牌
    def ReqQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQueryCFMMCTradingAccountToken(<CThostFtdcQueryCFMMCTradingAccountTokenField *> <size_t> ctypes.addressof(pQueryCFMMCTradingAccountToken), nRequestID)
            return result
        #期货发起银行资金转期货请求
    def ReqFromBankToFutureByFuture(self, pReqTransfer, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqFromBankToFutureByFuture(<CThostFtdcReqTransferField *> <size_t> ctypes.addressof(pReqTransfer), nRequestID)
            return result
        #期货发起期货资金转银行请求
    def ReqFromFutureToBankByFuture(self, pReqTransfer, int nRequestID):
        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqFromFutureToBankByFuture(<CThostFtdcReqTransferField *> <size_t> ctypes.addressof(pReqTransfer), nRequestID)
            return result
        #期货发起查询银行余额请求
    def ReqQueryBankAccountMoneyByFuture(self, pReqQueryAccount, int nRequestID):

        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqQueryBankAccountMoneyByFuture(<CThostFtdcReqQueryAccountField *> <size_t> ctypes.addressof(pReqQueryAccount),nRequestID)
            return result
