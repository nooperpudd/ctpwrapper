# encoding:utf-8
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
import time
from typing import Optional

from ctpwrapper.ApiStructure import (
    FensUserInfoField, UserSystemInfoField,
    ReqAuthenticateField, ReqGenUserCaptchaField,
    ReqGenUserTextField, ReqQueryAccountField,
    ReqTransferField, QueryCFMMCTradingAccountTokenField,
    QryBrokerTradingAlgosField, QryBrokerTradingParamsField,
    QryTradingNoticeField, UserLogoutField,
    QryParkedOrderActionField, QryParkedOrderField,
    QryContractBankField, QryAccountregisterField,
    QryTransferSerialField, QryCombActionField,
    QryCombInstrumentGuardField, QryInvestUnitField,
    QryOptionSelfCloseField, QryQuoteField,
    QryForQuoteField, QryExecOrderField,
    QryOptionInstrCommRateField, QryOptionInstrTradeCostField,
    QrySecAgentTradeInfoField, QrySecAgentCheckModeField,
    QryInstrumentOrderCommRateField, QryMMOptionInstrCommRateField,
    QryMMInstrumentCommissionRateField, QryProductGroupField,
    QryProductExchRateField, QrySecAgentACIDMapField,
    QryExchangeMarginRateAdjustField, ReqUserLoginField,
    InputOrderField, ParkedOrderField,
    ParkedOrderActionField, InputOrderActionField,
    QryMaxOrderVolumeField, SettlementInfoConfirmField,
    RemoveParkedOrderField, RemoveParkedOrderActionField,
    InputExecOrderField, InputExecOrderActionField,
    InputForQuoteField, InputQuoteField,
    InputQuoteActionField, InputBatchOrderActionField,
    InputOptionSelfCloseField, InputOptionSelfCloseActionField,
    InputCombActionField, ReqUserLoginWithCaptchaField,
    ReqUserLoginWithTextField, ReqUserLoginWithOTPField,
    UserPasswordUpdateField, TradingAccountPasswordUpdateField,
    QryOrderField, QryTradeField,
    QryInvestorPositionField, QryTradingAccountField,
    QryInvestorField, QryTradingCodeField,
    QryInstrumentCommissionRateField,
    QryExchangeField, QryProductField,
    QryInstrumentField, QryDepthMarketDataField,
    QrySettlementInfoField, QryTransferBankField,
    QryInvestorPositionDetailField, QryNoticeField,
    QrySettlementInfoConfirmField, QryInvestorPositionCombineDetailField,
    QryCFMMCTradingAccountKeyField, QryEWarrantOffsetField,
    QryInvestorProductGroupMarginField, QryExchangeMarginRateField,
    QryExchangeRateField, QryInstrumentMarginRateField,
    QryClassifiedInstrumentField, QryCombPromotionParamField

)
from ctpwrapper.TraderApi import TraderApiWrapper


