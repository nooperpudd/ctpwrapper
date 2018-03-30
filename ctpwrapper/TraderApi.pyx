# encoding:utf-8
# distutils: language = c++
# cython: nonecheck=True
# cython: profile=False
# cython: binding=True

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

from headers.ThostFtdcUserApiStruct cimport *
from libcpp cimport bool as cbool

from . import ApiStructure


class TraderApiWrapper:
    def __cinit__(self):
        pass

    def __dealloc__(self):
        pass


cdef extern int TraderSpi_OnFrontConnected(self) except -1:
    self.OnFrontConnected()
    return 0

cdef extern int TraderSpi_OnFrontDisconnected(self, int nReason) except -1:
    self.OnFrontDisconnected(nReason)
    return 0

cdef extern int TraderSpi_OnHeartBeatWarning(self, int nTimeLapse) except -1:
    self.OnHeartBeatWarning(nTimeLapse)
    return 0

cdef extern int TraderSpi_OnRspAuthenticate(self, CThostFtdcRspAuthenticateField *pRspAuthenticate,
                                            CThostFtdcRspInfoField *pRspInfo,
                                            int nRequestID, cbool bIsLast) except -1:
    self.OnRspAuthenticate(
        None if pRspAuthenticate is NULL else ApiStructure.RspAuthenticateField.from_address(<size_t> pRspAuthenticate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspUserLogin(self, CThostFtdcRspUserLoginField *pRspUserLogin,
                                         CThostFtdcRspInfoField *pRspInfo,
                                         int nRequestID, cbool bIsLast) except -1:
    self.OnRspUserLogin(
        None if pRspUserLogin is NULL else ApiStructure.RspUserLoginField.from_address(<size_t> pRspUserLogin),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspUserLogout(self, CThostFtdcUserLogoutField *pUserLogout,
                                          CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                          cbool bIsLast) except -1:
    self.OnRspUserLogout(
        None if pUserLogout is NULL else ApiStructure.UserLogoutField.from_address(<size_t> pUserLogout),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspUserPasswordUpdate(self, CThostFtdcUserPasswordUpdateField *pUserPasswordUpdate,
                                                  CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                  cbool bIsLast) except -1:
    self.OnRspUserPasswordUpdate(
        None if pUserPasswordUpdate is NULL else ApiStructure.UserPasswordUpdateField.from_address(
            <size_t> pUserPasswordUpdate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspTradingAccountPasswordUpdate(self,
                                                            CThostFtdcTradingAccountPasswordUpdateField *pTradingAccountPasswordUpdate,
                                                            CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                            cbool bIsLast) except -1:
    self.OnRspTradingAccountPasswordUpdate(
        None if pTradingAccountPasswordUpdate is NULL else ApiStructure.TradingAccountPasswordUpdateField.from_address(
            <size_t> pTradingAccountPasswordUpdate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspOrderInsert(self, CThostFtdcInputOrderField *pInputOrder,
                                           CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                           cbool bIsLast) except -1:
    self.OnRspOrderInsert(
        None if pInputOrder is NULL else ApiStructure.InputOrderField.from_address(<size_t> pInputOrder),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspParkedOrderInsert(self, CThostFtdcParkedOrderField *pParkedOrder,
                                                 CThostFtdcRspInfoField *pRspInfo,
                                                 int nRequestID, cbool bIsLast) except -1:
    self.OnRspParkedOrderInsert(
        None if pParkedOrder is NULL else ApiStructure.ParkedOrderField.from_address(<size_t> pParkedOrder),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspParkedOrderAction(self, CThostFtdcParkedOrderActionField *pParkedOrderAction,
                                                 CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                 cbool bIsLast) except -1:
    self.OnRspParkedOrderAction(
        None if pParkedOrderAction is NULL else ApiStructure.ParkedOrderActionField.from_address(
            <size_t> pParkedOrderAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspOrderAction(self, CThostFtdcInputOrderActionField *pInputOrderAction,
                                           CThostFtdcRspInfoField *pRspInfo,
                                           int nRequestID, cbool bIsLast) except -1:
    self.OnRspOrderAction(None if pInputOrderAction is NULL else ApiStructure.InputOrderActionField.from_address(
        <size_t> pInputOrderAction),
                          None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(
                              <size_t> pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQueryMaxOrderVolume(self, CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume,
                                                   CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                   cbool bIsLast) except -1:
    self.OnRspQueryMaxOrderVolume(
        None if pQueryMaxOrderVolume is NULL else ApiStructure.QueryMaxOrderVolumeField.from_address(
            <size_t> pQueryMaxOrderVolume),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspSettlementInfoConfirm(self, CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm,
                                                     CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                     cbool bIsLast) except -1:
    self.OnRspSettlementInfoConfirm(
        None if pSettlementInfoConfirm is NULL else ApiStructure.SettlementInfoConfirmField.from_address(
            <size_t> pSettlementInfoConfirm),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspRemoveParkedOrder(self, CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder,
                                                 CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                 cbool bIsLast) except -1:
    self.OnRspRemoveParkedOrder(
        None if pRemoveParkedOrder is NULL else ApiStructure.RemoveParkedOrderField.from_address(
            <size_t> pRemoveParkedOrder),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspRemoveParkedOrderAction(self,
                                                       CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction,
                                                       CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                       cbool bIsLast) except -1:
    self.OnRspRemoveParkedOrderAction(
        None if pRemoveParkedOrderAction is NULL else ApiStructure.RemoveParkedOrderAction(
            <size_t> pRemoveParkedOrderAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspExecOrderInsert(self, CThostFtdcInputExecOrderField *pInputExecOrder,
                                               CThostFtdcRspInfoField *pRspInfo,
                                               int nRequestID, cbool bIsLast) except -1:
    self.OnRspExecOrderInsert(
        None if pInputExecOrder is NULL else ApiStructure.InputExecOrderField.from_address(<size_t> pInputExecOrder),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspExecOrderAction(self, CThostFtdcInputExecOrderActionField *pInputExecOrderAction,
                                               CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                               cbool bIsLast) except -1:
    self.OnRspExecOrderAction(
        None if pInputExecOrderAction is NULL else ApiStructure.InputExecOrderActionField.from_address(
            <size_t> pInputExecOrderAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspForQuoteInsert(self, CThostFtdcInputForQuoteField *pInputForQuote,
                                              CThostFtdcRspInfoField *pRspInfo,
                                              int nRequestID, cbool bIsLast) except -1:
    self.OnRspForQuoteInsert(
        None if pInputForQuote is NULL else ApiStructure.InputForQuoteField.from_address(<size_t> pInputForQuote),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQuoteInsert(self, CThostFtdcInputQuoteField *pInputQuote,
                                           CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                           cbool bIsLast) except -1:
    self.OnRspQuoteInsert(
        None if pInputQuote is NULL else ApiStructure.InputQuoteField.from_address(<size_t> pInputQuote),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQuoteAction(self, CThostFtdcInputQuoteActionField *pInputQuoteAction,
                                           CThostFtdcRspInfoField *pRspInfo,
                                           int nRequestID, cbool bIsLast) except -1:
    self.OnRspQuoteAction(None if pInputQuoteAction is NULL else ApiStructure.InputQuoteActionField.from_address(
        <size_t> pInputQuoteAction),
                          None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(
                              <size_t> pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspCombActionInsert(self, CThostFtdcInputCombActionField *pInputCombAction,
                                                CThostFtdcRspInfoField *pRspInfo,
                                                int nRequestID, cbool bIsLast) except -1:
    self.OnRspCombActionInsert(
        None if pInputCombAction is NULL else ApiStructure.InputCombActionField.from_address(<size_t> pInputCombAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryOrder(self, CThostFtdcOrderField *pOrder, CThostFtdcRspInfoField *pRspInfo,
                                        int nRequestID,
                                        cbool bIsLast) except -1:
    self.OnRspQryOrder(None if pOrder is NULL else ApiStructure.OrderField.from_address(<size_t> pOrder),
                       None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(
                           <size_t> pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryTrade(self, CThostFtdcTradeField *pTrade, CThostFtdcRspInfoField *pRspInfo,
                                        int nRequestID,
                                        cbool bIsLast) except -1:
    self.OnRspQryTrade(None if pTrade is NULL else ApiStructure.TradeField.from_address(<size_t> pTrade),
                       None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(
                           <size_t> pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInvestorPosition(self, CThostFtdcInvestorPositionField *pInvestorPosition,
                                                   CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                   cbool bIsLast) except -1:
    self.OnRspQryInvestorPosition(
        None if pInvestorPosition is NULL else ApiStructure.InvestorPositionField.from_address(
            <size_t> pInvestorPosition),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryTradingAccount(self, CThostFtdcTradingAccountField *pTradingAccount,
                                                 CThostFtdcRspInfoField *pRspInfo,
                                                 int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryTradingAccount(
        None if pTradingAccount is NULL else ApiStructure.TradingAccountField.from_address(<size_t> pTradingAccount),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInvestor(self, CThostFtdcInvestorField *pInvestor, CThostFtdcRspInfoField *pRspInfo,
                                           int nRequestID,
                                           cbool bIsLast) except -1:
    self.OnRspQryInvestor(None if pInvestor is NULL else ApiStructure.InvestorField.from_address(<size_t> pInvestor),
                          None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(
                              <size_t> pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryTradingCode(self, CThostFtdcTradingCodeField *pTradingCode,
                                              CThostFtdcRspInfoField *pRspInfo,
                                              int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryTradingCode(
        None if pTradingCode is NULL else ApiStructure.TradingCodeField.from_address(<size_t> pTradingCode),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInstrumentMarginRate(self, CThostFtdcInstrumentMarginRateField *pInstrumentMarginRate,
                                                       CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                       cbool bIsLast) except -1:
    self.OnRspQryInstrumentMarginRate(
        None if pInstrumentMarginRate is NULL else ApiStructure.InstrumentMarginRateField.from_address(
            <size_t> pInstrumentMarginRate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInstrumentCommissionRate(self,
                                                           CThostFtdcInstrumentCommissionRateField *pInstrumentCommissionRate,
                                                           CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                           cbool bIsLast) except -1:
    self.OnRspQryInstrumentCommissionRate(
        None if pInstrumentCommissionRate is NULL else ApiStructure.InstrumentCommissionRateField.from_address(
            <size_t> pInstrumentCommissionRate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryExchange(self, CThostFtdcExchangeField *pExchange, CThostFtdcRspInfoField *pRspInfo,
                                           int nRequestID,
                                           cbool bIsLast) except -1:
    self.OnRspQryExchange(None if pExchange is NULL else ApiStructure.ExchangeField.from_address(<size_t> pExchange),
                          None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(
                              <size_t> pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryProduct(self, CThostFtdcProductField *pProduct, CThostFtdcRspInfoField *pRspInfo,
                                          int nRequestID,
                                          cbool bIsLast) except -1:
    self.OnRspQryProduct(None if pProduct is NULL else ApiStructure.ProductField.from_address(<size_t> pProduct),
                         None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(
                             <size_t> pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInstrument(self, CThostFtdcInstrumentField *pInstrument,
                                             CThostFtdcRspInfoField *pRspInfo,
                                             int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryInstrument(
        None if pInstrument is NULL else ApiStructure.InstrumentField.from_address(<size_t> pInstrument),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryDepthMarketData(self, CThostFtdcDepthMarketDataField *pDepthMarketData,
                                                  CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                  cbool bIsLast) except -1:
    self.OnRspQryDepthMarketData(
        None if pDepthMarketData is NULL else ApiStructure.DepthMarketDataField.from_address(<size_t> pDepthMarketData),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQrySettlementInfo(self, CThostFtdcSettlementInfoField *pSettlementInfo,
                                                 CThostFtdcRspInfoField *pRspInfo,
                                                 int nRequestID, cbool bIsLast) except -1:
    self.OnRspQrySettlementInfo(
        None if pSettlementInfo is NULL else ApiStructure.SettlementInfoField.from_address(<size_t> pSettlementInfo),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryTransferBank(self, CThostFtdcTransferBankField *pTransferBank,
                                               CThostFtdcRspInfoField *pRspInfo,
                                               int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryTransferBank(
        None if pTransferBank is NULL else ApiStructure.TransferBankField.from_address(<size_t> pTransferBank),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInvestorPositionDetail(self,
                                                         CThostFtdcInvestorPositionDetailField *pInvestorPositionDetail,
                                                         CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                         cbool bIsLast) except -1:
    self.OnRspQryInvestorPositionDetail(
        None if pInvestorPositionDetail is NULL else ApiStructure.InvestorPositionDetailField.from_address(
            <size_t> pInvestorPositionDetail),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryNotice(self, CThostFtdcNoticeField *pNotice, CThostFtdcRspInfoField *pRspInfo,
                                         int nRequestID,
                                         cbool bIsLast) except -1:
    self.OnRspQryNotice(None if pNotice is NULL else ApiStructure.NoticeField.from_address(<size_t> pNotice),
                        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(
                            <size_t> pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQrySettlementInfoConfirm(self,
                                                        CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm,
                                                        CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                        cbool bIsLast) except -1:
    self.OnRspQrySettlementInfoConfirm(
        None if pSettlementInfoConfirm is NULL else ApiStructure.SettlementInfoConfirmField.from_address(
            <size_t> pSettlementInfoConfirm),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInvestorPositionCombineDetail(self,
                                                                CThostFtdcInvestorPositionCombineDetailField *pInvestorPositionCombineDetail,
                                                                CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                                cbool bIsLast) except -1:
    self.OnRspQryInvestorPositionCombineDetail(
        None if pInvestorPositionCombineDetail is NULL else ApiStructure.InvestorPositionCombineDetailField.from_address(
            <size_t> pInvestorPositionCombineDetail),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryCFMMCTradingAccountKey(self,
                                                         CThostFtdcCFMMCTradingAccountKeyField *pCFMMCTradingAccountKey,
                                                         CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                         cbool bIsLast) except -1:
    self.OnRspQryCFMMCTradingAccountKey(
        None if pCFMMCTradingAccountKey is NULL else ApiStructure.CFMMCTradingAccountKeyField.from_address(
            <size_t> pCFMMCTradingAccountKey),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryEWarrantOffset(self, CThostFtdcEWarrantOffsetField *pEWarrantOffset,
                                                 CThostFtdcRspInfoField *pRspInfo,
                                                 int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryEWarrantOffset(
        None if pEWarrantOffset is NULL else ApiStructure.EWarrantOffsetField.from_address(<size_t> pEWarrantOffset),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryInvestorProductGroupMargin(self,
                                                             CThostFtdcInvestorProductGroupMarginField *pInvestorProductGroupMargin,
                                                             CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                             cbool bIsLast) except -1:
    self.OnRspQryInvestorProductGroupMargin(
        None if pInvestorProductGroupMargin is NULL else ApiStructure.InvestorProductGroupMarginField.from_address(
            <size_t> pInvestorProductGroupMargin),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryExchangeMarginRate(self, CThostFtdcExchangeMarginRateField *pExchangeMarginRate,
                                                     CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                     cbool bIsLast) except -1:
    self.OnRspQryExchangeMarginRate(
        None if pExchangeMarginRate is NULL else ApiStructure.ExchangeMarginRateField.from_address(
            <size_t> pExchangeMarginRate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryExchangeMarginRateAdjust(self,
                                                           CThostFtdcExchangeMarginRateAdjustField *pExchangeMarginRateAdjust,
                                                           CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                           cbool bIsLast) except -1:
    self.OnRspQryExchangeMarginRateAdjust(
        None if pExchangeMarginRateAdjust is NULL else ApiStructure.ExchangeMarginRateAdjustField.from_address(
            <size_t> pExchangeMarginRateAdjust),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryExchangeRate(self, CThostFtdcExchangeRateField *pExchangeRate,
                                               CThostFtdcRspInfoField *pRspInfo,
                                               int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryExchangeRate(
        None if pExchangeRate is NULL else ApiStructure.ExchangeRateField.from_address(<size_t> pExchangeRate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQrySecAgentACIDMap(self, CThostFtdcSecAgentACIDMapField *pSecAgentACIDMap,
                                                  CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                  cbool bIsLast) except -1:
    self.OnRspQrySecAgentACIDMap(
        None if pSecAgentACIDMap is NULL else ApiStructure.SecAgentACIDMapField.from_address(<size_t> pSecAgentACIDMap),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryProductExchRate(self, CThostFtdcProductExchRateField *pProductExchRate,
                                                  CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                  cbool bIsLast) except -1:
    self.OnRspQryProductExchRate(
        None if pProductExchRate is NULL else ApiStructure.ProductExchRateField.from_address(<size_t> pProductExchRate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryOptionInstrTradeCost(self, CThostFtdcOptionInstrTradeCostField *pOptionInstrTradeCost,
                                                       CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                       cbool bIsLast) except -1:
    self.OnRspQryOptionInstrTradeCost(
        None if pOptionInstrTradeCost is NULL else ApiStructure.OptionInstrTradeCostField.from_address(
            <size_t> pOptionInstrTradeCost),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryOptionInstrCommRate(self, CThostFtdcOptionInstrCommRateField *pOptionInstrCommRate,
                                                      CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                      cbool bIsLast) except -1:
    self.OnRspQryOptionInstrCommRate(
        None if pOptionInstrCommRate is NULL else ApiStructure.OptionInstrCommRateField.from_address(
            <size_t> pOptionInstrCommRate),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryExecOrder(self, CThostFtdcExecOrderField *pExecOrder,
                                            CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                            cbool bIsLast) except -1:
    self.OnRspQryExecOrder(
        None if pExecOrder is NULL else ApiStructure.ExecOrderField.from_address(<size_t> pExecOrder),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryForQuote(self, CThostFtdcForQuoteField *pForQuote, CThostFtdcRspInfoField *pRspInfo,
                                           int nRequestID,
                                           cbool bIsLast) except -1:
    self.OnRspQryForQuote(None if pForQuote is NULL else ApiStructure.ForQuoteField.from_address(<size_t> pForQuote),
                          None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(
                              <size_t> pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryQuote(self, CThostFtdcQuoteField *pQuote, CThostFtdcRspInfoField *pRspInfo,
                                        int nRequestID,
                                        cbool bIsLast) except -1:
    self.OnRspQryQuote(None if pQuote is NULL else ApiStructure.QuoteField.from_address(<size_t> pQuote),
                       None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(
                           <size_t> pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryCombInstrumentGuard(self, CThostFtdcCombInstrumentGuardField *pCombInstrumentGuard,
                                                      CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                      cbool bIsLast) except -1:
    self.OnRspQryCombInstrumentGuard(
        None if pCombInstrumentGuard is NULL else ApiStructure.CombInstrumentGuardField.from_address(
            <size_t> pCombInstrumentGuard),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryCombAction(self, CThostFtdcCombActionField *pCombAction,
                                             CThostFtdcRspInfoField *pRspInfo,
                                             int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryCombAction(
        None if pCombAction is NULL else ApiStructure.CombActionField.from_address(<size_t> pCombAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryTransferSerial(self, CThostFtdcTransferSerialField *pTransferSerial,
                                                 CThostFtdcRspInfoField *pRspInfo,
                                                 int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryTransferSerial(
        None if pTransferSerial is NULL else ApiStructure.TransferSerialField.from_address(<size_t> pTransferSerial),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryAccountregister(self, CThostFtdcAccountregisterField *pAccountregister,
                                                  CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                  cbool bIsLast) except -1:
    self.OnRspQryAccountregister(
        None if pAccountregister is NULL else ApiStructure.AccountregisterField.from_address(<size_t> pAccountregister),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspError(self, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    self.OnRspError(
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRtnOrder(self, CThostFtdcOrderField *pOrder) except -1:
    self.OnRtnOrder(None if pOrder is NULL else ApiStructure.OrderField.from_address(<size_t> pOrder))
    return 0

cdef extern int TraderSpi_OnRtnTrade(self, CThostFtdcTradeField *pTrade) except -1:
    self.OnRtnTrade(None if pTrade is NULL else ApiStructure.TradeField.from_address(<size_t> pTrade))
    return 0

cdef extern int TraderSpi_OnErrRtnOrderInsert(self, CThostFtdcInputOrderField *pInputOrder,
                                              CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnOrderInsert(
        None if pInputOrder is NULL else ApiStructure.InputOrderField.from_address(<size_t> pInputOrder),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo))
    return 0

cdef extern int TraderSpi_OnErrRtnOrderAction(self, CThostFtdcOrderActionField *pOrderAction,
                                              CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnOrderAction(
        None if pOrderAction is NULL else ApiStructure.OrderActionField.from_address(<size_t> pOrderAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo))
    return 0

cdef extern int TraderSpi_OnRtnInstrumentStatus(self, CThostFtdcInstrumentStatusField *pInstrumentStatus) except -1:
    self.OnRtnInstrumentStatus(
        None if pInstrumentStatus is NULL else ApiStructure.InstrumentStatusField.from_address(
            <size_t> pInstrumentStatus))
    return 0

cdef extern int TraderSpi_OnRtnTradingNotice(self, CThostFtdcTradingNoticeInfoField *pTradingNoticeInfo) except -1:
    self.OnRtnTradingNotice(
        None if pTradingNoticeInfo is NULL else ApiStructure.TradingNoticeInfoField.from_address(
            <size_t> pTradingNoticeInfo))
    return 0

cdef extern int TraderSpi_OnRtnErrorConditionalOrder(self,
                                                     CThostFtdcErrorConditionalOrderField *pErrorConditionalOrder) except -1:
    self.OnRtnErrorConditionalOrder(
        None if pErrorConditionalOrder is NULL else ApiStructure.ErrorConditionalOrderField.from_address(
            <size_t> pErrorConditionalOrder))
    return 0

cdef extern int TraderSpi_OnRtnExecOrder(self, CThostFtdcExecOrderField *pExecOrder) except -1:
    self.OnRtnExecOrder(None if pExecOrder is NULL else ApiStructure.ExecOrderField.from_address(<size_t> pExecOrder))
    return 0

cdef extern int TraderSpi_OnErrRtnExecOrderInsert(self, CThostFtdcInputExecOrderField *pInputExecOrder,
                                                  CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnExecOrderInsert(
        None if pInputExecOrder is NULL else ApiStructure.InputExecOrderField.from_address(<size_t> pInputExecOrder),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo))
    return 0

cdef extern int TraderSpi_OnErrRtnExecOrderAction(self, CThostFtdcExecOrderActionField *pExecOrderAction,
                                                  CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnExecOrderAction(
        None if pExecOrderAction is NULL else ApiStructure.ExecOrderActionField.from_address(<size_t> pExecOrderAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo))
    return 0

cdef extern int TraderSpi_OnErrRtnForQuoteInsert(self, CThostFtdcInputForQuoteField *pInputForQuote,
                                                 CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnForQuoteInsert(
        None if pInputForQuote is NULL else ApiStructure.InputForQuoteField.from_address(<size_t> pInputForQuote),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo))
    return 0

cdef extern int TraderSpi_OnRtnQuote(self, CThostFtdcQuoteField *pQuote) except -1:
    self.OnRtnQuote(None if pQuote is NULL else ApiStructure.QuoteField.from_address(<size_t> pQuote))
    return 0

cdef extern int TraderSpi_OnErrRtnQuoteInsert(self, CThostFtdcInputQuoteField *pInputQuote,
                                              CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnQuoteInsert(
        None if pInputQuote is NULL else ApiStructure.InputQuoteField.from_address(<size_t> pInputQuote),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo))
    return 0

cdef extern int TraderSpi_OnErrRtnQuoteAction(self, CThostFtdcQuoteActionField *pQuoteAction,
                                              CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnQuoteAction(
        None if pQuoteAction is NULL else ApiStructure.QuoteActionField.from_address(<size_t> pQuoteAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo))
    return 0

cdef extern int TraderSpi_OnRtnForQuoteRsp(self, CThostFtdcForQuoteRspField *pForQuoteRsp) except -1:
    self.OnRtnForQuoteRsp(
        None if pForQuoteRsp is NULL else ApiStructure.ForQuoteRspField.from_address(<size_t> pForQuoteRsp))
    return 0

cdef extern int TraderSpi_OnRtnCFMMCTradingAccountToken(self,
                                                        CThostFtdcCFMMCTradingAccountTokenField *pCFMMCTradingAccountToken) except -1:
    self.OnRtnCFMMCTradingAccountToken(
        None if pCFMMCTradingAccountToken is NULL else ApiStructure.CFMMCTradingAccountTokenField.from_address(
            <size_t> pCFMMCTradingAccountToken))
    return 0

cdef extern int TraderSpi_OnRtnCombAction(self, CThostFtdcCombActionField *pCombAction) except -1:
    self.OnRtnCombAction(
        None if pCombAction is NULL else ApiStructure.CombActionField.from_address(<size_t> pCombAction))
    return 0

cdef extern int TraderSpi_OnErrRtnCombActionInsert(self, CThostFtdcInputCombActionField *pInputCombAction,
                                                   CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnCombActionInsert(
        None if pInputCombAction is NULL else ApiStructure.InputCombActionField.from_address(<size_t> pInputCombAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo))
    return 0

cdef extern int TraderSpi_OnRspQryContractBank(self, CThostFtdcContractBankField *pContractBank,
                                               CThostFtdcRspInfoField *pRspInfo,
                                               int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryContractBank(
        None if pContractBank is NULL else ApiStructure.ContractBankField.from_address(<size_t> pContractBank),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryParkedOrder(self, CThostFtdcParkedOrderField *pParkedOrder,
                                              CThostFtdcRspInfoField *pRspInfo,
                                              int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryParkedOrder(
        None if pParkedOrder is NULL else ApiStructure.ParkedOrderField.from_address(<size_t> pParkedOrder),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryParkedOrderAction(self, CThostFtdcParkedOrderActionField *pParkedOrderAction,
                                                    CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                    cbool bIsLast) except -1:
    self.OnRspQryParkedOrderAction(
        None if pParkedOrderAction is NULL else ApiStructure.ParkedOrderActionField.from_address(
            <size_t> pParkedOrderAction),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryTradingNotice(self, CThostFtdcTradingNoticeField *pTradingNotice,
                                                CThostFtdcRspInfoField *pRspInfo,
                                                int nRequestID, cbool bIsLast) except -1:
    self.OnRspQryTradingNotice(
        None if pTradingNotice is NULL else ApiStructure.TradingNoticeField.from_address(<size_t> pTradingNotice),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryBrokerTradingParams(self, CThostFtdcBrokerTradingParamsField *pBrokerTradingParams,
                                                      CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                      cbool bIsLast) except -1:
    self.OnRspQryBrokerTradingParams(
        None if pBrokerTradingParams is NULL else ApiStructure.BrokerTradingParamsField.from_address(
            <size_t> pBrokerTradingParams),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQryBrokerTradingAlgos(self, CThostFtdcBrokerTradingAlgosField *pBrokerTradingAlgos,
                                                     CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                     cbool bIsLast) except -1:
    self.OnRspQryBrokerTradingAlgos(
        None if pBrokerTradingAlgos is NULL else ApiStructure.BrokerTradingAlgosField.from_address(
            <size_t> pBrokerTradingAlgos),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQueryCFMMCTradingAccountToken(self,
                                                             CThostFtdcQueryCFMMCTradingAccountTokenField *pQueryCFMMCTradingAccountToken,
                                                             CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                             cbool bIsLast) except -1:
    self.OnRspQueryCFMMCTradingAccountToken(
        None if pQueryCFMMCTradingAccountToken is NULL else ApiStructure.QueryCFMMCTradingAccountTokenField.from_address(
            <size_t> pQueryCFMMCTradingAccountToken),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRtnFromBankToFutureByBank(self, CThostFtdcRspTransferField *pRspTransfer) except -1:
    self.OnRtnFromBankToFutureByBank(
        None if pRspTransfer is NULL else ApiStructure.RspTransferField.from_address(<size_t> pRspTransfer))
    return 0

cdef extern int TraderSpi_OnRtnFromFutureToBankByBank(self, CThostFtdcRspTransferField *pRspTransfer) except -1:
    self.OnRtnFromFutureToBankByBank(
        None if pRspTransfer is NULL else ApiStructure.RspTransferField.from_address(<size_t> pRspTransfer))
    return 0

cdef extern int TraderSpi_OnRtnRepealFromBankToFutureByBank(self, CThostFtdcRspRepealField *pRspRepeal) except -1:
    self.OnRtnRepealFromBankToFutureByBank(
        None if pRspRepeal is NULL else ApiStructure.RspRepealField.from_address(<size_t> pRspRepeal))
    return 0

cdef extern int TraderSpi_OnRtnRepealFromFutureToBankByBank(self, CThostFtdcRspRepealField *pRspRepeal) except -1:
    self.OnRtnRepealFromFutureToBankByBank(
        None if pRspRepeal is NULL else ApiStructure.RspRepealField.from_address(<size_t> pRspRepeal))
    return 0

cdef extern int TraderSpi_OnRtnFromBankToFutureByFuture(self, CThostFtdcRspTransferField *pRspTransfer) except -1:
    self.OnRtnFromBankToFutureByFuture(
        None if pRspTransfer is NULL else ApiStructure.RspTransferField.from_address(<size_t> pRspTransfer))
    return 0

cdef extern int TraderSpi_OnRtnFromFutureToBankByFuture(self, CThostFtdcRspTransferField *pRspTransfer) except -1:
    self.OnRtnFromFutureToBankByFuture(
        None if pRspTransfer is NULL else ApiStructure.RspTransferField.from_address(<size_t> pRspTransfer))
    return 0

cdef extern int TraderSpi_OnRtnRepealFromBankToFutureByFutureManual(self,
                                                                    CThostFtdcRspRepealField *pRspRepeal) except -1:
    self.OnRtnRepealFromBankToFutureByFutureManual(
        None if pRspRepeal is NULL else ApiStructure.RspRepealField.from_address(<size_t> pRspRepeal))
    return 0

cdef extern int TraderSpi_OnRtnRepealFromFutureToBankByFutureManual(self,
                                                                    CThostFtdcRspRepealField *pRspRepeal) except -1:
    self.OnRtnRepealFromFutureToBankByFutureManual(
        None if pRspRepeal is NULL else ApiStructure.RspRepealField.from_address(<size_t> pRspRepeal))
    return 0

cdef extern int TraderSpi_OnRtnQueryBankBalanceByFuture(self,
                                                        CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount) except -1:
    self.OnRtnQueryBankBalanceByFuture(
        None if pNotifyQueryAccount is NULL else ApiStructure.NotifyQueryAccountField.from_address(
            <size_t> pNotifyQueryAccount))
    return 0

cdef extern int TraderSpi_OnErrRtnBankToFutureByFuture(self, CThostFtdcReqTransferField *pReqTransfer,
                                                       CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnBankToFutureByFuture(
        None if pReqTransfer is NULL else ApiStructure.ReqTransferField.from_address(<size_t> pReqTransfer),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo))
    return 0

cdef extern int TraderSpi_OnErrRtnFutureToBankByFuture(self, CThostFtdcReqTransferField *pReqTransfer,
                                                       CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnFutureToBankByFuture(
        None if pReqTransfer is NULL else ApiStructure.ReqTransferField.from_address(<size_t> pReqTransfer),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo))
    return 0

cdef extern int TraderSpi_OnErrRtnRepealBankToFutureByFutureManual(self, CThostFtdcReqRepealField *pReqRepeal,
                                                                   CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnRepealBankToFutureByFutureManual(
        None if pReqRepeal is NULL else ApiStructure.ReqRepealField.from_address(<size_t> pReqRepeal),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo))
    return 0

cdef extern int TraderSpi_OnErrRtnRepealFutureToBankByFutureManual(self, CThostFtdcReqRepealField *pReqRepeal,
                                                                   CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnRepealFutureToBankByFutureManual(
        None if pReqRepeal is NULL else ApiStructure.ReqRepealField.from_address(<size_t> pReqRepeal),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo))
    return 0

cdef extern int TraderSpi_OnErrRtnQueryBankBalanceByFuture(self, CThostFtdcReqQueryAccountField *pReqQueryAccount,
                                                           CThostFtdcRspInfoField *pRspInfo) except -1:
    self.OnErrRtnQueryBankBalanceByFuture(
        None if pReqQueryAccount is NULL else ApiStructure.ReqQueryAccountField.from_address(<size_t> pReqQueryAccount),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo))
    return 0

cdef extern int TraderSpi_OnRtnRepealFromBankToFutureByFuture(self, CThostFtdcRspRepealField *pRspRepeal) except -1:
    self.OnRtnRepealFromBankToFutureByFuture(
        None if pRspRepeal is NULL else ApiStructure.RspRepealField.from_address(<size_t> pRspRepeal))
    return 0

cdef extern int TraderSpi_OnRtnRepealFromFutureToBankByFuture(self, CThostFtdcRspRepealField *pRspRepeal) except -1:
    self.OnRtnRepealFromFutureToBankByFuture(
        None if pRspRepeal is NULL else ApiStructure.RspRepealField.from_address(<size_t> pRspRepeal))
    return 0

cdef extern int TraderSpi_OnRspFromBankToFutureByFuture(self, CThostFtdcReqTransferField *pReqTransfer,
                                                        CThostFtdcRspInfoField *pRspInfo,
                                                        int nRequestID, cbool bIsLast) except -1:
    self.OnRspFromBankToFutureByFuture(
        None if pReqTransfer is NULL else ApiStructure.ReqTransferField.from_address(<size_t> pReqTransfer),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast)
    return 0

cdef extern int TraderSpi_OnRspFromFutureToBankByFuture(self, CThostFtdcReqTransferField *pReqTransfer,
                                                        CThostFtdcRspInfoField *pRspInfo,
                                                        int nRequestID, cbool bIsLast) except -1:
    self.OnRspFromFutureToBankByFuture(
        None if pReqTransfer is NULL else ApiStructure.ReqTransferField.from_address(<size_t> pReqTransfer),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_address(<size_t> pRspInfo),
        nRequestID,
        bIsLast)
    return 0

cdef extern int TraderSpi_OnRspQueryBankAccountMoneyByFuture(self, CThostFtdcReqQueryAccountField *pReqQueryAccount,
                                                             CThostFtdcRspInfoField *pRspInfo, int nRequestID,
                                                             cbool bIsLast) except -1:
    self.OnRspQueryBankAccountMoneyByFuture(
        None if pReqQueryAccount is NULL else ApiStructure.ReqQueryAccountField.from_address(<size_t> pReqQueryAccount),
        None if pRspInfo is NULL else ApiStructure.RspInfoField.from_addressField.from_addressField.from_address(
            <size_t> pRspInfo), nRequestID, bIsLast)
    return 0

cdef extern int TraderSpi_OnRtnOpenAccountByBank(self, CThostFtdcOpenAccountField *pOpenAccount) except -1:
    self.OnRtnOpenAccountByBank(
        None if pOpenAccount is NULL else ApiStructure.OpenAccountField.from_addressField.from_address(
            <size_t> pOpenAccount))
    return 0

cdef extern int TraderSpi_OnRtnCancelAccountByBank(self, CThostFtdcCancelAccountField *pCancelAccount) except -1:
    self.OnRtnCancelAccountByBank(
        None if pCancelAccount is NULL else ApiStructure.CancelAccountField.from_addressField.from_address(
            <size_t> pCancelAccount))
    return 0

cdef extern int TraderSpi_OnRtnChangeAccountByBank(self, CThostFtdcChangeAccountField *pChangeAccount) except -1:
    self.OnRtnChangeAccountByBank(
        None if pChangeAccount is NULL else ApiStructure.ChangeAccountField.from_address(<size_t> pChangeAccount))
    return 0
