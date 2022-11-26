# encoding:utf-8
# distutils: language=c++
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
from cpython cimport PyObject
from libc.string cimport const_char
from libcpp cimport bool as cbool

from ctpwrapper.headers.ThostFtdcUserApiStruct cimport *
from ctpwrapper.headers.cTraderApi cimport CTraderSpi, CTraderApi, CreateFtdcTraderApi

# from libcpp.memory cimport shared_ptr,make_shared
import ctypes

from ctpwrapper import ApiStructure

cdef class TraderApiWrapper:
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

            if self._spi is not NULL:
                with nogil:
                    self._api.RegisterSpi(self._spi)
                    self._api.Init()
            else:
                raise MemoryError()

    def Join(self):

        cdef int result
        if self._spi is not NULL:
            with nogil:
                result = self._api.Join()
            return result

    def GetTradingDay(self):

        cdef const_char *result

        if self._spi is not NULL:
            with nogil:
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
        cdef size_t address
        if self._api is not NULL:
            address = ctypes.addressof(pFensUserInfo)
            with nogil:
                self._api.RegisterFensUserInfo(<CThostFtdcFensUserInfoField *> address)

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
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pReqAuthenticateField)
            with nogil:
                result = self._api.ReqAuthenticate(<CThostFtdcReqAuthenticateField *> address, nRequestID)
            return result

    # 注册用户终端信息，用于中继服务器多连接模式
    # 需要在终端认证成功后，用户登录前调用该接口
    def RegisterUserSystemInfo(self, pUserSystemInfo):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pUserSystemInfo)
            with nogil:
                result = self._api.RegisterUserSystemInfo(<CThostFtdcUserSystemInfoField *> address)
            return result

    # 上报用户终端信息，用于中继服务器操作员登录模式
    # 操作员登录后，可以多次调用该接口上报客户信息
    def SubmitUserSystemInfo(self, pUserSystemInfo):
        cdef int result
        cdef size_t address
        if self._api is not NULL:
            address = ctypes.addressof(pUserSystemInfo)
            with nogil:
                result = self._api.SubmitUserSystemInfo(<CThostFtdcUserSystemInfoField *> address)
            return result

    # 用户登录请求
    def ReqUserLogin(self, pReqUserLoginField, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pReqUserLoginField)
            with nogil:
                result = self._api.ReqUserLogin(<CThostFtdcReqUserLoginField *> address, nRequestID)
            return result

    # 登出请求
    def ReqUserLogout(self, pUserLogout, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pUserLogout)
            with nogil:
                result = self._api.ReqUserLogout(<CThostFtdcUserLogoutField *> address, nRequestID)
            return result

    # 用户口令更新请求
    def ReqUserPasswordUpdate(self, pUserPasswordUpdate, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pUserPasswordUpdate)
            with nogil:
                result = self._api.ReqUserPasswordUpdate(<CThostFtdcUserPasswordUpdateField *> address, nRequestID)
            return result

    # 资金账户口令更新请求
    def ReqTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pTradingAccountPasswordUpdate)
            with nogil:
                result = self._api.ReqTradingAccountPasswordUpdate(<CThostFtdcTradingAccountPasswordUpdateField *> address, nRequestID)
            return result

    # 查询用户当前支持的认证模式
    def ReqUserAuthMethod(self, pReqUserAuthMethod, int nRequestID):
        cdef int result
        cdef size_t address
        if self._api is not NULL:
            address = ctypes.addressof(pReqUserAuthMethod)
            with nogil:
                result = self._api.ReqUserAuthMethod(<CThostFtdcReqUserAuthMethodField *> address, nRequestID)
            return result

    # 用户发出获取图形验证码请求
    def ReqGenUserCaptcha(self, pReqGenUserCaptcha, int nRequestID):
        cdef int result
        cdef size_t address
        if self._api is not NULL:
            address = ctypes.addressof(pReqGenUserCaptcha)
            with nogil:
                result = self._api.ReqGenUserCaptcha(<CThostFtdcReqGenUserCaptchaField *> address, nRequestID)
            return result

    # 用户发出获取短信验证码请求
    def ReqGenUserText(self, pReqGenUserText, int nRequestID):
        cdef int result
        cdef size_t address
        if self._api is not NULL:
            address = ctypes.addressof(pReqGenUserText)
            with nogil:
                result = self._api.ReqGenUserText(<CThostFtdcReqGenUserTextField *> address, nRequestID)
            return result

    # 用户发出带有图片验证码的登陆请求
    def ReqUserLoginWithCaptcha(self, pReqUserLoginWithCaptcha, int nRequestID):
        cdef int result
        cdef size_t address
        if self._api is not NULL:
            address = ctypes.addressof(pReqUserLoginWithCaptcha)
            with nogil:
                result = self._api.ReqUserLoginWithCaptcha(<CThostFtdcReqUserLoginWithCaptchaField *> address, nRequestID)
            return result

    # 用户发出带有短信验证码的登陆请求
    def ReqUserLoginWithText(self, pReqUserLoginWithText, int nRequestID):
        cdef int result
        cdef size_t address
        if self._api is not NULL:
            address = ctypes.addressof(pReqUserLoginWithText)
            with nogil:
                result = self._api.ReqUserLoginWithText(<CThostFtdcReqUserLoginWithTextField *> address, nRequestID)
            return result

    # 用户发出带有动态口令的登陆请求
    def ReqUserLoginWithOTP(self, pReqUserLoginWithOTP, int nRequestID):
        cdef int result
        cdef size_t address
        if self._api is not NULL:
            address = ctypes.addressof(pReqUserLoginWithOTP)
            with nogil:
                result = self._api.ReqUserLoginWithOTP(<CThostFtdcReqUserLoginWithOTPField *> address, nRequestID)
            return result

    # 报单录入请求
    def ReqOrderInsert(self, pInputOrder, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pInputOrder)
            with nogil:
                result = self._api.ReqOrderInsert(<CThostFtdcInputOrderField *> address, nRequestID)
            return result

    # 预埋单录入请求
    def ReqParkedOrderInsert(self, pParkedOrder, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pParkedOrder)
            with nogil:
                result = self._api.ReqParkedOrderInsert(<CThostFtdcParkedOrderField *> address, nRequestID)
            return result

    # 预埋撤单录入请求
    def ReqParkedOrderAction(self, pParkedOrderAction, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pParkedOrderAction)
            with nogil:
                result = self._api.ReqParkedOrderAction(<CThostFtdcParkedOrderActionField *> address, nRequestID)
            return result

    # 报单操作请求
    def ReqOrderAction(self, pInputOrderAction, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pInputOrderAction)
            with nogil:
                result = self._api.ReqOrderAction(<CThostFtdcInputOrderActionField *> address, nRequestID)
            return result

    #查询最大报单数量请求
    def ReqQryMaxOrderVolume(self, pQryMaxOrderVolume, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryMaxOrderVolume)
            with nogil:
                result = self._api.ReqQryMaxOrderVolume(<CThostFtdcQryMaxOrderVolumeField *> address, nRequestID)
            return result

    # 投资者结算结果确认
    def ReqSettlementInfoConfirm(self, pSettlementInfoConfirm, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pSettlementInfoConfirm)
            with nogil:
                result = self._api.ReqSettlementInfoConfirm(<CThostFtdcSettlementInfoConfirmField *> address, nRequestID)
            return result

    # 请求删除预埋单
    def ReqRemoveParkedOrder(self, pRemoveParkedOrder, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pRemoveParkedOrder)
            with nogil:
                result = self._api.ReqRemoveParkedOrder(<CThostFtdcRemoveParkedOrderField *> address, nRequestID)
            return result

    # 请求删除预埋撤单
    def ReqRemoveParkedOrderAction(self, pRemoveParkedOrderAction, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pRemoveParkedOrderAction)
            with nogil:
                result = self._api.ReqRemoveParkedOrderAction(<CThostFtdcRemoveParkedOrderActionField *> address, nRequestID)
            return result

    #执行宣告录入请求
    def ReqExecOrderInsert(self, pInputExecOrder, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pInputExecOrder)
            with nogil:
                result = self._api.ReqExecOrderInsert(<CThostFtdcInputExecOrderField *> address, nRequestID)
            return result

    #执行宣告操作请求
    def ReqExecOrderAction(self, pInputExecOrderAction, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pInputExecOrderAction)
            with nogil:
                result = self._api.ReqExecOrderAction(<CThostFtdcInputExecOrderActionField *> address, nRequestID)
            return result

    #询价录入请求
    def ReqForQuoteInsert(self, pInputForQuote, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pInputForQuote)
            with nogil:
                result = self._api.ReqForQuoteInsert(<CThostFtdcInputForQuoteField *> address, nRequestID)
            return result

    #报价录入请求
    def ReqQuoteInsert(self, pInputQuote, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pInputQuote)
            with nogil:
                result = self._api.ReqQuoteInsert(<CThostFtdcInputQuoteField *> address, nRequestID)
            return result

    #报价操作请求
    def ReqQuoteAction(self, pInputQuoteAction, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pInputQuoteAction)
            with nogil:
                result = self._api.ReqQuoteAction(<CThostFtdcInputQuoteActionField *> address, nRequestID)
            return result

    #批量报单操作请求
    def ReqBatchOrderAction(self, pInputBatchOrderAction, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pInputBatchOrderAction)
            with nogil:
                result = self._api.ReqBatchOrderAction(<CThostFtdcInputBatchOrderActionField *> address, nRequestID)
            return result

    #期权自对冲录入请求
    def ReqOptionSelfCloseInsert(self, pInputOptionSelfClose, int nRequestID):

        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pInputOptionSelfClose)
            with nogil:
                result = self._api.ReqOptionSelfCloseInsert(<CThostFtdcInputOptionSelfCloseField *> address, nRequestID)
            return result
    #期权自对冲操作请求
    def ReqOptionSelfCloseAction(self, pInputOptionSelfCloseAction, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pInputOptionSelfCloseAction)
            with nogil:
                result = self._api.ReqOptionSelfCloseAction(<CThostFtdcInputOptionSelfCloseActionField *> address, nRequestID)
            return result

    #申请组合录入请求
    def ReqCombActionInsert(self, pInputCombAction, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pInputCombAction)
            with nogil:
                result = self._api.ReqCombActionInsert(<CThostFtdcInputCombActionField *> address, nRequestID)
            return result
    # 请求查询报单
    def ReqQryOrder(self, pQryOrder, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryOrder)
            with nogil:
                result = self._api.ReqQryOrder(<CThostFtdcQryOrderField *> address, nRequestID)
            return result
    # 请求查询成交
    def ReqQryTrade(self, pQryTrade, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryTrade)
            with nogil:
                result = self._api.ReqQryTrade(<CThostFtdcQryTradeField *> address, nRequestID)
            return result
    # 请求查询投资者持仓
    def ReqQryInvestorPosition(self, pQryInvestorPosition, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryInvestorPosition)
            with nogil:
                result = self._api.ReqQryInvestorPosition(<CThostFtdcQryInvestorPositionField *> address, nRequestID)
            return result
    # 请求查询资金账户
    def ReqQryTradingAccount(self, pQryTradingAccount, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryTradingAccount)
            with nogil:
                result = self._api.ReqQryTradingAccount(<CThostFtdcQryTradingAccountField *> address, nRequestID)
            return result
    # 请求查询投资者
    def ReqQryInvestor(self, pQryInvestor, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryInvestor)
            with nogil:
                result = self._api.ReqQryInvestor(<CThostFtdcQryInvestorField *> address, nRequestID)
            return result
    # 请求查询交易编码
    def ReqQryTradingCode(self, pQryTradingCode, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryTradingCode)
            with nogil:
                result = self._api.ReqQryTradingCode(<CThostFtdcQryTradingCodeField *> address, nRequestID)
            return result
    # 请求查询合约保证金率
    def ReqQryInstrumentMarginRate(self, pQryInstrumentMarginRate, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryInstrumentMarginRate)
            with nogil:
                result = self._api.ReqQryInstrumentMarginRate(<CThostFtdcQryInstrumentMarginRateField *> address, nRequestID)
            return result
    # 请求查询合约手续费率
    def ReqQryInstrumentCommissionRate(self, pQryInstrumentCommissionRate, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryInstrumentCommissionRate)
            with nogil:
                result = self._api.ReqQryInstrumentCommissionRate(<CThostFtdcQryInstrumentCommissionRateField *> address, nRequestID)
            return result
    # 请求查询交易所
    def ReqQryExchange(self, pQryExchange, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryExchange)
            with nogil:
                result = self._api.ReqQryExchange(<CThostFtdcQryExchangeField *> address, nRequestID)
            return result
    # 请求查询产品
    def ReqQryProduct(self, pQryProduct, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryProduct)
            with nogil:
                result = self._api.ReqQryProduct(<CThostFtdcQryProductField *> address, nRequestID)
            return result
    # 请求查询合约
    def ReqQryInstrument(self, pQryInstrument, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryInstrument)
            with nogil:
                result = self._api.ReqQryInstrument(<CThostFtdcQryInstrumentField *> address, nRequestID)
            return result
    # 请求查询行情
    def ReqQryDepthMarketData(self, pQryDepthMarketData, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryDepthMarketData)
            with nogil:
                result = self._api.ReqQryDepthMarketData(<CThostFtdcQryDepthMarketDataField *> address, nRequestID)
            return result

    def ReqQryTraderOffer(self, pQryTraderOffer, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryTraderOffer)
            with nogil:
                result = self._api.ReqQryTraderOffer(<CThostFtdcQryTraderOfferField *> address, nRequestID)
            return result
    # 请求查询投资者结算结果
    def ReqQrySettlementInfo(self, pQrySettlementInfo, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQrySettlementInfo)
            with nogil:
                result = self._api.ReqQrySettlementInfo(<CThostFtdcQrySettlementInfoField *> address, nRequestID)
            return result
    # 请求查询转帐银行
    def ReqQryTransferBank(self, pQryTransferBank, int nRequestID):
        cdef int result
        cdef size_t address

        if self._spi is not NULL:
            address = ctypes.addressof(pQryTransferBank)
            with nogil:
                result = self._api.ReqQryTransferBank(<CThostFtdcQryTransferBankField *> address, nRequestID)
            return result
    # 请求查询投资者持仓明细
    def ReqQryInvestorPositionDetail(self, pQryInvestorPositionDetail, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryInvestorPositionDetail)
            with nogil:
                result = self._api.ReqQryInvestorPositionDetail(<CThostFtdcQryInvestorPositionDetailField *> address, nRequestID)
            return result
    # 请求查询客户通知
    def ReqQryNotice(self, pQryNotice, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryNotice)
            with nogil:
                result = self._api.ReqQryNotice(<CThostFtdcQryNoticeField *> address, nRequestID)
            return result
    # 请求查询结算信息确认
    def ReqQrySettlementInfoConfirm(self, pQrySettlementInfoConfirm, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQrySettlementInfoConfirm)
            with nogil:
                result = self._api.ReqQrySettlementInfoConfirm(<CThostFtdcQrySettlementInfoConfirmField *> address, nRequestID)
            return result
    # 请求查询投资者持仓明细
    def ReqQryInvestorPositionCombineDetail(self, pQryInvestorPositionCombineDetail, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryInvestorPositionCombineDetail)
            with nogil:
                result = self._api.ReqQryInvestorPositionCombineDetail(<CThostFtdcQryInvestorPositionCombineDetailField *> address, nRequestID)
            return result
    # 请求查询保证金监管系统经纪公司资金账户密钥
    def ReqQryCFMMCTradingAccountKey(self, pQryCFMMCTradingAccountKey, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryCFMMCTradingAccountKey)
            with nogil:
                result = self._api.ReqQryCFMMCTradingAccountKey(<CThostFtdcQryCFMMCTradingAccountKeyField *> address, nRequestID)
            return result
    # 请求查询仓单折抵信息
    def ReqQryEWarrantOffset(self, pQryEWarrantOffset, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryEWarrantOffset)
            with nogil:
                result = self._api.ReqQryEWarrantOffset(<CThostFtdcQryEWarrantOffsetField *> address, nRequestID)
            return result
    # 请求查询投资者品种/跨品种保证金
    def ReqQryInvestorProductGroupMargin(self, pQryInvestorProductGroupMargin, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryInvestorProductGroupMargin)
            with nogil:
                result = self._api.ReqQryInvestorProductGroupMargin(<CThostFtdcQryInvestorProductGroupMarginField *> address, nRequestID)
            return result
    # 请求查询交易所保证金率
    def ReqQryExchangeMarginRate(self, pQryExchangeMarginRate, int nRequestID):
        cdef int result
        cdef size_t address

        if self._spi is not NULL:
            address = ctypes.addressof(pQryExchangeMarginRate)
            with nogil:
                result = self._api.ReqQryExchangeMarginRate(<CThostFtdcQryExchangeMarginRateField *> address, nRequestID)
            return result

    # 请求查询交易所调整保证金率
    def ReqQryExchangeMarginRateAdjust(self, pQryExchangeMarginRateAdjust, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryExchangeMarginRateAdjust)
            with nogil:
                result = self._api.ReqQryExchangeMarginRateAdjust(<CThostFtdcQryExchangeMarginRateAdjustField *> address, nRequestID)
            return result
    # 请求查询汇率
    def ReqQryExchangeRate(self, pQryExchangeRate, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryExchangeRate)
            with nogil:
                result = self._api.ReqQryExchangeRate(<CThostFtdcQryExchangeRateField *> address, nRequestID)
            return result

    # 请求查询二级代理操作员银期权限
    def ReqQrySecAgentACIDMap(self, pQrySecAgentACIDMap, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQrySecAgentACIDMap)
            with nogil:
                result = self._api.ReqQrySecAgentACIDMap(<CThostFtdcQrySecAgentACIDMapField *> address, nRequestID)
            return result

    # 请求查询产品报价汇率
    def ReqQryProductExchRate(self, pQryProductExchRate, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryProductExchRate)
            with nogil:
                result = self._api.ReqQryProductExchRate(<CThostFtdcQryProductExchRateField *> address, nRequestID)
            return result

    # 请求查询产品组
    def ReqQryProductGroup(self, pQryProductGroup, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryProductGroup)
            with nogil:
                result = self._api.ReqQryProductGroup(<CThostFtdcQryProductGroupField *> address, nRequestID)
            return result

    # 请求查询做市商合约手续费率
    def ReqQryMMInstrumentCommissionRate(self, pQryMMInstrumentCommissionRate, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryMMInstrumentCommissionRate)
            with nogil:
                result = self._api.ReqQryMMInstrumentCommissionRate(<CThostFtdcQryMMInstrumentCommissionRateField *> address, nRequestID)
            return result

    # 请求查询做市商期权合约手续费
    def ReqQryMMOptionInstrCommRate(self, pQryMMOptionInstrCommRate, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryMMOptionInstrCommRate)
            with nogil:
                result = self._api.ReqQryMMOptionInstrCommRate(<CThostFtdcQryMMOptionInstrCommRateField *> address, nRequestID)
            return result

    # 请求查询报单手续费
    def ReqQryInstrumentOrderCommRate(self, pQryInstrumentOrderCommRate, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryInstrumentOrderCommRate)
            with nogil:
                result = self._api.ReqQryInstrumentOrderCommRate(<CThostFtdcQryInstrumentOrderCommRateField *> address, nRequestID)
            return result

    # 请求查询资金账户
    def ReqQrySecAgentTradingAccount(self, pQryTradingAccount, int nRequestID):

        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryTradingAccount)
            with nogil:
                result = self._api.ReqQrySecAgentTradingAccount(<CThostFtdcQryTradingAccountField *> address, nRequestID)
            return result

    # 请求查询二级代理商资金校验模式
    def ReqQrySecAgentCheckMode(self, pQrySecAgentCheckMode, int nRequestID):

        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQrySecAgentCheckMode)
            with nogil:
                result = self._api.ReqQrySecAgentCheckMode(<CThostFtdcQrySecAgentCheckModeField *> address, nRequestID)
            return result

    # 请求查询期权交易成本
    def ReqQryOptionInstrTradeCost(self, pQryOptionInstrTradeCost, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryOptionInstrTradeCost)
            with nogil:
                result = self._api.ReqQryOptionInstrTradeCost(<CThostFtdcQryOptionInstrTradeCostField *> address, nRequestID)
            return result

    # 请求查询期权合约手续费
    def ReqQryOptionInstrCommRate(self, pQryOptionInstrCommRate, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryOptionInstrCommRate)
            with nogil:
                result = self._api.ReqQryOptionInstrCommRate(<CThostFtdcQryOptionInstrCommRateField *> address, nRequestID)
            return result

    # 请求查询执行宣告
    def ReqQryExecOrder(self, pQryExecOrder, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryExecOrder)
            with nogil:
                result = self._api.ReqQryExecOrder(<CThostFtdcQryExecOrderField *> address, nRequestID)
            return result

    # 请求查询询价
    def ReqQryForQuote(self, pQryForQuote, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryForQuote)
            with nogil:
                result = self._api.ReqQryForQuote(<CThostFtdcQryForQuoteField *> address, nRequestID)
            return result

    # 请求查询报价
    def ReqQryQuote(self, pQryQuote, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryQuote)
            with nogil:
                result = self._api.ReqQryQuote(<CThostFtdcQryQuoteField *> address, nRequestID)
            return result

    # 请求查询期权自对冲
    def ReqQryOptionSelfClose(self, pQryOptionSelfClose, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryOptionSelfClose)
            with nogil:
                result = self._api.ReqQryOptionSelfClose(<CThostFtdcQryOptionSelfCloseField *> address, nRequestID)
            return result

    # 请求查询投资单元
    def ReqQryInvestUnit(self, pQryInvestUnit, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryInvestUnit)
            with nogil:
                result = self._api.ReqQryInvestUnit(<CThostFtdcQryInvestUnitField *> address, nRequestID)
            return result

    # 请求查询组合合约安全系数
    def ReqQryCombInstrumentGuard(self, pQryCombInstrumentGuard, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryCombInstrumentGuard)
            with nogil:
                result = self._api.ReqQryCombInstrumentGuard(<CThostFtdcQryCombInstrumentGuardField *> address, nRequestID)
            return result

    # 请求查询申请组合
    def ReqQryCombAction(self, pQryCombAction, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryCombAction)
            with nogil:
                result = self._api.ReqQryCombAction(<CThostFtdcQryCombActionField *> address, nRequestID)
            return result

    # 请求查询转帐流水
    def ReqQryTransferSerial(self, pQryTransferSerial, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryTransferSerial)
            with nogil:
                result = self._api.ReqQryTransferSerial(<CThostFtdcQryTransferSerialField *> address, nRequestID)
            return result

    # 请求查询银期签约关系
    def ReqQryAccountregister(self, pQryAccountregister, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryAccountregister)
            with nogil:
                result = self._api.ReqQryAccountregister(<CThostFtdcQryAccountregisterField *> address, nRequestID)
            return result

    # 请求查询签约银行
    def ReqQryContractBank(self, pQryContractBank, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryContractBank)
            with nogil:
                result = self._api.ReqQryContractBank(<CThostFtdcQryContractBankField *> address, nRequestID)
            return result

    # 请求查询预埋单
    def ReqQryParkedOrder(self, pQryParkedOrder, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryParkedOrder)
            with nogil:
                result = self._api.ReqQryParkedOrder(<CThostFtdcQryParkedOrderField *> address, nRequestID)
            return result

    # 请求查询预埋撤单
    def ReqQryParkedOrderAction(self, pQryParkedOrderAction, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryParkedOrderAction)
            with nogil:
                result = self._api.ReqQryParkedOrderAction(<CThostFtdcQryParkedOrderActionField *> address, nRequestID)
            return result

    # 请求查询交易通知
    def ReqQryTradingNotice(self, pQryTradingNotice, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryTradingNotice)
            with nogil:
                result = self._api.ReqQryTradingNotice(<CThostFtdcQryTradingNoticeField *> address, nRequestID)
            return result

    # 请求查询经纪公司交易参数
    def ReqQryBrokerTradingParams(self, pQryBrokerTradingParams, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryBrokerTradingParams)
            with nogil:
                result = self._api.ReqQryBrokerTradingParams(<CThostFtdcQryBrokerTradingParamsField *> address, nRequestID)
            return result

    # 请求查询经纪公司交易算法
    def ReqQryBrokerTradingAlgos(self, pQryBrokerTradingAlgos, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryBrokerTradingAlgos)
            with nogil:
                result = self._api.ReqQryBrokerTradingAlgos(<CThostFtdcQryBrokerTradingAlgosField *> address, nRequestID)
            return result

    # 请求查询监控中心用户令牌
    def ReqQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQueryCFMMCTradingAccountToken)
            with nogil:
                result = self._api.ReqQueryCFMMCTradingAccountToken(<CThostFtdcQueryCFMMCTradingAccountTokenField *> address, nRequestID)
            return result

    # 期货发起银行资金转期货请求
    def ReqFromBankToFutureByFuture(self, pReqTransfer, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pReqTransfer)
            with nogil:
                result = self._api.ReqFromBankToFutureByFuture(<CThostFtdcReqTransferField *> address, nRequestID)
            return result

    # 期货发起期货资金转银行请求
    def ReqFromFutureToBankByFuture(self, pReqTransfer, int nRequestID):
        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pReqTransfer)
            with nogil:
                result = self._api.ReqFromFutureToBankByFuture(<CThostFtdcReqTransferField *> address, nRequestID)
            return result

    # 期货发起查询银行余额请求
    def ReqQueryBankAccountMoneyByFuture(self, pReqQueryAccount, int nRequestID):

        cdef int result
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pReqQueryAccount)
            with nogil:
                result = self._api.ReqQueryBankAccountMoneyByFuture(<CThostFtdcReqQueryAccountField *> address, nRequestID)
            return result

    # 请求查询二级代理商信息
    def ReqQrySecAgentTradeInfo(self, pQrySecAgentTradeInfo, int nRequestID):
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQrySecAgentTradeInfo)
            with nogil:
                result = self._api.ReqQrySecAgentTradeInfo(<CThostFtdcQrySecAgentTradeInfoField *> address, nRequestID)
            return result

    # 请求查询分类合约
    def ReqQryClassifiedInstrument(self, pQryClassifiedInstrument, int nRequestID):
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryClassifiedInstrument)
            with nogil:
                result = self._api.ReqQryClassifiedInstrument(<CThostFtdcQryClassifiedInstrumentField *> address, nRequestID)
            return result

    # 请求组合优惠比例
    def ReqQryCombPromotionParam(self, pQryCombPromotionParam, int nRequestID):
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryCombPromotionParam)
            with nogil:
                result = self._api.ReqQryCombPromotionParam(<CThostFtdcQryCombPromotionParamField *> address, nRequestID)
            return result

    # 投资者风险结算持仓查询
    def ReqQryRiskSettleInvstPosition(self, pQryRiskSettleInvstPosition, int nRequestID):
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryRiskSettleInvstPosition)
            with nogil:
                result = self._api.ReqQryRiskSettleInvstPosition(<CThostFtdcQryRiskSettleInvstPositionField *> address, nRequestID)
            return result

    # 风险结算产品查询
    def ReqQryRiskSettleProductStatus(self, pQryRiskSettleProductStatus, int nRequestID):
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryRiskSettleProductStatus)
            with nogil:
                result = self._api.ReqQryRiskSettleProductStatus(<CThostFtdcQryRiskSettleProductStatusField *> address, nRequestID)
            return result

    # SPBM期货合约参数查询
    def ReqQrySPBMFutureParameter(self, pQrySPBMFutureParameter, int nRequestID):
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQrySPBMFutureParameter)
            with nogil:
                result = self._api.ReqQrySPBMFutureParameter(<CThostFtdcQrySPBMFutureParameterField *> address, nRequestID)
            return result

    # SPBM期权合约参数查询
    def ReqQrySPBMOptionParameter(self, pQrySPBMOptionParameter, int nRequestID):
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQrySPBMOptionParameter)
            with nogil:
                result = self._api.ReqQrySPBMOptionParameter(<CThostFtdcQrySPBMOptionParameterField *> address, nRequestID)
            return result

    # SPBM品种内对锁仓折扣参数查询
    def ReqQrySPBMIntraParameter(self, pQrySPBMIntraParameter, int nRequestID):
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQrySPBMIntraParameter)
            with nogil:
                result = self._api.ReqQrySPBMIntraParameter(<CThostFtdcQrySPBMIntraParameterField *> address, nRequestID)
            return result

    # SPBM跨品种抵扣参数查询
    def ReqQrySPBMInterParameter(self, pQrySPBMInterParameter, int nRequestID):
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQrySPBMInterParameter)
            with nogil:
                result = self._api.ReqQrySPBMInterParameter(<CThostFtdcQrySPBMInterParameterField *> address, nRequestID)
            return result

    # SPBM组合保证金套餐查询
    def ReqQrySPBMPortfDefinition(self, pQrySPBMPortfDefinition, int nRequestID):
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQrySPBMPortfDefinition)
            with nogil:
                result = self._api.ReqQrySPBMPortfDefinition(<CThostFtdcQrySPBMPortfDefinitionField *> address, nRequestID)
            return result

    # 投资者SPBM套餐选择查询
    def ReqQrySPBMInvestorPortfDef(self, pQrySPBMInvestorPortfDef, int nRequestID):
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQrySPBMInvestorPortfDef)
            with nogil:
                result = self._api.ReqQrySPBMInvestorPortfDef(<CThostFtdcQrySPBMInvestorPortfDefField *> address, nRequestID)
            return result

    # 投资者新型组合保证金系数查询
    def ReqQryInvestorPortfMarginRatio(self, pQryInvestorPortfMarginRatio, int nRequestID):
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryInvestorPortfMarginRatio)
            with nogil:
                result = self._api.ReqQryInvestorPortfMarginRatio(<CThostFtdcQryInvestorPortfMarginRatioField *> address, nRequestID)
            return result

    # 投资者产品SPBM明细查询
    def ReqQryInvestorProdSPBMDetail(self, pQryInvestorProdSPBMDetail, int nRequestID):
        cdef size_t address
        if self._spi is not NULL:
            address = ctypes.addressof(pQryInvestorProdSPBMDetail)
            with nogil:
                result = self._api.ReqQryInvestorProdSPBMDetail(<CThostFtdcQryInvestorProdSPBMDetailField *> address, nRequestID)
            return result

