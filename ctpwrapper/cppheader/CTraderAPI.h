/*
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

*/

#ifndef CTRADERAPI_H
#define CTRADERAPI_H

#include "Python.h"
#include "pythread.h"
#include "ThostFtdcTraderApi.h"

static inline int TraderSpi_OnFrontConnected(PyObject *);
static inline int TraderSpi_OnFrontDisconnected(PyObject *, int);
static inline int TraderSpi_OnHeartBeatWarning(PyObject *, int);
static inline int TraderSpi_OnRspAuthenticate(PyObject *, CThostFtdcRspAuthenticateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspUserLogin(PyObject *, CThostFtdcRspUserLoginField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspUserLogout(PyObject *, CThostFtdcUserLogoutField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspUserPasswordUpdate(PyObject *, CThostFtdcUserPasswordUpdateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspTradingAccountPasswordUpdate(PyObject *, CThostFtdcTradingAccountPasswordUpdateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspOrderInsert(PyObject *, CThostFtdcInputOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspParkedOrderInsert(PyObject *, CThostFtdcParkedOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspParkedOrderAction(PyObject *, CThostFtdcParkedOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspOrderAction(PyObject *, CThostFtdcInputOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQueryMaxOrderVolume(PyObject *, CThostFtdcQueryMaxOrderVolumeField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspSettlementInfoConfirm(PyObject *, CThostFtdcSettlementInfoConfirmField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspRemoveParkedOrder(PyObject *, CThostFtdcRemoveParkedOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspRemoveParkedOrderAction(PyObject *, CThostFtdcRemoveParkedOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspExecOrderInsert(PyObject *, CThostFtdcInputExecOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspExecOrderAction(PyObject *, CThostFtdcInputExecOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspForQuoteInsert(PyObject *, CThostFtdcInputForQuoteField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQuoteInsert(PyObject *, CThostFtdcInputQuoteField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQuoteAction(PyObject *, CThostFtdcInputQuoteActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspCombActionInsert(PyObject *, CThostFtdcInputCombActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryOrder(PyObject *, CThostFtdcOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryTrade(PyObject *, CThostFtdcTradeField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInvestorPosition(PyObject *, CThostFtdcInvestorPositionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryTradingAccount(PyObject *, CThostFtdcTradingAccountField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInvestor(PyObject *, CThostFtdcInvestorField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryTradingCode(PyObject *, CThostFtdcTradingCodeField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInstrumentMarginRate(PyObject *, CThostFtdcInstrumentMarginRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInstrumentCommissionRate(PyObject *, CThostFtdcInstrumentCommissionRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryExchange(PyObject *, CThostFtdcExchangeField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryProduct(PyObject *, CThostFtdcProductField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInstrument(PyObject *, CThostFtdcInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryDepthMarketData(PyObject *, CThostFtdcDepthMarketDataField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQrySettlementInfo(PyObject *, CThostFtdcSettlementInfoField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryTransferBank(PyObject *, CThostFtdcTransferBankField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInvestorPositionDetail(PyObject *, CThostFtdcInvestorPositionDetailField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryNotice(PyObject *, CThostFtdcNoticeField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQrySettlementInfoConfirm(PyObject *, CThostFtdcSettlementInfoConfirmField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInvestorPositionCombineDetail(PyObject *, CThostFtdcInvestorPositionCombineDetailField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryCFMMCTradingAccountKey(PyObject *, CThostFtdcCFMMCTradingAccountKeyField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryEWarrantOffset(PyObject *, CThostFtdcEWarrantOffsetField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInvestorProductGroupMargin(PyObject *, CThostFtdcInvestorProductGroupMarginField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryExchangeMarginRate(PyObject *, CThostFtdcExchangeMarginRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryExchangeMarginRateAdjust(PyObject *, CThostFtdcExchangeMarginRateAdjustField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryExchangeRate(PyObject *, CThostFtdcExchangeRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQrySecAgentACIDMap(PyObject *, CThostFtdcSecAgentACIDMapField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryProductExchRate(PyObject *, CThostFtdcProductExchRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryOptionInstrTradeCost(PyObject *, CThostFtdcOptionInstrTradeCostField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryOptionInstrCommRate(PyObject *, CThostFtdcOptionInstrCommRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryExecOrder(PyObject *, CThostFtdcExecOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryForQuote(PyObject *, CThostFtdcForQuoteField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryQuote(PyObject *, CThostFtdcQuoteField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryCombInstrumentGuard(PyObject *, CThostFtdcCombInstrumentGuardField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryCombAction(PyObject *, CThostFtdcCombActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryTransferSerial(PyObject *, CThostFtdcTransferSerialField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryAccountregister(PyObject *, CThostFtdcAccountregisterField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspError(PyObject *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRtnOrder(PyObject *, CThostFtdcOrderField *);
static inline int TraderSpi_OnRtnTrade(PyObject *, CThostFtdcTradeField *);
static inline int TraderSpi_OnErrRtnOrderInsert(PyObject *, CThostFtdcInputOrderField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnErrRtnOrderAction(PyObject *, CThostFtdcOrderActionField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnRtnInstrumentStatus(PyObject *, CThostFtdcInstrumentStatusField *);
static inline int TraderSpi_OnRtnTradingNotice(PyObject *, CThostFtdcTradingNoticeInfoField *);
static inline int TraderSpi_OnRtnErrorConditionalOrder(PyObject *, CThostFtdcErrorConditionalOrderField *);
static inline int TraderSpi_OnRtnExecOrder(PyObject *, CThostFtdcExecOrderField *);
static inline int TraderSpi_OnErrRtnExecOrderInsert(PyObject *, CThostFtdcInputExecOrderField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnErrRtnExecOrderAction(PyObject *, CThostFtdcExecOrderActionField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnErrRtnForQuoteInsert(PyObject *, CThostFtdcInputForQuoteField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnRtnQuote(PyObject *, CThostFtdcQuoteField *);
static inline int TraderSpi_OnErrRtnQuoteInsert(PyObject *, CThostFtdcInputQuoteField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnErrRtnQuoteAction(PyObject *, CThostFtdcQuoteActionField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnRtnForQuoteRsp(PyObject *, CThostFtdcForQuoteRspField *);
static inline int TraderSpi_OnRtnCFMMCTradingAccountToken(PyObject *, CThostFtdcCFMMCTradingAccountTokenField *);
static inline int TraderSpi_OnRtnCombAction(PyObject *, CThostFtdcCombActionField *);
static inline int TraderSpi_OnErrRtnCombActionInsert(PyObject *, CThostFtdcInputCombActionField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnRspQryContractBank(PyObject *, CThostFtdcContractBankField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryParkedOrder(PyObject *, CThostFtdcParkedOrderField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryParkedOrderAction(PyObject *, CThostFtdcParkedOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryTradingNotice(PyObject *, CThostFtdcTradingNoticeField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryBrokerTradingParams(PyObject *, CThostFtdcBrokerTradingParamsField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryBrokerTradingAlgos(PyObject *, CThostFtdcBrokerTradingAlgosField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQueryCFMMCTradingAccountToken(PyObject *, CThostFtdcQueryCFMMCTradingAccountTokenField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRtnFromBankToFutureByBank(PyObject *, CThostFtdcRspTransferField *);
static inline int TraderSpi_OnRtnFromFutureToBankByBank(PyObject *, CThostFtdcRspTransferField *);
static inline int TraderSpi_OnRtnRepealFromBankToFutureByBank(PyObject *, CThostFtdcRspRepealField *);
static inline int TraderSpi_OnRtnRepealFromFutureToBankByBank(PyObject *, CThostFtdcRspRepealField *);
static inline int TraderSpi_OnRtnFromBankToFutureByFuture(PyObject *, CThostFtdcRspTransferField *);
static inline int TraderSpi_OnRtnFromFutureToBankByFuture(PyObject *, CThostFtdcRspTransferField *);
static inline int TraderSpi_OnRtnRepealFromBankToFutureByFutureManual(PyObject *, CThostFtdcRspRepealField *);
static inline int TraderSpi_OnRtnRepealFromFutureToBankByFutureManual(PyObject *, CThostFtdcRspRepealField *);
static inline int TraderSpi_OnRtnQueryBankBalanceByFuture(PyObject *, CThostFtdcNotifyQueryAccountField *);
static inline int TraderSpi_OnErrRtnBankToFutureByFuture(PyObject *, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnErrRtnFutureToBankByFuture(PyObject *, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnErrRtnRepealBankToFutureByFutureManual(PyObject *, CThostFtdcReqRepealField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnErrRtnRepealFutureToBankByFutureManual(PyObject *, CThostFtdcReqRepealField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnErrRtnQueryBankBalanceByFuture(PyObject *, CThostFtdcReqQueryAccountField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnRtnRepealFromBankToFutureByFuture(PyObject *, CThostFtdcRspRepealField *);
static inline int TraderSpi_OnRtnRepealFromFutureToBankByFuture(PyObject *, CThostFtdcRspRepealField *);
static inline int TraderSpi_OnRspFromBankToFutureByFuture(PyObject *, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspFromFutureToBankByFuture(PyObject *, CThostFtdcReqTransferField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQueryBankAccountMoneyByFuture(PyObject *, CThostFtdcReqQueryAccountField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRtnOpenAccountByBank(PyObject *, CThostFtdcOpenAccountField *);
static inline int TraderSpi_OnRtnCancelAccountByBank(PyObject *, CThostFtdcCancelAccountField *);
static inline int TraderSpi_OnRtnChangeAccountByBank(PyObject *, CThostFtdcChangeAccountField *);

static inline int TraderSpi_OnErrRtnBatchOrderAction(PyObject *, CThostFtdcBatchOrderActionField *, CThostFtdcRspInfoField *);
static inline int TraderSpi_OnRtnBulletin(PyObject *, CThostFtdcBulletinField *);
static inline int TraderSpi_OnRspQryInstrumentOrderCommRate(PyObject *,CThostFtdcInstrumentOrderCommRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryMMOptionInstrCommRate(PyObject *,CThostFtdcMMOptionInstrCommRateField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspBatchOrderAction(PyObject *, CThostFtdcInputBatchOrderActionField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryMMInstrumentCommissionRate(PyObject *, CThostFtdcMMInstrumentCommissionRateField *,CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryProductGroup(PyObject *, CThostFtdcProductGroupField *,CThostFtdcRspInfoField *, int, bool);

static inline int TraderSpi_OnRspOptionSelfCloseInsert(PyObject *, CThostFtdcInputOptionSelfCloseField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspOptionSelfCloseAction(PyObject *, CThostFtdcInputOptionSelfCloseActionField *, CThostFtdcRspInfoField *, int, bool);

static inline int TraderSpi_OnRspQrySecAgentTradingAccount(PyObject *, CThostFtdcTradingAccountField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQrySecAgentCheckMode(PyObject *, CThostFtdcSecAgentCheckModeField *, CThostFtdcRspInfoField *, int, bool);

static inline int TraderSpi_OnRspQryOptionSelfClose(PyObject *, CThostFtdcOptionSelfCloseField *, CThostFtdcRspInfoField *, int, bool);
static inline int TraderSpi_OnRspQryInvestUnit(PyObject *, CThostFtdcInvestUnitField *, CThostFtdcRspInfoField *, int, bool);

static inline int TraderSpi_OnRtnOptionSelfClose(PyObject *, CThostFtdcOptionSelfCloseField *);

static inline int TraderSpi_OnErrRtnOptionSelfCloseInsert(PyObject *, CThostFtdcInputOptionSelfCloseField *, CThostFtdcRspInfoField *);

static inline int TraderSpi_OnErrRtnOptionSelfCloseAction(PyObject *, CThostFtdcOptionSelfCloseActionField *, CThostFtdcRspInfoField *);




#define Python_GIL(func) \
	do { \
		PyGILState_STATE gil_state = PyGILState_Ensure(); \
		if ((func) == -1) PyErr_Print();  \
		PyGILState_Release(gil_state); \
	} while (false)


class CTraderSpi: public CThostFtdcTraderSpi {
public:

    CTraderSpi(PyObject *obj):self(obj) {};

    virtual ~CTraderSpi() {};

    ///当客户端与交易后台建立起通信连接时（还未登录前），该方法被调用。
    virtual void OnFrontConnected() {
        Python_GIL(TraderSpi_OnFrontConnected(self));
    };

    ///当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
    ///@param nReason 错误原因
    ///        0x1001 网络读失败
    ///        0x1002 网络写失败
    ///        0x2001 接收心跳超时
    ///        0x2002 发送心跳失败
    ///        0x2003 收到错误报文
    virtual void OnFrontDisconnected(int nReason) {
        Python_GIL(TraderSpi_OnFrontDisconnected(self,nReason));
    };

    ///心跳超时警告。当长时间未收到报文时，该方法被调用。
    ///@param nTimeLapse 距离上次接收报文的时间
    virtual void OnHeartBeatWarning(int nTimeLapse) {
        Python_GIL(TraderSpi_OnHeartBeatWarning(self,nTimeLapse));
    };

    ///客户端认证响应
    virtual void OnRspAuthenticate(CThostFtdcRspAuthenticateField *pRspAuthenticateField, CThostFtdcRspInfoField *pRspInfo,int nRequestID, bool bIsLast) {
        Python_GIL(TraderSpi_OnRspAuthenticate(self,pRspAuthenticateField,pRspInfo,nRequestID,bIsLast));
    };


    ///登录请求响应
    virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        Python_GIL(TraderSpi_OnRspUserLogin(self,pRspUserLogin,pRspInfo,nRequestID,bIsLast));
    };

    ///登出请求响应
    virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID,bool bIsLast) {
        Python_GIL(TraderSpi_OnRspUserLogout(self,pUserLogout,pRspInfo,nRequestID,bIsLast));
    };

    ///用户口令更新请求响应
    virtual void OnRspUserPasswordUpdate(CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        Python_GIL(TraderSpi_OnRspUserPasswordUpdate(self,pUserPasswordUpdate,pRspInfo,nRequestID,bIsLast));
    };

    ///资金账户口令更新请求响应
    virtual void OnRspTradingAccountPasswordUpdate(CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        Python_GIL(TraderSpi_OnRspTradingAccountPasswordUpdate(self,pTradingAccountPasswordUpdate,pRspInfo,nRequestID,bIsLast));
    };

    ///报单录入请求响应
    virtual void OnRspOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                     bool bIsLast) {
                     Python_GIL(TraderSpi_OnRspOrderInsert(self,pInputOrder,pRspInfo,nRequestID,bIsLast));
                     };

    ///预埋单录入请求响应
    virtual void OnRspParkedOrderInsert(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                           bool bIsLast) {
                           Python_GIL(TraderSpi_OnRspParkedOrderInsert(self,pParkedOrder,pRspInfo,nRequestID,bIsLast));
                           };

    ///预埋撤单录入请求响应
    virtual void OnRspParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo,
                           int nRequestID, bool bIsLast) {
                           Python_GIL(TraderSpi_OnRspParkedOrderAction(self,pParkedOrderAction,pRspInfo,nRequestID,bIsLast));
                           };

    ///报单操作请求响应
    virtual void OnRspOrderAction(CThostFtdcInputOrderActionField *pInputOrderAction, CThostFtdcRspInfoField *pRspInfo,
                                  int nRequestID, bool bIsLast) {
                                  Python_GIL(TraderSpi_OnRspOrderAction(self,pInputOrderAction,pRspInfo,nRequestID,bIsLast));
                                  };

    ///查询最大报单数量响应
    virtual void OnRspQueryMaxOrderVolume(CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, CThostFtdcRspInfoField *pRspInfo,
                             int nRequestID, bool bIsLast) {
                             Python_GIL(TraderSpi_OnRspQueryMaxOrderVolume(self,pQueryMaxOrderVolume,pRspInfo,nRequestID,bIsLast));
                             };

    ///投资者结算结果确认响应
    virtual void OnRspSettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm,
                                            CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                            Python_GIL(TraderSpi_OnRspSettlementInfoConfirm(self,pSettlementInfoConfirm,pRspInfo,nRequestID,bIsLast));
                                            };

    ///删除预埋单响应
    virtual void OnRspRemoveParkedOrder(CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, CThostFtdcRspInfoField *pRspInfo,
                           int nRequestID, bool bIsLast) {
                           Python_GIL(TraderSpi_OnRspRemoveParkedOrder(self,pRemoveParkedOrder,pRspInfo,nRequestID,bIsLast));
                           };

    ///删除预埋撤单响应
    virtual void OnRspRemoveParkedOrderAction(CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction,
                                              CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                              Python_GIL(TraderSpi_OnRspRemoveParkedOrderAction(self,pRemoveParkedOrderAction,pRspInfo,nRequestID,bIsLast));
                                              };

    ///执行宣告录入请求响应
    virtual void OnRspExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo,
                                      int nRequestID, bool bIsLast) {
                                      Python_GIL(TraderSpi_OnRspExecOrderInsert(self,pInputExecOrder,pRspInfo,nRequestID,bIsLast));
                                      };

    ///执行宣告操作请求响应
    virtual void OnRspExecOrderAction(CThostFtdcInputExecOrderActionField *pInputExecOrderAction, CThostFtdcRspInfoField *pRspInfo,
                         int nRequestID, bool bIsLast) {
                         Python_GIL(TraderSpi_OnRspExecOrderAction(self,pInputExecOrderAction,pRspInfo,nRequestID,bIsLast));
                         };

    ///询价录入请求响应
    virtual void OnRspForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                        bool bIsLast) {
                        Python_GIL(TraderSpi_OnRspForQuoteInsert(self,pInputForQuote,pRspInfo,nRequestID,bIsLast));
                        };

    ///报价录入请求响应
    virtual void OnRspQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                     bool bIsLast) {
                     Python_GIL(TraderSpi_OnRspQuoteInsert(self,pInputQuote,pRspInfo,nRequestID,bIsLast));
                     };

    ///报价操作请求响应
    virtual void OnRspQuoteAction(CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo,
                                  int nRequestID, bool bIsLast) {
                                  Python_GIL(TraderSpi_OnRspQuoteAction(self,pInputQuoteAction,pRspInfo,nRequestID,bIsLast));
                                  };

    ///批量报单操作请求响应
    virtual void OnRspBatchOrderAction(CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction,
                                       CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                       Python_GIL(TraderSpi_OnRspBatchOrderAction(self,pInputBatchOrderAction,pRspInfo,nRequestID,bIsLast));
                                       };
    ///期权自对冲录入请求响应
    virtual void OnRspOptionSelfCloseInsert(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose,
                                            CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                            Python_GIL(TraderSpi_OnRspOptionSelfCloseInsert(self,pInputOptionSelfClose,pRspInfo,nRequestID,bIsLast));
                                            };

    ///期权自对冲操作请求响应
    virtual void OnRspOptionSelfCloseAction(CThostFtdcInputOptionSelfCloseActionField *pInputOptionSelfCloseAction,
                                            CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                            Python_GIL(TraderSpi_OnRspOptionSelfCloseAction(self,pInputOptionSelfCloseAction,pRspInfo,nRequestID,bIsLast));
                                            };

    ///申请组合录入请求响应
    virtual void OnRspCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo,
                          int nRequestID, bool bIsLast) {
                          Python_GIL(TraderSpi_OnRspCombActionInsert(self,pInputCombAction,pRspInfo,nRequestID,bIsLast));
                          };

    ///请求查询报单响应
    virtual void OnRspQryOrder(CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    Python_GIL(TraderSpi_OnRspQryOrder(self,pOrder,pRspInfo,nRequestID,bIsLast));
    };

    ///请求查询成交响应
    virtual void OnRspQryTrade(CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    Python_GIL(TraderSpi_OnRspQryTrade(self,pTrade,pRspInfo,nRequestID,bIsLast));
    };

    ///请求查询投资者持仓响应
    virtual void OnRspQryInvestorPosition(CThostFtdcInvestorPositionField *pInvestorPosition, CThostFtdcRspInfoField *pRspInfo,
                             int nRequestID, bool bIsLast) {
                             Python_GIL(TraderSpi_OnRspQryInvestorPosition(self,pInvestorPosition,pRspInfo,nRequestID,bIsLast));
                             };

    ///请求查询资金账户响应
    virtual void OnRspQryTradingAccount(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo,
                           int nRequestID, bool bIsLast) {
                           Python_GIL(TraderSpi_OnRspQryTradingAccount(self,pTradingAccount,pRspInfo,nRequestID,bIsLast));
                           };

    ///请求查询投资者响应
    virtual void OnRspQryInvestor(CThostFtdcInvestorField *pInvestor, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                  bool bIsLast) {
                                  Python_GIL(TraderSpi_OnRspQryInvestor(self,pInvestor,pRspInfo,nRequestID,bIsLast));
                                  };

    ///请求查询交易编码响应
    virtual void OnRspQryTradingCode(CThostFtdcTradingCodeField *pTradingCode, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                        bool bIsLast) {
                        Python_GIL(TraderSpi_OnRspQryTradingCode(self,pTradingCode,pRspInfo,nRequestID,bIsLast));
                        };

    ///请求查询合约保证金率响应
    virtual void OnRspQryInstrumentMarginRate(CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate,
                                              CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                              Python_GIL(TraderSpi_OnRspQryInstrumentMarginRate(self,pInstrumentMarginRate,pRspInfo,nRequestID,bIsLast));
                                              };

    ///请求查询合约手续费率响应
    virtual void OnRspQryInstrumentCommissionRate(CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate,
                                                  CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                                  Python_GIL(TraderSpi_OnRspQryInstrumentCommissionRate(self,pInstrumentCommissionRate,pRspInfo,nRequestID,bIsLast));
                                                  };

    ///请求查询交易所响应
    virtual void OnRspQryExchange(CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                  bool bIsLast) {
                                  Python_GIL(TraderSpi_OnRspQryExchange(self,pExchange,pRspInfo,nRequestID,bIsLast));
                                  };

    ///请求查询产品响应
    virtual void OnRspQryProduct(CThostFtdcProductField *pProduct, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                 bool bIsLast) {
                                 Python_GIL(TraderSpi_OnRspQryProduct(self,pProduct,pRspInfo,nRequestID,bIsLast));
                                 };

    ///请求查询合约响应
    virtual void OnRspQryInstrument(CThostFtdcInstrumentField *pInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                       bool bIsLast) {
                       Python_GIL(TraderSpi_OnRspQryInstrument(self,pInstrument,pRspInfo,nRequestID,bIsLast));
                       };

    ///请求查询行情响应
    virtual void OnRspQryDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData, CThostFtdcRspInfoField *pRspInfo,
                            int nRequestID, bool bIsLast) {
                            Python_GIL(TraderSpi_OnRspQryDepthMarketData(self,pDepthMarketData,pRspInfo,nRequestID,bIsLast));
                            };

    ///请求查询投资者结算结果响应
    virtual void OnRspQrySettlementInfo(CThostFtdcSettlementInfoField *pSettlementInfo, CThostFtdcRspInfoField *pRspInfo,
                           int nRequestID, bool bIsLast) {
                           Python_GIL(TraderSpi_OnRspQrySettlementInfo(self,pSettlementInfo,pRspInfo,nRequestID,bIsLast));
                           };

    ///请求查询转帐银行响应
    virtual void OnRspQryTransferBank(CThostFtdcTransferBankField *pTransferBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                         bool bIsLast) {
                         Python_GIL(TraderSpi_OnRspQryTransferBank(self,pTransferBank,pRspInfo,nRequestID,bIsLast));
                         };

    ///请求查询投资者持仓明细响应
    virtual void OnRspQryInvestorPositionDetail(CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail,
                                                CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                                Python_GIL(TraderSpi_OnRspQryInvestorPositionDetail(self,pInvestorPositionDetail,pRspInfo,nRequestID,bIsLast));
                                                };

    ///请求查询客户通知响应
    virtual void OnRspQryNotice(CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    Python_GIL(TraderSpi_OnRspQryNotice(self,pNotice,pRspInfo,nRequestID,bIsLast));
    };

    ///请求查询结算信息确认响应
    virtual void OnRspQrySettlementInfoConfirm(CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm,
                                               CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                               Python_GIL(TraderSpi_OnRspQrySettlementInfoConfirm(self,pSettlementInfoConfirm,pRspInfo,nRequestID,bIsLast));
                                               };

    ///请求查询投资者持仓明细响应
    virtual void OnRspQryInvestorPositionCombineDetail(CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail,
                                          CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                          Python_GIL(TraderSpi_OnRspQryInvestorPositionCombineDetail(self,pInvestorPositionCombineDetail,pRspInfo,nRequestID,bIsLast));
                                          };

    ///查询保证金监管系统经纪公司资金账户密钥响应
    virtual void OnRspQryCFMMCTradingAccountKey(CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey,
                                                CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                                Python_GIL(TraderSpi_OnRspQryCFMMCTradingAccountKey(self,pCFMMCTradingAccountKey,pRspInfo,nRequestID,bIsLast));
                                                };

    ///请求查询仓单折抵信息响应
    virtual void OnRspQryEWarrantOffset(CThostFtdcEWarrantOffsetField *pEWarrantOffset, CThostFtdcRspInfoField *pRspInfo,
                           int nRequestID, bool bIsLast) {
                           Python_GIL(TraderSpi_OnRspQryEWarrantOffset(self,pEWarrantOffset,pRspInfo,nRequestID,bIsLast));
                           };

    ///请求查询投资者品种/跨品种保证金响应
    virtual void OnRspQryInvestorProductGroupMargin(CThostFtdcInvestorProductGroupMarginField *pInvestorProductGroupMargin,
                                       CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                       Python_GIL(TraderSpi_OnRspQryInvestorProductGroupMargin(self,pInvestorProductGroupMargin,pRspInfo,nRequestID,bIsLast));
                                       };

    ///请求查询交易所保证金率响应
    virtual void OnRspQryExchangeMarginRate(CThostFtdcExchangeMarginRateField *pExchangeMarginRate, CThostFtdcRspInfoField *pRspInfo,
                               int nRequestID, bool bIsLast) {
                               Python_GIL(TraderSpi_OnRspQryExchangeMarginRate(self,pExchangeMarginRate,pRspInfo,nRequestID,bIsLast));
                               };

    ///请求查询交易所调整保证金率响应
    virtual void OnRspQryExchangeMarginRateAdjust(CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust,
                                                  CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                                  Python_GIL(TraderSpi_OnRspQryExchangeMarginRateAdjust(self,pExchangeMarginRateAdjust,pRspInfo,nRequestID,bIsLast));
                                                  };

    ///请求查询汇率响应
    virtual void OnRspQryExchangeRate(CThostFtdcExchangeRateField *pExchangeRate, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                         bool bIsLast) {
                         Python_GIL(TraderSpi_OnRspQryExchangeRate(self,pExchangeRate,pRspInfo,nRequestID,bIsLast));
                         };

    ///请求查询二级代理操作员银期权限响应
    virtual void
    OnRspQrySecAgentACIDMap(CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap, CThostFtdcRspInfoField *pRspInfo,
                            int nRequestID, bool bIsLast) {
                            Python_GIL(TraderSpi_OnRspQrySecAgentACIDMap(self,pSecAgentACIDMap,pRspInfo,nRequestID,bIsLast));
                            };

    ///请求查询产品报价汇率
    virtual void OnRspQryProductExchRate(CThostFtdcProductExchRateField *pProductExchRate, CThostFtdcRspInfoField *pRspInfo,int nRequestID, bool bIsLast) {
        Python_GIL(TraderSpi_OnRspQryProductExchRate(self,pProductExchRate,pRspInfo,nRequestID,bIsLast));
    };

    ///请求查询产品组
    virtual void OnRspQryProductGroup(CThostFtdcProductGroupField *pProductGroup, CThostFtdcRspInfoField *pRspInfo, int nRequestID,bool bIsLast) {
        Python_GIL(TraderSpi_OnRspQryProductGroup(self,pProductGroup,pRspInfo,nRequestID,bIsLast));
    };

    ///请求查询做市商合约手续费率响应
    virtual void OnRspQryMMInstrumentCommissionRate(CThostFtdcMMInstrumentCommissionRateField *pMMInstrumentCommissionRate,
                                       CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                       Python_GIL(TraderSpi_OnRspQryMMInstrumentCommissionRate(self,pMMInstrumentCommissionRate,pRspInfo,nRequestID,bIsLast));
                                       };

    ///请求查询做市商期权合约手续费响应
    virtual void OnRspQryMMOptionInstrCommRate(CThostFtdcMMOptionInstrCommRateField *pMMOptionInstrCommRate,
                                               CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                               Python_GIL(TraderSpi_OnRspQryMMOptionInstrCommRate(self,pMMOptionInstrCommRate,pRspInfo,nRequestID,bIsLast));
                                               };

    ///请求查询报单手续费响应
    virtual void OnRspQryInstrumentOrderCommRate(CThostFtdcInstrumentOrderCommRateField *pInstrumentOrderCommRate,
                                                 CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                                 Python_GIL(TraderSpi_OnRspQryInstrumentOrderCommRate(self,pInstrumentOrderCommRate,pRspInfo,nRequestID,bIsLast));
                                                 };

    ///请求查询资金账户响应
    virtual void OnRspQrySecAgentTradingAccount(CThostFtdcTradingAccountField *pTradingAccount, CThostFtdcRspInfoField *pRspInfo,
                                   int nRequestID, bool bIsLast) {
                                   Python_GIL(TraderSpi_OnRspQrySecAgentTradingAccount(self,pTradingAccount,pRspInfo,nRequestID,bIsLast));
                                   };

    ///请求查询二级代理商资金校验模式响应
    virtual void OnRspQrySecAgentCheckMode(CThostFtdcSecAgentCheckModeField *pSecAgentCheckMode, CThostFtdcRspInfoField *pRspInfo,
                              int nRequestID, bool bIsLast) {
                              Python_GIL(TraderSpi_OnRspQrySecAgentCheckMode(self,pSecAgentCheckMode,pRspInfo,nRequestID,bIsLast));
                              };


    ///请求查询期权交易成本响应
    virtual void OnRspQryOptionInstrTradeCost(CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost,
                                              CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                              Python_GIL(TraderSpi_OnRspQryOptionInstrTradeCost(self,pOptionInstrTradeCost,pRspInfo,nRequestID,bIsLast));
                                              };

    ///请求查询期权合约手续费响应
    virtual void OnRspQryOptionInstrCommRate(CThostFtdcOptionInstrCommRateField *pOptionInstrCommRate,
                                             CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                             Python_GIL(TraderSpi_OnRspQryOptionInstrCommRate(self,pOptionInstrCommRate,pRspInfo,nRequestID,bIsLast));
                                             };

    ///请求查询执行宣告响应
    virtual void OnRspQryExecOrder(CThostFtdcExecOrderField *pExecOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                      bool bIsLast) {
                      Python_GIL(TraderSpi_OnRspQryExecOrder(self,pExecOrder,pRspInfo,nRequestID,bIsLast));
                      };

    ///请求查询询价响应
    virtual void OnRspQryForQuote(CThostFtdcForQuoteField *pForQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                  bool bIsLast) {
                                  Python_GIL(TraderSpi_OnRspQryForQuote(self,pForQuote,pRspInfo,nRequestID,bIsLast));
                                  };

    ///请求查询报价响应
    virtual void OnRspQryQuote(CThostFtdcQuoteField *pQuote, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    Python_GIL(TraderSpi_OnRspQryQuote(self,pQuote,pRspInfo,nRequestID,bIsLast));
    };

    ///请求查询期权自对冲响应
    virtual void OnRspQryOptionSelfClose(CThostFtdcOptionSelfCloseField *pOptionSelfClose, CThostFtdcRspInfoField *pRspInfo,
                            int nRequestID, bool bIsLast) {
                            Python_GIL(TraderSpi_OnRspQryOptionSelfClose(self,pOptionSelfClose,pRspInfo,nRequestID,bIsLast));

                            };

    ///请求查询投资单元响应
    virtual void OnRspQryInvestUnit(CThostFtdcInvestUnitField *pInvestUnit, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                       bool bIsLast) {
                       Python_GIL(TraderSpi_OnRspQryInvestUnit(self,pInvestUnit,pRspInfo,nRequestID,bIsLast));

                       };

    ///请求查询组合合约安全系数响应
    virtual void OnRspQryCombInstrumentGuard(CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard,
                                             CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                             Python_GIL(TraderSpi_OnRspQryCombInstrumentGuard(self,pCombInstrumentGuard,pRspInfo,nRequestID,bIsLast));
                                             };

    ///请求查询申请组合响应
    virtual void
    OnRspQryCombAction(CThostFtdcCombActionField *pCombAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                       bool bIsLast) {
                       Python_GIL(TraderSpi_OnRspQryCombAction(self,pCombAction,pRspInfo,nRequestID,bIsLast));
                       };

    ///请求查询转帐流水响应
    virtual void
    OnRspQryTransferSerial(CThostFtdcTransferSerialField *pTransferSerial, CThostFtdcRspInfoField *pRspInfo,
                           int nRequestID, bool bIsLast) {
                           Python_GIL(TraderSpi_OnRspQryTransferSerial(self,pTransferSerial,pRspInfo,nRequestID,bIsLast));
                           };

    ///请求查询银期签约关系响应
    virtual void
    OnRspQryAccountregister(CThostFtdcAccountregisterField *pAccountregister, CThostFtdcRspInfoField *pRspInfo,
                            int nRequestID, bool bIsLast) {
                            Python_GIL(TraderSpi_OnRspQryAccountregister(self,pAccountregister,pRspInfo,nRequestID,bIsLast));
                            };

    ///错误应答
    virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
    Python_GIL(TraderSpi_OnRspError(self,pRspInfo,nRequestID,bIsLast));
    };

    ///报单通知
    virtual void OnRtnOrder(CThostFtdcOrderField *pOrder) {
    Python_GIL(TraderSpi_OnRtnOrder(self,pOrder));
    };

    ///成交通知
    virtual void OnRtnTrade(CThostFtdcTradeField *pTrade) {
    Python_GIL(TraderSpi_OnRtnTrade(self,pTrade));
    };

    ///报单录入错误回报
    virtual void OnErrRtnOrderInsert(CThostFtdcInputOrderField *pInputOrder, CThostFtdcRspInfoField *pRspInfo) {
    Python_GIL(TraderSpi_OnErrRtnOrderInsert(self,pInputOrder,pRspInfo));
    };

    ///报单操作错误回报
    virtual void OnErrRtnOrderAction(CThostFtdcOrderActionField *pOrderAction, CThostFtdcRspInfoField *pRspInfo) {
    Python_GIL(TraderSpi_OnErrRtnOrderAction(self,pOrderAction,pRspInfo));
    };

    ///合约交易状态通知
    virtual void OnRtnInstrumentStatus(CThostFtdcInstrumentStatusField *pInstrumentStatus) {
    Python_GIL(TraderSpi_OnRtnInstrumentStatus(self,pInstrumentStatus));
    };

    ///交易所公告通知
    virtual void OnRtnBulletin(CThostFtdcBulletinField *pBulletin) {
    Python_GIL(TraderSpi_OnRtnBulletin(self,pBulletin));
    };

    ///交易通知
    virtual void OnRtnTradingNotice(CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) {
    Python_GIL(TraderSpi_OnRtnTradingNotice(self,pTradingNoticeInfo));
    };

    ///提示条件单校验错误
    virtual void OnRtnErrorConditionalOrder(CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder) {
    Python_GIL(TraderSpi_OnRtnErrorConditionalOrder(self,pErrorConditionalOrder));
    };

    ///执行宣告通知
    virtual void OnRtnExecOrder(CThostFtdcExecOrderField *pExecOrder) {
    Python_GIL(TraderSpi_OnRtnExecOrder(self,pExecOrder));
    };

    ///执行宣告录入错误回报
    virtual void OnErrRtnExecOrderInsert(CThostFtdcInputExecOrderField *pInputExecOrder, CThostFtdcRspInfoField *pRspInfo) {
    Python_GIL(TraderSpi_OnErrRtnExecOrderInsert(self,pInputExecOrder,pRspInfo));
    };

    ///执行宣告操作错误回报
    virtual void OnErrRtnExecOrderAction(CThostFtdcExecOrderActionField *pExecOrderAction, CThostFtdcRspInfoField *pRspInfo) {
    Python_GIL(TraderSpi_OnErrRtnExecOrderAction(self,pExecOrderAction,pRspInfo));
    };

    ///询价录入错误回报
    virtual void OnErrRtnForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo) {
    Python_GIL(TraderSpi_OnErrRtnForQuoteInsert(self,pInputForQuote,pRspInfo));
    };

    ///报价通知
    virtual void OnRtnQuote(CThostFtdcQuoteField *pQuote) {
    Python_GIL(TraderSpi_OnRtnQuote(self,pQuote));
    };

    ///报价录入错误回报
    virtual void OnErrRtnQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo) {
    Python_GIL(TraderSpi_OnErrRtnQuoteInsert(self,pInputQuote,pRspInfo));
    };

    ///报价操作错误回报
    virtual void OnErrRtnQuoteAction(CThostFtdcQuoteActionField *pQuoteAction, CThostFtdcRspInfoField *pRspInfo) {
    Python_GIL(TraderSpi_OnErrRtnQuoteAction(self,pQuoteAction,pRspInfo));
    };

    ///询价通知
    virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {
        Python_GIL(TraderSpi_OnRtnForQuoteRsp(self,pForQuoteRsp));
    };

    ///保证金监控中心用户令牌
    virtual void OnRtnCFMMCTradingAccountToken(CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken) {
        Python_GIL(TraderSpi_OnRtnCFMMCTradingAccountToken(self,pCFMMCTradingAccountToken));
    };

    ///批量报单操作错误回报
    virtual void OnErrRtnBatchOrderAction(CThostFtdcBatchOrderActionField *pBatchOrderAction, CThostFtdcRspInfoField *pRspInfo) {
    Python_GIL(TraderSpi_OnErrRtnBatchOrderAction(self,pBatchOrderAction,pRspInfo));
    };

    ///期权自对冲通知
    virtual void OnRtnOptionSelfClose(CThostFtdcOptionSelfCloseField *pOptionSelfClose) {
    Python_GIL(TraderSpi_OnRtnOptionSelfClose(self,pOptionSelfClose));

    };

    ///期权自对冲录入错误回报
    virtual void OnErrRtnOptionSelfCloseInsert(CThostFtdcInputOptionSelfCloseField *pInputOptionSelfClose,
                                               CThostFtdcRspInfoField *pRspInfo) {
                                               Python_GIL(TraderSpi_OnErrRtnOptionSelfCloseInsert(self,pInputOptionSelfClose,pRspInfo));

                                               };

    ///期权自对冲操作错误回报
    virtual void OnErrRtnOptionSelfCloseAction(CThostFtdcOptionSelfCloseActionField *pOptionSelfCloseAction,
                                               CThostFtdcRspInfoField *pRspInfo) {
                                               Python_GIL(TraderSpi_OnErrRtnOptionSelfCloseAction(self,pOptionSelfCloseAction,pRspInfo));

                                               };



    ///申请组合通知
    virtual void OnRtnCombAction(CThostFtdcCombActionField *pCombAction) {
    Python_GIL(TraderSpi_OnRtnCombAction(self,pCombAction));
    };

    ///申请组合录入错误回报
    virtual void OnErrRtnCombActionInsert(CThostFtdcInputCombActionField *pInputCombAction, CThostFtdcRspInfoField *pRspInfo) {
    Python_GIL(TraderSpi_OnErrRtnCombActionInsert(self,pInputCombAction,pRspInfo));
    };

    ///请求查询签约银行响应
    virtual void OnRspQryContractBank(CThostFtdcContractBankField *pContractBank, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                         bool bIsLast) {
                         Python_GIL(TraderSpi_OnRspQryContractBank(self,pContractBank,pRspInfo,nRequestID,bIsLast));
                         };

    ///请求查询预埋单响应
    virtual void OnRspQryParkedOrder(CThostFtdcParkedOrderField *pParkedOrder, CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                        bool bIsLast) {
                        Python_GIL(TraderSpi_OnRspQryParkedOrder(self,pParkedOrder,pRspInfo,nRequestID,bIsLast));
                        };

    ///请求查询预埋撤单响应
    virtual void OnRspQryParkedOrderAction(CThostFtdcParkedOrderActionField *pParkedOrderAction, CThostFtdcRspInfoField *pRspInfo,
                              int nRequestID, bool bIsLast) {
                              Python_GIL(TraderSpi_OnRspQryParkedOrderAction(self,pParkedOrderAction,pRspInfo,nRequestID,bIsLast));
                              };

    ///请求查询交易通知响应
    virtual void OnRspQryTradingNotice(CThostFtdcTradingNoticeField *pTradingNotice, CThostFtdcRspInfoField *pRspInfo,
                                       int nRequestID, bool bIsLast) {
                                       Python_GIL(TraderSpi_OnRspQryTradingNotice(self,pTradingNotice,pRspInfo,nRequestID,bIsLast));
                                       };

    ///请求查询经纪公司交易参数响应
    virtual void OnRspQryBrokerTradingParams(CThostFtdcBrokerTradingParamsField *pBrokerTradingParams,
                                             CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                             Python_GIL(TraderSpi_OnRspQryBrokerTradingParams(self,pBrokerTradingParams,pRspInfo,nRequestID,bIsLast));
                                             };

    ///请求查询经纪公司交易算法响应
    virtual void OnRspQryBrokerTradingAlgos(CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos, CThostFtdcRspInfoField *pRspInfo,
                               int nRequestID, bool bIsLast) {
                               Python_GIL(TraderSpi_OnRspQryBrokerTradingAlgos(self,pBrokerTradingAlgos,pRspInfo,nRequestID,bIsLast));
                               };

    ///请求查询监控中心用户令牌
    virtual void OnRspQueryCFMMCTradingAccountToken(CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken,
                                       CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
                                       Python_GIL(TraderSpi_OnRspQueryCFMMCTradingAccountToken(self,pQueryCFMMCTradingAccountToken,pRspInfo,nRequestID,bIsLast));
                                       };

    ///银行发起银行资金转期货通知
    virtual void OnRtnFromBankToFutureByBank(CThostFtdcRspTransferField *pRspTransfer) {
    Python_GIL(TraderSpi_OnRtnFromBankToFutureByBank(self,pRspTransfer));
    };

    ///银行发起期货资金转银行通知
    virtual void OnRtnFromFutureToBankByBank(CThostFtdcRspTransferField *pRspTransfer) {
    Python_GIL(TraderSpi_OnRtnFromFutureToBankByBank(self,pRspTransfer));
    };

    ///银行发起冲正银行转期货通知
    virtual void OnRtnRepealFromBankToFutureByBank(CThostFtdcRspRepealField *pRspRepeal) {
    Python_GIL(TraderSpi_OnRtnRepealFromBankToFutureByBank(self,pRspRepeal));
    };

    ///银行发起冲正期货转银行通知
    virtual void OnRtnRepealFromFutureToBankByBank(CThostFtdcRspRepealField *pRspRepeal) {
    Python_GIL(TraderSpi_OnRtnRepealFromFutureToBankByBank(self,pRspRepeal));
    };

    ///期货发起银行资金转期货通知
    virtual void OnRtnFromBankToFutureByFuture(CThostFtdcRspTransferField *pRspTransfer) {
    Python_GIL(TraderSpi_OnRtnFromBankToFutureByFuture(self,pRspTransfer));
    };

    ///期货发起期货资金转银行通知
    virtual void OnRtnFromFutureToBankByFuture(CThostFtdcRspTransferField *pRspTransfer) {
    Python_GIL(TraderSpi_OnRtnFromFutureToBankByFuture(self,pRspTransfer));
    };

    ///系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
    virtual void OnRtnRepealFromBankToFutureByFutureManual(CThostFtdcRspRepealField *pRspRepeal) {
    Python_GIL(TraderSpi_OnRtnRepealFromBankToFutureByFutureManual(self,pRspRepeal));
    };

    ///系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
    virtual void OnRtnRepealFromFutureToBankByFutureManual(CThostFtdcRspRepealField *pRspRepeal) {
    Python_GIL(TraderSpi_OnRtnRepealFromFutureToBankByFutureManual(self,pRspRepeal));
    };

    ///期货发起查询银行余额通知
    virtual void OnRtnQueryBankBalanceByFuture(CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount) {
    Python_GIL(TraderSpi_OnRtnQueryBankBalanceByFuture(self,pNotifyQueryAccount));
    };

    ///期货发起银行资金转期货错误回报
    virtual void OnErrRtnBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo) {
    Python_GIL(TraderSpi_OnErrRtnBankToFutureByFuture(self,pReqTransfer,pRspInfo));
    };

    ///期货发起期货资金转银行错误回报
    virtual void OnErrRtnFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo) {
    Python_GIL(TraderSpi_OnErrRtnFutureToBankByFuture(self,pReqTransfer,pRspInfo));
    };

    ///系统运行时期货端手工发起冲正银行转期货错误回报
    virtual void OnErrRtnRepealBankToFutureByFutureManual(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo) {
    Python_GIL(TraderSpi_OnErrRtnRepealBankToFutureByFutureManual(self,pReqRepeal,pRspInfo));
    };

    ///系统运行时期货端手工发起冲正期货转银行错误回报
    virtual void OnErrRtnRepealFutureToBankByFutureManual(CThostFtdcReqRepealField *pReqRepeal, CThostFtdcRspInfoField *pRspInfo) {
    Python_GIL(TraderSpi_OnErrRtnRepealFutureToBankByFutureManual(self,pReqRepeal,pRspInfo));
    };

    ///期货发起查询银行余额错误回报
    virtual void OnErrRtnQueryBankBalanceByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount,
                                                  CThostFtdcRspInfoField *pRspInfo) {
                                                  Python_GIL(TraderSpi_OnErrRtnQueryBankBalanceByFuture(self,pReqQueryAccount,pRspInfo));
                                                  };

    ///期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
    virtual void OnRtnRepealFromBankToFutureByFuture(CThostFtdcRspRepealField *pRspRepeal) {
    Python_GIL(TraderSpi_OnRtnRepealFromBankToFutureByFuture(self,pRspRepeal));
    };

    ///期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
    virtual void OnRtnRepealFromFutureToBankByFuture(CThostFtdcRspRepealField *pRspRepeal) {
    Python_GIL(TraderSpi_OnRtnRepealFromFutureToBankByFuture(self,pRspRepeal));
    };

    ///期货发起银行资金转期货应答
    virtual void OnRspFromBankToFutureByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo,
                                  int nRequestID, bool bIsLast) {
                                  Python_GIL(TraderSpi_OnRspFromBankToFutureByFuture(self,pReqTransfer,pRspInfo,nRequestID,bIsLast));
                                  };

    ///期货发起期货资金转银行应答
    virtual void OnRspFromFutureToBankByFuture(CThostFtdcReqTransferField *pReqTransfer, CThostFtdcRspInfoField *pRspInfo,
                                  int nRequestID, bool bIsLast) {
                                  Python_GIL(TraderSpi_OnRspFromFutureToBankByFuture(self,pReqTransfer,pRspInfo,nRequestID,bIsLast));
                                  };

    ///期货发起查询银行余额应答
    virtual void OnRspQueryBankAccountMoneyByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
        Python_GIL(TraderSpi_OnRspQueryBankAccountMoneyByFuture(self,pReqQueryAccount,pRspInfo,nRequestID,bIsLast));
    };

    ///银行发起银期开户通知
    virtual void OnRtnOpenAccountByBank(CThostFtdcOpenAccountField *pOpenAccount) {
        Python_GIL(TraderSpi_OnRtnOpenAccountByBank(self,pOpenAccount));
    };

    ///银行发起银期销户通知
    virtual void OnRtnCancelAccountByBank(CThostFtdcCancelAccountField *pCancelAccount) {
        Python_GIL(TraderSpi_OnRtnCancelAccountByBank(self,pCancelAccount));
    };

    ///银行发起变更银行账号通知
    virtual void OnRtnChangeAccountByBank(CThostFtdcChangeAccountField *pChangeAccount) {
        Python_GIL(TraderSpi_OnRtnChangeAccountByBank(self,pChangeAccount));
    };

private:
	PyObject *self;
};

#endif /* CTRADERAPI_H */