class TraderApiPy(TraderApiWrapper):

    def Create(self, pszFlowPath: Optional[str] = "") -> None:
        super(TraderApiPy, self).Create(pszFlowPath.encode())

    def Release(self) -> None:
        super(TraderApiPy, self).Release()

    def Init(self) -> None:
        super(TraderApiPy, self).Init()
        time.sleep(1)  # wait for c++ init

    def Join(self) -> int:
        return super(TraderApiPy, self).Join()

    def GetTradingDay(self) -> str:
        """
        获取当前交易日
        :retrun 获取到的交易日
        @remark 只有登录成功后,才能得到正确的交易日
        """
        day = super(TraderApiPy, self).GetTradingDay()
        return day.decode()

    def RegisterFront(self, pszFrontAddress: str) -> None:
        """
        注册前置机网络地址
        @param pszFrontAddress：前置机网络地址。
        @remark 网络地址的格式为：“protocol:
        ipaddress:port”，如：”tcp:
        127.0.0.1:17001”。
        @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
        """
        super(TraderApiPy, self).RegisterFront(pszFrontAddress.encode())

    def RegisterNameServer(self, pszNsAddress: str) -> None:
        """
        注册名字服务器网络地址
        :param pszNsAddress：名字服务器网络地址。
        @remark 网络地址的格式为：“protocol:
        ipaddress:port”，如：”tcp:
        127.0.0.1:12001”。
        @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”12001”代表服务器端口号。
        @remark RegisterNameServer优先于RegisterFront
        """
        super(TraderApiPy, self).RegisterNameServer(pszNsAddress.encode())

    def RegisterFensUserInfo(self, pFensUserInfo: "FensUserInfoField") -> None:
        """
        注册名字服务器用户信息
        :param pFensUserInfo：用户信息。
        """
        super(TraderApiPy, self).RegisterFensUserInfo(pFensUserInfo)

    def SubscribePrivateTopic(self, nResumeType: int) -> None:
        """
        订阅私有流。
        :param nResumeType: 私有流重传方式
                THOST_TERT_RESTART:0,从本交易日开始重传
                THOST_TERT_RESUME:1,从上次收到的续传
                THOST_TERT_QUICK:2,只传送登录后私有流的内容

        @remark 该方法要在Init方法前调用。若不调用则不会收到私有流的数据。
        """
        super(TraderApiPy, self).SubscribePrivateTopic(nResumeType)

    def RegisterUserSystemInfo(self, pUserSystemInfo: "UserSystemInfoField") -> None:
        """
        注册用户终端信息，用于中继服务器多连接模式
        需要在终端认证成功后，用户登录前调用该接口
        """
        super(TraderApiPy, self).RegisterUserSystemInfo(pUserSystemInfo)

    def SubmitUserSystemInfo(self, pUserSystemInfo: "UserSystemInfoField") -> None:
        """
        上报用户终端信息，用于中继服务器操作员登录模式
        操作员登录后，可以多次调用该接口上报客户信息
        """
        super(TraderApiPy, self).SubmitUserSystemInfo(pUserSystemInfo)

    def SubscribePublicTopic(self, nResumeType: int) -> None:
        """
        订阅公共流。
        :param nResumeType: 公共流重传方式
                THOST_TERT_RESTART:0,从本交易日开始重传
                THOST_TERT_RESUME:1,从上次收到的续传
                THOST_TERT_QUICK:2只传送登录后公共流的内容
        该方法要在Init方法前调用。若不调用则不会收到公共流的数据。
        """
        super(TraderApiPy, self).SubscribePublicTopic(nResumeType)

    def ReqAuthenticate(self, pReqAuthenticate: "ReqAuthenticateField", nRequestID: int) -> int:
        """
        客户端认证请求
        """
        return super(TraderApiPy, self).ReqAuthenticate(pReqAuthenticate, nRequestID)

    def ReqUserLogin(self, pReqUserLogin: "ReqUserLoginField", nRequestID: int) -> int:
        """
        用户登录请求
        """
        return super(TraderApiPy, self).ReqUserLogin(pReqUserLogin, nRequestID)

    def ReqUserAuthMethod(self, pReqUserAuthMethod: "ReqUserAuthMethod", nRequestID: int) -> int:
        """
        查询用户当前支持的认证模式
        """
        return super(TraderApiPy, self).ReqUserAuthMethod(pReqUserAuthMethod, nRequestID)

    def ReqGenUserCaptcha(self, pReqGenUserCaptcha: "ReqGenUserCaptchaField", nRequestID: int) -> int:
        """
        用户发出获取图形验证码请求
        """
        return super(TraderApiPy, self).ReqGenUserCaptcha(pReqGenUserCaptcha, nRequestID)

    def ReqGenUserText(self, pReqGenUserText: "ReqGenUserTextField", nRequestID: int) -> int:
        """
        用户发出获取短信验证码请求
        """
        return super(TraderApiPy, self).ReqGenUserText(pReqGenUserText, nRequestID)

    def ReqUserLoginWithCaptcha(self, pReqUserLoginWithCaptcha: "ReqUserLoginWithCaptchaField", nRequestID: int) -> int:
        """
        用户发出带有图片验证码的登陆请求
        """
        return super(TraderApiPy, self).ReqUserLoginWithCaptcha(pReqUserLoginWithCaptcha, nRequestID)

    def ReqUserLoginWithText(self, pReqUserLoginWithText: "ReqUserLoginWithTextField", nRequestID: int) -> int:
        """
        用户发出带有短信验证码的登陆请求
        """
        return super(TraderApiPy, self).ReqUserLoginWithText(pReqUserLoginWithText, nRequestID)

    def ReqUserLoginWithOTP(self, pReqUserLoginWithOTP: "ReqUserLoginWithOTPField", nRequestID: int) -> int:
        """
        用户发出带有动态口令的登陆请求
        """
        return super(TraderApiPy, self).ReqUserLoginWithOTP(pReqUserLoginWithOTP, nRequestID)

    def ReqUserLogout(self, pUserLogout: "UserLogoutField", nRequestID: int) -> int:
        """
        登出请求
        """
        return super(TraderApiPy, self).ReqUserLogout(pUserLogout, nRequestID)

    def ReqUserPasswordUpdate(self, pUserPasswordUpdate: "UserPasswordUpdateField", nRequestID: int) -> int:
        """
        用户口令更新请求
        """
        return super(TraderApiPy, self).ReqUserPasswordUpdate(pUserPasswordUpdate, nRequestID)

    def ReqTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate: "TradingAccountPasswordUpdateField", nRequestID: int) -> int:
        """
        资金账户口令更新请求
        """
        return super(TraderApiPy, self).ReqTradingAccountPasswordUpdate(pTradingAccountPasswordUpdate, nRequestID)

    def ReqOrderInsert(self, pInputOrder: "InputOrderField", nRequestID: int) -> int:
        """
        报单录入请求
        """
        return super(TraderApiPy, self).ReqOrderInsert(pInputOrder, nRequestID)

    def ReqParkedOrderInsert(self, pParkedOrder: "ParkedOrderField", nRequestID: int) -> int:
        """
        预埋单录入请求
        """
        return super(TraderApiPy, self).ReqParkedOrderInsert(pParkedOrder, nRequestID)

    def ReqParkedOrderAction(self, pParkedOrderAction: "ParkedOrderActionField", nRequestID: int) -> int:
        """
        预埋撤单录入请求
        """
        return super(TraderApiPy, self).ReqParkedOrderAction(pParkedOrderAction, nRequestID)

    def ReqOrderAction(self, pInputOrderAction: "InputOrderActionField", nRequestID: int) -> int:
        """
        报单操作请求
        """
        return super(TraderApiPy, self).ReqOrderAction(pInputOrderAction, nRequestID)

    def ReqQryMaxOrderVolume(self, pQryMaxOrderVolume: "QryMaxOrderVolumeField", nRequestID: int) -> int:
        """
        查询最大报单数量请求
        """
        return super(TraderApiPy, self).ReqQryMaxOrderVolume(pQryMaxOrderVolume, nRequestID)

    def ReqSettlementInfoConfirm(self, pSettlementInfoConfirm: "SettlementInfoConfirmField", nRequestID: int) -> int:
        """
        投资者结算结果确认
        """
        return super(TraderApiPy, self).ReqSettlementInfoConfirm(pSettlementInfoConfirm, nRequestID)

    def ReqRemoveParkedOrder(self, pRemoveParkedOrder: "RemoveParkedOrderField", nRequestID: int) -> int:
        """
        请求删除预埋单
        """
        return super(TraderApiPy, self).ReqRemoveParkedOrder(pRemoveParkedOrder, nRequestID)

    def ReqRemoveParkedOrderAction(self, pRemoveParkedOrderAction: "RemoveParkedOrderActionField", nRequestID: int) -> int:
        """
        请求删除预埋撤单
        """
        return super(TraderApiPy, self).ReqRemoveParkedOrderAction(pRemoveParkedOrderAction, nRequestID)

    def ReqExecOrderInsert(self, pInputExecOrder: "InputExecOrderField", nRequestID: int) -> int:
        """
        执行宣告录入请求
        """
        return super(TraderApiPy, self).ReqExecOrderInsert(pInputExecOrder, nRequestID)

    def ReqExecOrderAction(self, pInputExecOrderAction: "InputExecOrderActionField", nRequestID: int) -> int:
        """
        执行宣告操作请求
        """
        return super(TraderApiPy, self).ReqExecOrderAction(pInputExecOrderAction, nRequestID)

    def ReqForQuoteInsert(self, pInputForQuote: "InputForQuoteField", nRequestID: int) -> int:
        """
        询价录入请求
        """
        return super(TraderApiPy, self).ReqForQuoteInsert(pInputForQuote, nRequestID)

    def ReqQuoteInsert(self, pInputQuote: "InputQuoteField", nRequestID: int) -> int:
        """
        报价录入请求
        """
        return super(TraderApiPy, self).ReqQuoteInsert(pInputQuote, nRequestID)

    def ReqQuoteAction(self, pInputQuoteAction: "InputQuoteActionField", nRequestID: int) -> int:
        """
        报价操作请求
        """
        return super(TraderApiPy, self).ReqQuoteAction(pInputQuoteAction, nRequestID)

    def ReqBatchOrderAction(self, pInputBatchOrderAction: "InputBatchOrderActionField", nRequestID: int) -> int:
        """
        批量报单操作请求
        :param pInputBatchOrderAction:
        :param nRequestID:
        :return:
        """
        return super(TraderApiPy, self).ReqBatchOrderAction(pInputBatchOrderAction, nRequestID)

    def ReqOptionSelfCloseInsert(self, pInputOptionSelfClose: "InputOptionSelfCloseField", nRequestID: int) -> int:
        """
        期权自对冲录入请求
        """
        return super(TraderApiPy, self).ReqOptionSelfCloseInsert(pInputOptionSelfClose, nRequestID)

    def ReqOptionSelfCloseAction(self, pInputOptionSelfCloseAction: "InputOptionSelfCloseActionField", nRequestID: int) -> int:
        """
        期权自对冲操作请求
        """
        return super(TraderApiPy, self).ReqOptionSelfCloseAction(pInputOptionSelfCloseAction, nRequestID)

    def ReqCombActionInsert(self, pInputCombAction: "InputCombActionField", nRequestID: int) -> int:
        """
        申请组合录入请求
        """
        return super(TraderApiPy, self).ReqCombActionInsert(pInputCombAction, nRequestID)

    def ReqQryOrder(self, pQryOrder: "QryOrderField", nRequestID: int) -> int:
        """
        请求查询报单
        """
        return super(TraderApiPy, self).ReqQryOrder(pQryOrder, nRequestID)

    def ReqQryTrade(self, pQryTrade: "QryTradeField", nRequestID: int) -> int:
        """
        请求查询成交
        """
        return super(TraderApiPy, self).ReqQryTrade(pQryTrade, nRequestID)

    def ReqQryInvestorPosition(self, pQryInvestorPosition: "QryInvestorPositionField", nRequestID: int) -> int:
        """
        请求查询投资者持仓
        """
        return super(TraderApiPy, self).ReqQryInvestorPosition(pQryInvestorPosition, nRequestID)

    def ReqQryTradingAccount(self, pQryTradingAccount: "QryTradingAccountField", nRequestID: int) -> int:
        """
        请求查询资金账户
        """
        return super(TraderApiPy, self).ReqQryTradingAccount(pQryTradingAccount, nRequestID)

    def ReqQryInvestor(self, pQryInvestor: "QryInvestorField", nRequestID: int) -> int:
        """
        请求查询投资者
        """
        return super(TraderApiPy, self).ReqQryInvestor(pQryInvestor, nRequestID)

    def ReqQryTradingCode(self, pQryTradingCode: "QryTradingCodeField", nRequestID: int) -> int:
        """
        请求查询交易编码
        """
        return super(TraderApiPy, self).ReqQryTradingCode(pQryTradingCode, nRequestID)

    def ReqQryInstrumentMarginRate(self, pQryInstrumentMarginRate: "QryInstrumentMarginRateField", nRequestID: int) -> int:
        """
        请求查询合约保证金率
        """
        return super(TraderApiPy, self).ReqQryInstrumentMarginRate(pQryInstrumentMarginRate, nRequestID)

    def ReqQryInstrumentCommissionRate(self, pQryInstrumentCommissionRate: "QryInstrumentCommissionRateField", nRequestID: int) -> int:
        """
        请求查询合约手续费率
        """
        return super(TraderApiPy, self).ReqQryInstrumentCommissionRate(pQryInstrumentCommissionRate, nRequestID)

    def ReqQryExchange(self, pQryExchange: "QryExchangeField", nRequestID: int) -> int:
        """
        请求查询交易所
        """
        return super(TraderApiPy, self).ReqQryExchange(pQryExchange, nRequestID)

    def ReqQryProduct(self, pQryProduct: "QryProductField", nRequestID: int) -> int:
        """
        请求查询产品
        """
        return super(TraderApiPy, self).ReqQryProduct(pQryProduct, nRequestID)

    def ReqQryInstrument(self, pQryInstrument: "QryInstrumentField", nRequestID: int) -> int:
        """
        请求查询合约
        """
        return super(TraderApiPy, self).ReqQryInstrument(pQryInstrument, nRequestID)

    def ReqQryDepthMarketData(self, pQryDepthMarketData: "QryDepthMarketDataField", nRequestID: int) -> int:
        """
        请求查询行情
        """
        return super(TraderApiPy, self).ReqQryDepthMarketData(pQryDepthMarketData, nRequestID)

    def ReqQrySettlementInfo(self, pQrySettlementInfo: "QrySettlementInfoField", nRequestID: int) -> int:
        """
        请求查询投资者结算结果
        """
        return super(TraderApiPy, self).ReqQrySettlementInfo(pQrySettlementInfo, nRequestID)

    def ReqQryTransferBank(self, pQryTransferBank: "QryTransferBankField", nRequestID: int) -> int:
        """
        请求查询转帐银行
        """
        return super(TraderApiPy, self).ReqQryTransferBank(pQryTransferBank, nRequestID)

    def ReqQryInvestorPositionDetail(self, pQryInvestorPositionDetail: "QryInvestorPositionDetailField", nRequestID: int) -> int:
        """
        请求查询投资者持仓明细
        """
        return super(TraderApiPy, self).ReqQryInvestorPositionDetail(pQryInvestorPositionDetail, nRequestID)

    def ReqQryNotice(self, pQryNotice: "QryNoticeField", nRequestID: int) -> int:
        """
        请求查询客户通知
        """
        return super(TraderApiPy, self).ReqQryNotice(pQryNotice, nRequestID)

    def ReqQrySettlementInfoConfirm(self, pQrySettlementInfoConfirm: "QrySettlementInfoConfirmField", nRequestID: int) -> int:
        """
        请求查询结算信息确认
        """
        return super(TraderApiPy, self).ReqQrySettlementInfoConfirm(pQrySettlementInfoConfirm, nRequestID)

    def ReqQryInvestorPositionCombineDetail(self, pQryInvestorPositionCombineDetail: "QryInvestorPositionCombineDetailField", nRequestID: int) -> int:
        """
        请求查询投资者持仓明细"""
        return super(TraderApiPy, self).ReqQryInvestorPositionCombineDetail(pQryInvestorPositionCombineDetail,
                                                                            nRequestID)

    def ReqQryCFMMCTradingAccountKey(self, pQryCFMMCTradingAccountKey: "QryCFMMCTradingAccountKeyField", nRequestID: int) -> int:
        """
        请求查询保证金监管系统经纪公司资金账户密钥
        """
        return super(TraderApiPy, self).ReqQryCFMMCTradingAccountKey(pQryCFMMCTradingAccountKey, nRequestID)

    def ReqQryEWarrantOffset(self, pQryEWarrantOffset: "QryEWarrantOffsetField", nRequestID: int) -> int:
        """
        请求查询仓单折抵信息
        """
        return super(TraderApiPy, self).ReqQryEWarrantOffset(pQryEWarrantOffset, nRequestID)

    def ReqQryInvestorProductGroupMargin(self, pQryInvestorProductGroupMargin: "QryInvestorProductGroupMarginField", nRequestID: int) -> int:
        """
        请求查询投资者品种/跨品种保证金
        """
        return super(TraderApiPy, self).ReqQryInvestorProductGroupMargin(pQryInvestorProductGroupMargin, nRequestID)

    def ReqQryExchangeMarginRate(self, pQryExchangeMarginRate: "QryExchangeMarginRateField", nRequestID: int) -> int:
        """
        请求查询交易所保证金率
        """
        return super(TraderApiPy, self).ReqQryExchangeMarginRate(pQryExchangeMarginRate, nRequestID)

    def ReqQryExchangeMarginRateAdjust(self, pQryExchangeMarginRateAdjust: "QryExchangeMarginRateAdjustField", nRequestID: int) -> int:
        """
        请求查询交易所调整保证金率
        """
        return super(TraderApiPy, self).ReqQryExchangeMarginRateAdjust(pQryExchangeMarginRateAdjust, nRequestID)

    def ReqQryExchangeRate(self, pQryExchangeRate: "QryExchangeRateField", nRequestID: int) -> int:
        """
        请求查询汇率
        """
        return super(TraderApiPy, self).ReqQryExchangeRate(pQryExchangeRate, nRequestID)

    def ReqQrySecAgentACIDMap(self, pQrySecAgentACIDMap: "QrySecAgentACIDMapField", nRequestID: int) -> int:
        """
        请求查询二级代理操作员银期权限
        """
        return super(TraderApiPy, self).ReqQrySecAgentACIDMap(pQrySecAgentACIDMap, nRequestID)

    def ReqQryProductExchRate(self, pQryProductExchRate: "QryProductExchRateField", nRequestID: int) -> int:
        """
        请求查询产品报价汇率
        """
        return super(TraderApiPy, self).ReqQryProductExchRate(pQryProductExchRate, nRequestID)

    def ReqQryProductGroup(self, pQryProductGroup: "QryProductGroupField", nRequestID: int) -> int:
        """
        请求查询产品组
        """
        return super(TraderApiPy, self).ReqQryProductGroup(pQryProductGroup, nRequestID)

    def ReqQryMMInstrumentCommissionRate(self, pQryMMInstrumentCommissionRate: "QryMMInstrumentCommissionRateField", nRequestID: int) -> int:
        """
        请求查询做市商合约手续费率
        """
        return super(TraderApiPy, self).ReqQryMMInstrumentCommissionRate(pQryMMInstrumentCommissionRate, nRequestID)

    def ReqQryMMOptionInstrCommRate(self, pQryMMOptionInstrCommRate: "QryMMOptionInstrCommRateField", nRequestID: int) -> int:
        """
        请求查询做市商期权合约手续费
        """
        return super(TraderApiPy, self).ReqQryMMOptionInstrCommRate(pQryMMOptionInstrCommRate, nRequestID)

    def ReqQryInstrumentOrderCommRate(self, pQryInstrumentOrderCommRate: "QryInstrumentOrderCommRateField", nRequestID: int) -> int:
        """
        请求查询报单手续费
        """
        return super(TraderApiPy, self).ReqQryInstrumentOrderCommRate(pQryInstrumentOrderCommRate, nRequestID)

    def ReqQrySecAgentTradingAccount(self, pQryTradingAccount: "QryTradingAccountField", nRequestID: int) -> int:
        """
        请求查询资金账户
        """
        return super(TraderApiPy, self).ReqQrySecAgentTradingAccount(pQryTradingAccount, nRequestID)

    def ReqQrySecAgentCheckMode(self, pQrySecAgentCheckMode: "QrySecAgentCheckModeField", nRequestID: int) -> int:
        """
        请求查询二级代理商资金校验模式
        """
        return super(TraderApiPy, self).ReqQrySecAgentCheckMode(pQrySecAgentCheckMode, nRequestID)

    def ReqQryOptionInstrTradeCost(self, pQryOptionInstrTradeCost: "QryOptionInstrTradeCostField", nRequestID: int) -> int:
        """
        请求查询期权交易成本
        """
        return super(TraderApiPy, self).ReqQryOptionInstrTradeCost(pQryOptionInstrTradeCost, nRequestID)

    def ReqQryOptionInstrCommRate(self, pQryOptionInstrCommRate: "QryOptionInstrCommRateField", nRequestID: int) -> int:
        """
        请求查询期权合约手续费
        """
        return super(TraderApiPy, self).ReqQryOptionInstrCommRate(pQryOptionInstrCommRate, nRequestID)

    def ReqQryExecOrder(self, pQryExecOrder: "QryExecOrderField", nRequestID: int) -> int:
        """
        请求查询执行宣告
        """
        return super(TraderApiPy, self).ReqQryExecOrder(pQryExecOrder, nRequestID)

    def ReqQryForQuote(self, pQryForQuote: "QryForQuoteField", nRequestID: int) -> int:
        """
        请求查询询价
        """
        return super(TraderApiPy, self).ReqQryForQuote(pQryForQuote, nRequestID)

    def ReqQryQuote(self, pQryQuote: "QryQuoteField", nRequestID: int) -> int:
        """
        请求查询报价
        """
        return super(TraderApiPy, self).ReqQryQuote(pQryQuote, nRequestID)

    def ReqQryOptionSelfClose(self, pQryOptionSelfClose: "QryOptionSelfCloseField", nRequestID: int) -> int:
        """
        请求查询期权自对冲
        """
        return super(TraderApiPy, self).ReqQryOptionSelfClose(pQryOptionSelfClose, nRequestID)

    def ReqQryInvestUnit(self, pQryInvestUnit: "QryInvestUnitField", nRequestID: int) -> int:
        """
        请求查询投资单元
        """
        return super(TraderApiPy, self).ReqQryInvestUnit(pQryInvestUnit, nRequestID)

    def ReqQryCombInstrumentGuard(self, pQryCombInstrumentGuard: "QryCombInstrumentGuardField", nRequestID: int) -> int:
        """
        请求查询组合合约安全系数
        """
        return super(TraderApiPy, self).ReqQryCombInstrumentGuard(pQryCombInstrumentGuard, nRequestID)

    def ReqQryCombAction(self, pQryCombAction: "QryCombActionField", nRequestID: int) -> int:
        """
        请求查询申请组合
        """
        return super(TraderApiPy, self).ReqQryCombAction(pQryCombAction, nRequestID)

    def ReqQryTransferSerial(self, pQryTransferSerial: "QryTransferSerialField", nRequestID: int) -> int:
        """
        请求查询转帐流水
        """
        return super(TraderApiPy, self).ReqQryTransferSerial(pQryTransferSerial, nRequestID)

    def ReqQryAccountregister(self, pQryAccountregister: "QryAccountregisterField", nRequestID: int) -> int:
        """
        请求查询银期签约关系
        """
        return super(TraderApiPy, self).ReqQryAccountregister(pQryAccountregister, nRequestID)

    def ReqQryContractBank(self, pQryContractBank: "QryContractBankField", nRequestID: int) -> int:
        """
        请求查询签约银行"""
        return super(TraderApiPy, self).ReqQryContractBank(pQryContractBank, nRequestID)

    def ReqQryParkedOrder(self, pQryParkedOrder: "QryParkedOrderField", nRequestID: int) -> int:
        """
        请求查询预埋单
        """
        return super(TraderApiPy, self).ReqQryParkedOrder(pQryParkedOrder, nRequestID)

    def ReqQryParkedOrderAction(self, pQryParkedOrderAction: "QryParkedOrderActionField", nRequestID: int) -> int:
        """
        请求查询预埋撤单"""
        return super(TraderApiPy, self).ReqQryParkedOrderAction(pQryParkedOrderAction, nRequestID)

    def ReqQryTradingNotice(self, pQryTradingNotice: "QryTradingNoticeField", nRequestID: int) -> int:
        """
        请求查询交易通知"""
        return super(TraderApiPy, self).ReqQryTradingNotice(pQryTradingNotice, nRequestID)

    def ReqQryBrokerTradingParams(self, pQryBrokerTradingParams: "QryBrokerTradingParamsField", nRequestID: int) -> int:
        """
        请求查询经纪公司交易参数
        """
        return super(TraderApiPy, self).ReqQryBrokerTradingParams(pQryBrokerTradingParams, nRequestID)

    def ReqQryBrokerTradingAlgos(self, pQryBrokerTradingAlgos: "QryBrokerTradingAlgosField", nRequestID: int) -> int:
        """
        请求查询经纪公司交易算法
        """
        return super(TraderApiPy, self).ReqQryBrokerTradingAlgos(pQryBrokerTradingAlgos, nRequestID)

    def ReqQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken: "QueryCFMMCTradingAccountTokenField", nRequestID: int) -> int:
        """
        请求查询监控中心用户令牌
        """
        return super(TraderApiPy, self).ReqQueryCFMMCTradingAccountToken(pQueryCFMMCTradingAccountToken, nRequestID)

    def ReqFromBankToFutureByFuture(self, pReqTransfer: "ReqTransferField", nRequestID: int) -> int:
        """
        期货发起银行资金转期货请求
        """
        return super(TraderApiPy, self).ReqFromBankToFutureByFuture(pReqTransfer, nRequestID)

    def ReqFromFutureToBankByFuture(self, pReqTransfer: "ReqTransferField", nRequestID: int) -> int:
        """
        期货发起期货资金转银行请求
        """
        return super(TraderApiPy, self).ReqFromFutureToBankByFuture(pReqTransfer, nRequestID)

    def ReqQueryBankAccountMoneyByFuture(self, pReqQueryAccount: "ReqQueryAccountField", nRequestID: int) -> int:
        """
        期货发起查询银行余额请求
        """
        return super(TraderApiPy, self).ReqQueryBankAccountMoneyByFuture(pReqQueryAccount, nRequestID)

    def ReqQrySecAgentTradeInfo(self, pQrySecAgentTradeInfo: "QrySecAgentTradeInfoField", nRequestID: int) -> int:
        """
        请求查询二级代理商信息
        """
        return super(TraderApiPy, self).ReqQrySecAgentTradeInfo(pQrySecAgentTradeInfo, nRequestID)

    def ReqQryClassifiedInstrument(self, pQryClassifiedInstrument: "QryClassifiedInstrumentField", nRequestID: int) -> int:
        """
        请求查询分类合约
        """
        return super(TraderApiPy, self).ReqQryClassifiedInstrument(pQryClassifiedInstrument, nRequestID)

    def ReqQryCombPromotionParam(self, pQryCombPromotionParam: "QryCombPromotionParamField", nRequestID: int) -> int:
        """
        请求组合优惠比例
        """
        return super(TraderApiPy, self).ReqQryCombPromotionParam(pQryCombPromotionParam, nRequestID)

    def ReqQryRiskSettleInvstPosition(self, pQryRiskSettleInvstPosition: "QryRiskSettleInvstPositionField", nRequestID: int) -> int:
        """
        投资者风险结算持仓查询
        """
        return super(TraderApiPy, self).ReqQryRiskSettleInvstPosition(pQryRiskSettleInvstPosition, nRequestID)

    def ReqQryRiskSettleProductStatus(self, pQryRiskSettleProductStatus: "QryRiskSettleProductStatusField", nRequestID: int) -> int:
        """
        风险结算产品查询
        """
        return super(TraderApiPy, self).ReqQryRiskSettleProductStatus(pQryRiskSettleProductStatus, nRequestID)

    def OnFrontConnected(self) -> None:
        pass

    # 当客户端与交易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
    # @param nReason 错误原因
    #        0x1001 网络读失败
    #        0x1002 网络写失败
    #        0x2001 接收心跳超时
    #        0x2002 发送心跳失败
    #        0x2003 收到错误报文
    def OnFrontDisconnected(self, nReason) -> None:
        pass

    # 心跳超时警告。当长时间未收到报文时，该方法被调用。
    # @param nTimeLapse 距离上次接收报文的时间
    def OnHeartBeatWarning(self, nTimeLapse) -> None:
        pass

    # 客户端认证响应
    def OnRspAuthenticate(self, pRspAuthenticateField, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 登录请求响应
    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 登出请求响应
    def OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 用户口令更新请求响应
    def OnRspUserPasswordUpdate(self, pUserPasswordUpdate, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 资金账户口令更新请求响应
    def OnRspTradingAccountPasswordUpdate(self, pTradingAccountPasswordUpdate, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 报单录入请求响应
    def OnRspOrderInsert(self, pInputOrder, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 预埋单录入请求响应
    def OnRspParkedOrderInsert(self, pParkedOrder, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 预埋撤单录入请求响应
    def OnRspParkedOrderAction(self, pParkedOrderAction, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 报单操作请求响应
    def OnRspOrderAction(self, pInputOrderAction, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 查询最大报单数量响应
    def OnRspQryMaxOrderVolume(self, pQryMaxOrderVolume, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 投资者结算结果确认响应
    def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 删除预埋单响应
    def OnRspRemoveParkedOrder(self, pRemoveParkedOrder, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 删除预埋撤单响应
    def OnRspRemoveParkedOrderAction(self, pRemoveParkedOrderAction, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 执行宣告录入请求响应
    def OnRspExecOrderInsert(self, pInputExecOrder, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 执行宣告操作请求响应
    def OnRspExecOrderAction(self, pInputExecOrderAction, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 询价录入请求响应
    def OnRspForQuoteInsert(self, pInputForQuote, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 报价录入请求响应
    def OnRspQuoteInsert(self, pInputQuote, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 报价操作请求响应
    def OnRspQuoteAction(self, pInputQuoteAction, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 批量报单操作请求响应
    def OnRspBatchOrderAction(self, pInputBatchOrderAction, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 申请组合录入请求响应
    def OnRspCombActionInsert(self, pInputCombAction, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询报单响应
    def OnRspQryOrder(self, pOrder, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询成交响应
    def OnRspQryTrade(self, pTrade, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询投资者持仓响应
    def OnRspQryInvestorPosition(self, pInvestorPosition, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询资金账户响应
    def OnRspQryTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询投资者响应
    def OnRspQryInvestor(self, pInvestor, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询交易编码响应
    def OnRspQryTradingCode(self, pTradingCode, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询合约保证金率响应
    def OnRspQryInstrumentMarginRate(self, pInstrumentMarginRate, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询合约手续费率响应
    def OnRspQryInstrumentCommissionRate(self, pInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询交易所响应
    def OnRspQryExchange(self, pExchange, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询产品响应
    def OnRspQryProduct(self, pProduct, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询合约响应
    def OnRspQryInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询行情响应
    def OnRspQryDepthMarketData(self, pDepthMarketData, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询投资者结算结果响应
    def OnRspQrySettlementInfo(self, pSettlementInfo, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询转帐银行响应
    def OnRspQryTransferBank(self, pTransferBank, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询投资者持仓明细响应
    def OnRspQryInvestorPositionDetail(self, pInvestorPositionDetail, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询客户通知响应
    def OnRspQryNotice(self, pNotice, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询结算信息确认响应
    def OnRspQrySettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询投资者持仓明细响应
    def OnRspQryInvestorPositionCombineDetail(self, pInvestorPositionCombineDetail, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 查询保证金监管系统经纪公司资金账户密钥响应
    def OnRspQryCFMMCTradingAccountKey(self, pCFMMCTradingAccountKey, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询仓单折抵信息响应
    def OnRspQryEWarrantOffset(self, pEWarrantOffset, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询投资者品种/跨品种保证金响应
    def OnRspQryInvestorProductGroupMargin(self, pInvestorProductGroupMargin, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询交易所保证金率响应
    def OnRspQryExchangeMarginRate(self, pExchangeMarginRate, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询交易所调整保证金率响应
    def OnRspQryExchangeMarginRateAdjust(self, pExchangeMarginRateAdjust, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询汇率响应
    def OnRspQryExchangeRate(self, pExchangeRate, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询二级代理操作员银期权限响应
    def OnRspQrySecAgentACIDMap(self, pSecAgentACIDMap, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询产品报价汇率
    def OnRspQryProductExchRate(self, pProductExchRate, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询产品组
    def OnRspQryProductGroup(self, pProductGroup, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询做市商合约手续费率响应
    def OnRspQryMMInstrumentCommissionRate(self, pMMInstrumentCommissionRate, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询做市商期权合约手续费响应
    def OnRspQryMMOptionInstrCommRate(self, pMMOptionInstrCommRate, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询报单手续费响应
    def OnRspQryInstrumentOrderCommRate(self, pInstrumentOrderCommRate, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询期权交易成本响应
    def OnRspQryOptionInstrTradeCost(self, pOptionInstrTradeCost, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询期权合约手续费响应
    def OnRspQryOptionInstrCommRate(self, pOptionInstrCommRate, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询执行宣告响应
    def OnRspQryExecOrder(self, pExecOrder, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询询价响应
    def OnRspQryForQuote(self, pForQuote, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询报价响应
    def OnRspQryQuote(self, pQuote, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询组合合约安全系数响应
    def OnRspQryCombInstrumentGuard(self, pCombInstrumentGuard, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询申请组合响应
    def OnRspQryCombAction(self, pCombAction, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询转帐流水响应
    def OnRspQryTransferSerial(self, pTransferSerial, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询银期签约关系响应
    def OnRspQryAccountregister(self, pAccountregister, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 错误应答
    def OnRspError(self, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 报单通知
    def OnRtnOrder(self, pOrder) -> None:
        pass

    # 成交通知
    def OnRtnTrade(self, pTrade) -> None:
        pass

    # 报单录入错误回报
    def OnErrRtnOrderInsert(self, pInputOrder, pRspInfo) -> None:
        pass

    # 报单操作错误回报
    def OnErrRtnOrderAction(self, pOrderAction, pRspInfo) -> None:
        pass

    # 合约交易状态通知
    def OnRtnInstrumentStatus(self, pInstrumentStatus) -> None:
        pass

    # 交易所公告通知
    def OnRtnBulletin(self, pBulletin) -> None:
        pass

    # 交易通知
    def OnRtnTradingNotice(self, pTradingNoticeInfo) -> None:
        pass

    # 提示条件单校验错误
    def OnRtnErrorConditionalOrder(self, pErrorConditionalOrder) -> None:
        pass

    # 执行宣告通知
    def OnRtnExecOrder(self, pExecOrder) -> None:
        pass

    # 执行宣告录入错误回报
    def OnErrRtnExecOrderInsert(self, pInputExecOrder, pRspInfo) -> None:
        pass

    # 执行宣告操作错误回报
    def OnErrRtnExecOrderAction(self, pExecOrderAction, pRspInfo) -> None:
        pass

    # 询价录入错误回报
    def OnErrRtnForQuoteInsert(self, pInputForQuote, pRspInfo) -> None:
        pass

    # 报价通知
    def OnRtnQuote(self, pQuote) -> None:
        pass

    # 报价录入错误回报
    def OnErrRtnQuoteInsert(self, pInputQuote, pRspInfo) -> None:
        pass

    # 报价操作错误回报
    def OnErrRtnQuoteAction(self, pQuoteAction, pRspInfo) -> None:
        pass

    # 询价通知
    def OnRtnForQuoteRsp(self, pForQuoteRsp) -> None:
        pass

    # 保证金监控中心用户令牌
    def OnRtnCFMMCTradingAccountToken(self, pCFMMCTradingAccountToken) -> None:
        pass

    # 批量报单操作错误回报
    def OnErrRtnBatchOrderAction(self, pBatchOrderAction, pRspInfo) -> None:
        pass

    # 申请组合通知
    def OnRtnCombAction(self, pCombAction) -> None:
        pass

    # 申请组合录入错误回报
    def OnErrRtnCombActionInsert(self, pInputCombAction, pRspInfo) -> None:
        pass

    # 请求查询签约银行响应
    def OnRspQryContractBank(self, pContractBank, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询预埋单响应
    def OnRspQryParkedOrder(self, pParkedOrder, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询预埋撤单响应
    def OnRspQryParkedOrderAction(self, pParkedOrderAction, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询交易通知响应
    def OnRspQryTradingNotice(self, pTradingNotice, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询经纪公司交易参数响应
    def OnRspQryBrokerTradingParams(self, pBrokerTradingParams, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询经纪公司交易算法响应
    def OnRspQryBrokerTradingAlgos(self, pBrokerTradingAlgos, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询监控中心用户令牌
    def OnRspQueryCFMMCTradingAccountToken(self, pQueryCFMMCTradingAccountToken, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 银行发起银行资金转期货通知
    def OnRtnFromBankToFutureByBank(self, pRspTransfer) -> None:
        pass

    # 银行发起期货资金转银行通知
    def OnRtnFromFutureToBankByBank(self, pRspTransfer) -> None:
        pass

    # 银行发起冲正银行转期货通知
    def OnRtnRepealFromBankToFutureByBank(self, pRspRepeal) -> None:
        pass

    # 银行发起冲正期货转银行通知
    def OnRtnRepealFromFutureToBankByBank(self, pRspRepeal) -> None:
        pass

    # 期货发起银行资金转期货通知
    def OnRtnFromBankToFutureByFuture(self, pRspTransfer) -> None:
        pass

    # 期货发起期货资金转银行通知
    def OnRtnFromFutureToBankByFuture(self, pRspTransfer) -> None:
        pass

    # 系统运行时期货端手工发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
    def OnRtnRepealFromBankToFutureByFutureManual(self, pRspRepeal) -> None:
        pass

    # 系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
    def OnRtnRepealFromFutureToBankByFutureManual(self, pRspRepeal) -> None:
        pass

    # 期货发起查询银行余额通知
    def OnRtnQueryBankBalanceByFuture(self, pNotifyQueryAccount) -> None:
        pass

    # 期货发起银行资金转期货错误回报
    def OnErrRtnBankToFutureByFuture(self, pReqTransfer, pRspInfo) -> None:
        pass

    # 期货发起期货资金转银行错误回报
    def OnErrRtnFutureToBankByFuture(self, pReqTransfer, pRspInfo) -> None:
        pass

    # 系统运行时期货端手工发起冲正银行转期货错误回报
    def OnErrRtnRepealBankToFutureByFutureManual(self, pReqRepeal, pRspInfo) -> None:
        pass

    # 系统运行时期货端手工发起冲正期货转银行错误回报
    def OnErrRtnRepealFutureToBankByFutureManual(self, pReqRepeal, pRspInfo) -> None:
        pass

    # 期货发起查询银行余额错误回报
    def OnErrRtnQueryBankBalanceByFuture(self, pReqQueryAccount, pRspInfo) -> None:
        pass

    # 期货发起冲正银行转期货请求，银行处理完毕后报盘发回的通知
    def OnRtnRepealFromBankToFutureByFuture(self, pRspRepeal) -> None:
        pass

    # 期货发起冲正期货转银行请求，银行处理完毕后报盘发回的通知
    def OnRtnRepealFromFutureToBankByFuture(self, pRspRepeal) -> None:
        pass

    # 期货发起银行资金转期货应答
    def OnRspFromBankToFutureByFuture(self, pReqTransfer, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 期货发起期货资金转银行应答
    def OnRspFromFutureToBankByFuture(self, pReqTransfer, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 期货发起查询银行余额应答
    def OnRspQueryBankAccountMoneyByFuture(self, pReqQueryAccount, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 银行发起银期开户通知
    def OnRtnOpenAccountByBank(self, pOpenAccount) -> None:
        pass

    # 银行发起银期销户通知
    def OnRtnCancelAccountByBank(self, pCancelAccount) -> None:
        pass

    # 银行发起变更银行账号通知
    def OnRtnChangeAccountByBank(self, pChangeAccount) -> None:
        pass

    # 期权自对冲录入请求响应
    def OnRspOptionSelfCloseInsert(self, pInputOptionSelfClose, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 期权自对冲操作请求响应
    def OnRspOptionSelfCloseAction(self, pInputOptionSelfCloseAction, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询资金账户响应
    def OnRspQrySecAgentTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询二级代理商资金校验模式响应
    def OnRspQrySecAgentCheckMode(self, pSecAgentCheckMode, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询期权自对冲响应
    def OnRspQryOptionSelfClose(self, *pOptionSelfClose, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询投资单元响应
    def OnRspQryInvestUnit(self, pInvestUnit, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 期权自对冲通知
    def OnRtnOptionSelfClose(self, pOptionSelfClose) -> None:
        pass

    # 期权自对冲录入错误回报
    def OnErrRtnOptionSelfCloseInsert(self, pInputOptionSelfClose, pRspInfo) -> None:
        pass

    # 期权自对冲操作错误回报
    def OnErrRtnOptionSelfCloseAction(self, pOptionSelfCloseAction, pRspInfo) -> None:
        pass

    # 查询用户当前支持的认证模式的回复
    def OnRspUserAuthMethod(self, pRspUserAuthMethod, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 获取图形验证码请求的回复
    def OnRspGenUserCaptcha(self, pRspGenUserCaptcha, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 获取短信验证码请求的回复
    def OnRspGenUserText(self, pRspGenUserText, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询二级代理商信息响应
    def OnRspQrySecAgentTradeInfo(self, pSecAgentTradeInfo, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求查询分类合约响应
    def OnRspQryClassifiedInstrument(self, pInstrument, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 请求组合优惠比例响应
    def OnRspQryCombPromotionParam(self, pCombPromotionParam, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 投资者风险结算持仓查询响应
    def OnRspQryRiskSettleInvstPosition(self, pRiskSettleInvstPosition, pRspInfo, nRequestID, bIsLast) -> None:
        pass

    # 风险结算产品查询响应
    def OnRspQryRiskSettleProductStatus(self, pRiskSettleProductStatus, pRspInfo, nRequestID, bIsLast) -> None:
        pass