cdef extern int TraderSpi_OnFrontConnected(self) except -1:
    self.OnFrontConnected()
    return 0

cdef extern int TraderSpi_OnFrontDisconnected(self, int nReason) except -1:
    self.OnFrontDisconnected(nReason)
    return 0

cdef extern int TraderSpi_OnHeartBeatWarning(self, int nTimeLapse) except -1:
    self.OnHeartBeatWarning(nTimeLapse)
    return 0

cdef extern int TraderSpi_OnRspAuthenticate(self,
                                            CThostFtdcRspAuthenticateField *pRspAuthenticate,
                                            CThostFtdcRspInfoField *pRspInfo,
                                            int nRequestID,
                                            cbool bIsLast) except -1:
    self.OnRspAuthenticate(
        None if pRspAuthenticate is NULL else ApiStructure.RspAuthenticateField.from_address(<size_t> pRspAuthenticate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspUserLogin(self,
                                         CThostFtdcRspUserLoginField *pRspUserLogin,
                                         CThostFtdcRspInfoField *pRspInfo,
                                         int nRequestID,
                                         cbool bIsLast) except -1:
    self.OnRspUserLogin(
        None if pRspUserLogin is NULL else ApiStructure.RspUserLoginField.from_address(<size_t> pRspUserLogin),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspUserLogout(self,
                                          CThostFtdcUserLogoutField *pUserLogout,
                                          CThostFtdcRspInfoField *pRspInfo,
                                          int nRequestID,
                                          cbool bIsLast) except -1:
    self.OnRspUserLogout(
        None if pUserLogout is NULL else ApiStructure.UserLogoutField.from_address(<size_t> pUserLogout),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspUserPasswordUpdate(self,
                                                  CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate,
                                                  CThostFtdcRspInfoField *pRspInfo,
                                                  int nRequestID,
                                                  cbool bIsLast) except -1:
    self.OnRspUserPasswordUpdate(
        None if pUserPasswordUpdate is NULL else ApiStructure.UserPasswordUpdateField.from_address(<size_t> pUserPasswordUpdate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspTradingAccountPasswordUpdate(self,
                                                            CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate,
                                                            CThostFtdcRspInfoField *pRspInfo,
                                                            int nRequestID,
                                                            cbool bIsLast) except -1:
    self.OnRspTradingAccountPasswordUpdate(
        None if pTradingAccountPasswordUpdate is NULL else ApiStructure.TradingAccountPasswordUpdateField.from_address(<size_t> pTradingAccountPasswordUpdate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspOrderInsert(self,
                                           CThostFtdcInputOrderField *pInputOrder,
                                           CThostFtdcRspInfoField *pRspInfo,
                                           int nRequestID,
                                           cbool bIsLast) except -1:
    self.OnRspOrderInsert(
        None if pInputOrder is NULL else ApiStructure.InputOrderField.from_address(<size_t> pInputOrder),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspParkedOrderInsert(self,
                                                 CThostFtdcParkedOrderField *pParkedOrder,
                                                 CThostFtdcRspInfoField *pRspInfo,
                                                 int nRequestID,
                                                 cbool bIsLast) except -1:
    self.OnRspParkedOrderInsert(
        None if pParkedOrder is NULL else ApiStructure.ParkedOrderField.from_address(<size_t> pParkedOrder),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspParkedOrderAction(self,
                                                 CThostFtdcParkedOrderActionField *pParkedOrderAction,
                                                 CThostFtdcRspInfoField *pRspInfo,
                                                 int nRequestID,
                                                 cbool bIsLast) except -1:
    self.OnRspParkedOrderAction(
        None if pParkedOrderAction is NULL else ApiStructure.ParkedOrderActionField.from_address(<size_t> pParkedOrderAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspOrderAction(self,
                                           CThostFtdcInputOrderActionField *pInputOrderAction,
                                           CThostFtdcRspInfoField *pRspInfo,
                                           int nRequestID,
                                           cbool bIsLast) except -1:
    self.OnRspOrderAction(
        None if pInputOrderAction is NULL else ApiStructure.InputOrderActionField.from_address(<size_t> pInputOrderAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryMaxOrderVolume(self,
                                                 CThostFtdcQryMaxOrderVolumeField *pQueryMaxOrderVolume,
                                                 CThostFtdcRspInfoField *pRspInfo,
                                                 int nRequestID,
                                                 cbool bIsLast) except -1:
    self.OnRspQryMaxOrderVolume(
        None if pQueryMaxOrderVolume is NULL else ApiStructure.QryMaxOrderVolumeField.from_address(<size_t> pQueryMaxOrderVolume),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspSettlementInfoConfirm(self,
                                                     CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm,
                                                     CThostFtdcRspInfoField *pRspInfo,
                                                     int nRequestID,
                                                     cbool bIsLast) except -1:
    self.OnRspSettlementInfoConfirm(
        None if pSettlementInfoConfirm is NULL else ApiStructure.SettlementInfoConfirmField.from_address(<size_t> pSettlementInfoConfirm),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspRemoveParkedOrder(self,
                                                 CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder,
                                                 CThostFtdcRspInfoField *pRspInfo,
                                                 int nRequestID,
                                                 cbool bIsLast) except -1:
    self.OnRspRemoveParkedOrder(
        None if pRemoveParkedOrder is NULL else ApiStructure.RemoveParkedOrderField.from_address(<size_t> pRemoveParkedOrder),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspRemoveParkedOrderAction(self,
                                                       CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction,
                                                       CThostFtdcRspInfoField *pRspInfo,
                                                       int nRequestID,
                                                       cbool bIsLast) except -1:
    self.OnRspRemoveParkedOrderAction(
        None if pRemoveParkedOrderAction is NULL else ApiStructure.RemoveParkedOrderActionField(<size_t> pRemoveParkedOrderAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspExecOrderInsert(self,
                                               CThostFtdcInputExecOrderField *pInputExecOrder,
                                               CThostFtdcRspInfoField *pRspInfo,
                                               int nRequestID,
                                               cbool bIsLast) except -1:
    self.OnRspExecOrderInsert(
        None if pInputExecOrder is NULL else ApiStructure.InputExecOrderField.from_address(<size_t> pInputExecOrder),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspExecOrderAction(self,
                                               CThostFtdcInputExecOrderActionField *pInputExecOrderAction,
                                               CThostFtdcRspInfoField *pRspInfo,
                                               int nRequestID,
                                               cbool bIsLast) except -1:
    self.OnRspExecOrderAction(
        None if pInputExecOrderAction is NULL else ApiStructure.InputExecOrderActionField.from_address(<size_t> pInputExecOrderAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspForQuoteInsert(self,
                                              CThostFtdcInputForQuoteField *pInputForQuote,
                                              CThostFtdcRspInfoField *pRspInfo,
                                              int nRequestID,
                                              cbool bIsLast) except -1:
    self.OnRspForQuoteInsert(
        None if pInputForQuote is NULL else ApiStructure.InputForQuoteField.from_address(<size_t> pInputForQuote),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQuoteInsert(self,
                                           CThostFtdcInputQuoteField *pInputQuote,
                                           CThostFtdcRspInfoField *pRspInfo,
                                           int nRequestID,
                                           cbool bIsLast) except -1:
    self.OnRspQuoteInsert(
        None if pInputQuote is NULL else ApiStructure.InputQuoteField.from_address(<size_t> pInputQuote),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQuoteAction(self,
                                           CThostFtdcInputQuoteActionField *pInputQuoteAction,
                                           CThostFtdcRspInfoField *pRspInfo,
                                           int nRequestID,
                                           cbool bIsLast) except -1:
    self.OnRspQuoteAction(
        None if pInputQuoteAction is NULL else ApiStructure.InputQuoteActionField.from_address(<size_t> pInputQuoteAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspCombActionInsert(self,
                                                CThostFtdcInputCombActionField *pInputCombAction,
                                                CThostFtdcRspInfoField *pRspInfo,
                                                int nRequestID,
                                                cbool bIsLast) except -1:
    self.OnRspCombActionInsert(
        None if pInputCombAction is NULL else ApiStructure.InputCombActionField.from_address(<size_t> pInputCombAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryOrder(self,
                                        CThostFtdcOrderField *pOrder,
                                        CThostFtdcRspInfoField *pRspInfo,
                                        int nRequestID,
                                        cbool bIsLast) except -1:
    self.OnRspQryOrder(
        None if pOrder is NULL else ApiStructure.OrderField.from_address(<size_t> pOrder),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryTrade(self,
                                        CThostFtdcTradeField *pTrade,
                                        CThostFtdcRspInfoField *pRspInfo,
                                        int nRequestID,
                                        cbool bIsLast) except -1:
    self.OnRspQryTrade(
        None if pTrade is NULL else ApiStructure.TradeField.from_address(<size_t> pTrade),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryInvestorPosition(self,
                                                   CThostFtdcInvestorPositionField *pInvestorPosition,
                                                   CThostFtdcRspInfoField *pRspInfo,
                                                   int nRequestID,
                                                   cbool bIsLast) except -1:
    self.OnRspQryInvestorPosition(
        None if pInvestorPosition is NULL else ApiStructure.InvestorPositionField.from_address(<size_t> pInvestorPosition),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryTradingAccount(self,
                                                 CThostFtdcTradingAccountField *pTradingAccount,
                                                 CThostFtdcRspInfoField *pRspInfo,
                                                 int nRequestID,
                                                 cbool bIsLast) except -1:
    self.OnRspQryTradingAccount(
        None if pTradingAccount is NULL else ApiStructure.TradingAccountField.from_address(<size_t> pTradingAccount),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryInvestor(self,
                                           CThostFtdcInvestorField *pInvestor,
                                           CThostFtdcRspInfoField *pRspInfo,
                                           int nRequestID,
                                           cbool bIsLast) except -1:
    self.OnRspQryInvestor(
        None if pInvestor is NULL else ApiStructure.InvestorField.from_address(<size_t> pInvestor),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryTradingCode(self,
                                              CThostFtdcTradingCodeField *pTradingCode,
                                              CThostFtdcRspInfoField *pRspInfo,
                                              int nRequestID,
                                              cbool bIsLast) except -1:
    self.OnRspQryTradingCode(
        None if pTradingCode is NULL else ApiStructure.TradingCodeField.from_address(<size_t> pTradingCode),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryInstrumentMarginRate(self,
                                                       CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate,
                                                       CThostFtdcRspInfoField *pRspInfo,
                                                       int nRequestID,
                                                       cbool bIsLast) except -1:
    self.OnRspQryInstrumentMarginRate(
        None if pInstrumentMarginRate is NULL else ApiStructure.InstrumentMarginRateField.from_address(<size_t> pInstrumentMarginRate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryInstrumentCommissionRate(self,
                                                           CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate,
                                                           CThostFtdcRspInfoField *pRspInfo,
                                                           int nRequestID,
                                                           cbool bIsLast) except -1:
    self.OnRspQryInstrumentCommissionRate(
        None if pInstrumentCommissionRate is NULL else ApiStructure.InstrumentCommissionRateField.from_address(<size_t> pInstrumentCommissionRate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryExchange(self,
                                           CThostFtdcExchangeField *pExchange,
                                           CThostFtdcRspInfoField *pRspInfo,
                                           int nRequestID,
                                           cbool bIsLast) except -1:
    self.OnRspQryExchange(
        None if pExchange is NULL else ApiStructure.ExchangeField.from_address(<size_t> pExchange),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryProduct(self,
                                          CThostFtdcProductField *pProduct,
                                          CThostFtdcRspInfoField *pRspInfo,
                                          int nRequestID,
                                          cbool bIsLast) except -1:
    self.OnRspQryProduct(
        None if pProduct is NULL else ApiStructure.ProductField.from_address(<size_t> pProduct),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )

    return 0

cdef extern int TraderSpi_OnRspQryInstrument(self,
                                             CThostFtdcInstrumentField *pInstrument,
                                             CThostFtdcRspInfoField *pRspInfo,
                                             int nRequestID,
                                             cbool bIsLast) except -1:
    self.OnRspQryInstrument(
        None if pInstrument is NULL else ApiStructure.InstrumentField.from_address(<size_t> pInstrument),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryDepthMarketData(self,
                                                  CThostFtdcDepthMarketDataField *pDepthMarketData,
                                                  CThostFtdcRspInfoField *pRspInfo,
                                                  int nRequestID,
                                                  cbool bIsLast) except -1:
    self.OnRspQryDepthMarketData(
        None if pDepthMarketData is NULL else ApiStructure.DepthMarketDataField.from_address(<size_t> pDepthMarketData),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQrySettlementInfo(self,
                                                 CThostFtdcSettlementInfoField *pSettlementInfo,
                                                 CThostFtdcRspInfoField *pRspInfo,
                                                 int nRequestID,
                                                 cbool bIsLast) except -1:
    self.OnRspQrySettlementInfo(
        None if pSettlementInfo is NULL else ApiStructure.SettlementInfoField.from_address(<size_t> pSettlementInfo),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryTransferBank(self,
                                               CThostFtdcTransferBankField *pTransferBank,
                                               CThostFtdcRspInfoField *pRspInfo,
                                               int nRequestID,
                                               cbool bIsLast) except -1:
    self.OnRspQryTransferBank(
        None if pTransferBank is NULL else ApiStructure.TransferBankField.from_address(<size_t> pTransferBank),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryInvestorPositionDetail(self,
                                                         CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail,
                                                         CThostFtdcRspInfoField *pRspInfo,
                                                         int nRequestID,
                                                         cbool bIsLast) except -1:
    self.OnRspQryInvestorPositionDetail(
        None if pInvestorPositionDetail is NULL else ApiStructure.InvestorPositionDetailField.from_address(<size_t> pInvestorPositionDetail),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryNotice(self,
                                         CThostFtdcNoticeField *pNotice,
                                         CThostFtdcRspInfoField *pRspInfo,
                                         int nRequestID,
                                         cbool bIsLast) except -1:
    self.OnRspQryNotice(
        None if pNotice is NULL else ApiStructure.NoticeField.from_address(<size_t> pNotice),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQrySettlementInfoConfirm(self,
                                                        CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm,
                                                        CThostFtdcRspInfoField *pRspInfo,
                                                        int nRequestID,
                                                        cbool bIsLast) except -1:
    self.OnRspQrySettlementInfoConfirm(
        None if pSettlementInfoConfirm is NULL else ApiStructure.SettlementInfoConfirmField.from_address(<size_t> pSettlementInfoConfirm),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryInvestorPositionCombineDetail(self,
                                                                CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail,
                                                                CThostFtdcRspInfoField *pRspInfo,
                                                                int nRequestID,
                                                                cbool bIsLast) except -1:
    self.OnRspQryInvestorPositionCombineDetail(
        None if pInvestorPositionCombineDetail is NULL else ApiStructure.InvestorPositionCombineDetailField.from_address(<size_t> pInvestorPositionCombineDetail),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryCFMMCTradingAccountKey(self,
                                                         CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey,
                                                         CThostFtdcRspInfoField *pRspInfo,
                                                         int nRequestID,
                                                         cbool bIsLast) except -1:
    self.OnRspQryCFMMCTradingAccountKey(
        None if pCFMMCTradingAccountKey is NULL else ApiStructure.CFMMCTradingAccountKeyField.from_address(<size_t> pCFMMCTradingAccountKey),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryEWarrantOffset(self,
                                                 CThostFtdcEWarrantOffsetField *pEWarrantOffset,
                                                 CThostFtdcRspInfoField *pRspInfo,
                                                 int nRequestID,
                                                 cbool bIsLast) except -1:
    self.OnRspQryEWarrantOffset(
        None if pEWarrantOffset is NULL else ApiStructure.EWarrantOffsetField.from_address(<size_t> pEWarrantOffset),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryInvestorProductGroupMargin(self,
                                                             CThostFtdcInvestorProductGroupMarginField *pInvestorProductGroupMargin,
                                                             CThostFtdcRspInfoField *pRspInfo,
                                                             int nRequestID,
                                                             cbool bIsLast) except -1:
    self.OnRspQryInvestorProductGroupMargin(
        None if pInvestorProductGroupMargin is NULL else ApiStructure.InvestorProductGroupMarginField.from_address(<size_t> pInvestorProductGroupMargin),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryExchangeMarginRate(self,
                                                     CThostFtdcExchangeMarginRateField *pExchangeMarginRate,
                                                     CThostFtdcRspInfoField *pRspInfo,
                                                     int nRequestID,
                                                     cbool bIsLast) except -1:
    self.OnRspQryExchangeMarginRate(
        None if pExchangeMarginRate is NULL else ApiStructure.ExchangeMarginRateField.from_address(<size_t> pExchangeMarginRate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryExchangeMarginRateAdjust(self,
                                                           CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust,
                                                           CThostFtdcRspInfoField *pRspInfo,
                                                           int nRequestID,
                                                           cbool bIsLast) except -1:
    self.OnRspQryExchangeMarginRateAdjust(
        None if pExchangeMarginRateAdjust is NULL else ApiStructure.ExchangeMarginRateAdjustField.from_address(<size_t> pExchangeMarginRateAdjust),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryExchangeRate(self,
                                               CThostFtdcExchangeRateField *pExchangeRate,
                                               CThostFtdcRspInfoField *pRspInfo,
                                               int nRequestID,
                                               cbool bIsLast) except -1:
    self.OnRspQryExchangeRate(
        None if pExchangeRate is NULL else ApiStructure.ExchangeRateField.from_address(<size_t> pExchangeRate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQrySecAgentACIDMap(self,
                                                  CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap,
                                                  CThostFtdcRspInfoField *pRspInfo,
                                                  int nRequestID,
                                                  cbool bIsLast) except -1:
    self.OnRspQrySecAgentACIDMap(
        None if pSecAgentACIDMap is NULL else ApiStructure.SecAgentACIDMapField.from_address(<size_t> pSecAgentACIDMap),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryProductExchRate(self,
                                                  CThostFtdcProductExchRateField *pProductExchRate,
                                                  CThostFtdcRspInfoField *pRspInfo,
                                                  int nRequestID,
                                                  cbool bIsLast) except -1:
    self.OnRspQryProductExchRate(
        None if pProductExchRate is NULL else ApiStructure.ProductExchRateField.from_address(<size_t> pProductExchRate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryOptionInstrTradeCost(self,
                                                       CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost,
                                                       CThostFtdcRspInfoField *pRspInfo,
                                                       int nRequestID,
                                                       cbool bIsLast) except -1:
    self.OnRspQryOptionInstrTradeCost(
        None if pOptionInstrTradeCost is NULL else ApiStructure.OptionInstrTradeCostField.from_address(<size_t> pOptionInstrTradeCost),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryOptionInstrCommRate(self,
                                                      CThostFtdcOptionInstrCommRateField *pOptionInstrCommRate,
                                                      CThostFtdcRspInfoField *pRspInfo,
                                                      int nRequestID,
                                                      cbool bIsLast) except -1:
    self.OnRspQryOptionInstrCommRate(
        None if pOptionInstrCommRate is NULL else ApiStructure.OptionInstrCommRateField.from_address(<size_t> pOptionInstrCommRate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryExecOrder(self,
                                            CThostFtdcExecOrderField *pExecOrder,
                                            CThostFtdcRspInfoField *pRspInfo,
                                            int nRequestID,
                                            cbool bIsLast) except -1:
    self.OnRspQryExecOrder(
        None if pExecOrder is NULL else ApiStructure.ExecOrderField.from_address(<size_t> pExecOrder),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryForQuote(self,
                                           CThostFtdcForQuoteField *pForQuote,
                                           CThostFtdcRspInfoField *pRspInfo,
                                           int nRequestID,
                                           cbool bIsLast) except -1:
    self.OnRspQryForQuote(
        None if pForQuote is NULL else ApiStructure.ForQuoteField.from_address(<size_t> pForQuote),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryQuote(self,
                                        CThostFtdcQuoteField *pQuote,
                                        CThostFtdcRspInfoField *pRspInfo,
                                        int nRequestID,
                                        cbool bIsLast) except -1:
    self.OnRspQryQuote(
        None if pQuote is NULL else ApiStructure.QuoteField.from_address(<size_t> pQuote),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryCombInstrumentGuard(self,
                                                      CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard,
                                                      CThostFtdcRspInfoField *pRspInfo,
                                                      int nRequestID,
                                                      cbool bIsLast) except -1:
    self.OnRspQryCombInstrumentGuard(
        None if pCombInstrumentGuard is NULL else ApiStructure.CombInstrumentGuardField.from_address(<size_t> pCombInstrumentGuard),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryCombAction(self,
                                             CThostFtdcCombActionField *pCombAction,
                                             CThostFtdcRspInfoField *pRspInfo,
                                             int nRequestID,
                                             cbool bIsLast) except -1:
    self.OnRspQryCombAction(
        None if pCombAction is NULL else ApiStructure.CombActionField.from_address(<size_t> pCombAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryTransferSerial(self,
                                                 CThostFtdcTransferSerialField *pTransferSerial,
                                                 CThostFtdcRspInfoField *pRspInfo,
                                                 int nRequestID,
                                                 cbool bIsLast) except -1:
    self.OnRspQryTransferSerial(
        None if pTransferSerial is NULL else ApiStructure.TransferSerialField.from_address(<size_t> pTransferSerial),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryAccountregister(self,
                                                  CThostFtdcAccountregisterField *pAccountregister,
                                                  CThostFtdcRspInfoField *pRspInfo,
                                                  int nRequestID,
                                                  cbool bIsLast) except -1:
    self.OnRspQryAccountregister(
        None if pAccountregister is NULL else ApiStructure.AccountregisterField.from_address(<size_t> pAccountregister),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )

    return 0

cdef extern int TraderSpi_OnRspError(self,
                                     CThostFtdcRspInfoField *pRspInfo,
                                     int nRequestID,
                                     cbool bIsLast) except -1:
    self.OnRspError(
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRtnOrder(self, CThostFtdcOrderField *pOrder) except -1:
    self.OnRtnOrder(
        None if pOrder is NULL else ApiStructure.OrderField.from_address(<size_t> pOrder)
    )
    return 0

cdef extern int TraderSpi_OnRtnTrade(self, CThostFtdcTradeField *pTrade) except -1:
    self.OnRtnTrade(
        None if pTrade is NULL else ApiStructure.TradeField.from_address(<size_t> pTrade)
    )
    return 0

cdef extern int TraderSpi_OnErrRtnOrderInsert(self,
                                              CThostFtdcInputOrderField *pInputOrder,
                                              CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnOrderInsert(
        None if pInputOrder is NULL else ApiStructure.InputOrderField.from_address(<size_t> pInputOrder),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)
    )
    return 0

cdef extern int TraderSpi_OnErrRtnOrderAction(self,
                                              CThostFtdcOrderActionField *pOrderAction,
                                              CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnOrderAction(
        None if pOrderAction is NULL else ApiStructure.OrderActionField.from_address(<size_t> pOrderAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)
    )
    return 0

cdef extern int TraderSpi_OnRtnInstrumentStatus(self, CThostFtdcInstrumentStatusField *pInstrumentStatus) except -1:
    self.OnRtnInstrumentStatus(
        None if pInstrumentStatus is NULL else ApiStructure.InstrumentStatusField.from_address(<size_t> pInstrumentStatus)
    )
    return 0

cdef extern int TraderSpi_OnRtnTradingNotice(self, CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) except -1:
    self.OnRtnTradingNotice(
        None if pTradingNoticeInfo is NULL else ApiStructure.TradingNoticeInfoField.from_address(<size_t> pTradingNoticeInfo)
    )
    return 0

cdef extern int TraderSpi_OnRtnErrorConditionalOrder(self, CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder) except -1:
    self.OnRtnErrorConditionalOrder(
        None if pErrorConditionalOrder is NULL else ApiStructure.ErrorConditionalOrderField.from_address(<size_t> pErrorConditionalOrder)
    )
    return 0

cdef extern int TraderSpi_OnRtnExecOrder(self, CThostFtdcExecOrderField *pExecOrder) except -1:
    self.OnRtnExecOrder(
        None if pExecOrder is NULL else ApiStructure.ExecOrderField.from_address(<size_t> pExecOrder)
    )
    return 0

cdef extern int TraderSpi_OnErrRtnExecOrderInsert(self,
                                                  CThostFtdcInputExecOrderField *pInputExecOrder,
                                                  CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnExecOrderInsert(
        None if pInputExecOrder is NULL else ApiStructure.InputExecOrderField.from_address(<size_t> pInputExecOrder),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)
    )
    return 0

cdef extern int TraderSpi_OnErrRtnExecOrderAction(self,
                                                  CThostFtdcExecOrderActionField *pExecOrderAction,
                                                  CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnExecOrderAction(
        None if pExecOrderAction is NULL else ApiStructure.ExecOrderActionField.from_address(<size_t> pExecOrderAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)
    )
    return 0

cdef extern int TraderSpi_OnErrRtnForQuoteInsert(self,
                                                 CThostFtdcInputForQuoteField *pInputForQuote,
                                                 CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnForQuoteInsert(
        None if pInputForQuote is NULL else ApiStructure.InputForQuoteField.from_address(<size_t> pInputForQuote),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)
    )
    return 0

cdef extern int TraderSpi_OnRtnQuote(self, CThostFtdcQuoteField *pQuote) except -1:
    self.OnRtnQuote(
        None if pQuote is NULL else ApiStructure.QuoteField.from_address(<size_t> pQuote)
    )
    return 0

cdef extern int TraderSpi_OnErrRtnQuoteInsert(self,
                                              CThostFtdcInputQuoteField *pInputQuote,
                                              CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnQuoteInsert(
        None if pInputQuote is NULL else ApiStructure.InputQuoteField.from_address(<size_t> pInputQuote),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)
    )
    return 0

cdef extern int TraderSpi_OnErrRtnQuoteAction(self,
                                              CThostFtdcQuoteActionField *pQuoteAction,
                                              CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnQuoteAction(
        None if pQuoteAction is NULL else ApiStructure.QuoteActionField.from_address(<size_t> pQuoteAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)
    )
    return 0

cdef extern int TraderSpi_OnRtnForQuoteRsp(self, CThostFtdcForQuoteRspField *pForQuoteRsp) except -1:
    self.OnRtnForQuoteRsp(
        None if pForQuoteRsp is NULL else ApiStructure.ForQuoteRspField.from_address(<size_t> pForQuoteRsp)
    )
    return 0

cdef extern int TraderSpi_OnRtnCFMMCTradingAccountToken(self, CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken) except -1:
    self.OnRtnCFMMCTradingAccountToken(
        None if pCFMMCTradingAccountToken is NULL else ApiStructure.CFMMCTradingAccountTokenField.from_address(<size_t> pCFMMCTradingAccountToken)
    )
    return 0

cdef extern int TraderSpi_OnRtnCombAction(self, CThostFtdcCombActionField *pCombAction) except -1:
    self.OnRtnCombAction(
        None if pCombAction is NULL else ApiStructure.CombActionField.from_address(<size_t> pCombAction)
    )
    return 0

cdef extern int TraderSpi_OnErrRtnCombActionInsert(self,
                                                   CThostFtdcInputCombActionField *pInputCombAction,
                                                   CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnCombActionInsert(
        None if pInputCombAction is NULL else ApiStructure.InputCombActionField.from_address(<size_t> pInputCombAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)
    )
    return 0

cdef extern int TraderSpi_OnRspQryContractBank(self,
                                               CThostFtdcContractBankField *pContractBank,
                                               CThostFtdcRspInfoField *pRspInfo,
                                               int nRequestID,
                                               cbool bIsLast) except -1:
    self.OnRspQryContractBank(
        None if pContractBank is NULL else ApiStructure.ContractBankField.from_address(<size_t> pContractBank),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryParkedOrder(self,
                                              CThostFtdcParkedOrderField *pParkedOrder,
                                              CThostFtdcRspInfoField *pRspInfo,
                                              int nRequestID,
                                              cbool bIsLast) except -1:
    self.OnRspQryParkedOrder(
        None if pParkedOrder is NULL else ApiStructure.ParkedOrderField.from_address(<size_t> pParkedOrder),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryParkedOrderAction(self,
                                                    CThostFtdcParkedOrderActionField *pParkedOrderAction,
                                                    CThostFtdcRspInfoField *pRspInfo,
                                                    int nRequestID,
                                                    cbool bIsLast) except -1:
    self.OnRspQryParkedOrderAction(
        None if pParkedOrderAction is NULL else ApiStructure.ParkedOrderActionField.from_address(<size_t> pParkedOrderAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryTradingNotice(self,
                                                CThostFtdcTradingNoticeField *pTradingNotice,
                                                CThostFtdcRspInfoField *pRspInfo,
                                                int nRequestID,
                                                cbool bIsLast) except -1:
    self.OnRspQryTradingNotice(
        None if pTradingNotice is NULL else ApiStructure.TradingNoticeField.from_address(<size_t> pTradingNotice),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryBrokerTradingParams(self,
                                                      CThostFtdcBrokerTradingParamsField *pBrokerTradingParams,
                                                      CThostFtdcRspInfoField *pRspInfo,
                                                      int nRequestID,
                                                      cbool bIsLast) except -1:
    self.OnRspQryBrokerTradingParams(
        None if pBrokerTradingParams is NULL else ApiStructure.BrokerTradingParamsField.from_address(<size_t> pBrokerTradingParams),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryBrokerTradingAlgos(self,
                                                     CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos,
                                                     CThostFtdcRspInfoField *pRspInfo,
                                                     int nRequestID,
                                                     cbool bIsLast) except -1:
    self.OnRspQryBrokerTradingAlgos(
        None if pBrokerTradingAlgos is NULL else ApiStructure.BrokerTradingAlgosField.from_address(<size_t> pBrokerTradingAlgos),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQueryCFMMCTradingAccountToken(self,
                                                             CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken,
                                                             CThostFtdcRspInfoField *pRspInfo,
                                                             int nRequestID,
                                                             cbool bIsLast) except -1:
    self.OnRspQueryCFMMCTradingAccountToken(
        None if pQueryCFMMCTradingAccountToken is NULL else ApiStructure.QueryCFMMCTradingAccountTokenField.from_address(<size_t> pQueryCFMMCTradingAccountToken),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRtnFromBankToFutureByBank(self, CThostFtdcRspTransferField *pRspTransfer) except -1:
    self.OnRtnFromBankToFutureByBank(
        None if pRspTransfer is NULL else ApiStructure.RspTransferField.from_address(<size_t> pRspTransfer)
    )
    return 0

cdef extern int TraderSpi_OnRtnFromFutureToBankByBank(self, CThostFtdcRspTransferField *pRspTransfer) except -1:
    self.OnRtnFromFutureToBankByBank(
        None if pRspTransfer is NULL else ApiStructure.RspTransferField.from_address(<size_t> pRspTransfer)
    )
    return 0

cdef extern int TraderSpi_OnRtnRepealFromBankToFutureByBank(self, CThostFtdcRspRepealField *pRspRepeal) except -1:
    self.OnRtnRepealFromBankToFutureByBank(
        None if pRspRepeal is NULL else ApiStructure.RspRepealField.from_address(<size_t> pRspRepeal)
    )
    return 0

cdef extern int TraderSpi_OnRtnRepealFromFutureToBankByBank(self, CThostFtdcRspRepealField *pRspRepeal) except -1:
    self.OnRtnRepealFromFutureToBankByBank(
        None if pRspRepeal is NULL else ApiStructure.RspRepealField.from_address(<size_t> pRspRepeal)
    )
    return 0

cdef extern int TraderSpi_OnRtnFromBankToFutureByFuture(self, CThostFtdcRspTransferField *pRspTransfer) except -1:
    self.OnRtnFromBankToFutureByFuture(
        None if pRspTransfer is NULL else ApiStructure.RspTransferField.from_address(<size_t> pRspTransfer)
    )
    return 0

cdef extern int TraderSpi_OnRtnFromFutureToBankByFuture(self, CThostFtdcRspTransferField *pRspTransfer) except -1:
    self.OnRtnFromFutureToBankByFuture(
        None if pRspTransfer is NULL else ApiStructure.RspTransferField.from_address(<size_t> pRspTransfer)
    )
    return 0

cdef extern int TraderSpi_OnRtnRepealFromBankToFutureByFutureManual(self, CThostFtdcRspRepealField *pRspRepeal) except -1:
    self.OnRtnRepealFromBankToFutureByFutureManual(
        None if pRspRepeal is NULL else ApiStructure.RspRepealField.from_address(<size_t> pRspRepeal)
    )
    return 0

cdef extern int TraderSpi_OnRtnRepealFromFutureToBankByFutureManual(self, CThostFtdcRspRepealField *pRspRepeal) except -1:
    self.OnRtnRepealFromFutureToBankByFutureManual(
        None if pRspRepeal is NULL else ApiStructure.RspRepealField.from_address(<size_t> pRspRepeal)
    )
    return 0

cdef extern int TraderSpi_OnRtnQueryBankBalanceByFuture(self, CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount) except -1:
    self.OnRtnQueryBankBalanceByFuture(
        None if pNotifyQueryAccount is NULL else ApiStructure.NotifyQueryAccountField.from_address(<size_t> pNotifyQueryAccount)
    )
    return 0

cdef extern int TraderSpi_OnErrRtnBankToFutureByFuture(self,
                                                       CThostFtdcReqTransferField *pReqTransfer,
                                                       CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnBankToFutureByFuture(
        None if pReqTransfer is NULL else ApiStructure.ReqTransferField.from_address(<size_t> pReqTransfer),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)
    )
    return 0

cdef extern int TraderSpi_OnErrRtnFutureToBankByFuture(self,
                                                       CThostFtdcReqTransferField *pReqTransfer,
                                                       CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnFutureToBankByFuture(
        None if pReqTransfer is NULL else ApiStructure.ReqTransferField.from_address(<size_t> pReqTransfer),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)
    )
    return 0

cdef extern int TraderSpi_OnErrRtnRepealBankToFutureByFutureManual(self,
                                                                   CThostFtdcReqRepealField *pReqRepeal,
                                                                   CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnRepealBankToFutureByFutureManual(
        None if pReqRepeal is NULL else ApiStructure.ReqRepealField.from_address(<size_t> pReqRepeal),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)
    )
    return 0

cdef extern int TraderSpi_OnErrRtnRepealFutureToBankByFutureManual(self,
                                                                   CThostFtdcReqRepealField *pReqRepeal,
                                                                   CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnRepealFutureToBankByFutureManual(
        None if pReqRepeal is NULL else ApiStructure.ReqRepealField.from_address(<size_t> pReqRepeal),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)
    )
    return 0

cdef extern int TraderSpi_OnErrRtnQueryBankBalanceByFuture(self,
                                                           CThostFtdcReqQueryAccountField *pReqQueryAccount,
                                                           CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnQueryBankBalanceByFuture(
        None if pReqQueryAccount is NULL else ApiStructure.ReqQueryAccountField.from_address(<size_t> pReqQueryAccount),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)
    )
    return 0

cdef extern int TraderSpi_OnRtnRepealFromBankToFutureByFuture(self, CThostFtdcRspRepealField *pRspRepeal) except -1:
    self.OnRtnRepealFromBankToFutureByFuture(
        None if pRspRepeal is NULL else ApiStructure.RspRepealField.from_address(<size_t> pRspRepeal)
    )
    return 0

cdef extern int TraderSpi_OnRtnRepealFromFutureToBankByFuture(self, CThostFtdcRspRepealField *pRspRepeal) except -1:
    self.OnRtnRepealFromFutureToBankByFuture(
        None if pRspRepeal is NULL else ApiStructure.RspRepealField.from_address(<size_t> pRspRepeal)
    )
    return 0

cdef extern int TraderSpi_OnRspFromBankToFutureByFuture(self,
                                                        CThostFtdcReqTransferField *pReqTransfer,
                                                        CThostFtdcRspInfoField *pRspInfo,
                                                        int nRequestID,
                                                        cbool bIsLast) except -1:
    self.OnRspFromBankToFutureByFuture(
        None if pReqTransfer is NULL else ApiStructure.ReqTransferField.from_address(<size_t> pReqTransfer),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspFromFutureToBankByFuture(self,
                                                        CThostFtdcReqTransferField *pReqTransfer,
                                                        CThostFtdcRspInfoField *pRspInfo,
                                                        int nRequestID,
                                                        cbool bIsLast) except -1:
    self.OnRspFromFutureToBankByFuture(
        None if pReqTransfer is NULL else ApiStructure.ReqTransferField.from_address(<size_t> pReqTransfer),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQueryBankAccountMoneyByFuture(self,
                                                             CThostFtdcReqQueryAccountField *pReqQueryAccount,
                                                             CThostFtdcRspInfoField *pRspInfo,
                                                             int nRequestID,
                                                             cbool bIsLast) except -1:
    self.OnRspQueryBankAccountMoneyByFuture(
        None if pReqQueryAccount is NULL else ApiStructure.ReqQueryAccountField.from_address(<size_t> pReqQueryAccount),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRtnOpenAccountByBank(self, CThostFtdcOpenAccountField *pOpenAccount) except -1:
    self.OnRtnOpenAccountByBank(
        None if pOpenAccount is NULL else ApiStructure.OpenAccountField.from_address(<size_t> pOpenAccount)
    )
    return 0

cdef extern int TraderSpi_OnRtnCancelAccountByBank(self, CThostFtdcCancelAccountField *pCancelAccount) except -1:
    self.OnRtnCancelAccountByBank(
        None if pCancelAccount is NULL else ApiStructure.CancelAccountField.from_address(<size_t> pCancelAccount)
    )
    return 0

cdef extern int TraderSpi_OnRtnChangeAccountByBank(self, CThostFtdcChangeAccountField *pChangeAccount) except -1:
    self.OnRtnChangeAccountByBank(
        None if pChangeAccount is NULL else ApiStructure.ChangeAccountField.from_address(<size_t> pChangeAccount)
    )
    return 0

cdef extern int TraderSpi_OnErrRtnBatchOrderAction(self,
                                                   CThostFtdcBatchOrderActionField *pBatchOrderAction,
                                                   CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnBatchOrderAction(
        None if pBatchOrderAction is NULL else ApiStructure.BatchOrderActionField.from_address(<size_t> pBatchOrderAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)
    )
    return 0

cdef extern int TraderSpi_OnRtnBulletin(self, CThostFtdcBulletinField *pBulletin) except -1:
    self.OnRtnBulletin(
        None if pBulletin is NULL else ApiStructure.BulletinField.from_address(<size_t> pBulletin)
    )
    return 0

cdef extern int TraderSpi_OnRspQryInstrumentOrderCommRate(self,
                                                          CThostFtdcInstrumentOrderCommRateField *pInstrumentOrderCommRate,
                                                          CThostFtdcRspInfoField *pRspInfo,
                                                          int nRequestID,
                                                          cbool bIsLast) except -1:
    self.OnRspQryInstrumentOrderCommRate(
        None if pInstrumentOrderCommRate is NULL else ApiStructure.InstrumentOrderCommRateField.from_address(<size_t> pInstrumentOrderCommRate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryMMOptionInstrCommRate(self,
                                                        CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate,
                                                        CThostFtdcRspInfoField *pRspInfo,
                                                        int nRequestID,
                                                        cbool bIsLast) except -1:
    self.OnRspQryMMOptionInstrCommRate(
        None if pMMOptionInstrCommRate is NULL else ApiStructure.MMOptionInstrCommRateField.from_address(<size_t> pMMOptionInstrCommRate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspBatchOrderAction(self, CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction,
                                                CThostFtdcRspInfoField *pRspInfo,
                                                int nRequestID,
                                                cbool bIsLast) except -1:
    self.OnRspBatchOrderAction(
        None if pInputBatchOrderAction is NULL else ApiStructure.InputBatchOrderActionField.from_address(<size_t> pInputBatchOrderAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

cdef extern int TraderSpi_OnRspQryMMInstrumentCommissionRate(self,
                                                             CThostFtdcMMInstrumentCommissionRateField *pMMInstrumentCommissionRate,
                                                             CThostFtdcRspInfoField *pRspInfo,
                                                             int nRequestID,
                                                             cbool bIsLast) except -1:
    self.OnRspQryMMInstrumentCommissionRate(
        None if pRspInfo is NULL else ApiStructure.MMInstrumentCommissionRateField.from_address(<size_t> pMMInstrumentCommissionRate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0
cdef extern int TraderSpi_OnRspQryProductGroup(self,
                                               CThostFtdcProductGroupField *pProductGroup,
                                               CThostFtdcRspInfoField *pRspInfo,
                                               int nRequestID,
                                               cbool bIsLast) except -1:
    self.OnRspQryProductGroup(
        None if pProductGroup is NULL else ApiStructure.ProductGroupField.from_address(<size_t> pProductGroup),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# 期权自对冲录入请求响应
cdef extern int TraderSpi_OnRspOptionSelfCloseInsert(self,
                                                     CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose,
                                                     CThostFtdcRspInfoField *pRspInfo,
                                                     int nRequestID,
                                                     cbool bIsLast) except -1:
    self.OnRspOptionSelfCloseInsert(
        None if pInputOptionSelfClose is NULL else ApiStructure.InputOptionSelfCloseField.from_address(<size_t> pInputOptionSelfClose),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# 期权自对冲操作请求响应
cdef extern int TraderSpi_OnRspOptionSelfCloseAction(self,
                                                     CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction,
                                                     CThostFtdcRspInfoField *pRspInfo,
                                                     int nRequestID,
                                                     cbool bIsLast) except -1:
    self.OnRspOptionSelfCloseAction(
        None if pInputOptionSelfCloseAction is NULL else ApiStructure.InputOptionSelfCloseActionField.from_address(<size_t> pInputOptionSelfCloseAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# 请求查询资金账户响应
cdef extern int TraderSpi_OnRspQrySecAgentTradingAccount(self,
                                                         CThostFtdcTradingAccountField *pTradingAccount,
                                                         CThostFtdcRspInfoField *pRspInfo,
                                                         int nRequestID,
                                                         cbool bIsLast) except -1:
    self.OnRspQrySecAgentTradingAccount(
        None if pTradingAccount is NULL else ApiStructure.TradingAccountField.from_address(<size_t> pTradingAccount),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# 请求查询二级代理商资金校验模式响应
cdef extern int TraderSpi_OnRspQrySecAgentCheckMode(self,
                                                    CThostFtdcSecAgentCheckModeField *pSecAgentCheckMode,
                                                    CThostFtdcRspInfoField *pRspInfo,
                                                    int nRequestID,
                                                    cbool bIsLast) except -1:
    self.OnRspQrySecAgentCheckMode(
        None if pSecAgentCheckMode is NULL else ApiStructure.SecAgentCheckModeField.from_address(<size_t> pSecAgentCheckMode),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# 请求查询期权自对冲响应
cdef extern int TraderSpi_OnRspQryOptionSelfClose(self,
                                                  CThostFtdcOptionSelfCloseField *pOptionSelfClose,
                                                  CThostFtdcRspInfoField *pRspInfo,
                                                  int nRequestID,
                                                  cbool bIsLast) except -1:
    self.OnRspQryOptionSelfClose(
        None if pOptionSelfClose is NULL else ApiStructure.OptionSelfCloseField.from_address(<size_t> pOptionSelfClose),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# 请求查询投资单元响应
cdef extern int TraderSpi_OnRspQryInvestUnit(self,
                                             CThostFtdcInvestUnitField *pInvestUnit,
                                             CThostFtdcRspInfoField *pRspInfo,
                                             int nRequestID,
                                             cbool bIsLast) except -1:
    self.OnRspQryInvestUnit(
        None if pInvestUnit is NULL else ApiStructure.InvestUnitField.from_address(<size_t> pInvestUnit),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# 期权自对冲通知
cdef extern int TraderSpi_OnRtnOptionSelfClose(self, CThostFtdcOptionSelfCloseField *pOptionSelfClose) except -1:
    self.OnRtnOptionSelfClose(
        None if pOptionSelfClose is NULL else ApiStructure.OptionSelfCloseField.from_address(<size_t> pOptionSelfClose)
    )
    return 0

# 期权自对冲录入错误回报
cdef extern int TraderSpi_OnErrRtnOptionSelfCloseInsert(self,
                                                        CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose,
                                                        CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnOptionSelfCloseInsert(
        None if pInputOptionSelfClose is NULL else ApiStructure.InputOptionSelfCloseField.from_address(<size_t> pInputOptionSelfClose),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
    )
    return 0

# 期权自对冲操作错误回报
cdef extern int TraderSpi_OnErrRtnOptionSelfCloseAction(self,
                                                        CThostFtdcOptionSelfCloseActionField *pOptionSelfCloseAction,
                                                        CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnOptionSelfCloseAction(
        None if pOptionSelfCloseAction is NULL else ApiStructure.OptionSelfCloseActionField.from_address(<size_t> pOptionSelfCloseAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
    )
    return 0

# 查询用户当前支持的认证模式的回复
cdef extern int TraderSpi_OnRspUserAuthMethod(self,
                                              CThostFtdcRspUserAuthMethodField *pRspUserAuthMethod,
                                              CThostFtdcRspInfoField *pRspInfo,
                                              int nRequestID,
                                              cbool bIsLast) except -1:
    self.OnErrRtnOptionSelfCloseAction(
        None if pRspUserAuthMethod is NULL else ApiStructure.RspUserAuthMethodField.from_address(<size_t> pRspUserAuthMethod),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# 获取图形验证码请求的回复
cdef extern int TraderSpi_OnRspGenUserCaptcha(self,
                                              CThostFtdcRspGenUserCaptchaField *pRspGenUserCaptcha,
                                              CThostFtdcRspInfoField *pRspInfo,
                                              int nRequestID,
                                              cbool bIsLast) except -1:
    self.OnErrRtnOptionSelfCloseAction(
        None if pRspGenUserCaptcha is NULL else ApiStructure.RspGenUserCaptchaField.from_address(<size_t> pRspGenUserCaptcha),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# 获取短信验证码请求的回复
cdef extern int TraderSpi_OnRspGenUserText(self,
                                           CThostFtdcRspGenUserTextField *pRspGenUserText,
                                           CThostFtdcRspInfoField *pRspInfo,
                                           int nRequestID,
                                           cbool bIsLast) except -1:
    self.OnErrRtnOptionSelfCloseAction(
        None if pRspGenUserText is NULL else ApiStructure.RspGenUserTextField.from_address(<size_t> pRspGenUserText),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# 请求查询二级代理商信息响应
cdef extern int TraderSpi_OnRspQrySecAgentTradeInfo(self,
                                                    CThostFtdcSecAgentTradeInfoField *pSecAgentTradeInfo,
                                                    CThostFtdcRspInfoField *pRspInfo,
                                                    int nRequestID,
                                                    cbool bIsLast) except -1:
    self.OnErrRtnOptionSelfCloseAction(
        None if pSecAgentTradeInfo is NULL else ApiStructure.SecAgentTradeInfoField.from_address(<size_t> pSecAgentTradeInfo),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# 请求查询分类合约响应
cdef extern int TraderSpi_OnRspQryClassifiedInstrument(self,
                                                       CThostFtdcInstrumentField *pInstrument,
                                                       CThostFtdcRspInfoField *pRspInfo,
                                                       int nRequestID,
                                                       cbool bIsLast) except -1:
    self.OnRspQryClassifiedInstrument(
        None if pInstrument is NULL else ApiStructure.InstrumentField.from_address(<size_t> pInstrument),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# 请求组合优惠比例响应
cdef extern int TraderSpi_OnRspQryCombPromotionParam(self,
                                                     CThostFtdcCombPromotionParamField *pCombPromotionParam,
                                                     CThostFtdcRspInfoField *pRspInfo,
                                                     int nRequestID,
                                                     cbool bIsLast) except -1:
    self.OnRspQryClassifiedInstrument(
        None if pCombPromotionParam is NULL else ApiStructure.CombPromotionParamField.from_address(<size_t> pCombPromotionParam),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# 投资者风险结算持仓查询响应
cdef extern int TraderSpi_OnRspQryRiskSettleInvstPosition(self,
                                                          CThostFtdcRiskSettleInvstPositionField *pRiskSettleInvstPosition,
                                                          CThostFtdcRspInfoField *pRspInfo,
                                                          int nRequestID,
                                                          cbool bIsLast) except -1:
    self.OnRspQryRiskSettleInvstPosition(
        None if pRiskSettleInvstPosition is NULL else ApiStructure.RiskSettleInvstPositionField.from_address(<size_t> pRiskSettleInvstPosition),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# 风险结算产品查询
cdef extern int TraderSpi_OnRspQryRiskSettleProductStatus(self,
                                                          CThostFtdcRiskSettleProductStatusField *pRiskSettleProductStatus,
                                                          CThostFtdcRspInfoField *pRspInfo,
                                                          int nRequestID,
                                                          cbool bIsLast) except -1:
    self.OnRspQryRiskSettleProductStatus(
        None if pRiskSettleProductStatus is NULL else ApiStructure.RiskSettleProductStatusField.from_address(<size_t> pRiskSettleProductStatus),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# 风险结算产品查询
cdef extern int TraderSpi_OnRspQryTraderOffer(self,
                                              CThostFtdcTraderOfferField *pTraderOffer,
                                              CThostFtdcRspInfoField *pRspInfo,
                                              int nRequestID,
                                              cbool bIsLast) except -1:
    self.OnRspQryTraderOffer(
        None if pTraderOffer is NULL else ApiStructure.TraderOfferField.from_address(<size_t> pTraderOffer),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# SPBM期货合约参数查询响应
cdef extern int TraderSpi_OnRspQrySPBMFutureParameter(self,
                                                      CThostFtdcSPBMFutureParameterField *pSPBMFutureParameter,
                                                      CThostFtdcRspInfoField *pRspInfo,
                                                      int nRequestID,
                                                      cbool bIsLast) except -1:
    self.OnRspQrySPBMFutureParameter(
        None if pSPBMFutureParameter is NULL else ApiStructure.SPBMFutureParameterField.from_address(<size_t> pSPBMFutureParameter),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# SPBM期权合约参数查询响应
cdef extern int TraderSpi_OnRspQrySPBMOptionParameter(self,
                                                      CThostFtdcSPBMOptionParameterField *pSPBMOptionParameter,
                                                      CThostFtdcRspInfoField *pRspInfo,
                                                      int nRequestID,
                                                      cbool bIsLast) except -1:
    self.OnRspQrySPBMOptionParameter(
        None if pSPBMOptionParameter is NULL else ApiStructure.SPBMOptionParameterField.from_address(<size_t> pSPBMOptionParameter),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# SPBM品种内对锁仓折扣参数查询响应
cdef extern int TraderSpi_OnRspQrySPBMIntraParameter(self,
                                                     CThostFtdcSPBMIntraParameterField *pSPBMIntraParameter,
                                                     CThostFtdcRspInfoField *pRspInfo,
                                                     int nRequestID,
                                                     cbool bIsLast) except -1:
    self.OnRspQrySPBMIntraParameter(
        None if pSPBMIntraParameter is NULL else ApiStructure.SPBMIntraParameterField.from_address(<size_t> pSPBMIntraParameter),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# SPBM跨品种抵扣参数查询响应
cdef extern int TraderSpi_OnRspQrySPBMInterParameter(self,
                                                     CThostFtdcSPBMInterParameterField *pSPBMInterParameter,
                                                     CThostFtdcRspInfoField *pRspInfo,
                                                     int nRequestID,
                                                     cbool bIsLast) except -1:
    self.OnRspQrySPBMInterParameter(
        None if pSPBMInterParameter is NULL else ApiStructure.SPBMInterParameterField.from_address(<size_t> pSPBMInterParameter),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# SPBM组合保证金套餐查询响应
cdef extern int TraderSpi_OnRspQrySPBMPortfDefinition(self,
                                                      CThostFtdcSPBMPortfDefinitionField *pSPBMPortfDefinition,
                                                      CThostFtdcRspInfoField *pRspInfo,
                                                      int nRequestID,
                                                      cbool bIsLast) except -1:
    self.OnRspQrySPBMPortfDefinition(
        None if pSPBMPortfDefinition is NULL else ApiStructure.SPBMPortfDefinitionField.from_address(<size_t> pSPBMPortfDefinition),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# 投资者SPBM套餐选择查询响应
cdef extern int TraderSpi_OnRspQrySPBMInvestorPortfDef(self,
                                                       CThostFtdcSPBMInvestorPortfDefField *pSPBMInvestorPortfDef,
                                                       CThostFtdcRspInfoField *pRspInfo,
                                                       int nRequestID,
                                                       cbool bIsLast) except -1:
    self.OnRspQrySPBMInvestorPortfDef(
        None if pSPBMInvestorPortfDef is NULL else ApiStructure.SPBMInvestorPortfDefField.from_address(<size_t> pSPBMInvestorPortfDef),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# 投资者新型组合保证金系数查询响应
cdef extern int TraderSpi_OnRspQryInvestorPortfMarginRatio(self,
                                                           CThostFtdcInvestorPortfMarginRatioField *pInvestorPortfMarginRatio,
                                                           CThostFtdcRspInfoField *pRspInfo,
                                                           int nRequestID,
                                                           cbool bIsLast) except -1:
    self.OnRspQryInvestorPortfMarginRatio(
        None if pInvestorPortfMarginRatio is NULL else ApiStructure.InvestorPortfMarginRatioField.from_address(<size_t> pInvestorPortfMarginRatio),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0

# 投资者产品SPBM明细查询响应
cdef extern int TraderSpi_OnRspQryInvestorProdSPBMDetail(self,
                                                         CThostFtdcInvestorProdSPBMDetailField *pInvestorProdSPBMDetail,
                                                         CThostFtdcRspInfoField *pRspInfo,
                                                         int nRequestID,
                                                         cbool bIsLast) except -1:
    self.OnRspQryInvestorProdSPBMDetail(
        None if pInvestorProdSPBMDetail is NULL else ApiStructure.InvestorProdSPBMDetailField.from_address(<size_t> pInvestorProdSPBMDetail),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast
    )
    return 0
