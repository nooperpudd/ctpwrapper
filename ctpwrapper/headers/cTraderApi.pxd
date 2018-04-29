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

from .ThostFtdcUserApiStruct cimport *


cdef extern from "ThostFtdcTraderApi.h":

    cdef cppclass CTraderApi "CThostFtdcTraderApi":

        @staticmethod
        const_char *GetApiVersion() nogil

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
        void RegisterSpi(CTraderSpi *pSpi) nogil except +

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

        #登录请求2
        int ReqUserLogin2(CThostFtdcReqUserLoginField *pReqUserLogin, int nRequestID) nogil except +

        #用户口令更新请求2
        int ReqUserPasswordUpdate2(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, int nRequestID) nogil except +


        #报单录入请求
        int ReqOrderInsert(CThostFtdcInputOrderField *pInputOrder, int nRequestID) nogil except +

        #预埋单录入请求
        int ReqParkedOrderInsert(CThostFtdcParkedOrderField *pParkedOrder, int nRequestID) nogil except +

        #预埋撤单录入请求
        int ReqParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, int nRequestID) nogil except +

        #报单操作请求
        int ReqOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, int nRequestID) nogil except +

        #查询最大报单数量请求
        int ReqQueryMaxOrderVolume(CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, int nRequestID) nogil except +

        #投资者结算结果确认
        int ReqSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, int nRequestID) nogil except +

        #请求删除预埋单
        int ReqRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, int nRequestID) nogil except +

        #请求删除预埋撤单
        int ReqRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, int nRequestID) nogil except +

        #执行宣告录入请求
        int ReqExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, int nRequestID) nogil except +

        #执行宣告操作请求
        int ReqExecOrderAction(CThostFtdcInputExecOrderActionField *pInputExecOrderAction, int nRequestID) nogil except +

        #询价录入请求
        int ReqForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, int nRequestID) nogil except +

        #报价录入请求
        int ReqQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, int nRequestID) nogil except +

        #报价操作请求
        int ReqQuoteAction(CThostFtdcInputQuoteActionField *pInputQuoteAction, int nRequestID) nogil except +

        #批量报单操作请求
        int ReqBatchOrderAction(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, int nRequestID) nogil except +


        #期权自对冲录入请求
        int ReqOptionSelfCloseInsert(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose, int nRequestID) nogil except +

        #期权自对冲操作请求
        int ReqOptionSelfCloseAction(CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction,
                                         int nRequestID) nogil except +

        #申请组合录入请求
        int ReqCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, int nRequestID) nogil except +

        #请求查询报单
        int ReqQryOrder(CThostFtdcQryOrderField *pQryOrder, int nRequestID) nogil except +

        #请求查询成交
        int ReqQryTrade(CThostFtdcQryTradeField *pQryTrade, int nRequestID) nogil except +

        #请求查询投资者持仓
        int ReqQryInvestorPosition(CThostFtdcQryInvestorPositionField *pQryInvestorPosition, int nRequestID) nogil except +

        #请求查询资金账户
        int ReqQryTradingAccount(CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID) nogil except +

        #请求查询投资者
        int ReqQryInvestor(CThostFtdcQryInvestorField *pQryInvestor, int nRequestID) nogil except +

        #请求查询交易编码
        int ReqQryTradingCode(CThostFtdcQryTradingCodeField *pQryTradingCode, int nRequestID) nogil except +

        #请求查询合约保证金率
        int ReqQryInstrumentMarginRate(CThostFtdcQryInstrumentMarginRateField *pQryInstrumentMarginRate, int nRequestID) nogil except +

        #请求查询合约手续费率
        int ReqQryInstrumentCommissionRate(CThostFtdcQryInstrumentCommissionRateField *pQryInstrumentCommissionRate, int nRequestID) nogil except +

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
        int ReqQryInvestorPositionDetail(CThostFtdcQryInvestorPositionDetailField *pQryInvestorPositionDetail, int nRequestID) nogil except +

        #请求查询客户通知
        int ReqQryNotice(CThostFtdcQryNoticeField *pQryNotice, int nRequestID) nogil except +

        #请求查询结算信息确认
        int ReqQrySettlementInfoConfirm(CThostFtdcQrySettlementInfoConfirmField *pQrySettlementInfoConfirm, int nRequestID) nogil except +

        #请求查询投资者持仓明细
        int ReqQryInvestorPositionCombineDetail(CThostFtdcQryInvestorPositionCombineDetailField *pQryInvestorPositionCombineDetail, int nRequestID) nogil except +

        #请求查询保证金监管系统经纪公司资金账户密钥
        int ReqQryCFMMCTradingAccountKey(CThostFtdcQryCFMMCTradingAccountKeyField *pQryCFMMCTradingAccountKey, int nRequestID) nogil except +

        #请求查询仓单折抵信息
        int ReqQryEWarrantOffset(CThostFtdcQryEWarrantOffsetField *pQryEWarrantOffset, int nRequestID) nogil except +

        #请求查询投资者品种/跨品种保证金
        int ReqQryInvestorProductGroupMargin(CThostFtdcQryInvestorProductGroupMarginField *pQryInvestorProductGroupMargin, int nRequestID) nogil except +

        #请求查询交易所保证金率
        int ReqQryExchangeMarginRate(CThostFtdcQryExchangeMarginRateField *pQryExchangeMarginRate, int nRequestID) nogil except +

        #请求查询交易所调整保证金率
        int ReqQryExchangeMarginRateAdjust(CThostFtdcQryExchangeMarginRateAdjustField *pQryExchangeMarginRateAdjust, int nRequestID) nogil except +

        #请求查询汇率
        int ReqQryExchangeRate(CThostFtdcQryExchangeRateField *pQryExchangeRate, int nRequestID) nogil except +

        #请求查询二级代理操作员银期权限
        int ReqQrySecAgentACIDMap(CThostFtdcQrySecAgentACIDMapField *pQrySecAgentACIDMap, int nRequestID) nogil except +

        #请求查询产品报价汇率
        int ReqQryProductExchRate(CThostFtdcQryProductExchRateField *pQryProductExchRate, int nRequestID) nogil except +

        #请求查询产品组
        int ReqQryProductGroup(CThostFtdcQryProductGroupField *pQryProductGroup, int nRequestID) nogil except +

        #请求查询做市商合约手续费率
        int ReqQryMMInstrumentCommissionRate(CThostFtdcQryMMInstrumentCommissionRateField *pQryMMInstrumentCommissionRate, int nRequestID) nogil except +

        #请求查询做市商期权合约手续费
        int ReqQryMMOptionInstrCommRate(CThostFtdcQryMMOptionInstrCommRateField *pQryMMOptionInstrCommRate, int nRequestID) nogil except +

        #请求查询报单手续费
        int ReqQryInstrumentOrderCommRate(CThostFtdcQryInstrumentOrderCommRateField *pQryInstrumentOrderCommRate, int nRequestID) nogil except +

        #请求查询资金账户
        int ReqQrySecAgentTradingAccount(CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID) nogil except +

        #请求查询二级代理商资金校验模式
        int ReqQrySecAgentCheckMode(CThostFtdcQrySecAgentCheckModeField *pQrySecAgentCheckMode, int nRequestID) nogil except +


        #请求查询期权交易成本
        int ReqQryOptionInstrTradeCost(CThostFtdcQryOptionInstrTradeCostField *pQryOptionInstrTradeCost, int nRequestID) nogil except +

        #请求查询期权合约手续费
        int ReqQryOptionInstrCommRate(CThostFtdcQryOptionInstrCommRateField *pQryOptionInstrCommRate, int nRequestID) nogil except +

        #请求查询执行宣告
        int ReqQryExecOrder(CThostFtdcQryExecOrderField *pQryExecOrder, int nRequestID) nogil except +

        #请求查询询价
        int ReqQryForQuote(CThostFtdcQryForQuoteField *pQryForQuote, int nRequestID) nogil except +

        #请求查询报价
        int ReqQryQuote(CThostFtdcQryQuoteField *pQryQuote, int nRequestID) nogil except +

        #请求查询期权自对冲
        int ReqQryOptionSelfClose(CThostFtdcQryOptionSelfCloseField *pQryOptionSelfClose, int nRequestID) nogil except +

        #请求查询投资单元
        int ReqQryInvestUnit(CThostFtdcQryInvestUnitField *pQryInvestUnit, int nRequestID) nogil except +

        #请求查询组合合约安全系数
        int ReqQryCombInstrumentGuard(CThostFtdcQryCombInstrumentGuardField *pQryCombInstrumentGuard, int nRequestID) nogil except +

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
        int ReqQryParkedOrderAction(CThostFtdcQryParkedOrderActionField *pQryParkedOrderAction, int nRequestID) nogil except +

        #请求查询交易通知
        int ReqQryTradingNotice(CThostFtdcQryTradingNoticeField *pQryTradingNotice, int nRequestID) nogil except +

        #请求查询经纪公司交易参数
        int ReqQryBrokerTradingParams(CThostFtdcQryBrokerTradingParamsField *pQryBrokerTradingParams, int nRequestID) nogil except +

        #请求查询经纪公司交易算法
        int ReqQryBrokerTradingAlgos(CThostFtdcQryBrokerTradingAlgosField *pQryBrokerTradingAlgos, int nRequestID) nogil except +

        #请求查询监控中心用户令牌
        int ReqQueryCFMMCTradingAccountToken(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken, int nRequestID) nogil except +

        #期货发起银行资金转期货请求
        int ReqFromBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, int nRequestID) nogil except +

        #期货发起期货资金转银行请求
        int ReqFromFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, int nRequestID) nogil except +

        #期货发起查询银行余额请求
        int ReqQueryBankAccountMoneyByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, int nRequestID) nogil except +

cdef extern from "ThostFtdcTraderApi.h" namespace "CThostFtdcTraderApi":
    CTraderApi *CreateFtdcTraderApi(const_char *pszFlowPath) nogil except +

cdef extern from "CTraderAPI.h":
    cdef cppclass CTraderSpi:
        CTraderSpi(PyObject *obj)  # todo nogil
