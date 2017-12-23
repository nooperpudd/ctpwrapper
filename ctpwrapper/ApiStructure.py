# encoding=utf-8

from ctpwrapper.base import Base


class DisseminationField(Base):
    def __init__(self, SequenceSeries='', SequenceNo=''):
        self.SequenceSeries = int(SequenceSeries)
        self.SequenceNo = int(SequenceNo)


class ReqUserLoginField(Base):
    def __init__(self, TradingDay='', BrokerID='', UserID='', Password='', UserProductInfo='', InterfaceProductInfo='',
                 ProtocolInfo='', MacAddress='', OneTimePassword='', ClientIPAddress='', LoginRemark=''):
        self.TradingDay = TradingDay
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.Password = Password
        self.UserProductInfo = UserProductInfo
        self.InterfaceProductInfo = InterfaceProductInfo
        self.ProtocolInfo = ProtocolInfo
        self.MacAddress = MacAddress
        self.OneTimePassword = OneTimePassword
        self.ClientIPAddress = ClientIPAddress
        self.LoginRemark = LoginRemark


class RspUserLoginField(Base):
    def __init__(self, TradingDay='', LoginTime='', BrokerID='', UserID='', SystemName='', FrontID='', SessionID='',
                 MaxOrderRef='', SHFETime='', DCETime='', CZCETime='', FFEXTime='', INETime=''):
        self.TradingDay = TradingDay
        self.LoginTime = LoginTime
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.SystemName = SystemName
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.MaxOrderRef = MaxOrderRef
        self.SHFETime = SHFETime
        self.DCETime = DCETime
        self.CZCETime = CZCETime
        self.FFEXTime = FFEXTime
        self.INETime = INETime


class UserLogoutField(Base):
    def __init__(self, BrokerID='', UserID=''):
        self.BrokerID = BrokerID
        self.UserID = UserID


class ForceUserLogoutField(Base):
    def __init__(self, BrokerID='', UserID=''):
        self.BrokerID = BrokerID
        self.UserID = UserID


class ReqAuthenticateField(Base):
    def __init__(self, BrokerID='', UserID='', UserProductInfo='', AuthCode=''):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.UserProductInfo = UserProductInfo
        self.AuthCode = AuthCode


class RspAuthenticateField(Base):
    def __init__(self, BrokerID='', UserID='', UserProductInfo=''):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.UserProductInfo = UserProductInfo


class AuthenticationInfoField(Base):
    def __init__(self, BrokerID='', UserID='', UserProductInfo='', AuthInfo='', IsResult=''):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.UserProductInfo = UserProductInfo
        self.AuthInfo = AuthInfo
        self.IsResult = int(IsResult)


class TransferHeaderField(Base):
    def __init__(self, Version='', TradeCode='', TradeDate='', TradeTime='', TradeSerial='', FutureID='', BankID='',
                 BankBrchID='', OperNo='', DeviceID='', RecordNum='', SessionID='', RequestID=''):
        self.Version = Version
        self.TradeCode = TradeCode
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.TradeSerial = TradeSerial
        self.FutureID = FutureID
        self.BankID = BankID
        self.BankBrchID = BankBrchID
        self.OperNo = OperNo
        self.DeviceID = DeviceID
        self.RecordNum = RecordNum
        self.SessionID = int(SessionID)
        self.RequestID = int(RequestID)


class TransferBankToFutureReqField(Base):
    def __init__(self, FutureAccount='', FuturePwdFlag='', FutureAccPwd='', TradeAmt='', CustFee='', CurrencyCode=''):
        self.FutureAccount = FutureAccount
        self.FuturePwdFlag = FuturePwdFlag
        self.FutureAccPwd = FutureAccPwd
        self.TradeAmt = float(TradeAmt)
        self.CustFee = float(CustFee)
        self.CurrencyCode = CurrencyCode


class TransferBankToFutureRspField(Base):
    def __init__(self, RetCode='', RetInfo='', FutureAccount='', TradeAmt='', CustFee='', CurrencyCode=''):
        self.RetCode = RetCode
        self.RetInfo = RetInfo
        self.FutureAccount = FutureAccount
        self.TradeAmt = float(TradeAmt)
        self.CustFee = float(CustFee)
        self.CurrencyCode = CurrencyCode


class TransferFutureToBankReqField(Base):
    def __init__(self, FutureAccount='', FuturePwdFlag='', FutureAccPwd='', TradeAmt='', CustFee='', CurrencyCode=''):
        self.FutureAccount = FutureAccount
        self.FuturePwdFlag = FuturePwdFlag
        self.FutureAccPwd = FutureAccPwd
        self.TradeAmt = float(TradeAmt)
        self.CustFee = float(CustFee)
        self.CurrencyCode = CurrencyCode


class TransferFutureToBankRspField(Base):
    def __init__(self, RetCode='', RetInfo='', FutureAccount='', TradeAmt='', CustFee='', CurrencyCode=''):
        self.RetCode = RetCode
        self.RetInfo = RetInfo
        self.FutureAccount = FutureAccount
        self.TradeAmt = float(TradeAmt)
        self.CustFee = float(CustFee)
        self.CurrencyCode = CurrencyCode


class TransferQryBankReqField(Base):
    def __init__(self, FutureAccount='', FuturePwdFlag='', FutureAccPwd='', CurrencyCode=''):
        self.FutureAccount = FutureAccount
        self.FuturePwdFlag = FuturePwdFlag
        self.FutureAccPwd = FutureAccPwd
        self.CurrencyCode = CurrencyCode


class TransferQryBankRspField(Base):
    def __init__(self, RetCode='', RetInfo='', FutureAccount='', TradeAmt='', UseAmt='', FetchAmt='', CurrencyCode=''):
        self.RetCode = RetCode
        self.RetInfo = RetInfo
        self.FutureAccount = FutureAccount
        self.TradeAmt = float(TradeAmt)
        self.UseAmt = float(UseAmt)
        self.FetchAmt = float(FetchAmt)
        self.CurrencyCode = CurrencyCode


class TransferQryDetailReqField(Base):
    def __init__(self, FutureAccount=''):
        self.FutureAccount = FutureAccount


class TransferQryDetailRspField(Base):
    def __init__(self, TradeDate='', TradeTime='', TradeCode='', FutureSerial='', FutureID='', FutureAccount='',
                 BankSerial='', BankID='', BankBrchID='', BankAccount='', CertCode='', CurrencyCode='', TxAmount='',
                 Flag=''):
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.TradeCode = TradeCode
        self.FutureSerial = int(FutureSerial)
        self.FutureID = FutureID
        self.FutureAccount = FutureAccount
        self.BankSerial = int(BankSerial)
        self.BankID = BankID
        self.BankBrchID = BankBrchID
        self.BankAccount = BankAccount
        self.CertCode = CertCode
        self.CurrencyCode = CurrencyCode
        self.TxAmount = float(TxAmount)
        self.Flag = Flag


class RspInfoField(Base):
    def __init__(self, ErrorID='', ErrorMsg=''):
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg


class ExchangeField(Base):
    def __init__(self, ExchangeID='', ExchangeName='', ExchangeProperty=''):
        self.ExchangeID = ExchangeID
        self.ExchangeName = ExchangeName
        self.ExchangeProperty = ExchangeProperty


class ProductField(Base):
    def __init__(self, ProductID='', ProductName='', ExchangeID='', ProductClass='', VolumeMultiple='', PriceTick='',
                 MaxMarketOrderVolume='', MinMarketOrderVolume='', MaxLimitOrderVolume='', MinLimitOrderVolume='',
                 PositionType='', PositionDateType='', CloseDealType='', TradeCurrencyID='', MortgageFundUseRange='',
                 ExchangeProductID='', UnderlyingMultiple=''):
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.ExchangeID = ExchangeID
        self.ProductClass = ProductClass
        self.VolumeMultiple = int(VolumeMultiple)
        self.PriceTick = float(PriceTick)
        self.MaxMarketOrderVolume = int(MaxMarketOrderVolume)
        self.MinMarketOrderVolume = int(MinMarketOrderVolume)
        self.MaxLimitOrderVolume = int(MaxLimitOrderVolume)
        self.MinLimitOrderVolume = int(MinLimitOrderVolume)
        self.PositionType = PositionType
        self.PositionDateType = PositionDateType
        self.CloseDealType = CloseDealType
        self.TradeCurrencyID = TradeCurrencyID
        self.MortgageFundUseRange = MortgageFundUseRange
        self.ExchangeProductID = ExchangeProductID
        self.UnderlyingMultiple = float(UnderlyingMultiple)


class InstrumentField(Base):
    def __init__(self, InstrumentID='', ExchangeID='', InstrumentName='', ExchangeInstID='', ProductID='',
                 ProductClass='', DeliveryYear='', DeliveryMonth='', MaxMarketOrderVolume='', MinMarketOrderVolume='',
                 MaxLimitOrderVolume='', MinLimitOrderVolume='', VolumeMultiple='', PriceTick='', CreateDate='',
                 OpenDate='', ExpireDate='', StartDelivDate='', EndDelivDate='', InstLifePhase='', IsTrading='',
                 PositionType='', PositionDateType='', LongMarginRatio='', ShortMarginRatio='',
                 MaxMarginSideAlgorithm='', UnderlyingInstrID='', StrikePrice='', OptionsType='', UnderlyingMultiple='',
                 CombinationType=''):
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID
        self.InstrumentName = InstrumentName
        self.ExchangeInstID = ExchangeInstID
        self.ProductID = ProductID
        self.ProductClass = ProductClass
        self.DeliveryYear = int(DeliveryYear)
        self.DeliveryMonth = int(DeliveryMonth)
        self.MaxMarketOrderVolume = int(MaxMarketOrderVolume)
        self.MinMarketOrderVolume = int(MinMarketOrderVolume)
        self.MaxLimitOrderVolume = int(MaxLimitOrderVolume)
        self.MinLimitOrderVolume = int(MinLimitOrderVolume)
        self.VolumeMultiple = int(VolumeMultiple)
        self.PriceTick = float(PriceTick)
        self.CreateDate = CreateDate
        self.OpenDate = OpenDate
        self.ExpireDate = ExpireDate
        self.StartDelivDate = StartDelivDate
        self.EndDelivDate = EndDelivDate
        self.InstLifePhase = InstLifePhase
        self.IsTrading = int(IsTrading)
        self.PositionType = PositionType
        self.PositionDateType = PositionDateType
        self.LongMarginRatio = float(LongMarginRatio)
        self.ShortMarginRatio = float(ShortMarginRatio)
        self.MaxMarginSideAlgorithm = MaxMarginSideAlgorithm
        self.UnderlyingInstrID = UnderlyingInstrID
        self.StrikePrice = float(StrikePrice)
        self.OptionsType = OptionsType
        self.UnderlyingMultiple = float(UnderlyingMultiple)
        self.CombinationType = CombinationType


class BrokerField(Base):
    def __init__(self, BrokerID='', BrokerAbbr='', BrokerName='', IsActive=''):
        self.BrokerID = BrokerID
        self.BrokerAbbr = BrokerAbbr
        self.BrokerName = BrokerName
        self.IsActive = int(IsActive)


class TraderField(Base):
    def __init__(self, ExchangeID='', TraderID='', ParticipantID='', Password='', InstallCount='', BrokerID=''):
        self.ExchangeID = ExchangeID
        self.TraderID = TraderID
        self.ParticipantID = ParticipantID
        self.Password = Password
        self.InstallCount = int(InstallCount)
        self.BrokerID = BrokerID


class InvestorField(Base):
    def __init__(self, InvestorID='', BrokerID='', InvestorGroupID='', InvestorName='', IdentifiedCardType='',
                 IdentifiedCardNo='', IsActive='', Telephone='', Address='', OpenDate='', Mobile='', CommModelID='',
                 MarginModelID=''):
        self.InvestorID = InvestorID
        self.BrokerID = BrokerID
        self.InvestorGroupID = InvestorGroupID
        self.InvestorName = InvestorName
        self.IdentifiedCardType = IdentifiedCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.IsActive = int(IsActive)
        self.Telephone = Telephone
        self.Address = Address
        self.OpenDate = OpenDate
        self.Mobile = Mobile
        self.CommModelID = CommModelID
        self.MarginModelID = MarginModelID


class TradingCodeField(Base):
    def __init__(self, InvestorID='', BrokerID='', ExchangeID='', ClientID='', IsActive='', ClientIDType=''):
        self.InvestorID = InvestorID
        self.BrokerID = BrokerID
        self.ExchangeID = ExchangeID
        self.ClientID = ClientID
        self.IsActive = int(IsActive)
        self.ClientIDType = ClientIDType


class PartBrokerField(Base):
    def __init__(self, BrokerID='', ExchangeID='', ParticipantID='', IsActive=''):
        self.BrokerID = BrokerID
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.IsActive = int(IsActive)


class SuperUserField(Base):
    def __init__(self, UserID='', UserName='', Password='', IsActive=''):
        self.UserID = UserID
        self.UserName = UserName
        self.Password = Password
        self.IsActive = int(IsActive)


class SuperUserFunctionField(Base):
    def __init__(self, UserID='', FunctionCode=''):
        self.UserID = UserID
        self.FunctionCode = FunctionCode


class InvestorGroupField(Base):
    def __init__(self, BrokerID='', InvestorGroupID='', InvestorGroupName=''):
        self.BrokerID = BrokerID
        self.InvestorGroupID = InvestorGroupID
        self.InvestorGroupName = InvestorGroupName


class TradingAccountField(Base):
    def __init__(self, BrokerID='', AccountID='', PreMortgage='', PreCredit='', PreDeposit='', PreBalance='',
                 PreMargin='', InterestBase='', Interest='', Deposit='', Withdraw='', FrozenMargin='', FrozenCash='',
                 FrozenCommission='', CurrMargin='', CashIn='', Commission='', CloseProfit='', PositionProfit='',
                 Balance='', Available='', WithdrawQuota='', Reserve='', TradingDay='', SettlementID='', Credit='',
                 Mortgage='', ExchangeMargin='', DeliveryMargin='', ExchangeDeliveryMargin='', ReserveBalance='',
                 CurrencyID='', PreFundMortgageIn='', PreFundMortgageOut='', FundMortgageIn='', FundMortgageOut='',
                 FundMortgageAvailable='', MortgageableFund='', SpecProductMargin='', SpecProductFrozenMargin='',
                 SpecProductCommission='', SpecProductFrozenCommission='', SpecProductPositionProfit='',
                 SpecProductCloseProfit='', SpecProductPositionProfitByAlg='', SpecProductExchangeMargin=''):
        self.BrokerID = BrokerID
        self.AccountID = AccountID
        self.PreMortgage = float(PreMortgage)
        self.PreCredit = float(PreCredit)
        self.PreDeposit = float(PreDeposit)
        self.PreBalance = float(PreBalance)
        self.PreMargin = float(PreMargin)
        self.InterestBase = float(InterestBase)
        self.Interest = float(Interest)
        self.Deposit = float(Deposit)
        self.Withdraw = float(Withdraw)
        self.FrozenMargin = float(FrozenMargin)
        self.FrozenCash = float(FrozenCash)
        self.FrozenCommission = float(FrozenCommission)
        self.CurrMargin = float(CurrMargin)
        self.CashIn = float(CashIn)
        self.Commission = float(Commission)
        self.CloseProfit = float(CloseProfit)
        self.PositionProfit = float(PositionProfit)
        self.Balance = float(Balance)
        self.Available = float(Available)
        self.WithdrawQuota = float(WithdrawQuota)
        self.Reserve = float(Reserve)
        self.TradingDay = TradingDay
        self.SettlementID = int(SettlementID)
        self.Credit = float(Credit)
        self.Mortgage = float(Mortgage)
        self.ExchangeMargin = float(ExchangeMargin)
        self.DeliveryMargin = float(DeliveryMargin)
        self.ExchangeDeliveryMargin = float(ExchangeDeliveryMargin)
        self.ReserveBalance = float(ReserveBalance)
        self.CurrencyID = CurrencyID
        self.PreFundMortgageIn = float(PreFundMortgageIn)
        self.PreFundMortgageOut = float(PreFundMortgageOut)
        self.FundMortgageIn = float(FundMortgageIn)
        self.FundMortgageOut = float(FundMortgageOut)
        self.FundMortgageAvailable = float(FundMortgageAvailable)
        self.MortgageableFund = float(MortgageableFund)
        self.SpecProductMargin = float(SpecProductMargin)
        self.SpecProductFrozenMargin = float(SpecProductFrozenMargin)
        self.SpecProductCommission = float(SpecProductCommission)
        self.SpecProductFrozenCommission = float(SpecProductFrozenCommission)
        self.SpecProductPositionProfit = float(SpecProductPositionProfit)
        self.SpecProductCloseProfit = float(SpecProductCloseProfit)
        self.SpecProductPositionProfitByAlg = float(SpecProductPositionProfitByAlg)
        self.SpecProductExchangeMargin = float(SpecProductExchangeMargin)


class InvestorPositionField(Base):
    def __init__(self, InstrumentID='', BrokerID='', InvestorID='', PosiDirection='', HedgeFlag='', PositionDate='',
                 YdPosition='', Position='', LongFrozen='', ShortFrozen='', LongFrozenAmount='', ShortFrozenAmount='',
                 OpenVolume='', CloseVolume='', OpenAmount='', CloseAmount='', PositionCost='', PreMargin='',
                 UseMargin='', FrozenMargin='', FrozenCash='', FrozenCommission='', CashIn='', Commission='',
                 CloseProfit='', PositionProfit='', PreSettlementPrice='', SettlementPrice='', TradingDay='',
                 SettlementID='', OpenCost='', ExchangeMargin='', CombPosition='', CombLongFrozen='',
                 CombShortFrozen='', CloseProfitByDate='', CloseProfitByTrade='', TodayPosition='',
                 MarginRateByMoney='', MarginRateByVolume='', StrikeFrozen='', StrikeFrozenAmount='', AbandonFrozen=''):
        self.InstrumentID = InstrumentID
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.PosiDirection = PosiDirection
        self.HedgeFlag = HedgeFlag
        self.PositionDate = PositionDate
        self.YdPosition = int(YdPosition)
        self.Position = int(Position)
        self.LongFrozen = int(LongFrozen)
        self.ShortFrozen = int(ShortFrozen)
        self.LongFrozenAmount = float(LongFrozenAmount)
        self.ShortFrozenAmount = float(ShortFrozenAmount)
        self.OpenVolume = int(OpenVolume)
        self.CloseVolume = int(CloseVolume)
        self.OpenAmount = float(OpenAmount)
        self.CloseAmount = float(CloseAmount)
        self.PositionCost = float(PositionCost)
        self.PreMargin = float(PreMargin)
        self.UseMargin = float(UseMargin)
        self.FrozenMargin = float(FrozenMargin)
        self.FrozenCash = float(FrozenCash)
        self.FrozenCommission = float(FrozenCommission)
        self.CashIn = float(CashIn)
        self.Commission = float(Commission)
        self.CloseProfit = float(CloseProfit)
        self.PositionProfit = float(PositionProfit)
        self.PreSettlementPrice = float(PreSettlementPrice)
        self.SettlementPrice = float(SettlementPrice)
        self.TradingDay = TradingDay
        self.SettlementID = int(SettlementID)
        self.OpenCost = float(OpenCost)
        self.ExchangeMargin = float(ExchangeMargin)
        self.CombPosition = int(CombPosition)
        self.CombLongFrozen = int(CombLongFrozen)
        self.CombShortFrozen = int(CombShortFrozen)
        self.CloseProfitByDate = float(CloseProfitByDate)
        self.CloseProfitByTrade = float(CloseProfitByTrade)
        self.TodayPosition = int(TodayPosition)
        self.MarginRateByMoney = float(MarginRateByMoney)
        self.MarginRateByVolume = float(MarginRateByVolume)
        self.StrikeFrozen = int(StrikeFrozen)
        self.StrikeFrozenAmount = float(StrikeFrozenAmount)
        self.AbandonFrozen = int(AbandonFrozen)


class InstrumentMarginRateField(Base):
    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', HedgeFlag='',
                 LongMarginRatioByMoney='', LongMarginRatioByVolume='', ShortMarginRatioByMoney='',
                 ShortMarginRatioByVolume='', IsRelative=''):
        self.InstrumentID = InstrumentID
        self.InvestorRange = InvestorRange
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.HedgeFlag = HedgeFlag
        self.LongMarginRatioByMoney = float(LongMarginRatioByMoney)
        self.LongMarginRatioByVolume = float(LongMarginRatioByVolume)
        self.ShortMarginRatioByMoney = float(ShortMarginRatioByMoney)
        self.ShortMarginRatioByVolume = float(ShortMarginRatioByVolume)
        self.IsRelative = int(IsRelative)


class InstrumentCommissionRateField(Base):
    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', OpenRatioByMoney='',
                 OpenRatioByVolume='', CloseRatioByMoney='', CloseRatioByVolume='', CloseTodayRatioByMoney='',
                 CloseTodayRatioByVolume=''):
        self.InstrumentID = InstrumentID
        self.InvestorRange = InvestorRange
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.OpenRatioByMoney = float(OpenRatioByMoney)
        self.OpenRatioByVolume = float(OpenRatioByVolume)
        self.CloseRatioByMoney = float(CloseRatioByMoney)
        self.CloseRatioByVolume = float(CloseRatioByVolume)
        self.CloseTodayRatioByMoney = float(CloseTodayRatioByMoney)
        self.CloseTodayRatioByVolume = float(CloseTodayRatioByVolume)


class DepthMarketDataField(Base):
    def __init__(self, TradingDay='', InstrumentID='', ExchangeID='', ExchangeInstID='', LastPrice='',
                 PreSettlementPrice='', PreClosePrice='', PreOpenInterest='', OpenPrice='', HighestPrice='',
                 LowestPrice='', Volume='', Turnover='', OpenInterest='', ClosePrice='', SettlementPrice='',
                 UpperLimitPrice='', LowerLimitPrice='', PreDelta='', CurrDelta='', UpdateTime='', UpdateMillisec='',
                 BidPrice1='', BidVolume1='', AskPrice1='', AskVolume1='', BidPrice2='', BidVolume2='', AskPrice2='',
                 AskVolume2='', BidPrice3='', BidVolume3='', AskPrice3='', AskVolume3='', BidPrice4='', BidVolume4='',
                 AskPrice4='', AskVolume4='', BidPrice5='', BidVolume5='', AskPrice5='', AskVolume5='', AveragePrice='',
                 ActionDay=''):
        self.TradingDay = TradingDay
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID
        self.ExchangeInstID = ExchangeInstID
        self.LastPrice = float(LastPrice)
        self.PreSettlementPrice = float(PreSettlementPrice)
        self.PreClosePrice = float(PreClosePrice)
        self.PreOpenInterest = float(PreOpenInterest)
        self.OpenPrice = float(OpenPrice)
        self.HighestPrice = float(HighestPrice)
        self.LowestPrice = float(LowestPrice)
        self.Volume = int(Volume)
        self.Turnover = float(Turnover)
        self.OpenInterest = float(OpenInterest)
        self.ClosePrice = float(ClosePrice)
        self.SettlementPrice = float(SettlementPrice)
        self.UpperLimitPrice = float(UpperLimitPrice)
        self.LowerLimitPrice = float(LowerLimitPrice)
        self.PreDelta = float(PreDelta)
        self.CurrDelta = float(CurrDelta)
        self.UpdateTime = UpdateTime
        self.UpdateMillisec = int(UpdateMillisec)
        self.BidPrice1 = float(BidPrice1)
        self.BidVolume1 = int(BidVolume1)
        self.AskPrice1 = float(AskPrice1)
        self.AskVolume1 = int(AskVolume1)
        self.BidPrice2 = float(BidPrice2)
        self.BidVolume2 = int(BidVolume2)
        self.AskPrice2 = float(AskPrice2)
        self.AskVolume2 = int(AskVolume2)
        self.BidPrice3 = float(BidPrice3)
        self.BidVolume3 = int(BidVolume3)
        self.AskPrice3 = float(AskPrice3)
        self.AskVolume3 = int(AskVolume3)
        self.BidPrice4 = float(BidPrice4)
        self.BidVolume4 = int(BidVolume4)
        self.AskPrice4 = float(AskPrice4)
        self.AskVolume4 = int(AskVolume4)
        self.BidPrice5 = float(BidPrice5)
        self.BidVolume5 = int(BidVolume5)
        self.AskPrice5 = float(AskPrice5)
        self.AskVolume5 = int(AskVolume5)
        self.AveragePrice = float(AveragePrice)
        self.ActionDay = ActionDay


class InstrumentTradingRightField(Base):
    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', TradingRight=''):
        self.InstrumentID = InstrumentID
        self.InvestorRange = InvestorRange
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.TradingRight = TradingRight


class BrokerUserField(Base):
    def __init__(self, BrokerID='', UserID='', UserName='', UserType='', IsActive='', IsUsingOTP=''):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.UserName = UserName
        self.UserType = UserType
        self.IsActive = int(IsActive)
        self.IsUsingOTP = int(IsUsingOTP)


class BrokerUserPasswordField(Base):
    def __init__(self, BrokerID='', UserID='', Password=''):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.Password = Password


class BrokerUserFunctionField(Base):
    def __init__(self, BrokerID='', UserID='', BrokerFunctionCode=''):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.BrokerFunctionCode = BrokerFunctionCode


class TraderOfferField(Base):
    def __init__(self, ExchangeID='', TraderID='', ParticipantID='', Password='', InstallID='', OrderLocalID='',
                 TraderConnectStatus='', ConnectRequestDate='', ConnectRequestTime='', LastReportDate='',
                 LastReportTime='', ConnectDate='', ConnectTime='', StartDate='', StartTime='', TradingDay='',
                 BrokerID='', MaxTradeID='', MaxOrderMessageReference=''):
        self.ExchangeID = ExchangeID
        self.TraderID = TraderID
        self.ParticipantID = ParticipantID
        self.Password = Password
        self.InstallID = int(InstallID)
        self.OrderLocalID = OrderLocalID
        self.TraderConnectStatus = TraderConnectStatus
        self.ConnectRequestDate = ConnectRequestDate
        self.ConnectRequestTime = ConnectRequestTime
        self.LastReportDate = LastReportDate
        self.LastReportTime = LastReportTime
        self.ConnectDate = ConnectDate
        self.ConnectTime = ConnectTime
        self.StartDate = StartDate
        self.StartTime = StartTime
        self.TradingDay = TradingDay
        self.BrokerID = BrokerID
        self.MaxTradeID = MaxTradeID
        self.MaxOrderMessageReference = MaxOrderMessageReference


class SettlementInfoField(Base):
    def __init__(self, TradingDay='', SettlementID='', BrokerID='', InvestorID='', SequenceNo='', Content=''):
        self.TradingDay = TradingDay
        self.SettlementID = int(SettlementID)
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.SequenceNo = int(SequenceNo)
        self.Content = Content


class InstrumentMarginRateAdjustField(Base):
    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', HedgeFlag='',
                 LongMarginRatioByMoney='', LongMarginRatioByVolume='', ShortMarginRatioByMoney='',
                 ShortMarginRatioByVolume='', IsRelative=''):
        self.InstrumentID = InstrumentID
        self.InvestorRange = InvestorRange
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.HedgeFlag = HedgeFlag
        self.LongMarginRatioByMoney = float(LongMarginRatioByMoney)
        self.LongMarginRatioByVolume = float(LongMarginRatioByVolume)
        self.ShortMarginRatioByMoney = float(ShortMarginRatioByMoney)
        self.ShortMarginRatioByVolume = float(ShortMarginRatioByVolume)
        self.IsRelative = int(IsRelative)


class ExchangeMarginRateField(Base):
    def __init__(self, BrokerID='', InstrumentID='', HedgeFlag='', LongMarginRatioByMoney='',
                 LongMarginRatioByVolume='', ShortMarginRatioByMoney='', ShortMarginRatioByVolume=''):
        self.BrokerID = BrokerID
        self.InstrumentID = InstrumentID
        self.HedgeFlag = HedgeFlag
        self.LongMarginRatioByMoney = float(LongMarginRatioByMoney)
        self.LongMarginRatioByVolume = float(LongMarginRatioByVolume)
        self.ShortMarginRatioByMoney = float(ShortMarginRatioByMoney)
        self.ShortMarginRatioByVolume = float(ShortMarginRatioByVolume)


class ExchangeMarginRateAdjustField(Base):
    def __init__(self, BrokerID='', InstrumentID='', HedgeFlag='', LongMarginRatioByMoney='',
                 LongMarginRatioByVolume='', ShortMarginRatioByMoney='', ShortMarginRatioByVolume='',
                 ExchLongMarginRatioByMoney='', ExchLongMarginRatioByVolume='', ExchShortMarginRatioByMoney='',
                 ExchShortMarginRatioByVolume='', NoLongMarginRatioByMoney='', NoLongMarginRatioByVolume='',
                 NoShortMarginRatioByMoney='', NoShortMarginRatioByVolume=''):
        self.BrokerID = BrokerID
        self.InstrumentID = InstrumentID
        self.HedgeFlag = HedgeFlag
        self.LongMarginRatioByMoney = float(LongMarginRatioByMoney)
        self.LongMarginRatioByVolume = float(LongMarginRatioByVolume)
        self.ShortMarginRatioByMoney = float(ShortMarginRatioByMoney)
        self.ShortMarginRatioByVolume = float(ShortMarginRatioByVolume)
        self.ExchLongMarginRatioByMoney = float(ExchLongMarginRatioByMoney)
        self.ExchLongMarginRatioByVolume = float(ExchLongMarginRatioByVolume)
        self.ExchShortMarginRatioByMoney = float(ExchShortMarginRatioByMoney)
        self.ExchShortMarginRatioByVolume = float(ExchShortMarginRatioByVolume)
        self.NoLongMarginRatioByMoney = float(NoLongMarginRatioByMoney)
        self.NoLongMarginRatioByVolume = float(NoLongMarginRatioByVolume)
        self.NoShortMarginRatioByMoney = float(NoShortMarginRatioByMoney)
        self.NoShortMarginRatioByVolume = float(NoShortMarginRatioByVolume)


class ExchangeRateField(Base):
    def __init__(self, BrokerID='', FromCurrencyID='', FromCurrencyUnit='', ToCurrencyID='', ExchangeRate=''):
        self.BrokerID = BrokerID
        self.FromCurrencyID = FromCurrencyID
        self.FromCurrencyUnit = float(FromCurrencyUnit)
        self.ToCurrencyID = ToCurrencyID
        self.ExchangeRate = float(ExchangeRate)


class SettlementRefField(Base):
    def __init__(self, TradingDay='', SettlementID=''):
        self.TradingDay = TradingDay
        self.SettlementID = int(SettlementID)


class CurrentTimeField(Base):
    def __init__(self, CurrDate='', CurrTime='', CurrMillisec='', ActionDay=''):
        self.CurrDate = CurrDate
        self.CurrTime = CurrTime
        self.CurrMillisec = int(CurrMillisec)
        self.ActionDay = ActionDay


class CommPhaseField(Base):
    def __init__(self, TradingDay='', CommPhaseNo='', SystemID=''):
        self.TradingDay = TradingDay
        self.CommPhaseNo = int(CommPhaseNo)
        self.SystemID = SystemID


class LoginInfoField(Base):
    def __init__(self, FrontID='', SessionID='', BrokerID='', UserID='', LoginDate='', LoginTime='', IPAddress='',
                 UserProductInfo='', InterfaceProductInfo='', ProtocolInfo='', SystemName='', Password='',
                 MaxOrderRef='', SHFETime='', DCETime='', CZCETime='', FFEXTime='', MacAddress='', OneTimePassword='',
                 INETime='', IsQryControl='', LoginRemark=''):
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.LoginDate = LoginDate
        self.LoginTime = LoginTime
        self.IPAddress = IPAddress
        self.UserProductInfo = UserProductInfo
        self.InterfaceProductInfo = InterfaceProductInfo
        self.ProtocolInfo = ProtocolInfo
        self.SystemName = SystemName
        self.Password = Password
        self.MaxOrderRef = MaxOrderRef
        self.SHFETime = SHFETime
        self.DCETime = DCETime
        self.CZCETime = CZCETime
        self.FFEXTime = FFEXTime
        self.MacAddress = MacAddress
        self.OneTimePassword = OneTimePassword
        self.INETime = INETime
        self.IsQryControl = int(IsQryControl)
        self.LoginRemark = LoginRemark


class LogoutAllField(Base):
    def __init__(self, FrontID='', SessionID='', SystemName=''):
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.SystemName = SystemName


class FrontStatusField(Base):
    def __init__(self, FrontID='', LastReportDate='', LastReportTime='', IsActive=''):
        self.FrontID = int(FrontID)
        self.LastReportDate = LastReportDate
        self.LastReportTime = LastReportTime
        self.IsActive = int(IsActive)


class UserPasswordUpdateField(Base):
    def __init__(self, BrokerID='', UserID='', OldPassword='', NewPassword=''):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.OldPassword = OldPassword
        self.NewPassword = NewPassword


class InputOrderField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', OrderRef='', UserID='', OrderPriceType='',
                 Direction='', CombOffsetFlag='', CombHedgeFlag='', LimitPrice='', VolumeTotalOriginal='',
                 TimeCondition='', GTDDate='', VolumeCondition='', MinVolume='', ContingentCondition='', StopPrice='',
                 ForceCloseReason='', IsAutoSuspend='', BusinessUnit='', RequestID='', UserForceClose='',
                 IsSwapOrder='', ExchangeID='', InvestUnitID='', AccountID='', CurrencyID='', ClientID='', IPAddress='',
                 MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.OrderRef = OrderRef
        self.UserID = UserID
        self.OrderPriceType = OrderPriceType
        self.Direction = Direction
        self.CombOffsetFlag = CombOffsetFlag
        self.CombHedgeFlag = CombHedgeFlag
        self.LimitPrice = float(LimitPrice)
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = TimeCondition
        self.GTDDate = GTDDate
        self.VolumeCondition = VolumeCondition
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = ContingentCondition
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = ForceCloseReason
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = BusinessUnit
        self.RequestID = int(RequestID)
        self.UserForceClose = int(UserForceClose)
        self.IsSwapOrder = int(IsSwapOrder)
        self.ExchangeID = ExchangeID
        self.InvestUnitID = InvestUnitID
        self.AccountID = AccountID
        self.CurrencyID = CurrencyID
        self.ClientID = ClientID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class OrderField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', OrderRef='', UserID='', OrderPriceType='',
                 Direction='', CombOffsetFlag='', CombHedgeFlag='', LimitPrice='', VolumeTotalOriginal='',
                 TimeCondition='', GTDDate='', VolumeCondition='', MinVolume='', ContingentCondition='', StopPrice='',
                 ForceCloseReason='', IsAutoSuspend='', BusinessUnit='', RequestID='', OrderLocalID='', ExchangeID='',
                 ParticipantID='', ClientID='', ExchangeInstID='', TraderID='', InstallID='', OrderSubmitStatus='',
                 NotifySequence='', TradingDay='', SettlementID='', OrderSysID='', OrderSource='', OrderStatus='',
                 OrderType='', VolumeTraded='', VolumeTotal='', InsertDate='', InsertTime='', ActiveTime='',
                 SuspendTime='', UpdateTime='', CancelTime='', ActiveTraderID='', ClearingPartID='', SequenceNo='',
                 FrontID='', SessionID='', UserProductInfo='', StatusMsg='', UserForceClose='', ActiveUserID='',
                 BrokerOrderSeq='', RelativeOrderSysID='', ZCETotalTradedVolume='', IsSwapOrder='', BranchID='',
                 InvestUnitID='', AccountID='', CurrencyID='', IPAddress='', MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.OrderRef = OrderRef
        self.UserID = UserID
        self.OrderPriceType = OrderPriceType
        self.Direction = Direction
        self.CombOffsetFlag = CombOffsetFlag
        self.CombHedgeFlag = CombHedgeFlag
        self.LimitPrice = float(LimitPrice)
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = TimeCondition
        self.GTDDate = GTDDate
        self.VolumeCondition = VolumeCondition
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = ContingentCondition
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = ForceCloseReason
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = BusinessUnit
        self.RequestID = int(RequestID)
        self.OrderLocalID = OrderLocalID
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeInstID = ExchangeInstID
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.OrderSubmitStatus = OrderSubmitStatus
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = TradingDay
        self.SettlementID = int(SettlementID)
        self.OrderSysID = OrderSysID
        self.OrderSource = OrderSource
        self.OrderStatus = OrderStatus
        self.OrderType = OrderType
        self.VolumeTraded = int(VolumeTraded)
        self.VolumeTotal = int(VolumeTotal)
        self.InsertDate = InsertDate
        self.InsertTime = InsertTime
        self.ActiveTime = ActiveTime
        self.SuspendTime = SuspendTime
        self.UpdateTime = UpdateTime
        self.CancelTime = CancelTime
        self.ActiveTraderID = ActiveTraderID
        self.ClearingPartID = ClearingPartID
        self.SequenceNo = int(SequenceNo)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.UserProductInfo = UserProductInfo
        self.StatusMsg = StatusMsg
        self.UserForceClose = int(UserForceClose)
        self.ActiveUserID = ActiveUserID
        self.BrokerOrderSeq = int(BrokerOrderSeq)
        self.RelativeOrderSysID = RelativeOrderSysID
        self.ZCETotalTradedVolume = int(ZCETotalTradedVolume)
        self.IsSwapOrder = int(IsSwapOrder)
        self.BranchID = BranchID
        self.InvestUnitID = InvestUnitID
        self.AccountID = AccountID
        self.CurrencyID = CurrencyID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class ExchangeOrderField(Base):
    def __init__(self, OrderPriceType='', Direction='', CombOffsetFlag='', CombHedgeFlag='', LimitPrice='',
                 VolumeTotalOriginal='', TimeCondition='', GTDDate='', VolumeCondition='', MinVolume='',
                 ContingentCondition='', StopPrice='', ForceCloseReason='', IsAutoSuspend='', BusinessUnit='',
                 RequestID='', OrderLocalID='', ExchangeID='', ParticipantID='', ClientID='', ExchangeInstID='',
                 TraderID='', InstallID='', OrderSubmitStatus='', NotifySequence='', TradingDay='', SettlementID='',
                 OrderSysID='', OrderSource='', OrderStatus='', OrderType='', VolumeTraded='', VolumeTotal='',
                 InsertDate='', InsertTime='', ActiveTime='', SuspendTime='', UpdateTime='', CancelTime='',
                 ActiveTraderID='', ClearingPartID='', SequenceNo='', BranchID='', IPAddress='', MacAddress=''):
        self.OrderPriceType = OrderPriceType
        self.Direction = Direction
        self.CombOffsetFlag = CombOffsetFlag
        self.CombHedgeFlag = CombHedgeFlag
        self.LimitPrice = float(LimitPrice)
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = TimeCondition
        self.GTDDate = GTDDate
        self.VolumeCondition = VolumeCondition
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = ContingentCondition
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = ForceCloseReason
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = BusinessUnit
        self.RequestID = int(RequestID)
        self.OrderLocalID = OrderLocalID
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeInstID = ExchangeInstID
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.OrderSubmitStatus = OrderSubmitStatus
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = TradingDay
        self.SettlementID = int(SettlementID)
        self.OrderSysID = OrderSysID
        self.OrderSource = OrderSource
        self.OrderStatus = OrderStatus
        self.OrderType = OrderType
        self.VolumeTraded = int(VolumeTraded)
        self.VolumeTotal = int(VolumeTotal)
        self.InsertDate = InsertDate
        self.InsertTime = InsertTime
        self.ActiveTime = ActiveTime
        self.SuspendTime = SuspendTime
        self.UpdateTime = UpdateTime
        self.CancelTime = CancelTime
        self.ActiveTraderID = ActiveTraderID
        self.ClearingPartID = ClearingPartID
        self.SequenceNo = int(SequenceNo)
        self.BranchID = BranchID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class ExchangeOrderInsertErrorField(Base):
    def __init__(self, ExchangeID='', ParticipantID='', TraderID='', InstallID='', OrderLocalID='', ErrorID='',
                 ErrorMsg=''):
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.OrderLocalID = OrderLocalID
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg


class InputOrderActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', OrderActionRef='', OrderRef='', RequestID='', FrontID='',
                 SessionID='', ExchangeID='', OrderSysID='', ActionFlag='', LimitPrice='', VolumeChange='', UserID='',
                 InstrumentID='', InvestUnitID='', IPAddress='', MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.OrderActionRef = int(OrderActionRef)
        self.OrderRef = OrderRef
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = ExchangeID
        self.OrderSysID = OrderSysID
        self.ActionFlag = ActionFlag
        self.LimitPrice = float(LimitPrice)
        self.VolumeChange = int(VolumeChange)
        self.UserID = UserID
        self.InstrumentID = InstrumentID
        self.InvestUnitID = InvestUnitID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class OrderActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', OrderActionRef='', OrderRef='', RequestID='', FrontID='',
                 SessionID='', ExchangeID='', OrderSysID='', ActionFlag='', LimitPrice='', VolumeChange='',
                 ActionDate='', ActionTime='', TraderID='', InstallID='', OrderLocalID='', ActionLocalID='',
                 ParticipantID='', ClientID='', BusinessUnit='', OrderActionStatus='', UserID='', StatusMsg='',
                 InstrumentID='', BranchID='', InvestUnitID='', IPAddress='', MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.OrderActionRef = int(OrderActionRef)
        self.OrderRef = OrderRef
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = ExchangeID
        self.OrderSysID = OrderSysID
        self.ActionFlag = ActionFlag
        self.LimitPrice = float(LimitPrice)
        self.VolumeChange = int(VolumeChange)
        self.ActionDate = ActionDate
        self.ActionTime = ActionTime
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.OrderLocalID = OrderLocalID
        self.ActionLocalID = ActionLocalID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.BusinessUnit = BusinessUnit
        self.OrderActionStatus = OrderActionStatus
        self.UserID = UserID
        self.StatusMsg = StatusMsg
        self.InstrumentID = InstrumentID
        self.BranchID = BranchID
        self.InvestUnitID = InvestUnitID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class ExchangeOrderActionField(Base):
    def __init__(self, ExchangeID='', OrderSysID='', ActionFlag='', LimitPrice='', VolumeChange='', ActionDate='',
                 ActionTime='', TraderID='', InstallID='', OrderLocalID='', ActionLocalID='', ParticipantID='',
                 ClientID='', BusinessUnit='', OrderActionStatus='', UserID='', BranchID='', IPAddress='',
                 MacAddress=''):
        self.ExchangeID = ExchangeID
        self.OrderSysID = OrderSysID
        self.ActionFlag = ActionFlag
        self.LimitPrice = float(LimitPrice)
        self.VolumeChange = int(VolumeChange)
        self.ActionDate = ActionDate
        self.ActionTime = ActionTime
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.OrderLocalID = OrderLocalID
        self.ActionLocalID = ActionLocalID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.BusinessUnit = BusinessUnit
        self.OrderActionStatus = OrderActionStatus
        self.UserID = UserID
        self.BranchID = BranchID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class ExchangeOrderActionErrorField(Base):
    def __init__(self, ExchangeID='', OrderSysID='', TraderID='', InstallID='', OrderLocalID='', ActionLocalID='',
                 ErrorID='', ErrorMsg=''):
        self.ExchangeID = ExchangeID
        self.OrderSysID = OrderSysID
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.OrderLocalID = OrderLocalID
        self.ActionLocalID = ActionLocalID
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg


class ExchangeTradeField(Base):
    def __init__(self, ExchangeID='', TradeID='', Direction='', OrderSysID='', ParticipantID='', ClientID='',
                 TradingRole='', ExchangeInstID='', OffsetFlag='', HedgeFlag='', Price='', Volume='', TradeDate='',
                 TradeTime='', TradeType='', PriceSource='', TraderID='', OrderLocalID='', ClearingPartID='',
                 BusinessUnit='', SequenceNo='', TradeSource=''):
        self.ExchangeID = ExchangeID
        self.TradeID = TradeID
        self.Direction = Direction
        self.OrderSysID = OrderSysID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.TradingRole = TradingRole
        self.ExchangeInstID = ExchangeInstID
        self.OffsetFlag = OffsetFlag
        self.HedgeFlag = HedgeFlag
        self.Price = float(Price)
        self.Volume = int(Volume)
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.TradeType = TradeType
        self.PriceSource = PriceSource
        self.TraderID = TraderID
        self.OrderLocalID = OrderLocalID
        self.ClearingPartID = ClearingPartID
        self.BusinessUnit = BusinessUnit
        self.SequenceNo = int(SequenceNo)
        self.TradeSource = TradeSource


class TradeField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', OrderRef='', UserID='', ExchangeID='', TradeID='',
                 Direction='', OrderSysID='', ParticipantID='', ClientID='', TradingRole='', ExchangeInstID='',
                 OffsetFlag='', HedgeFlag='', Price='', Volume='', TradeDate='', TradeTime='', TradeType='',
                 PriceSource='', TraderID='', OrderLocalID='', ClearingPartID='', BusinessUnit='', SequenceNo='',
                 TradingDay='', SettlementID='', BrokerOrderSeq='', TradeSource=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.OrderRef = OrderRef
        self.UserID = UserID
        self.ExchangeID = ExchangeID
        self.TradeID = TradeID
        self.Direction = Direction
        self.OrderSysID = OrderSysID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.TradingRole = TradingRole
        self.ExchangeInstID = ExchangeInstID
        self.OffsetFlag = OffsetFlag
        self.HedgeFlag = HedgeFlag
        self.Price = float(Price)
        self.Volume = int(Volume)
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.TradeType = TradeType
        self.PriceSource = PriceSource
        self.TraderID = TraderID
        self.OrderLocalID = OrderLocalID
        self.ClearingPartID = ClearingPartID
        self.BusinessUnit = BusinessUnit
        self.SequenceNo = int(SequenceNo)
        self.TradingDay = TradingDay
        self.SettlementID = int(SettlementID)
        self.BrokerOrderSeq = int(BrokerOrderSeq)
        self.TradeSource = TradeSource


class UserSessionField(Base):
    def __init__(self, FrontID='', SessionID='', BrokerID='', UserID='', LoginDate='', LoginTime='', IPAddress='',
                 UserProductInfo='', InterfaceProductInfo='', ProtocolInfo='', MacAddress='', LoginRemark=''):
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.LoginDate = LoginDate
        self.LoginTime = LoginTime
        self.IPAddress = IPAddress
        self.UserProductInfo = UserProductInfo
        self.InterfaceProductInfo = InterfaceProductInfo
        self.ProtocolInfo = ProtocolInfo
        self.MacAddress = MacAddress
        self.LoginRemark = LoginRemark


class QueryMaxOrderVolumeField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', Direction='', OffsetFlag='', HedgeFlag='',
                 MaxVolume=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.Direction = Direction
        self.OffsetFlag = OffsetFlag
        self.HedgeFlag = HedgeFlag
        self.MaxVolume = int(MaxVolume)


class SettlementInfoConfirmField(Base):
    def __init__(self, BrokerID='', InvestorID='', ConfirmDate='', ConfirmTime=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ConfirmDate = ConfirmDate
        self.ConfirmTime = ConfirmTime


class SyncDepositField(Base):
    def __init__(self, DepositSeqNo='', BrokerID='', InvestorID='', Deposit='', IsForce='', CurrencyID=''):
        self.DepositSeqNo = DepositSeqNo
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.Deposit = float(Deposit)
        self.IsForce = int(IsForce)
        self.CurrencyID = CurrencyID


class SyncFundMortgageField(Base):
    def __init__(self, MortgageSeqNo='', BrokerID='', InvestorID='', FromCurrencyID='', MortgageAmount='',
                 ToCurrencyID=''):
        self.MortgageSeqNo = MortgageSeqNo
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.FromCurrencyID = FromCurrencyID
        self.MortgageAmount = float(MortgageAmount)
        self.ToCurrencyID = ToCurrencyID


class BrokerSyncField(Base):
    def __init__(self, BrokerID=''):
        self.BrokerID = BrokerID


class SyncingInvestorField(Base):
    def __init__(self, InvestorID='', BrokerID='', InvestorGroupID='', InvestorName='', IdentifiedCardType='',
                 IdentifiedCardNo='', IsActive='', Telephone='', Address='', OpenDate='', Mobile='', CommModelID='',
                 MarginModelID=''):
        self.InvestorID = InvestorID
        self.BrokerID = BrokerID
        self.InvestorGroupID = InvestorGroupID
        self.InvestorName = InvestorName
        self.IdentifiedCardType = IdentifiedCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.IsActive = int(IsActive)
        self.Telephone = Telephone
        self.Address = Address
        self.OpenDate = OpenDate
        self.Mobile = Mobile
        self.CommModelID = CommModelID
        self.MarginModelID = MarginModelID


class SyncingTradingCodeField(Base):
    def __init__(self, InvestorID='', BrokerID='', ExchangeID='', ClientID='', IsActive='', ClientIDType=''):
        self.InvestorID = InvestorID
        self.BrokerID = BrokerID
        self.ExchangeID = ExchangeID
        self.ClientID = ClientID
        self.IsActive = int(IsActive)
        self.ClientIDType = ClientIDType


class SyncingInvestorGroupField(Base):
    def __init__(self, BrokerID='', InvestorGroupID='', InvestorGroupName=''):
        self.BrokerID = BrokerID
        self.InvestorGroupID = InvestorGroupID
        self.InvestorGroupName = InvestorGroupName


class SyncingTradingAccountField(Base):
    def __init__(self, BrokerID='', AccountID='', PreMortgage='', PreCredit='', PreDeposit='', PreBalance='',
                 PreMargin='', InterestBase='', Interest='', Deposit='', Withdraw='', FrozenMargin='', FrozenCash='',
                 FrozenCommission='', CurrMargin='', CashIn='', Commission='', CloseProfit='', PositionProfit='',
                 Balance='', Available='', WithdrawQuota='', Reserve='', TradingDay='', SettlementID='', Credit='',
                 Mortgage='', ExchangeMargin='', DeliveryMargin='', ExchangeDeliveryMargin='', ReserveBalance='',
                 CurrencyID='', PreFundMortgageIn='', PreFundMortgageOut='', FundMortgageIn='', FundMortgageOut='',
                 FundMortgageAvailable='', MortgageableFund='', SpecProductMargin='', SpecProductFrozenMargin='',
                 SpecProductCommission='', SpecProductFrozenCommission='', SpecProductPositionProfit='',
                 SpecProductCloseProfit='', SpecProductPositionProfitByAlg='', SpecProductExchangeMargin=''):
        self.BrokerID = BrokerID
        self.AccountID = AccountID
        self.PreMortgage = float(PreMortgage)
        self.PreCredit = float(PreCredit)
        self.PreDeposit = float(PreDeposit)
        self.PreBalance = float(PreBalance)
        self.PreMargin = float(PreMargin)
        self.InterestBase = float(InterestBase)
        self.Interest = float(Interest)
        self.Deposit = float(Deposit)
        self.Withdraw = float(Withdraw)
        self.FrozenMargin = float(FrozenMargin)
        self.FrozenCash = float(FrozenCash)
        self.FrozenCommission = float(FrozenCommission)
        self.CurrMargin = float(CurrMargin)
        self.CashIn = float(CashIn)
        self.Commission = float(Commission)
        self.CloseProfit = float(CloseProfit)
        self.PositionProfit = float(PositionProfit)
        self.Balance = float(Balance)
        self.Available = float(Available)
        self.WithdrawQuota = float(WithdrawQuota)
        self.Reserve = float(Reserve)
        self.TradingDay = TradingDay
        self.SettlementID = int(SettlementID)
        self.Credit = float(Credit)
        self.Mortgage = float(Mortgage)
        self.ExchangeMargin = float(ExchangeMargin)
        self.DeliveryMargin = float(DeliveryMargin)
        self.ExchangeDeliveryMargin = float(ExchangeDeliveryMargin)
        self.ReserveBalance = float(ReserveBalance)
        self.CurrencyID = CurrencyID
        self.PreFundMortgageIn = float(PreFundMortgageIn)
        self.PreFundMortgageOut = float(PreFundMortgageOut)
        self.FundMortgageIn = float(FundMortgageIn)
        self.FundMortgageOut = float(FundMortgageOut)
        self.FundMortgageAvailable = float(FundMortgageAvailable)
        self.MortgageableFund = float(MortgageableFund)
        self.SpecProductMargin = float(SpecProductMargin)
        self.SpecProductFrozenMargin = float(SpecProductFrozenMargin)
        self.SpecProductCommission = float(SpecProductCommission)
        self.SpecProductFrozenCommission = float(SpecProductFrozenCommission)
        self.SpecProductPositionProfit = float(SpecProductPositionProfit)
        self.SpecProductCloseProfit = float(SpecProductCloseProfit)
        self.SpecProductPositionProfitByAlg = float(SpecProductPositionProfitByAlg)
        self.SpecProductExchangeMargin = float(SpecProductExchangeMargin)


class SyncingInvestorPositionField(Base):
    def __init__(self, InstrumentID='', BrokerID='', InvestorID='', PosiDirection='', HedgeFlag='', PositionDate='',
                 YdPosition='', Position='', LongFrozen='', ShortFrozen='', LongFrozenAmount='', ShortFrozenAmount='',
                 OpenVolume='', CloseVolume='', OpenAmount='', CloseAmount='', PositionCost='', PreMargin='',
                 UseMargin='', FrozenMargin='', FrozenCash='', FrozenCommission='', CashIn='', Commission='',
                 CloseProfit='', PositionProfit='', PreSettlementPrice='', SettlementPrice='', TradingDay='',
                 SettlementID='', OpenCost='', ExchangeMargin='', CombPosition='', CombLongFrozen='',
                 CombShortFrozen='', CloseProfitByDate='', CloseProfitByTrade='', TodayPosition='',
                 MarginRateByMoney='', MarginRateByVolume='', StrikeFrozen='', StrikeFrozenAmount='', AbandonFrozen=''):
        self.InstrumentID = InstrumentID
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.PosiDirection = PosiDirection
        self.HedgeFlag = HedgeFlag
        self.PositionDate = PositionDate
        self.YdPosition = int(YdPosition)
        self.Position = int(Position)
        self.LongFrozen = int(LongFrozen)
        self.ShortFrozen = int(ShortFrozen)
        self.LongFrozenAmount = float(LongFrozenAmount)
        self.ShortFrozenAmount = float(ShortFrozenAmount)
        self.OpenVolume = int(OpenVolume)
        self.CloseVolume = int(CloseVolume)
        self.OpenAmount = float(OpenAmount)
        self.CloseAmount = float(CloseAmount)
        self.PositionCost = float(PositionCost)
        self.PreMargin = float(PreMargin)
        self.UseMargin = float(UseMargin)
        self.FrozenMargin = float(FrozenMargin)
        self.FrozenCash = float(FrozenCash)
        self.FrozenCommission = float(FrozenCommission)
        self.CashIn = float(CashIn)
        self.Commission = float(Commission)
        self.CloseProfit = float(CloseProfit)
        self.PositionProfit = float(PositionProfit)
        self.PreSettlementPrice = float(PreSettlementPrice)
        self.SettlementPrice = float(SettlementPrice)
        self.TradingDay = TradingDay
        self.SettlementID = int(SettlementID)
        self.OpenCost = float(OpenCost)
        self.ExchangeMargin = float(ExchangeMargin)
        self.CombPosition = int(CombPosition)
        self.CombLongFrozen = int(CombLongFrozen)
        self.CombShortFrozen = int(CombShortFrozen)
        self.CloseProfitByDate = float(CloseProfitByDate)
        self.CloseProfitByTrade = float(CloseProfitByTrade)
        self.TodayPosition = int(TodayPosition)
        self.MarginRateByMoney = float(MarginRateByMoney)
        self.MarginRateByVolume = float(MarginRateByVolume)
        self.StrikeFrozen = int(StrikeFrozen)
        self.StrikeFrozenAmount = float(StrikeFrozenAmount)
        self.AbandonFrozen = int(AbandonFrozen)


class SyncingInstrumentMarginRateField(Base):
    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', HedgeFlag='',
                 LongMarginRatioByMoney='', LongMarginRatioByVolume='', ShortMarginRatioByMoney='',
                 ShortMarginRatioByVolume='', IsRelative=''):
        self.InstrumentID = InstrumentID
        self.InvestorRange = InvestorRange
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.HedgeFlag = HedgeFlag
        self.LongMarginRatioByMoney = float(LongMarginRatioByMoney)
        self.LongMarginRatioByVolume = float(LongMarginRatioByVolume)
        self.ShortMarginRatioByMoney = float(ShortMarginRatioByMoney)
        self.ShortMarginRatioByVolume = float(ShortMarginRatioByVolume)
        self.IsRelative = int(IsRelative)


class SyncingInstrumentCommissionRateField(Base):
    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', OpenRatioByMoney='',
                 OpenRatioByVolume='', CloseRatioByMoney='', CloseRatioByVolume='', CloseTodayRatioByMoney='',
                 CloseTodayRatioByVolume=''):
        self.InstrumentID = InstrumentID
        self.InvestorRange = InvestorRange
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.OpenRatioByMoney = float(OpenRatioByMoney)
        self.OpenRatioByVolume = float(OpenRatioByVolume)
        self.CloseRatioByMoney = float(CloseRatioByMoney)
        self.CloseRatioByVolume = float(CloseRatioByVolume)
        self.CloseTodayRatioByMoney = float(CloseTodayRatioByMoney)
        self.CloseTodayRatioByVolume = float(CloseTodayRatioByVolume)


class SyncingInstrumentTradingRightField(Base):
    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', TradingRight=''):
        self.InstrumentID = InstrumentID
        self.InvestorRange = InvestorRange
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.TradingRight = TradingRight


class QryOrderField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID='', OrderSysID='', InsertTimeStart='',
                 InsertTimeEnd=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID
        self.OrderSysID = OrderSysID
        self.InsertTimeStart = InsertTimeStart
        self.InsertTimeEnd = InsertTimeEnd


class QryTradeField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID='', TradeID='', TradeTimeStart='',
                 TradeTimeEnd=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID
        self.TradeID = TradeID
        self.TradeTimeStart = TradeTimeStart
        self.TradeTimeEnd = TradeTimeEnd


class QryInvestorPositionField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID


class QryTradingAccountField(Base):
    def __init__(self, BrokerID='', InvestorID='', CurrencyID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.CurrencyID = CurrencyID


class QryInvestorField(Base):
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID


class QryTradingCodeField(Base):
    def __init__(self, BrokerID='', InvestorID='', ExchangeID='', ClientID='', ClientIDType=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExchangeID = ExchangeID
        self.ClientID = ClientID
        self.ClientIDType = ClientIDType


class QryInvestorGroupField(Base):
    def __init__(self, BrokerID=''):
        self.BrokerID = BrokerID


class QryInstrumentMarginRateField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', HedgeFlag=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.HedgeFlag = HedgeFlag


class QryInstrumentCommissionRateField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID


class QryInstrumentTradingRightField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID


class QryBrokerField(Base):
    def __init__(self, BrokerID=''):
        self.BrokerID = BrokerID


class QryTraderField(Base):
    def __init__(self, ExchangeID='', ParticipantID='', TraderID=''):
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.TraderID = TraderID


class QrySuperUserFunctionField(Base):
    def __init__(self, UserID=''):
        self.UserID = UserID


class QryUserSessionField(Base):
    def __init__(self, FrontID='', SessionID='', BrokerID='', UserID=''):
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.BrokerID = BrokerID
        self.UserID = UserID


class QryPartBrokerField(Base):
    def __init__(self, ExchangeID='', BrokerID='', ParticipantID=''):
        self.ExchangeID = ExchangeID
        self.BrokerID = BrokerID
        self.ParticipantID = ParticipantID


class QryFrontStatusField(Base):
    def __init__(self, FrontID=''):
        self.FrontID = int(FrontID)


class QryExchangeOrderField(Base):
    def __init__(self, ParticipantID='', ClientID='', ExchangeInstID='', ExchangeID='', TraderID=''):
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeInstID = ExchangeInstID
        self.ExchangeID = ExchangeID
        self.TraderID = TraderID


class QryOrderActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', ExchangeID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExchangeID = ExchangeID


class QryExchangeOrderActionField(Base):
    def __init__(self, ParticipantID='', ClientID='', ExchangeID='', TraderID=''):
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeID = ExchangeID
        self.TraderID = TraderID


class QrySuperUserField(Base):
    def __init__(self, UserID=''):
        self.UserID = UserID


class QryExchangeField(Base):
    def __init__(self, ExchangeID=''):
        self.ExchangeID = ExchangeID


class QryProductField(Base):
    def __init__(self, ProductID='', ProductClass=''):
        self.ProductID = ProductID
        self.ProductClass = ProductClass


class QryInstrumentField(Base):
    def __init__(self, InstrumentID='', ExchangeID='', ExchangeInstID='', ProductID=''):
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID
        self.ExchangeInstID = ExchangeInstID
        self.ProductID = ProductID


class QryDepthMarketDataField(Base):
    def __init__(self, InstrumentID=''):
        self.InstrumentID = InstrumentID


class QryBrokerUserField(Base):
    def __init__(self, BrokerID='', UserID=''):
        self.BrokerID = BrokerID
        self.UserID = UserID


class QryBrokerUserFunctionField(Base):
    def __init__(self, BrokerID='', UserID=''):
        self.BrokerID = BrokerID
        self.UserID = UserID


class QryTraderOfferField(Base):
    def __init__(self, ExchangeID='', ParticipantID='', TraderID=''):
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.TraderID = TraderID


class QrySyncDepositField(Base):
    def __init__(self, BrokerID='', DepositSeqNo=''):
        self.BrokerID = BrokerID
        self.DepositSeqNo = DepositSeqNo


class QrySettlementInfoField(Base):
    def __init__(self, BrokerID='', InvestorID='', TradingDay=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.TradingDay = TradingDay


class QryExchangeMarginRateField(Base):
    def __init__(self, BrokerID='', InstrumentID='', HedgeFlag=''):
        self.BrokerID = BrokerID
        self.InstrumentID = InstrumentID
        self.HedgeFlag = HedgeFlag


class QryExchangeMarginRateAdjustField(Base):
    def __init__(self, BrokerID='', InstrumentID='', HedgeFlag=''):
        self.BrokerID = BrokerID
        self.InstrumentID = InstrumentID
        self.HedgeFlag = HedgeFlag


class QryExchangeRateField(Base):
    def __init__(self, BrokerID='', FromCurrencyID='', ToCurrencyID=''):
        self.BrokerID = BrokerID
        self.FromCurrencyID = FromCurrencyID
        self.ToCurrencyID = ToCurrencyID


class QrySyncFundMortgageField(Base):
    def __init__(self, BrokerID='', MortgageSeqNo=''):
        self.BrokerID = BrokerID
        self.MortgageSeqNo = MortgageSeqNo


class QryHisOrderField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID='', OrderSysID='', InsertTimeStart='',
                 InsertTimeEnd='', TradingDay='', SettlementID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID
        self.OrderSysID = OrderSysID
        self.InsertTimeStart = InsertTimeStart
        self.InsertTimeEnd = InsertTimeEnd
        self.TradingDay = TradingDay
        self.SettlementID = int(SettlementID)


class OptionInstrMiniMarginField(Base):
    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', MinMargin='', ValueMethod='',
                 IsRelative=''):
        self.InstrumentID = InstrumentID
        self.InvestorRange = InvestorRange
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.MinMargin = float(MinMargin)
        self.ValueMethod = ValueMethod
        self.IsRelative = int(IsRelative)


class OptionInstrMarginAdjustField(Base):
    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', SShortMarginRatioByMoney='',
                 SShortMarginRatioByVolume='', HShortMarginRatioByMoney='', HShortMarginRatioByVolume='',
                 AShortMarginRatioByMoney='', AShortMarginRatioByVolume='', IsRelative='', MShortMarginRatioByMoney='',
                 MShortMarginRatioByVolume=''):
        self.InstrumentID = InstrumentID
        self.InvestorRange = InvestorRange
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.SShortMarginRatioByMoney = float(SShortMarginRatioByMoney)
        self.SShortMarginRatioByVolume = float(SShortMarginRatioByVolume)
        self.HShortMarginRatioByMoney = float(HShortMarginRatioByMoney)
        self.HShortMarginRatioByVolume = float(HShortMarginRatioByVolume)
        self.AShortMarginRatioByMoney = float(AShortMarginRatioByMoney)
        self.AShortMarginRatioByVolume = float(AShortMarginRatioByVolume)
        self.IsRelative = int(IsRelative)
        self.MShortMarginRatioByMoney = float(MShortMarginRatioByMoney)
        self.MShortMarginRatioByVolume = float(MShortMarginRatioByVolume)


class OptionInstrCommRateField(Base):
    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', OpenRatioByMoney='',
                 OpenRatioByVolume='', CloseRatioByMoney='', CloseRatioByVolume='', CloseTodayRatioByMoney='',
                 CloseTodayRatioByVolume='', StrikeRatioByMoney='', StrikeRatioByVolume=''):
        self.InstrumentID = InstrumentID
        self.InvestorRange = InvestorRange
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.OpenRatioByMoney = float(OpenRatioByMoney)
        self.OpenRatioByVolume = float(OpenRatioByVolume)
        self.CloseRatioByMoney = float(CloseRatioByMoney)
        self.CloseRatioByVolume = float(CloseRatioByVolume)
        self.CloseTodayRatioByMoney = float(CloseTodayRatioByMoney)
        self.CloseTodayRatioByVolume = float(CloseTodayRatioByVolume)
        self.StrikeRatioByMoney = float(StrikeRatioByMoney)
        self.StrikeRatioByVolume = float(StrikeRatioByVolume)


class OptionInstrTradeCostField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', HedgeFlag='', FixedMargin='', MiniMargin='',
                 Royalty='', ExchFixedMargin='', ExchMiniMargin=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.HedgeFlag = HedgeFlag
        self.FixedMargin = float(FixedMargin)
        self.MiniMargin = float(MiniMargin)
        self.Royalty = float(Royalty)
        self.ExchFixedMargin = float(ExchFixedMargin)
        self.ExchMiniMargin = float(ExchMiniMargin)


class QryOptionInstrTradeCostField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', HedgeFlag='', InputPrice='', UnderlyingPrice=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.HedgeFlag = HedgeFlag
        self.InputPrice = float(InputPrice)
        self.UnderlyingPrice = float(UnderlyingPrice)


class QryOptionInstrCommRateField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID


class IndexPriceField(Base):
    def __init__(self, BrokerID='', InstrumentID='', ClosePrice=''):
        self.BrokerID = BrokerID
        self.InstrumentID = InstrumentID
        self.ClosePrice = float(ClosePrice)


class InputExecOrderField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExecOrderRef='', UserID='', Volume='', RequestID='',
                 BusinessUnit='', OffsetFlag='', HedgeFlag='', ActionType='', PosiDirection='', ReservePositionFlag='',
                 CloseFlag='', ExchangeID='', InvestUnitID='', AccountID='', CurrencyID='', ClientID='', IPAddress='',
                 MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.ExecOrderRef = ExecOrderRef
        self.UserID = UserID
        self.Volume = int(Volume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = BusinessUnit
        self.OffsetFlag = OffsetFlag
        self.HedgeFlag = HedgeFlag
        self.ActionType = ActionType
        self.PosiDirection = PosiDirection
        self.ReservePositionFlag = ReservePositionFlag
        self.CloseFlag = CloseFlag
        self.ExchangeID = ExchangeID
        self.InvestUnitID = InvestUnitID
        self.AccountID = AccountID
        self.CurrencyID = CurrencyID
        self.ClientID = ClientID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class InputExecOrderActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', ExecOrderActionRef='', ExecOrderRef='', RequestID='', FrontID='',
                 SessionID='', ExchangeID='', ExecOrderSysID='', ActionFlag='', UserID='', InstrumentID='',
                 InvestUnitID='', IPAddress='', MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExecOrderActionRef = int(ExecOrderActionRef)
        self.ExecOrderRef = ExecOrderRef
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = ExchangeID
        self.ExecOrderSysID = ExecOrderSysID
        self.ActionFlag = ActionFlag
        self.UserID = UserID
        self.InstrumentID = InstrumentID
        self.InvestUnitID = InvestUnitID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class ExecOrderField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExecOrderRef='', UserID='', Volume='', RequestID='',
                 BusinessUnit='', OffsetFlag='', HedgeFlag='', ActionType='', PosiDirection='', ReservePositionFlag='',
                 CloseFlag='', ExecOrderLocalID='', ExchangeID='', ParticipantID='', ClientID='', ExchangeInstID='',
                 TraderID='', InstallID='', OrderSubmitStatus='', NotifySequence='', TradingDay='', SettlementID='',
                 ExecOrderSysID='', InsertDate='', InsertTime='', CancelTime='', ExecResult='', ClearingPartID='',
                 SequenceNo='', FrontID='', SessionID='', UserProductInfo='', StatusMsg='', ActiveUserID='',
                 BrokerExecOrderSeq='', BranchID='', InvestUnitID='', AccountID='', CurrencyID='', IPAddress='',
                 MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.ExecOrderRef = ExecOrderRef
        self.UserID = UserID
        self.Volume = int(Volume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = BusinessUnit
        self.OffsetFlag = OffsetFlag
        self.HedgeFlag = HedgeFlag
        self.ActionType = ActionType
        self.PosiDirection = PosiDirection
        self.ReservePositionFlag = ReservePositionFlag
        self.CloseFlag = CloseFlag
        self.ExecOrderLocalID = ExecOrderLocalID
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeInstID = ExchangeInstID
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.OrderSubmitStatus = OrderSubmitStatus
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = TradingDay
        self.SettlementID = int(SettlementID)
        self.ExecOrderSysID = ExecOrderSysID
        self.InsertDate = InsertDate
        self.InsertTime = InsertTime
        self.CancelTime = CancelTime
        self.ExecResult = ExecResult
        self.ClearingPartID = ClearingPartID
        self.SequenceNo = int(SequenceNo)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.UserProductInfo = UserProductInfo
        self.StatusMsg = StatusMsg
        self.ActiveUserID = ActiveUserID
        self.BrokerExecOrderSeq = int(BrokerExecOrderSeq)
        self.BranchID = BranchID
        self.InvestUnitID = InvestUnitID
        self.AccountID = AccountID
        self.CurrencyID = CurrencyID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class ExecOrderActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', ExecOrderActionRef='', ExecOrderRef='', RequestID='', FrontID='',
                 SessionID='', ExchangeID='', ExecOrderSysID='', ActionFlag='', ActionDate='', ActionTime='',
                 TraderID='', InstallID='', ExecOrderLocalID='', ActionLocalID='', ParticipantID='', ClientID='',
                 BusinessUnit='', OrderActionStatus='', UserID='', ActionType='', StatusMsg='', InstrumentID='',
                 BranchID='', InvestUnitID='', IPAddress='', MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExecOrderActionRef = int(ExecOrderActionRef)
        self.ExecOrderRef = ExecOrderRef
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = ExchangeID
        self.ExecOrderSysID = ExecOrderSysID
        self.ActionFlag = ActionFlag
        self.ActionDate = ActionDate
        self.ActionTime = ActionTime
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.ExecOrderLocalID = ExecOrderLocalID
        self.ActionLocalID = ActionLocalID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.BusinessUnit = BusinessUnit
        self.OrderActionStatus = OrderActionStatus
        self.UserID = UserID
        self.ActionType = ActionType
        self.StatusMsg = StatusMsg
        self.InstrumentID = InstrumentID
        self.BranchID = BranchID
        self.InvestUnitID = InvestUnitID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class QryExecOrderField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID='', ExecOrderSysID='',
                 InsertTimeStart='', InsertTimeEnd=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID
        self.ExecOrderSysID = ExecOrderSysID
        self.InsertTimeStart = InsertTimeStart
        self.InsertTimeEnd = InsertTimeEnd


class ExchangeExecOrderField(Base):
    def __init__(self, Volume='', RequestID='', BusinessUnit='', OffsetFlag='', HedgeFlag='', ActionType='',
                 PosiDirection='', ReservePositionFlag='', CloseFlag='', ExecOrderLocalID='', ExchangeID='',
                 ParticipantID='', ClientID='', ExchangeInstID='', TraderID='', InstallID='', OrderSubmitStatus='',
                 NotifySequence='', TradingDay='', SettlementID='', ExecOrderSysID='', InsertDate='', InsertTime='',
                 CancelTime='', ExecResult='', ClearingPartID='', SequenceNo='', BranchID='', IPAddress='',
                 MacAddress=''):
        self.Volume = int(Volume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = BusinessUnit
        self.OffsetFlag = OffsetFlag
        self.HedgeFlag = HedgeFlag
        self.ActionType = ActionType
        self.PosiDirection = PosiDirection
        self.ReservePositionFlag = ReservePositionFlag
        self.CloseFlag = CloseFlag
        self.ExecOrderLocalID = ExecOrderLocalID
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeInstID = ExchangeInstID
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.OrderSubmitStatus = OrderSubmitStatus
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = TradingDay
        self.SettlementID = int(SettlementID)
        self.ExecOrderSysID = ExecOrderSysID
        self.InsertDate = InsertDate
        self.InsertTime = InsertTime
        self.CancelTime = CancelTime
        self.ExecResult = ExecResult
        self.ClearingPartID = ClearingPartID
        self.SequenceNo = int(SequenceNo)
        self.BranchID = BranchID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class QryExchangeExecOrderField(Base):
    def __init__(self, ParticipantID='', ClientID='', ExchangeInstID='', ExchangeID='', TraderID=''):
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeInstID = ExchangeInstID
        self.ExchangeID = ExchangeID
        self.TraderID = TraderID


class QryExecOrderActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', ExchangeID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExchangeID = ExchangeID


class ExchangeExecOrderActionField(Base):
    def __init__(self, ExchangeID='', ExecOrderSysID='', ActionFlag='', ActionDate='', ActionTime='', TraderID='',
                 InstallID='', ExecOrderLocalID='', ActionLocalID='', ParticipantID='', ClientID='', BusinessUnit='',
                 OrderActionStatus='', UserID='', ActionType='', BranchID='', IPAddress='', MacAddress=''):
        self.ExchangeID = ExchangeID
        self.ExecOrderSysID = ExecOrderSysID
        self.ActionFlag = ActionFlag
        self.ActionDate = ActionDate
        self.ActionTime = ActionTime
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.ExecOrderLocalID = ExecOrderLocalID
        self.ActionLocalID = ActionLocalID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.BusinessUnit = BusinessUnit
        self.OrderActionStatus = OrderActionStatus
        self.UserID = UserID
        self.ActionType = ActionType
        self.BranchID = BranchID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class QryExchangeExecOrderActionField(Base):
    def __init__(self, ParticipantID='', ClientID='', ExchangeID='', TraderID=''):
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeID = ExchangeID
        self.TraderID = TraderID


class ErrExecOrderField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExecOrderRef='', UserID='', Volume='', RequestID='',
                 BusinessUnit='', OffsetFlag='', HedgeFlag='', ActionType='', PosiDirection='', ReservePositionFlag='',
                 CloseFlag='', ExchangeID='', InvestUnitID='', AccountID='', CurrencyID='', ClientID='', IPAddress='',
                 MacAddress='', ErrorID='', ErrorMsg=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.ExecOrderRef = ExecOrderRef
        self.UserID = UserID
        self.Volume = int(Volume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = BusinessUnit
        self.OffsetFlag = OffsetFlag
        self.HedgeFlag = HedgeFlag
        self.ActionType = ActionType
        self.PosiDirection = PosiDirection
        self.ReservePositionFlag = ReservePositionFlag
        self.CloseFlag = CloseFlag
        self.ExchangeID = ExchangeID
        self.InvestUnitID = InvestUnitID
        self.AccountID = AccountID
        self.CurrencyID = CurrencyID
        self.ClientID = ClientID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg


class QryErrExecOrderField(Base):
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID


class ErrExecOrderActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', ExecOrderActionRef='', ExecOrderRef='', RequestID='', FrontID='',
                 SessionID='', ExchangeID='', ExecOrderSysID='', ActionFlag='', UserID='', InstrumentID='',
                 InvestUnitID='', IPAddress='', MacAddress='', ErrorID='', ErrorMsg=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExecOrderActionRef = int(ExecOrderActionRef)
        self.ExecOrderRef = ExecOrderRef
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = ExchangeID
        self.ExecOrderSysID = ExecOrderSysID
        self.ActionFlag = ActionFlag
        self.UserID = UserID
        self.InstrumentID = InstrumentID
        self.InvestUnitID = InvestUnitID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg


class QryErrExecOrderActionField(Base):
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID


class OptionInstrTradingRightField(Base):
    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', Direction='', TradingRight=''):
        self.InstrumentID = InstrumentID
        self.InvestorRange = InvestorRange
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.Direction = Direction
        self.TradingRight = TradingRight


class QryOptionInstrTradingRightField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', Direction=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.Direction = Direction


class InputForQuoteField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ForQuoteRef='', UserID='', ExchangeID='',
                 InvestUnitID='', IPAddress='', MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.ForQuoteRef = ForQuoteRef
        self.UserID = UserID
        self.ExchangeID = ExchangeID
        self.InvestUnitID = InvestUnitID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class ForQuoteField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ForQuoteRef='', UserID='', ForQuoteLocalID='',
                 ExchangeID='', ParticipantID='', ClientID='', ExchangeInstID='', TraderID='', InstallID='',
                 InsertDate='', InsertTime='', ForQuoteStatus='', FrontID='', SessionID='', StatusMsg='',
                 ActiveUserID='', BrokerForQutoSeq='', InvestUnitID='', IPAddress='', MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.ForQuoteRef = ForQuoteRef
        self.UserID = UserID
        self.ForQuoteLocalID = ForQuoteLocalID
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeInstID = ExchangeInstID
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.InsertDate = InsertDate
        self.InsertTime = InsertTime
        self.ForQuoteStatus = ForQuoteStatus
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.StatusMsg = StatusMsg
        self.ActiveUserID = ActiveUserID
        self.BrokerForQutoSeq = int(BrokerForQutoSeq)
        self.InvestUnitID = InvestUnitID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class QryForQuoteField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID='', InsertTimeStart='',
                 InsertTimeEnd=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID
        self.InsertTimeStart = InsertTimeStart
        self.InsertTimeEnd = InsertTimeEnd


class ExchangeForQuoteField(Base):
    def __init__(self, ForQuoteLocalID='', ExchangeID='', ParticipantID='', ClientID='', ExchangeInstID='', TraderID='',
                 InstallID='', InsertDate='', InsertTime='', ForQuoteStatus='', IPAddress='', MacAddress=''):
        self.ForQuoteLocalID = ForQuoteLocalID
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeInstID = ExchangeInstID
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.InsertDate = InsertDate
        self.InsertTime = InsertTime
        self.ForQuoteStatus = ForQuoteStatus
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class QryExchangeForQuoteField(Base):
    def __init__(self, ParticipantID='', ClientID='', ExchangeInstID='', ExchangeID='', TraderID=''):
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeInstID = ExchangeInstID
        self.ExchangeID = ExchangeID
        self.TraderID = TraderID


class InputQuoteField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', QuoteRef='', UserID='', AskPrice='', BidPrice='',
                 AskVolume='', BidVolume='', RequestID='', BusinessUnit='', AskOffsetFlag='', BidOffsetFlag='',
                 AskHedgeFlag='', BidHedgeFlag='', AskOrderRef='', BidOrderRef='', ForQuoteSysID='', ExchangeID='',
                 InvestUnitID='', ClientID='', IPAddress='', MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.QuoteRef = QuoteRef
        self.UserID = UserID
        self.AskPrice = float(AskPrice)
        self.BidPrice = float(BidPrice)
        self.AskVolume = int(AskVolume)
        self.BidVolume = int(BidVolume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = BusinessUnit
        self.AskOffsetFlag = AskOffsetFlag
        self.BidOffsetFlag = BidOffsetFlag
        self.AskHedgeFlag = AskHedgeFlag
        self.BidHedgeFlag = BidHedgeFlag
        self.AskOrderRef = AskOrderRef
        self.BidOrderRef = BidOrderRef
        self.ForQuoteSysID = ForQuoteSysID
        self.ExchangeID = ExchangeID
        self.InvestUnitID = InvestUnitID
        self.ClientID = ClientID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class InputQuoteActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', QuoteActionRef='', QuoteRef='', RequestID='', FrontID='',
                 SessionID='', ExchangeID='', QuoteSysID='', ActionFlag='', UserID='', InstrumentID='', InvestUnitID='',
                 ClientID='', IPAddress='', MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.QuoteActionRef = int(QuoteActionRef)
        self.QuoteRef = QuoteRef
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = ExchangeID
        self.QuoteSysID = QuoteSysID
        self.ActionFlag = ActionFlag
        self.UserID = UserID
        self.InstrumentID = InstrumentID
        self.InvestUnitID = InvestUnitID
        self.ClientID = ClientID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class QuoteField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', QuoteRef='', UserID='', AskPrice='', BidPrice='',
                 AskVolume='', BidVolume='', RequestID='', BusinessUnit='', AskOffsetFlag='', BidOffsetFlag='',
                 AskHedgeFlag='', BidHedgeFlag='', QuoteLocalID='', ExchangeID='', ParticipantID='', ClientID='',
                 ExchangeInstID='', TraderID='', InstallID='', NotifySequence='', OrderSubmitStatus='', TradingDay='',
                 SettlementID='', QuoteSysID='', InsertDate='', InsertTime='', CancelTime='', QuoteStatus='',
                 ClearingPartID='', SequenceNo='', AskOrderSysID='', BidOrderSysID='', FrontID='', SessionID='',
                 UserProductInfo='', StatusMsg='', ActiveUserID='', BrokerQuoteSeq='', AskOrderRef='', BidOrderRef='',
                 ForQuoteSysID='', BranchID='', InvestUnitID='', AccountID='', CurrencyID='', IPAddress='',
                 MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.QuoteRef = QuoteRef
        self.UserID = UserID
        self.AskPrice = float(AskPrice)
        self.BidPrice = float(BidPrice)
        self.AskVolume = int(AskVolume)
        self.BidVolume = int(BidVolume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = BusinessUnit
        self.AskOffsetFlag = AskOffsetFlag
        self.BidOffsetFlag = BidOffsetFlag
        self.AskHedgeFlag = AskHedgeFlag
        self.BidHedgeFlag = BidHedgeFlag
        self.QuoteLocalID = QuoteLocalID
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeInstID = ExchangeInstID
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.NotifySequence = int(NotifySequence)
        self.OrderSubmitStatus = OrderSubmitStatus
        self.TradingDay = TradingDay
        self.SettlementID = int(SettlementID)
        self.QuoteSysID = QuoteSysID
        self.InsertDate = InsertDate
        self.InsertTime = InsertTime
        self.CancelTime = CancelTime
        self.QuoteStatus = QuoteStatus
        self.ClearingPartID = ClearingPartID
        self.SequenceNo = int(SequenceNo)
        self.AskOrderSysID = AskOrderSysID
        self.BidOrderSysID = BidOrderSysID
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.UserProductInfo = UserProductInfo
        self.StatusMsg = StatusMsg
        self.ActiveUserID = ActiveUserID
        self.BrokerQuoteSeq = int(BrokerQuoteSeq)
        self.AskOrderRef = AskOrderRef
        self.BidOrderRef = BidOrderRef
        self.ForQuoteSysID = ForQuoteSysID
        self.BranchID = BranchID
        self.InvestUnitID = InvestUnitID
        self.AccountID = AccountID
        self.CurrencyID = CurrencyID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class QuoteActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', QuoteActionRef='', QuoteRef='', RequestID='', FrontID='',
                 SessionID='', ExchangeID='', QuoteSysID='', ActionFlag='', ActionDate='', ActionTime='', TraderID='',
                 InstallID='', QuoteLocalID='', ActionLocalID='', ParticipantID='', ClientID='', BusinessUnit='',
                 OrderActionStatus='', UserID='', StatusMsg='', InstrumentID='', BranchID='', InvestUnitID='',
                 IPAddress='', MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.QuoteActionRef = int(QuoteActionRef)
        self.QuoteRef = QuoteRef
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = ExchangeID
        self.QuoteSysID = QuoteSysID
        self.ActionFlag = ActionFlag
        self.ActionDate = ActionDate
        self.ActionTime = ActionTime
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.QuoteLocalID = QuoteLocalID
        self.ActionLocalID = ActionLocalID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.BusinessUnit = BusinessUnit
        self.OrderActionStatus = OrderActionStatus
        self.UserID = UserID
        self.StatusMsg = StatusMsg
        self.InstrumentID = InstrumentID
        self.BranchID = BranchID
        self.InvestUnitID = InvestUnitID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class QryQuoteField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID='', QuoteSysID='', InsertTimeStart='',
                 InsertTimeEnd=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID
        self.QuoteSysID = QuoteSysID
        self.InsertTimeStart = InsertTimeStart
        self.InsertTimeEnd = InsertTimeEnd


class ExchangeQuoteField(Base):
    def __init__(self, AskPrice='', BidPrice='', AskVolume='', BidVolume='', RequestID='', BusinessUnit='',
                 AskOffsetFlag='', BidOffsetFlag='', AskHedgeFlag='', BidHedgeFlag='', QuoteLocalID='', ExchangeID='',
                 ParticipantID='', ClientID='', ExchangeInstID='', TraderID='', InstallID='', NotifySequence='',
                 OrderSubmitStatus='', TradingDay='', SettlementID='', QuoteSysID='', InsertDate='', InsertTime='',
                 CancelTime='', QuoteStatus='', ClearingPartID='', SequenceNo='', AskOrderSysID='', BidOrderSysID='',
                 ForQuoteSysID='', BranchID='', IPAddress='', MacAddress=''):
        self.AskPrice = float(AskPrice)
        self.BidPrice = float(BidPrice)
        self.AskVolume = int(AskVolume)
        self.BidVolume = int(BidVolume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = BusinessUnit
        self.AskOffsetFlag = AskOffsetFlag
        self.BidOffsetFlag = BidOffsetFlag
        self.AskHedgeFlag = AskHedgeFlag
        self.BidHedgeFlag = BidHedgeFlag
        self.QuoteLocalID = QuoteLocalID
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeInstID = ExchangeInstID
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.NotifySequence = int(NotifySequence)
        self.OrderSubmitStatus = OrderSubmitStatus
        self.TradingDay = TradingDay
        self.SettlementID = int(SettlementID)
        self.QuoteSysID = QuoteSysID
        self.InsertDate = InsertDate
        self.InsertTime = InsertTime
        self.CancelTime = CancelTime
        self.QuoteStatus = QuoteStatus
        self.ClearingPartID = ClearingPartID
        self.SequenceNo = int(SequenceNo)
        self.AskOrderSysID = AskOrderSysID
        self.BidOrderSysID = BidOrderSysID
        self.ForQuoteSysID = ForQuoteSysID
        self.BranchID = BranchID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class QryExchangeQuoteField(Base):
    def __init__(self, ParticipantID='', ClientID='', ExchangeInstID='', ExchangeID='', TraderID=''):
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeInstID = ExchangeInstID
        self.ExchangeID = ExchangeID
        self.TraderID = TraderID


class QryQuoteActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', ExchangeID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExchangeID = ExchangeID


class ExchangeQuoteActionField(Base):
    def __init__(self, ExchangeID='', QuoteSysID='', ActionFlag='', ActionDate='', ActionTime='', TraderID='',
                 InstallID='', QuoteLocalID='', ActionLocalID='', ParticipantID='', ClientID='', BusinessUnit='',
                 OrderActionStatus='', UserID='', IPAddress='', MacAddress=''):
        self.ExchangeID = ExchangeID
        self.QuoteSysID = QuoteSysID
        self.ActionFlag = ActionFlag
        self.ActionDate = ActionDate
        self.ActionTime = ActionTime
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.QuoteLocalID = QuoteLocalID
        self.ActionLocalID = ActionLocalID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.BusinessUnit = BusinessUnit
        self.OrderActionStatus = OrderActionStatus
        self.UserID = UserID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class QryExchangeQuoteActionField(Base):
    def __init__(self, ParticipantID='', ClientID='', ExchangeID='', TraderID=''):
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeID = ExchangeID
        self.TraderID = TraderID


class OptionInstrDeltaField(Base):
    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', Delta=''):
        self.InstrumentID = InstrumentID
        self.InvestorRange = InvestorRange
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.Delta = float(Delta)


class ForQuoteRspField(Base):
    def __init__(self, TradingDay='', InstrumentID='', ForQuoteSysID='', ForQuoteTime='', ActionDay='', ExchangeID=''):
        self.TradingDay = TradingDay
        self.InstrumentID = InstrumentID
        self.ForQuoteSysID = ForQuoteSysID
        self.ForQuoteTime = ForQuoteTime
        self.ActionDay = ActionDay
        self.ExchangeID = ExchangeID


class StrikeOffsetField(Base):
    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', Offset='', OffsetType=''):
        self.InstrumentID = InstrumentID
        self.InvestorRange = InvestorRange
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.Offset = float(Offset)
        self.OffsetType = OffsetType


class QryStrikeOffsetField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID


class InputBatchOrderActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', OrderActionRef='', RequestID='', FrontID='', SessionID='',
                 ExchangeID='', UserID='', InvestUnitID='', IPAddress='', MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.OrderActionRef = int(OrderActionRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = ExchangeID
        self.UserID = UserID
        self.InvestUnitID = InvestUnitID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class BatchOrderActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', OrderActionRef='', RequestID='', FrontID='', SessionID='',
                 ExchangeID='', ActionDate='', ActionTime='', TraderID='', InstallID='', ActionLocalID='',
                 ParticipantID='', ClientID='', BusinessUnit='', OrderActionStatus='', UserID='', StatusMsg='',
                 InvestUnitID='', IPAddress='', MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.OrderActionRef = int(OrderActionRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = ExchangeID
        self.ActionDate = ActionDate
        self.ActionTime = ActionTime
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.ActionLocalID = ActionLocalID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.BusinessUnit = BusinessUnit
        self.OrderActionStatus = OrderActionStatus
        self.UserID = UserID
        self.StatusMsg = StatusMsg
        self.InvestUnitID = InvestUnitID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class ExchangeBatchOrderActionField(Base):
    def __init__(self, ExchangeID='', ActionDate='', ActionTime='', TraderID='', InstallID='', ActionLocalID='',
                 ParticipantID='', ClientID='', BusinessUnit='', OrderActionStatus='', UserID='', IPAddress='',
                 MacAddress=''):
        self.ExchangeID = ExchangeID
        self.ActionDate = ActionDate
        self.ActionTime = ActionTime
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.ActionLocalID = ActionLocalID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.BusinessUnit = BusinessUnit
        self.OrderActionStatus = OrderActionStatus
        self.UserID = UserID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class QryBatchOrderActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', ExchangeID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExchangeID = ExchangeID


class CombInstrumentGuardField(Base):
    def __init__(self, BrokerID='', InstrumentID='', GuarantRatio=''):
        self.BrokerID = BrokerID
        self.InstrumentID = InstrumentID
        self.GuarantRatio = float(GuarantRatio)


class QryCombInstrumentGuardField(Base):
    def __init__(self, BrokerID='', InstrumentID=''):
        self.BrokerID = BrokerID
        self.InstrumentID = InstrumentID


class InputCombActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', CombActionRef='', UserID='', Direction='',
                 Volume='', CombDirection='', HedgeFlag='', ExchangeID='', IPAddress='', MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.CombActionRef = CombActionRef
        self.UserID = UserID
        self.Direction = Direction
        self.Volume = int(Volume)
        self.CombDirection = CombDirection
        self.HedgeFlag = HedgeFlag
        self.ExchangeID = ExchangeID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class CombActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', CombActionRef='', UserID='', Direction='',
                 Volume='', CombDirection='', HedgeFlag='', ActionLocalID='', ExchangeID='', ParticipantID='',
                 ClientID='', ExchangeInstID='', TraderID='', InstallID='', ActionStatus='', NotifySequence='',
                 TradingDay='', SettlementID='', SequenceNo='', FrontID='', SessionID='', UserProductInfo='',
                 StatusMsg='', IPAddress='', MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.CombActionRef = CombActionRef
        self.UserID = UserID
        self.Direction = Direction
        self.Volume = int(Volume)
        self.CombDirection = CombDirection
        self.HedgeFlag = HedgeFlag
        self.ActionLocalID = ActionLocalID
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeInstID = ExchangeInstID
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.ActionStatus = ActionStatus
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = TradingDay
        self.SettlementID = int(SettlementID)
        self.SequenceNo = int(SequenceNo)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.UserProductInfo = UserProductInfo
        self.StatusMsg = StatusMsg
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class QryCombActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID


class ExchangeCombActionField(Base):
    def __init__(self, Direction='', Volume='', CombDirection='', HedgeFlag='', ActionLocalID='', ExchangeID='',
                 ParticipantID='', ClientID='', ExchangeInstID='', TraderID='', InstallID='', ActionStatus='',
                 NotifySequence='', TradingDay='', SettlementID='', SequenceNo='', IPAddress='', MacAddress=''):
        self.Direction = Direction
        self.Volume = int(Volume)
        self.CombDirection = CombDirection
        self.HedgeFlag = HedgeFlag
        self.ActionLocalID = ActionLocalID
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeInstID = ExchangeInstID
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.ActionStatus = ActionStatus
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = TradingDay
        self.SettlementID = int(SettlementID)
        self.SequenceNo = int(SequenceNo)
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class QryExchangeCombActionField(Base):
    def __init__(self, ParticipantID='', ClientID='', ExchangeInstID='', ExchangeID='', TraderID=''):
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeInstID = ExchangeInstID
        self.ExchangeID = ExchangeID
        self.TraderID = TraderID


class ProductExchRateField(Base):
    def __init__(self, ProductID='', QuoteCurrencyID='', ExchangeRate=''):
        self.ProductID = ProductID
        self.QuoteCurrencyID = QuoteCurrencyID
        self.ExchangeRate = float(ExchangeRate)


class QryProductExchRateField(Base):
    def __init__(self, ProductID=''):
        self.ProductID = ProductID


class QryForQuoteParamField(Base):
    def __init__(self, BrokerID='', InstrumentID='', ExchangeID=''):
        self.BrokerID = BrokerID
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID


class ForQuoteParamField(Base):
    def __init__(self, BrokerID='', InstrumentID='', ExchangeID='', LastPrice='', PriceInterval=''):
        self.BrokerID = BrokerID
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID
        self.LastPrice = float(LastPrice)
        self.PriceInterval = float(PriceInterval)


class MMOptionInstrCommRateField(Base):
    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', OpenRatioByMoney='',
                 OpenRatioByVolume='', CloseRatioByMoney='', CloseRatioByVolume='', CloseTodayRatioByMoney='',
                 CloseTodayRatioByVolume='', StrikeRatioByMoney='', StrikeRatioByVolume=''):
        self.InstrumentID = InstrumentID
        self.InvestorRange = InvestorRange
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.OpenRatioByMoney = float(OpenRatioByMoney)
        self.OpenRatioByVolume = float(OpenRatioByVolume)
        self.CloseRatioByMoney = float(CloseRatioByMoney)
        self.CloseRatioByVolume = float(CloseRatioByVolume)
        self.CloseTodayRatioByMoney = float(CloseTodayRatioByMoney)
        self.CloseTodayRatioByVolume = float(CloseTodayRatioByVolume)
        self.StrikeRatioByMoney = float(StrikeRatioByMoney)
        self.StrikeRatioByVolume = float(StrikeRatioByVolume)


class QryMMOptionInstrCommRateField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID


class MMInstrumentCommissionRateField(Base):
    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', OpenRatioByMoney='',
                 OpenRatioByVolume='', CloseRatioByMoney='', CloseRatioByVolume='', CloseTodayRatioByMoney='',
                 CloseTodayRatioByVolume=''):
        self.InstrumentID = InstrumentID
        self.InvestorRange = InvestorRange
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.OpenRatioByMoney = float(OpenRatioByMoney)
        self.OpenRatioByVolume = float(OpenRatioByVolume)
        self.CloseRatioByMoney = float(CloseRatioByMoney)
        self.CloseRatioByVolume = float(CloseRatioByVolume)
        self.CloseTodayRatioByMoney = float(CloseTodayRatioByMoney)
        self.CloseTodayRatioByVolume = float(CloseTodayRatioByVolume)


class QryMMInstrumentCommissionRateField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID


class InstrumentOrderCommRateField(Base):
    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', HedgeFlag='',
                 OrderCommByVolume='', OrderActionCommByVolume=''):
        self.InstrumentID = InstrumentID
        self.InvestorRange = InvestorRange
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.HedgeFlag = HedgeFlag
        self.OrderCommByVolume = float(OrderCommByVolume)
        self.OrderActionCommByVolume = float(OrderActionCommByVolume)


class QryInstrumentOrderCommRateField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID


class MarketDataField(Base):
    def __init__(self, TradingDay='', InstrumentID='', ExchangeID='', ExchangeInstID='', LastPrice='',
                 PreSettlementPrice='', PreClosePrice='', PreOpenInterest='', OpenPrice='', HighestPrice='',
                 LowestPrice='', Volume='', Turnover='', OpenInterest='', ClosePrice='', SettlementPrice='',
                 UpperLimitPrice='', LowerLimitPrice='', PreDelta='', CurrDelta='', UpdateTime='', UpdateMillisec='',
                 ActionDay=''):
        self.TradingDay = TradingDay
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID
        self.ExchangeInstID = ExchangeInstID
        self.LastPrice = float(LastPrice)
        self.PreSettlementPrice = float(PreSettlementPrice)
        self.PreClosePrice = float(PreClosePrice)
        self.PreOpenInterest = float(PreOpenInterest)
        self.OpenPrice = float(OpenPrice)
        self.HighestPrice = float(HighestPrice)
        self.LowestPrice = float(LowestPrice)
        self.Volume = int(Volume)
        self.Turnover = float(Turnover)
        self.OpenInterest = float(OpenInterest)
        self.ClosePrice = float(ClosePrice)
        self.SettlementPrice = float(SettlementPrice)
        self.UpperLimitPrice = float(UpperLimitPrice)
        self.LowerLimitPrice = float(LowerLimitPrice)
        self.PreDelta = float(PreDelta)
        self.CurrDelta = float(CurrDelta)
        self.UpdateTime = UpdateTime
        self.UpdateMillisec = int(UpdateMillisec)
        self.ActionDay = ActionDay


class MarketDataBaseField(Base):
    def __init__(self, TradingDay='', PreSettlementPrice='', PreClosePrice='', PreOpenInterest='', PreDelta=''):
        self.TradingDay = TradingDay
        self.PreSettlementPrice = float(PreSettlementPrice)
        self.PreClosePrice = float(PreClosePrice)
        self.PreOpenInterest = float(PreOpenInterest)
        self.PreDelta = float(PreDelta)


class MarketDataStaticField(Base):
    def __init__(self, OpenPrice='', HighestPrice='', LowestPrice='', ClosePrice='', UpperLimitPrice='',
                 LowerLimitPrice='', SettlementPrice='', CurrDelta=''):
        self.OpenPrice = float(OpenPrice)
        self.HighestPrice = float(HighestPrice)
        self.LowestPrice = float(LowestPrice)
        self.ClosePrice = float(ClosePrice)
        self.UpperLimitPrice = float(UpperLimitPrice)
        self.LowerLimitPrice = float(LowerLimitPrice)
        self.SettlementPrice = float(SettlementPrice)
        self.CurrDelta = float(CurrDelta)


class MarketDataLastMatchField(Base):
    def __init__(self, LastPrice='', Volume='', Turnover='', OpenInterest=''):
        self.LastPrice = float(LastPrice)
        self.Volume = int(Volume)
        self.Turnover = float(Turnover)
        self.OpenInterest = float(OpenInterest)


class MarketDataBestPriceField(Base):
    def __init__(self, BidPrice1='', BidVolume1='', AskPrice1='', AskVolume1=''):
        self.BidPrice1 = float(BidPrice1)
        self.BidVolume1 = int(BidVolume1)
        self.AskPrice1 = float(AskPrice1)
        self.AskVolume1 = int(AskVolume1)


class MarketDataBid23Field(Base):
    def __init__(self, BidPrice2='', BidVolume2='', BidPrice3='', BidVolume3=''):
        self.BidPrice2 = float(BidPrice2)
        self.BidVolume2 = int(BidVolume2)
        self.BidPrice3 = float(BidPrice3)
        self.BidVolume3 = int(BidVolume3)


class MarketDataAsk23Field(Base):
    def __init__(self, AskPrice2='', AskVolume2='', AskPrice3='', AskVolume3=''):
        self.AskPrice2 = float(AskPrice2)
        self.AskVolume2 = int(AskVolume2)
        self.AskPrice3 = float(AskPrice3)
        self.AskVolume3 = int(AskVolume3)


class MarketDataBid45Field(Base):
    def __init__(self, BidPrice4='', BidVolume4='', BidPrice5='', BidVolume5=''):
        self.BidPrice4 = float(BidPrice4)
        self.BidVolume4 = int(BidVolume4)
        self.BidPrice5 = float(BidPrice5)
        self.BidVolume5 = int(BidVolume5)


class MarketDataAsk45Field(Base):
    def __init__(self, AskPrice4='', AskVolume4='', AskPrice5='', AskVolume5=''):
        self.AskPrice4 = float(AskPrice4)
        self.AskVolume4 = int(AskVolume4)
        self.AskPrice5 = float(AskPrice5)
        self.AskVolume5 = int(AskVolume5)


class MarketDataUpdateTimeField(Base):
    def __init__(self, InstrumentID='', UpdateTime='', UpdateMillisec='', ActionDay=''):
        self.InstrumentID = InstrumentID
        self.UpdateTime = UpdateTime
        self.UpdateMillisec = int(UpdateMillisec)
        self.ActionDay = ActionDay


class MarketDataExchangeField(Base):
    def __init__(self, ExchangeID=''):
        self.ExchangeID = ExchangeID


class SpecificInstrumentField(Base):
    def __init__(self, InstrumentID=''):
        self.InstrumentID = InstrumentID


class InstrumentStatusField(Base):
    def __init__(self, ExchangeID='', ExchangeInstID='', SettlementGroupID='', InstrumentID='', InstrumentStatus='',
                 TradingSegmentSN='', EnterTime='', EnterReason=''):
        self.ExchangeID = ExchangeID
        self.ExchangeInstID = ExchangeInstID
        self.SettlementGroupID = SettlementGroupID
        self.InstrumentID = InstrumentID
        self.InstrumentStatus = InstrumentStatus
        self.TradingSegmentSN = int(TradingSegmentSN)
        self.EnterTime = EnterTime
        self.EnterReason = EnterReason


class QryInstrumentStatusField(Base):
    def __init__(self, ExchangeID='', ExchangeInstID=''):
        self.ExchangeID = ExchangeID
        self.ExchangeInstID = ExchangeInstID


class InvestorAccountField(Base):
    def __init__(self, BrokerID='', InvestorID='', AccountID='', CurrencyID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.AccountID = AccountID
        self.CurrencyID = CurrencyID


class PositionProfitAlgorithmField(Base):
    def __init__(self, BrokerID='', AccountID='', Algorithm='', Memo='', CurrencyID=''):
        self.BrokerID = BrokerID
        self.AccountID = AccountID
        self.Algorithm = Algorithm
        self.Memo = Memo
        self.CurrencyID = CurrencyID


class DiscountField(Base):
    def __init__(self, BrokerID='', InvestorRange='', InvestorID='', Discount=''):
        self.BrokerID = BrokerID
        self.InvestorRange = InvestorRange
        self.InvestorID = InvestorID
        self.Discount = float(Discount)


class QryTransferBankField(Base):
    def __init__(self, BankID='', BankBrchID=''):
        self.BankID = BankID
        self.BankBrchID = BankBrchID


class TransferBankField(Base):
    def __init__(self, BankID='', BankBrchID='', BankName='', IsActive=''):
        self.BankID = BankID
        self.BankBrchID = BankBrchID
        self.BankName = BankName
        self.IsActive = int(IsActive)


class QryInvestorPositionDetailField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID


class InvestorPositionDetailField(Base):
    def __init__(self, InstrumentID='', BrokerID='', InvestorID='', HedgeFlag='', Direction='', OpenDate='', TradeID='',
                 Volume='', OpenPrice='', TradingDay='', SettlementID='', TradeType='', CombInstrumentID='',
                 ExchangeID='', CloseProfitByDate='', CloseProfitByTrade='', PositionProfitByDate='',
                 PositionProfitByTrade='', Margin='', ExchMargin='', MarginRateByMoney='', MarginRateByVolume='',
                 LastSettlementPrice='', SettlementPrice='', CloseVolume='', CloseAmount=''):
        self.InstrumentID = InstrumentID
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.HedgeFlag = HedgeFlag
        self.Direction = Direction
        self.OpenDate = OpenDate
        self.TradeID = TradeID
        self.Volume = int(Volume)
        self.OpenPrice = float(OpenPrice)
        self.TradingDay = TradingDay
        self.SettlementID = int(SettlementID)
        self.TradeType = TradeType
        self.CombInstrumentID = CombInstrumentID
        self.ExchangeID = ExchangeID
        self.CloseProfitByDate = float(CloseProfitByDate)
        self.CloseProfitByTrade = float(CloseProfitByTrade)
        self.PositionProfitByDate = float(PositionProfitByDate)
        self.PositionProfitByTrade = float(PositionProfitByTrade)
        self.Margin = float(Margin)
        self.ExchMargin = float(ExchMargin)
        self.MarginRateByMoney = float(MarginRateByMoney)
        self.MarginRateByVolume = float(MarginRateByVolume)
        self.LastSettlementPrice = float(LastSettlementPrice)
        self.SettlementPrice = float(SettlementPrice)
        self.CloseVolume = int(CloseVolume)
        self.CloseAmount = float(CloseAmount)


class TradingAccountPasswordField(Base):
    def __init__(self, BrokerID='', AccountID='', Password='', CurrencyID=''):
        self.BrokerID = BrokerID
        self.AccountID = AccountID
        self.Password = Password
        self.CurrencyID = CurrencyID


class MDTraderOfferField(Base):
    def __init__(self, ExchangeID='', TraderID='', ParticipantID='', Password='', InstallID='', OrderLocalID='',
                 TraderConnectStatus='', ConnectRequestDate='', ConnectRequestTime='', LastReportDate='',
                 LastReportTime='', ConnectDate='', ConnectTime='', StartDate='', StartTime='', TradingDay='',
                 BrokerID='', MaxTradeID='', MaxOrderMessageReference=''):
        self.ExchangeID = ExchangeID
        self.TraderID = TraderID
        self.ParticipantID = ParticipantID
        self.Password = Password
        self.InstallID = int(InstallID)
        self.OrderLocalID = OrderLocalID
        self.TraderConnectStatus = TraderConnectStatus
        self.ConnectRequestDate = ConnectRequestDate
        self.ConnectRequestTime = ConnectRequestTime
        self.LastReportDate = LastReportDate
        self.LastReportTime = LastReportTime
        self.ConnectDate = ConnectDate
        self.ConnectTime = ConnectTime
        self.StartDate = StartDate
        self.StartTime = StartTime
        self.TradingDay = TradingDay
        self.BrokerID = BrokerID
        self.MaxTradeID = MaxTradeID
        self.MaxOrderMessageReference = MaxOrderMessageReference


class QryMDTraderOfferField(Base):
    def __init__(self, ExchangeID='', ParticipantID='', TraderID=''):
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.TraderID = TraderID


class QryNoticeField(Base):
    def __init__(self, BrokerID=''):
        self.BrokerID = BrokerID


class NoticeField(Base):
    def __init__(self, BrokerID='', Content='', SequenceLabel=''):
        self.BrokerID = BrokerID
        self.Content = Content
        self.SequenceLabel = SequenceLabel


class UserRightField(Base):
    def __init__(self, BrokerID='', UserID='', UserRightType='', IsForbidden=''):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.UserRightType = UserRightType
        self.IsForbidden = int(IsForbidden)


class QrySettlementInfoConfirmField(Base):
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID


class LoadSettlementInfoField(Base):
    def __init__(self, BrokerID=''):
        self.BrokerID = BrokerID


class BrokerWithdrawAlgorithmField(Base):
    def __init__(self, BrokerID='', WithdrawAlgorithm='', UsingRatio='', IncludeCloseProfit='', AllWithoutTrade='',
                 AvailIncludeCloseProfit='', IsBrokerUserEvent='', CurrencyID='', FundMortgageRatio='',
                 BalanceAlgorithm=''):
        self.BrokerID = BrokerID
        self.WithdrawAlgorithm = WithdrawAlgorithm
        self.UsingRatio = float(UsingRatio)
        self.IncludeCloseProfit = IncludeCloseProfit
        self.AllWithoutTrade = AllWithoutTrade
        self.AvailIncludeCloseProfit = AvailIncludeCloseProfit
        self.IsBrokerUserEvent = int(IsBrokerUserEvent)
        self.CurrencyID = CurrencyID
        self.FundMortgageRatio = float(FundMortgageRatio)
        self.BalanceAlgorithm = BalanceAlgorithm


class TradingAccountPasswordUpdateV1Field(Base):
    def __init__(self, BrokerID='', InvestorID='', OldPassword='', NewPassword=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.OldPassword = OldPassword
        self.NewPassword = NewPassword


class TradingAccountPasswordUpdateField(Base):
    def __init__(self, BrokerID='', AccountID='', OldPassword='', NewPassword='', CurrencyID=''):
        self.BrokerID = BrokerID
        self.AccountID = AccountID
        self.OldPassword = OldPassword
        self.NewPassword = NewPassword
        self.CurrencyID = CurrencyID


class QryCombinationLegField(Base):
    def __init__(self, CombInstrumentID='', LegID='', LegInstrumentID=''):
        self.CombInstrumentID = CombInstrumentID
        self.LegID = int(LegID)
        self.LegInstrumentID = LegInstrumentID


class QrySyncStatusField(Base):
    def __init__(self, TradingDay=''):
        self.TradingDay = TradingDay


class CombinationLegField(Base):
    def __init__(self, CombInstrumentID='', LegID='', LegInstrumentID='', Direction='', LegMultiple='', ImplyLevel=''):
        self.CombInstrumentID = CombInstrumentID
        self.LegID = int(LegID)
        self.LegInstrumentID = LegInstrumentID
        self.Direction = Direction
        self.LegMultiple = int(LegMultiple)
        self.ImplyLevel = int(ImplyLevel)


class SyncStatusField(Base):
    def __init__(self, TradingDay='', DataSyncStatus=''):
        self.TradingDay = TradingDay
        self.DataSyncStatus = DataSyncStatus


class QryLinkManField(Base):
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID


class LinkManField(Base):
    def __init__(self, BrokerID='', InvestorID='', PersonType='', IdentifiedCardType='', IdentifiedCardNo='',
                 PersonName='', Telephone='', Address='', ZipCode='', Priority='', UOAZipCode='', PersonFullName=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.PersonType = PersonType
        self.IdentifiedCardType = IdentifiedCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.PersonName = PersonName
        self.Telephone = Telephone
        self.Address = Address
        self.ZipCode = ZipCode
        self.Priority = int(Priority)
        self.UOAZipCode = UOAZipCode
        self.PersonFullName = PersonFullName


class QryBrokerUserEventField(Base):
    def __init__(self, BrokerID='', UserID='', UserEventType=''):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.UserEventType = UserEventType


class BrokerUserEventField(Base):
    def __init__(self, BrokerID='', UserID='', UserEventType='', EventSequenceNo='', EventDate='', EventTime='',
                 UserEventInfo='', InvestorID='', InstrumentID=''):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.UserEventType = UserEventType
        self.EventSequenceNo = int(EventSequenceNo)
        self.EventDate = EventDate
        self.EventTime = EventTime
        self.UserEventInfo = UserEventInfo
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID


class QryContractBankField(Base):
    def __init__(self, BrokerID='', BankID='', BankBrchID=''):
        self.BrokerID = BrokerID
        self.BankID = BankID
        self.BankBrchID = BankBrchID


class ContractBankField(Base):
    def __init__(self, BrokerID='', BankID='', BankBrchID='', BankName=''):
        self.BrokerID = BrokerID
        self.BankID = BankID
        self.BankBrchID = BankBrchID
        self.BankName = BankName


class InvestorPositionCombineDetailField(Base):
    def __init__(self, TradingDay='', OpenDate='', ExchangeID='', SettlementID='', BrokerID='', InvestorID='',
                 ComTradeID='', TradeID='', InstrumentID='', HedgeFlag='', Direction='', TotalAmt='', Margin='',
                 ExchMargin='', MarginRateByMoney='', MarginRateByVolume='', LegID='', LegMultiple='',
                 CombInstrumentID='', TradeGroupID=''):
        self.TradingDay = TradingDay
        self.OpenDate = OpenDate
        self.ExchangeID = ExchangeID
        self.SettlementID = int(SettlementID)
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ComTradeID = ComTradeID
        self.TradeID = TradeID
        self.InstrumentID = InstrumentID
        self.HedgeFlag = HedgeFlag
        self.Direction = Direction
        self.TotalAmt = int(TotalAmt)
        self.Margin = float(Margin)
        self.ExchMargin = float(ExchMargin)
        self.MarginRateByMoney = float(MarginRateByMoney)
        self.MarginRateByVolume = float(MarginRateByVolume)
        self.LegID = int(LegID)
        self.LegMultiple = int(LegMultiple)
        self.CombInstrumentID = CombInstrumentID
        self.TradeGroupID = int(TradeGroupID)


class ParkedOrderField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', OrderRef='', UserID='', OrderPriceType='',
                 Direction='', CombOffsetFlag='', CombHedgeFlag='', LimitPrice='', VolumeTotalOriginal='',
                 TimeCondition='', GTDDate='', VolumeCondition='', MinVolume='', ContingentCondition='', StopPrice='',
                 ForceCloseReason='', IsAutoSuspend='', BusinessUnit='', RequestID='', UserForceClose='', ExchangeID='',
                 ParkedOrderID='', UserType='', Status='', ErrorID='', ErrorMsg='', IsSwapOrder='', AccountID='',
                 CurrencyID='', ClientID='', InvestUnitID='', IPAddress='', MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.OrderRef = OrderRef
        self.UserID = UserID
        self.OrderPriceType = OrderPriceType
        self.Direction = Direction
        self.CombOffsetFlag = CombOffsetFlag
        self.CombHedgeFlag = CombHedgeFlag
        self.LimitPrice = float(LimitPrice)
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = TimeCondition
        self.GTDDate = GTDDate
        self.VolumeCondition = VolumeCondition
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = ContingentCondition
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = ForceCloseReason
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = BusinessUnit
        self.RequestID = int(RequestID)
        self.UserForceClose = int(UserForceClose)
        self.ExchangeID = ExchangeID
        self.ParkedOrderID = ParkedOrderID
        self.UserType = UserType
        self.Status = Status
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg
        self.IsSwapOrder = int(IsSwapOrder)
        self.AccountID = AccountID
        self.CurrencyID = CurrencyID
        self.ClientID = ClientID
        self.InvestUnitID = InvestUnitID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class ParkedOrderActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', OrderActionRef='', OrderRef='', RequestID='', FrontID='',
                 SessionID='', ExchangeID='', OrderSysID='', ActionFlag='', LimitPrice='', VolumeChange='', UserID='',
                 InstrumentID='', ParkedOrderActionID='', UserType='', Status='', ErrorID='', ErrorMsg='',
                 InvestUnitID='', IPAddress='', MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.OrderActionRef = int(OrderActionRef)
        self.OrderRef = OrderRef
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = ExchangeID
        self.OrderSysID = OrderSysID
        self.ActionFlag = ActionFlag
        self.LimitPrice = float(LimitPrice)
        self.VolumeChange = int(VolumeChange)
        self.UserID = UserID
        self.InstrumentID = InstrumentID
        self.ParkedOrderActionID = ParkedOrderActionID
        self.UserType = UserType
        self.Status = Status
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg
        self.InvestUnitID = InvestUnitID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class QryParkedOrderField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID


class QryParkedOrderActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.ExchangeID = ExchangeID


class RemoveParkedOrderField(Base):
    def __init__(self, BrokerID='', InvestorID='', ParkedOrderID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ParkedOrderID = ParkedOrderID


class RemoveParkedOrderActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', ParkedOrderActionID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ParkedOrderActionID = ParkedOrderActionID


class InvestorWithdrawAlgorithmField(Base):
    def __init__(self, BrokerID='', InvestorRange='', InvestorID='', UsingRatio='', CurrencyID='',
                 FundMortgageRatio=''):
        self.BrokerID = BrokerID
        self.InvestorRange = InvestorRange
        self.InvestorID = InvestorID
        self.UsingRatio = float(UsingRatio)
        self.CurrencyID = CurrencyID
        self.FundMortgageRatio = float(FundMortgageRatio)


class QryInvestorPositionCombineDetailField(Base):
    def __init__(self, BrokerID='', InvestorID='', CombInstrumentID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.CombInstrumentID = CombInstrumentID


class MarketDataAveragePriceField(Base):
    def __init__(self, AveragePrice=''):
        self.AveragePrice = float(AveragePrice)


class VerifyInvestorPasswordField(Base):
    def __init__(self, BrokerID='', InvestorID='', Password=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.Password = Password


class UserIPField(Base):
    def __init__(self, BrokerID='', UserID='', IPAddress='', IPMask='', MacAddress=''):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.IPAddress = IPAddress
        self.IPMask = IPMask
        self.MacAddress = MacAddress


class TradingNoticeInfoField(Base):
    def __init__(self, BrokerID='', InvestorID='', SendTime='', FieldContent='', SequenceSeries='', SequenceNo=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.SendTime = SendTime
        self.FieldContent = FieldContent
        self.SequenceSeries = int(SequenceSeries)
        self.SequenceNo = int(SequenceNo)


class TradingNoticeField(Base):
    def __init__(self, BrokerID='', InvestorRange='', InvestorID='', SequenceSeries='', UserID='', SendTime='',
                 SequenceNo='', FieldContent=''):
        self.BrokerID = BrokerID
        self.InvestorRange = InvestorRange
        self.InvestorID = InvestorID
        self.SequenceSeries = int(SequenceSeries)
        self.UserID = UserID
        self.SendTime = SendTime
        self.SequenceNo = int(SequenceNo)
        self.FieldContent = FieldContent


class QryTradingNoticeField(Base):
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID


class QryErrOrderField(Base):
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID


class ErrOrderField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', OrderRef='', UserID='', OrderPriceType='',
                 Direction='', CombOffsetFlag='', CombHedgeFlag='', LimitPrice='', VolumeTotalOriginal='',
                 TimeCondition='', GTDDate='', VolumeCondition='', MinVolume='', ContingentCondition='', StopPrice='',
                 ForceCloseReason='', IsAutoSuspend='', BusinessUnit='', RequestID='', UserForceClose='', ErrorID='',
                 ErrorMsg='', IsSwapOrder='', ExchangeID='', InvestUnitID='', AccountID='', CurrencyID='', ClientID='',
                 IPAddress='', MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.OrderRef = OrderRef
        self.UserID = UserID
        self.OrderPriceType = OrderPriceType
        self.Direction = Direction
        self.CombOffsetFlag = CombOffsetFlag
        self.CombHedgeFlag = CombHedgeFlag
        self.LimitPrice = float(LimitPrice)
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = TimeCondition
        self.GTDDate = GTDDate
        self.VolumeCondition = VolumeCondition
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = ContingentCondition
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = ForceCloseReason
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = BusinessUnit
        self.RequestID = int(RequestID)
        self.UserForceClose = int(UserForceClose)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg
        self.IsSwapOrder = int(IsSwapOrder)
        self.ExchangeID = ExchangeID
        self.InvestUnitID = InvestUnitID
        self.AccountID = AccountID
        self.CurrencyID = CurrencyID
        self.ClientID = ClientID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class ErrorConditionalOrderField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', OrderRef='', UserID='', OrderPriceType='',
                 Direction='', CombOffsetFlag='', CombHedgeFlag='', LimitPrice='', VolumeTotalOriginal='',
                 TimeCondition='', GTDDate='', VolumeCondition='', MinVolume='', ContingentCondition='', StopPrice='',
                 ForceCloseReason='', IsAutoSuspend='', BusinessUnit='', RequestID='', OrderLocalID='', ExchangeID='',
                 ParticipantID='', ClientID='', ExchangeInstID='', TraderID='', InstallID='', OrderSubmitStatus='',
                 NotifySequence='', TradingDay='', SettlementID='', OrderSysID='', OrderSource='', OrderStatus='',
                 OrderType='', VolumeTraded='', VolumeTotal='', InsertDate='', InsertTime='', ActiveTime='',
                 SuspendTime='', UpdateTime='', CancelTime='', ActiveTraderID='', ClearingPartID='', SequenceNo='',
                 FrontID='', SessionID='', UserProductInfo='', StatusMsg='', UserForceClose='', ActiveUserID='',
                 BrokerOrderSeq='', RelativeOrderSysID='', ZCETotalTradedVolume='', ErrorID='', ErrorMsg='',
                 IsSwapOrder='', BranchID='', InvestUnitID='', AccountID='', CurrencyID='', IPAddress='',
                 MacAddress=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.OrderRef = OrderRef
        self.UserID = UserID
        self.OrderPriceType = OrderPriceType
        self.Direction = Direction
        self.CombOffsetFlag = CombOffsetFlag
        self.CombHedgeFlag = CombHedgeFlag
        self.LimitPrice = float(LimitPrice)
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = TimeCondition
        self.GTDDate = GTDDate
        self.VolumeCondition = VolumeCondition
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = ContingentCondition
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = ForceCloseReason
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = BusinessUnit
        self.RequestID = int(RequestID)
        self.OrderLocalID = OrderLocalID
        self.ExchangeID = ExchangeID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.ExchangeInstID = ExchangeInstID
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.OrderSubmitStatus = OrderSubmitStatus
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = TradingDay
        self.SettlementID = int(SettlementID)
        self.OrderSysID = OrderSysID
        self.OrderSource = OrderSource
        self.OrderStatus = OrderStatus
        self.OrderType = OrderType
        self.VolumeTraded = int(VolumeTraded)
        self.VolumeTotal = int(VolumeTotal)
        self.InsertDate = InsertDate
        self.InsertTime = InsertTime
        self.ActiveTime = ActiveTime
        self.SuspendTime = SuspendTime
        self.UpdateTime = UpdateTime
        self.CancelTime = CancelTime
        self.ActiveTraderID = ActiveTraderID
        self.ClearingPartID = ClearingPartID
        self.SequenceNo = int(SequenceNo)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.UserProductInfo = UserProductInfo
        self.StatusMsg = StatusMsg
        self.UserForceClose = int(UserForceClose)
        self.ActiveUserID = ActiveUserID
        self.BrokerOrderSeq = int(BrokerOrderSeq)
        self.RelativeOrderSysID = RelativeOrderSysID
        self.ZCETotalTradedVolume = int(ZCETotalTradedVolume)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg
        self.IsSwapOrder = int(IsSwapOrder)
        self.BranchID = BranchID
        self.InvestUnitID = InvestUnitID
        self.AccountID = AccountID
        self.CurrencyID = CurrencyID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress


class QryErrOrderActionField(Base):
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID


class ErrOrderActionField(Base):
    def __init__(self, BrokerID='', InvestorID='', OrderActionRef='', OrderRef='', RequestID='', FrontID='',
                 SessionID='', ExchangeID='', OrderSysID='', ActionFlag='', LimitPrice='', VolumeChange='',
                 ActionDate='', ActionTime='', TraderID='', InstallID='', OrderLocalID='', ActionLocalID='',
                 ParticipantID='', ClientID='', BusinessUnit='', OrderActionStatus='', UserID='', StatusMsg='',
                 InstrumentID='', BranchID='', InvestUnitID='', IPAddress='', MacAddress='', ErrorID='', ErrorMsg=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.OrderActionRef = int(OrderActionRef)
        self.OrderRef = OrderRef
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = ExchangeID
        self.OrderSysID = OrderSysID
        self.ActionFlag = ActionFlag
        self.LimitPrice = float(LimitPrice)
        self.VolumeChange = int(VolumeChange)
        self.ActionDate = ActionDate
        self.ActionTime = ActionTime
        self.TraderID = TraderID
        self.InstallID = int(InstallID)
        self.OrderLocalID = OrderLocalID
        self.ActionLocalID = ActionLocalID
        self.ParticipantID = ParticipantID
        self.ClientID = ClientID
        self.BusinessUnit = BusinessUnit
        self.OrderActionStatus = OrderActionStatus
        self.UserID = UserID
        self.StatusMsg = StatusMsg
        self.InstrumentID = InstrumentID
        self.BranchID = BranchID
        self.InvestUnitID = InvestUnitID
        self.IPAddress = IPAddress
        self.MacAddress = MacAddress
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg


class QryExchangeSequenceField(Base):
    def __init__(self, ExchangeID=''):
        self.ExchangeID = ExchangeID


class ExchangeSequenceField(Base):
    def __init__(self, ExchangeID='', SequenceNo='', MarketStatus=''):
        self.ExchangeID = ExchangeID
        self.SequenceNo = int(SequenceNo)
        self.MarketStatus = MarketStatus


class QueryMaxOrderVolumeWithPriceField(Base):
    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', Direction='', OffsetFlag='', HedgeFlag='',
                 MaxVolume='', Price=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.InstrumentID = InstrumentID
        self.Direction = Direction
        self.OffsetFlag = OffsetFlag
        self.HedgeFlag = HedgeFlag
        self.MaxVolume = int(MaxVolume)
        self.Price = float(Price)


class QryBrokerTradingParamsField(Base):
    def __init__(self, BrokerID='', InvestorID='', CurrencyID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.CurrencyID = CurrencyID


class BrokerTradingParamsField(Base):
    def __init__(self, BrokerID='', InvestorID='', MarginPriceType='', Algorithm='', AvailIncludeCloseProfit='',
                 CurrencyID='', OptionRoyaltyPriceType=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.MarginPriceType = MarginPriceType
        self.Algorithm = Algorithm
        self.AvailIncludeCloseProfit = AvailIncludeCloseProfit
        self.CurrencyID = CurrencyID
        self.OptionRoyaltyPriceType = OptionRoyaltyPriceType


class QryBrokerTradingAlgosField(Base):
    def __init__(self, BrokerID='', ExchangeID='', InstrumentID=''):
        self.BrokerID = BrokerID
        self.ExchangeID = ExchangeID
        self.InstrumentID = InstrumentID


class BrokerTradingAlgosField(Base):
    def __init__(self, BrokerID='', ExchangeID='', InstrumentID='', HandlePositionAlgoID='', FindMarginRateAlgoID='',
                 HandleTradingAccountAlgoID=''):
        self.BrokerID = BrokerID
        self.ExchangeID = ExchangeID
        self.InstrumentID = InstrumentID
        self.HandlePositionAlgoID = HandlePositionAlgoID
        self.FindMarginRateAlgoID = FindMarginRateAlgoID
        self.HandleTradingAccountAlgoID = HandleTradingAccountAlgoID


class QueryBrokerDepositField(Base):
    def __init__(self, BrokerID='', ExchangeID=''):
        self.BrokerID = BrokerID
        self.ExchangeID = ExchangeID


class BrokerDepositField(Base):
    def __init__(self, TradingDay='', BrokerID='', ParticipantID='', ExchangeID='', PreBalance='', CurrMargin='',
                 CloseProfit='', Balance='', Deposit='', Withdraw='', Available='', Reserve='', FrozenMargin=''):
        self.TradingDay = TradingDay
        self.BrokerID = BrokerID
        self.ParticipantID = ParticipantID
        self.ExchangeID = ExchangeID
        self.PreBalance = float(PreBalance)
        self.CurrMargin = float(CurrMargin)
        self.CloseProfit = float(CloseProfit)
        self.Balance = float(Balance)
        self.Deposit = float(Deposit)
        self.Withdraw = float(Withdraw)
        self.Available = float(Available)
        self.Reserve = float(Reserve)
        self.FrozenMargin = float(FrozenMargin)


class QryCFMMCBrokerKeyField(Base):
    def __init__(self, BrokerID=''):
        self.BrokerID = BrokerID


class CFMMCBrokerKeyField(Base):
    def __init__(self, BrokerID='', ParticipantID='', CreateDate='', CreateTime='', KeyID='', CurrentKey='',
                 KeyKind=''):
        self.BrokerID = BrokerID
        self.ParticipantID = ParticipantID
        self.CreateDate = CreateDate
        self.CreateTime = CreateTime
        self.KeyID = int(KeyID)
        self.CurrentKey = CurrentKey
        self.KeyKind = KeyKind


class CFMMCTradingAccountKeyField(Base):
    def __init__(self, BrokerID='', ParticipantID='', AccountID='', KeyID='', CurrentKey=''):
        self.BrokerID = BrokerID
        self.ParticipantID = ParticipantID
        self.AccountID = AccountID
        self.KeyID = int(KeyID)
        self.CurrentKey = CurrentKey


class QryCFMMCTradingAccountKeyField(Base):
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID


class BrokerUserOTPParamField(Base):
    def __init__(self, BrokerID='', UserID='', OTPVendorsID='', SerialNumber='', AuthKey='', LastDrift='',
                 LastSuccess='', OTPType=''):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.OTPVendorsID = OTPVendorsID
        self.SerialNumber = SerialNumber
        self.AuthKey = AuthKey
        self.LastDrift = int(LastDrift)
        self.LastSuccess = int(LastSuccess)
        self.OTPType = OTPType


class ManualSyncBrokerUserOTPField(Base):
    def __init__(self, BrokerID='', UserID='', OTPType='', FirstOTP='', SecondOTP=''):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.OTPType = OTPType
        self.FirstOTP = FirstOTP
        self.SecondOTP = SecondOTP


class CommRateModelField(Base):
    def __init__(self, BrokerID='', CommModelID='', CommModelName=''):
        self.BrokerID = BrokerID
        self.CommModelID = CommModelID
        self.CommModelName = CommModelName


class QryCommRateModelField(Base):
    def __init__(self, BrokerID='', CommModelID=''):
        self.BrokerID = BrokerID
        self.CommModelID = CommModelID


class MarginModelField(Base):
    def __init__(self, BrokerID='', MarginModelID='', MarginModelName=''):
        self.BrokerID = BrokerID
        self.MarginModelID = MarginModelID
        self.MarginModelName = MarginModelName


class QryMarginModelField(Base):
    def __init__(self, BrokerID='', MarginModelID=''):
        self.BrokerID = BrokerID
        self.MarginModelID = MarginModelID


class EWarrantOffsetField(Base):
    def __init__(self, TradingDay='', BrokerID='', InvestorID='', ExchangeID='', InstrumentID='', Direction='',
                 HedgeFlag='', Volume=''):
        self.TradingDay = TradingDay
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExchangeID = ExchangeID
        self.InstrumentID = InstrumentID
        self.Direction = Direction
        self.HedgeFlag = HedgeFlag
        self.Volume = int(Volume)


class QryEWarrantOffsetField(Base):
    def __init__(self, BrokerID='', InvestorID='', ExchangeID='', InstrumentID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ExchangeID = ExchangeID
        self.InstrumentID = InstrumentID


class QryInvestorProductGroupMarginField(Base):
    def __init__(self, BrokerID='', InvestorID='', ProductGroupID='', HedgeFlag=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.ProductGroupID = ProductGroupID
        self.HedgeFlag = HedgeFlag


class InvestorProductGroupMarginField(Base):
    def __init__(self, ProductGroupID='', BrokerID='', InvestorID='', TradingDay='', SettlementID='', FrozenMargin='',
                 LongFrozenMargin='', ShortFrozenMargin='', UseMargin='', LongUseMargin='', ShortUseMargin='',
                 ExchMargin='', LongExchMargin='', ShortExchMargin='', CloseProfit='', FrozenCommission='',
                 Commission='', FrozenCash='', CashIn='', PositionProfit='', OffsetAmount='', LongOffsetAmount='',
                 ShortOffsetAmount='', ExchOffsetAmount='', LongExchOffsetAmount='', ShortExchOffsetAmount='',
                 HedgeFlag=''):
        self.ProductGroupID = ProductGroupID
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.TradingDay = TradingDay
        self.SettlementID = int(SettlementID)
        self.FrozenMargin = float(FrozenMargin)
        self.LongFrozenMargin = float(LongFrozenMargin)
        self.ShortFrozenMargin = float(ShortFrozenMargin)
        self.UseMargin = float(UseMargin)
        self.LongUseMargin = float(LongUseMargin)
        self.ShortUseMargin = float(ShortUseMargin)
        self.ExchMargin = float(ExchMargin)
        self.LongExchMargin = float(LongExchMargin)
        self.ShortExchMargin = float(ShortExchMargin)
        self.CloseProfit = float(CloseProfit)
        self.FrozenCommission = float(FrozenCommission)
        self.Commission = float(Commission)
        self.FrozenCash = float(FrozenCash)
        self.CashIn = float(CashIn)
        self.PositionProfit = float(PositionProfit)
        self.OffsetAmount = float(OffsetAmount)
        self.LongOffsetAmount = float(LongOffsetAmount)
        self.ShortOffsetAmount = float(ShortOffsetAmount)
        self.ExchOffsetAmount = float(ExchOffsetAmount)
        self.LongExchOffsetAmount = float(LongExchOffsetAmount)
        self.ShortExchOffsetAmount = float(ShortExchOffsetAmount)
        self.HedgeFlag = HedgeFlag


class QueryCFMMCTradingAccountTokenField(Base):
    def __init__(self, BrokerID='', InvestorID=''):
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID


class CFMMCTradingAccountTokenField(Base):
    def __init__(self, BrokerID='', ParticipantID='', AccountID='', KeyID='', Token=''):
        self.BrokerID = BrokerID
        self.ParticipantID = ParticipantID
        self.AccountID = AccountID
        self.KeyID = int(KeyID)
        self.Token = Token


class QryProductGroupField(Base):
    def __init__(self, ProductID='', ExchangeID=''):
        self.ProductID = ProductID
        self.ExchangeID = ExchangeID


class ProductGroupField(Base):
    def __init__(self, ProductID='', ExchangeID='', ProductGroupID=''):
        self.ProductID = ProductID
        self.ExchangeID = ExchangeID
        self.ProductGroupID = ProductGroupID


class BulletinField(Base):
    def __init__(self, ExchangeID='', TradingDay='', BulletinID='', SequenceNo='', NewsType='', NewsUrgency='',
                 SendTime='', Abstract='', ComeFrom='', Content='', URLLink='', MarketID=''):
        self.ExchangeID = ExchangeID
        self.TradingDay = TradingDay
        self.BulletinID = int(BulletinID)
        self.SequenceNo = int(SequenceNo)
        self.NewsType = NewsType
        self.NewsUrgency = NewsUrgency
        self.SendTime = SendTime
        self.Abstract = Abstract
        self.ComeFrom = ComeFrom
        self.Content = Content
        self.URLLink = URLLink
        self.MarketID = MarketID


class QryBulletinField(Base):
    def __init__(self, ExchangeID='', BulletinID='', SequenceNo='', NewsType='', NewsUrgency=''):
        self.ExchangeID = ExchangeID
        self.BulletinID = int(BulletinID)
        self.SequenceNo = int(SequenceNo)
        self.NewsType = NewsType
        self.NewsUrgency = NewsUrgency


class ReqOpenAccountField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', Gender='', CountryCode='', CustType='',
                 Address='', ZipCode='', Telephone='', MobilePhone='', Fax='', EMail='', MoneyAccountStatus='',
                 BankAccount='', BankPassWord='', AccountID='', Password='', InstallID='', VerifyCertNoFlag='',
                 CurrencyID='', CashExchangeCode='', Digest='', BankAccType='', DeviceID='', BankSecuAccType='',
                 BrokerIDByBank='', BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='', OperNo='', TID='', UserID='',
                 LongCustomerName=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.CustomerName = CustomerName
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.Gender = Gender
        self.CountryCode = CountryCode
        self.CustType = CustType
        self.Address = Address
        self.ZipCode = ZipCode
        self.Telephone = Telephone
        self.MobilePhone = MobilePhone
        self.Fax = Fax
        self.EMail = EMail
        self.MoneyAccountStatus = MoneyAccountStatus
        self.BankAccount = BankAccount
        self.BankPassWord = BankPassWord
        self.AccountID = AccountID
        self.Password = Password
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = VerifyCertNoFlag
        self.CurrencyID = CurrencyID
        self.CashExchangeCode = CashExchangeCode
        self.Digest = Digest
        self.BankAccType = BankAccType
        self.DeviceID = DeviceID
        self.BankSecuAccType = BankSecuAccType
        self.BrokerIDByBank = BrokerIDByBank
        self.BankSecuAcc = BankSecuAcc
        self.BankPwdFlag = BankPwdFlag
        self.SecuPwdFlag = SecuPwdFlag
        self.OperNo = OperNo
        self.TID = int(TID)
        self.UserID = UserID
        self.LongCustomerName = LongCustomerName


class ReqCancelAccountField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', Gender='', CountryCode='', CustType='',
                 Address='', ZipCode='', Telephone='', MobilePhone='', Fax='', EMail='', MoneyAccountStatus='',
                 BankAccount='', BankPassWord='', AccountID='', Password='', InstallID='', VerifyCertNoFlag='',
                 CurrencyID='', CashExchangeCode='', Digest='', BankAccType='', DeviceID='', BankSecuAccType='',
                 BrokerIDByBank='', BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='', OperNo='', TID='', UserID='',
                 LongCustomerName=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.CustomerName = CustomerName
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.Gender = Gender
        self.CountryCode = CountryCode
        self.CustType = CustType
        self.Address = Address
        self.ZipCode = ZipCode
        self.Telephone = Telephone
        self.MobilePhone = MobilePhone
        self.Fax = Fax
        self.EMail = EMail
        self.MoneyAccountStatus = MoneyAccountStatus
        self.BankAccount = BankAccount
        self.BankPassWord = BankPassWord
        self.AccountID = AccountID
        self.Password = Password
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = VerifyCertNoFlag
        self.CurrencyID = CurrencyID
        self.CashExchangeCode = CashExchangeCode
        self.Digest = Digest
        self.BankAccType = BankAccType
        self.DeviceID = DeviceID
        self.BankSecuAccType = BankSecuAccType
        self.BrokerIDByBank = BrokerIDByBank
        self.BankSecuAcc = BankSecuAcc
        self.BankPwdFlag = BankPwdFlag
        self.SecuPwdFlag = SecuPwdFlag
        self.OperNo = OperNo
        self.TID = int(TID)
        self.UserID = UserID
        self.LongCustomerName = LongCustomerName


class ReqChangeAccountField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', Gender='', CountryCode='', CustType='',
                 Address='', ZipCode='', Telephone='', MobilePhone='', Fax='', EMail='', MoneyAccountStatus='',
                 BankAccount='', BankPassWord='', NewBankAccount='', NewBankPassWord='', AccountID='', Password='',
                 BankAccType='', InstallID='', VerifyCertNoFlag='', CurrencyID='', BrokerIDByBank='', BankPwdFlag='',
                 SecuPwdFlag='', TID='', Digest='', LongCustomerName=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.CustomerName = CustomerName
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.Gender = Gender
        self.CountryCode = CountryCode
        self.CustType = CustType
        self.Address = Address
        self.ZipCode = ZipCode
        self.Telephone = Telephone
        self.MobilePhone = MobilePhone
        self.Fax = Fax
        self.EMail = EMail
        self.MoneyAccountStatus = MoneyAccountStatus
        self.BankAccount = BankAccount
        self.BankPassWord = BankPassWord
        self.NewBankAccount = NewBankAccount
        self.NewBankPassWord = NewBankPassWord
        self.AccountID = AccountID
        self.Password = Password
        self.BankAccType = BankAccType
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = VerifyCertNoFlag
        self.CurrencyID = CurrencyID
        self.BrokerIDByBank = BrokerIDByBank
        self.BankPwdFlag = BankPwdFlag
        self.SecuPwdFlag = SecuPwdFlag
        self.TID = int(TID)
        self.Digest = Digest
        self.LongCustomerName = LongCustomerName


class ReqTransferField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', CustType='', BankAccount='', BankPassWord='',
                 AccountID='', Password='', InstallID='', FutureSerial='', UserID='', VerifyCertNoFlag='',
                 CurrencyID='', TradeAmount='', FutureFetchAmount='', FeePayFlag='', CustFee='', BrokerFee='',
                 Message='', Digest='', BankAccType='', DeviceID='', BankSecuAccType='', BrokerIDByBank='',
                 BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='', OperNo='', RequestID='', TID='', TransferStatus='',
                 LongCustomerName=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.CustomerName = CustomerName
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.CustType = CustType
        self.BankAccount = BankAccount
        self.BankPassWord = BankPassWord
        self.AccountID = AccountID
        self.Password = Password
        self.InstallID = int(InstallID)
        self.FutureSerial = int(FutureSerial)
        self.UserID = UserID
        self.VerifyCertNoFlag = VerifyCertNoFlag
        self.CurrencyID = CurrencyID
        self.TradeAmount = float(TradeAmount)
        self.FutureFetchAmount = float(FutureFetchAmount)
        self.FeePayFlag = FeePayFlag
        self.CustFee = float(CustFee)
        self.BrokerFee = float(BrokerFee)
        self.Message = Message
        self.Digest = Digest
        self.BankAccType = BankAccType
        self.DeviceID = DeviceID
        self.BankSecuAccType = BankSecuAccType
        self.BrokerIDByBank = BrokerIDByBank
        self.BankSecuAcc = BankSecuAcc
        self.BankPwdFlag = BankPwdFlag
        self.SecuPwdFlag = SecuPwdFlag
        self.OperNo = OperNo
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.TransferStatus = TransferStatus
        self.LongCustomerName = LongCustomerName


class RspTransferField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', CustType='', BankAccount='', BankPassWord='',
                 AccountID='', Password='', InstallID='', FutureSerial='', UserID='', VerifyCertNoFlag='',
                 CurrencyID='', TradeAmount='', FutureFetchAmount='', FeePayFlag='', CustFee='', BrokerFee='',
                 Message='', Digest='', BankAccType='', DeviceID='', BankSecuAccType='', BrokerIDByBank='',
                 BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='', OperNo='', RequestID='', TID='', TransferStatus='',
                 ErrorID='', ErrorMsg='', LongCustomerName=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.CustomerName = CustomerName
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.CustType = CustType
        self.BankAccount = BankAccount
        self.BankPassWord = BankPassWord
        self.AccountID = AccountID
        self.Password = Password
        self.InstallID = int(InstallID)
        self.FutureSerial = int(FutureSerial)
        self.UserID = UserID
        self.VerifyCertNoFlag = VerifyCertNoFlag
        self.CurrencyID = CurrencyID
        self.TradeAmount = float(TradeAmount)
        self.FutureFetchAmount = float(FutureFetchAmount)
        self.FeePayFlag = FeePayFlag
        self.CustFee = float(CustFee)
        self.BrokerFee = float(BrokerFee)
        self.Message = Message
        self.Digest = Digest
        self.BankAccType = BankAccType
        self.DeviceID = DeviceID
        self.BankSecuAccType = BankSecuAccType
        self.BrokerIDByBank = BrokerIDByBank
        self.BankSecuAcc = BankSecuAcc
        self.BankPwdFlag = BankPwdFlag
        self.SecuPwdFlag = SecuPwdFlag
        self.OperNo = OperNo
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.TransferStatus = TransferStatus
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg
        self.LongCustomerName = LongCustomerName


class ReqRepealField(Base):
    def __init__(self, RepealTimeInterval='', RepealedTimes='', BankRepealFlag='', BrokerRepealFlag='',
                 PlateRepealSerial='', BankRepealSerial='', FutureRepealSerial='', TradeCode='', BankID='',
                 BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='',
                 TradingDay='', PlateSerial='', LastFragment='', SessionID='', CustomerName='', IdCardType='',
                 IdentifiedCardNo='', CustType='', BankAccount='', BankPassWord='', AccountID='', Password='',
                 InstallID='', FutureSerial='', UserID='', VerifyCertNoFlag='', CurrencyID='', TradeAmount='',
                 FutureFetchAmount='', FeePayFlag='', CustFee='', BrokerFee='', Message='', Digest='', BankAccType='',
                 DeviceID='', BankSecuAccType='', BrokerIDByBank='', BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='',
                 OperNo='', RequestID='', TID='', TransferStatus='', LongCustomerName=''):
        self.RepealTimeInterval = int(RepealTimeInterval)
        self.RepealedTimes = int(RepealedTimes)
        self.BankRepealFlag = BankRepealFlag
        self.BrokerRepealFlag = BrokerRepealFlag
        self.PlateRepealSerial = int(PlateRepealSerial)
        self.BankRepealSerial = BankRepealSerial
        self.FutureRepealSerial = int(FutureRepealSerial)
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.CustomerName = CustomerName
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.CustType = CustType
        self.BankAccount = BankAccount
        self.BankPassWord = BankPassWord
        self.AccountID = AccountID
        self.Password = Password
        self.InstallID = int(InstallID)
        self.FutureSerial = int(FutureSerial)
        self.UserID = UserID
        self.VerifyCertNoFlag = VerifyCertNoFlag
        self.CurrencyID = CurrencyID
        self.TradeAmount = float(TradeAmount)
        self.FutureFetchAmount = float(FutureFetchAmount)
        self.FeePayFlag = FeePayFlag
        self.CustFee = float(CustFee)
        self.BrokerFee = float(BrokerFee)
        self.Message = Message
        self.Digest = Digest
        self.BankAccType = BankAccType
        self.DeviceID = DeviceID
        self.BankSecuAccType = BankSecuAccType
        self.BrokerIDByBank = BrokerIDByBank
        self.BankSecuAcc = BankSecuAcc
        self.BankPwdFlag = BankPwdFlag
        self.SecuPwdFlag = SecuPwdFlag
        self.OperNo = OperNo
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.TransferStatus = TransferStatus
        self.LongCustomerName = LongCustomerName


class RspRepealField(Base):
    def __init__(self, RepealTimeInterval='', RepealedTimes='', BankRepealFlag='', BrokerRepealFlag='',
                 PlateRepealSerial='', BankRepealSerial='', FutureRepealSerial='', TradeCode='', BankID='',
                 BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='',
                 TradingDay='', PlateSerial='', LastFragment='', SessionID='', CustomerName='', IdCardType='',
                 IdentifiedCardNo='', CustType='', BankAccount='', BankPassWord='', AccountID='', Password='',
                 InstallID='', FutureSerial='', UserID='', VerifyCertNoFlag='', CurrencyID='', TradeAmount='',
                 FutureFetchAmount='', FeePayFlag='', CustFee='', BrokerFee='', Message='', Digest='', BankAccType='',
                 DeviceID='', BankSecuAccType='', BrokerIDByBank='', BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='',
                 OperNo='', RequestID='', TID='', TransferStatus='', ErrorID='', ErrorMsg='', LongCustomerName=''):
        self.RepealTimeInterval = int(RepealTimeInterval)
        self.RepealedTimes = int(RepealedTimes)
        self.BankRepealFlag = BankRepealFlag
        self.BrokerRepealFlag = BrokerRepealFlag
        self.PlateRepealSerial = int(PlateRepealSerial)
        self.BankRepealSerial = BankRepealSerial
        self.FutureRepealSerial = int(FutureRepealSerial)
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.CustomerName = CustomerName
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.CustType = CustType
        self.BankAccount = BankAccount
        self.BankPassWord = BankPassWord
        self.AccountID = AccountID
        self.Password = Password
        self.InstallID = int(InstallID)
        self.FutureSerial = int(FutureSerial)
        self.UserID = UserID
        self.VerifyCertNoFlag = VerifyCertNoFlag
        self.CurrencyID = CurrencyID
        self.TradeAmount = float(TradeAmount)
        self.FutureFetchAmount = float(FutureFetchAmount)
        self.FeePayFlag = FeePayFlag
        self.CustFee = float(CustFee)
        self.BrokerFee = float(BrokerFee)
        self.Message = Message
        self.Digest = Digest
        self.BankAccType = BankAccType
        self.DeviceID = DeviceID
        self.BankSecuAccType = BankSecuAccType
        self.BrokerIDByBank = BrokerIDByBank
        self.BankSecuAcc = BankSecuAcc
        self.BankPwdFlag = BankPwdFlag
        self.SecuPwdFlag = SecuPwdFlag
        self.OperNo = OperNo
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.TransferStatus = TransferStatus
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg
        self.LongCustomerName = LongCustomerName


class ReqQueryAccountField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', CustType='', BankAccount='', BankPassWord='',
                 AccountID='', Password='', FutureSerial='', InstallID='', UserID='', VerifyCertNoFlag='',
                 CurrencyID='', Digest='', BankAccType='', DeviceID='', BankSecuAccType='', BrokerIDByBank='',
                 BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='', OperNo='', RequestID='', TID='', LongCustomerName=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.CustomerName = CustomerName
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.CustType = CustType
        self.BankAccount = BankAccount
        self.BankPassWord = BankPassWord
        self.AccountID = AccountID
        self.Password = Password
        self.FutureSerial = int(FutureSerial)
        self.InstallID = int(InstallID)
        self.UserID = UserID
        self.VerifyCertNoFlag = VerifyCertNoFlag
        self.CurrencyID = CurrencyID
        self.Digest = Digest
        self.BankAccType = BankAccType
        self.DeviceID = DeviceID
        self.BankSecuAccType = BankSecuAccType
        self.BrokerIDByBank = BrokerIDByBank
        self.BankSecuAcc = BankSecuAcc
        self.BankPwdFlag = BankPwdFlag
        self.SecuPwdFlag = SecuPwdFlag
        self.OperNo = OperNo
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.LongCustomerName = LongCustomerName


class RspQueryAccountField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', CustType='', BankAccount='', BankPassWord='',
                 AccountID='', Password='', FutureSerial='', InstallID='', UserID='', VerifyCertNoFlag='',
                 CurrencyID='', Digest='', BankAccType='', DeviceID='', BankSecuAccType='', BrokerIDByBank='',
                 BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='', OperNo='', RequestID='', TID='', BankUseAmount='',
                 BankFetchAmount='', LongCustomerName=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.CustomerName = CustomerName
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.CustType = CustType
        self.BankAccount = BankAccount
        self.BankPassWord = BankPassWord
        self.AccountID = AccountID
        self.Password = Password
        self.FutureSerial = int(FutureSerial)
        self.InstallID = int(InstallID)
        self.UserID = UserID
        self.VerifyCertNoFlag = VerifyCertNoFlag
        self.CurrencyID = CurrencyID
        self.Digest = Digest
        self.BankAccType = BankAccType
        self.DeviceID = DeviceID
        self.BankSecuAccType = BankSecuAccType
        self.BrokerIDByBank = BrokerIDByBank
        self.BankSecuAcc = BankSecuAcc
        self.BankPwdFlag = BankPwdFlag
        self.SecuPwdFlag = SecuPwdFlag
        self.OperNo = OperNo
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.BankUseAmount = float(BankUseAmount)
        self.BankFetchAmount = float(BankFetchAmount)
        self.LongCustomerName = LongCustomerName


class FutureSignIOField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 InstallID='', UserID='', Digest='', CurrencyID='', DeviceID='', BrokerIDByBank='', OperNo='',
                 RequestID='', TID=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = UserID
        self.Digest = Digest
        self.CurrencyID = CurrencyID
        self.DeviceID = DeviceID
        self.BrokerIDByBank = BrokerIDByBank
        self.OperNo = OperNo
        self.RequestID = int(RequestID)
        self.TID = int(TID)


class RspFutureSignInField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 InstallID='', UserID='', Digest='', CurrencyID='', DeviceID='', BrokerIDByBank='', OperNo='',
                 RequestID='', TID='', ErrorID='', ErrorMsg='', PinKey='', MacKey=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = UserID
        self.Digest = Digest
        self.CurrencyID = CurrencyID
        self.DeviceID = DeviceID
        self.BrokerIDByBank = BrokerIDByBank
        self.OperNo = OperNo
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg
        self.PinKey = PinKey
        self.MacKey = MacKey


class ReqFutureSignOutField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 InstallID='', UserID='', Digest='', CurrencyID='', DeviceID='', BrokerIDByBank='', OperNo='',
                 RequestID='', TID=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = UserID
        self.Digest = Digest
        self.CurrencyID = CurrencyID
        self.DeviceID = DeviceID
        self.BrokerIDByBank = BrokerIDByBank
        self.OperNo = OperNo
        self.RequestID = int(RequestID)
        self.TID = int(TID)


class RspFutureSignOutField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 InstallID='', UserID='', Digest='', CurrencyID='', DeviceID='', BrokerIDByBank='', OperNo='',
                 RequestID='', TID='', ErrorID='', ErrorMsg=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = UserID
        self.Digest = Digest
        self.CurrencyID = CurrencyID
        self.DeviceID = DeviceID
        self.BrokerIDByBank = BrokerIDByBank
        self.OperNo = OperNo
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg


class ReqQueryTradeResultBySerialField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 Reference='', RefrenceIssureType='', RefrenceIssure='', CustomerName='', IdCardType='',
                 IdentifiedCardNo='', CustType='', BankAccount='', BankPassWord='', AccountID='', Password='',
                 CurrencyID='', TradeAmount='', Digest='', LongCustomerName=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.Reference = int(Reference)
        self.RefrenceIssureType = RefrenceIssureType
        self.RefrenceIssure = RefrenceIssure
        self.CustomerName = CustomerName
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.CustType = CustType
        self.BankAccount = BankAccount
        self.BankPassWord = BankPassWord
        self.AccountID = AccountID
        self.Password = Password
        self.CurrencyID = CurrencyID
        self.TradeAmount = float(TradeAmount)
        self.Digest = Digest
        self.LongCustomerName = LongCustomerName


class RspQueryTradeResultBySerialField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='', ErrorID='',
                 ErrorMsg='', Reference='', RefrenceIssureType='', RefrenceIssure='', OriginReturnCode='',
                 OriginDescrInfoForReturnCode='', BankAccount='', BankPassWord='', AccountID='', Password='',
                 CurrencyID='', TradeAmount='', Digest=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg
        self.Reference = int(Reference)
        self.RefrenceIssureType = RefrenceIssureType
        self.RefrenceIssure = RefrenceIssure
        self.OriginReturnCode = OriginReturnCode
        self.OriginDescrInfoForReturnCode = OriginDescrInfoForReturnCode
        self.BankAccount = BankAccount
        self.BankPassWord = BankPassWord
        self.AccountID = AccountID
        self.Password = Password
        self.CurrencyID = CurrencyID
        self.TradeAmount = float(TradeAmount)
        self.Digest = Digest


class ReqDayEndFileReadyField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 FileBusinessCode='', Digest=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.FileBusinessCode = FileBusinessCode
        self.Digest = Digest


class ReturnResultField(Base):
    def __init__(self, ReturnCode='', DescrInfoForReturnCode=''):
        self.ReturnCode = ReturnCode
        self.DescrInfoForReturnCode = DescrInfoForReturnCode


class VerifyFuturePasswordField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 AccountID='', Password='', BankAccount='', BankPassWord='', InstallID='', TID='', CurrencyID=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.AccountID = AccountID
        self.Password = Password
        self.BankAccount = BankAccount
        self.BankPassWord = BankPassWord
        self.InstallID = int(InstallID)
        self.TID = int(TID)
        self.CurrencyID = CurrencyID


class VerifyCustInfoField(Base):
    def __init__(self, CustomerName='', IdCardType='', IdentifiedCardNo='', CustType='', LongCustomerName=''):
        self.CustomerName = CustomerName
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.CustType = CustType
        self.LongCustomerName = LongCustomerName


class VerifyFuturePasswordAndCustInfoField(Base):
    def __init__(self, CustomerName='', IdCardType='', IdentifiedCardNo='', CustType='', AccountID='', Password='',
                 CurrencyID='', LongCustomerName=''):
        self.CustomerName = CustomerName
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.CustType = CustType
        self.AccountID = AccountID
        self.Password = Password
        self.CurrencyID = CurrencyID
        self.LongCustomerName = LongCustomerName


class DepositResultInformField(Base):
    def __init__(self, DepositSeqNo='', BrokerID='', InvestorID='', Deposit='', RequestID='', ReturnCode='',
                 DescrInfoForReturnCode=''):
        self.DepositSeqNo = DepositSeqNo
        self.BrokerID = BrokerID
        self.InvestorID = InvestorID
        self.Deposit = float(Deposit)
        self.RequestID = int(RequestID)
        self.ReturnCode = ReturnCode
        self.DescrInfoForReturnCode = DescrInfoForReturnCode


class ReqSyncKeyField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 InstallID='', UserID='', Message='', DeviceID='', BrokerIDByBank='', OperNo='', RequestID='', TID=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = UserID
        self.Message = Message
        self.DeviceID = DeviceID
        self.BrokerIDByBank = BrokerIDByBank
        self.OperNo = OperNo
        self.RequestID = int(RequestID)
        self.TID = int(TID)


class RspSyncKeyField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 InstallID='', UserID='', Message='', DeviceID='', BrokerIDByBank='', OperNo='', RequestID='', TID='',
                 ErrorID='', ErrorMsg=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = UserID
        self.Message = Message
        self.DeviceID = DeviceID
        self.BrokerIDByBank = BrokerIDByBank
        self.OperNo = OperNo
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg


class NotifyQueryAccountField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', CustType='', BankAccount='', BankPassWord='',
                 AccountID='', Password='', FutureSerial='', InstallID='', UserID='', VerifyCertNoFlag='',
                 CurrencyID='', Digest='', BankAccType='', DeviceID='', BankSecuAccType='', BrokerIDByBank='',
                 BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='', OperNo='', RequestID='', TID='', BankUseAmount='',
                 BankFetchAmount='', ErrorID='', ErrorMsg='', LongCustomerName=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.CustomerName = CustomerName
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.CustType = CustType
        self.BankAccount = BankAccount
        self.BankPassWord = BankPassWord
        self.AccountID = AccountID
        self.Password = Password
        self.FutureSerial = int(FutureSerial)
        self.InstallID = int(InstallID)
        self.UserID = UserID
        self.VerifyCertNoFlag = VerifyCertNoFlag
        self.CurrencyID = CurrencyID
        self.Digest = Digest
        self.BankAccType = BankAccType
        self.DeviceID = DeviceID
        self.BankSecuAccType = BankSecuAccType
        self.BrokerIDByBank = BrokerIDByBank
        self.BankSecuAcc = BankSecuAcc
        self.BankPwdFlag = BankPwdFlag
        self.SecuPwdFlag = SecuPwdFlag
        self.OperNo = OperNo
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.BankUseAmount = float(BankUseAmount)
        self.BankFetchAmount = float(BankFetchAmount)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg
        self.LongCustomerName = LongCustomerName


class TransferSerialField(Base):
    def __init__(self, PlateSerial='', TradeDate='', TradingDay='', TradeTime='', TradeCode='', SessionID='', BankID='',
                 BankBranchID='', BankAccType='', BankAccount='', BankSerial='', BrokerID='', BrokerBranchID='',
                 FutureAccType='', AccountID='', InvestorID='', FutureSerial='', IdCardType='', IdentifiedCardNo='',
                 CurrencyID='', TradeAmount='', CustFee='', BrokerFee='', AvailabilityFlag='', OperatorCode='',
                 BankNewAccount='', ErrorID='', ErrorMsg=''):
        self.PlateSerial = int(PlateSerial)
        self.TradeDate = TradeDate
        self.TradingDay = TradingDay
        self.TradeTime = TradeTime
        self.TradeCode = TradeCode
        self.SessionID = int(SessionID)
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BankAccType = BankAccType
        self.BankAccount = BankAccount
        self.BankSerial = BankSerial
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.FutureAccType = FutureAccType
        self.AccountID = AccountID
        self.InvestorID = InvestorID
        self.FutureSerial = int(FutureSerial)
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.CurrencyID = CurrencyID
        self.TradeAmount = float(TradeAmount)
        self.CustFee = float(CustFee)
        self.BrokerFee = float(BrokerFee)
        self.AvailabilityFlag = AvailabilityFlag
        self.OperatorCode = OperatorCode
        self.BankNewAccount = BankNewAccount
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg


class QryTransferSerialField(Base):
    def __init__(self, BrokerID='', AccountID='', BankID='', CurrencyID=''):
        self.BrokerID = BrokerID
        self.AccountID = AccountID
        self.BankID = BankID
        self.CurrencyID = CurrencyID


class NotifyFutureSignInField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 InstallID='', UserID='', Digest='', CurrencyID='', DeviceID='', BrokerIDByBank='', OperNo='',
                 RequestID='', TID='', ErrorID='', ErrorMsg='', PinKey='', MacKey=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = UserID
        self.Digest = Digest
        self.CurrencyID = CurrencyID
        self.DeviceID = DeviceID
        self.BrokerIDByBank = BrokerIDByBank
        self.OperNo = OperNo
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg
        self.PinKey = PinKey
        self.MacKey = MacKey


class NotifyFutureSignOutField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 InstallID='', UserID='', Digest='', CurrencyID='', DeviceID='', BrokerIDByBank='', OperNo='',
                 RequestID='', TID='', ErrorID='', ErrorMsg=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = UserID
        self.Digest = Digest
        self.CurrencyID = CurrencyID
        self.DeviceID = DeviceID
        self.BrokerIDByBank = BrokerIDByBank
        self.OperNo = OperNo
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg


class NotifySyncKeyField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 InstallID='', UserID='', Message='', DeviceID='', BrokerIDByBank='', OperNo='', RequestID='', TID='',
                 ErrorID='', ErrorMsg=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = UserID
        self.Message = Message
        self.DeviceID = DeviceID
        self.BrokerIDByBank = BrokerIDByBank
        self.OperNo = OperNo
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg


class QryAccountregisterField(Base):
    def __init__(self, BrokerID='', AccountID='', BankID='', BankBranchID='', CurrencyID=''):
        self.BrokerID = BrokerID
        self.AccountID = AccountID
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.CurrencyID = CurrencyID


class AccountregisterField(Base):
    def __init__(self, TradeDay='', BankID='', BankBranchID='', BankAccount='', BrokerID='', BrokerBranchID='',
                 AccountID='', IdCardType='', IdentifiedCardNo='', CustomerName='', CurrencyID='', OpenOrDestroy='',
                 RegDate='', OutDate='', TID='', CustType='', BankAccType='', LongCustomerName=''):
        self.TradeDay = TradeDay
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BankAccount = BankAccount
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.AccountID = AccountID
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.CustomerName = CustomerName
        self.CurrencyID = CurrencyID
        self.OpenOrDestroy = OpenOrDestroy
        self.RegDate = RegDate
        self.OutDate = OutDate
        self.TID = int(TID)
        self.CustType = CustType
        self.BankAccType = BankAccType
        self.LongCustomerName = LongCustomerName


class OpenAccountField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', Gender='', CountryCode='', CustType='',
                 Address='', ZipCode='', Telephone='', MobilePhone='', Fax='', EMail='', MoneyAccountStatus='',
                 BankAccount='', BankPassWord='', AccountID='', Password='', InstallID='', VerifyCertNoFlag='',
                 CurrencyID='', CashExchangeCode='', Digest='', BankAccType='', DeviceID='', BankSecuAccType='',
                 BrokerIDByBank='', BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='', OperNo='', TID='', UserID='',
                 ErrorID='', ErrorMsg='', LongCustomerName=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.CustomerName = CustomerName
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.Gender = Gender
        self.CountryCode = CountryCode
        self.CustType = CustType
        self.Address = Address
        self.ZipCode = ZipCode
        self.Telephone = Telephone
        self.MobilePhone = MobilePhone
        self.Fax = Fax
        self.EMail = EMail
        self.MoneyAccountStatus = MoneyAccountStatus
        self.BankAccount = BankAccount
        self.BankPassWord = BankPassWord
        self.AccountID = AccountID
        self.Password = Password
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = VerifyCertNoFlag
        self.CurrencyID = CurrencyID
        self.CashExchangeCode = CashExchangeCode
        self.Digest = Digest
        self.BankAccType = BankAccType
        self.DeviceID = DeviceID
        self.BankSecuAccType = BankSecuAccType
        self.BrokerIDByBank = BrokerIDByBank
        self.BankSecuAcc = BankSecuAcc
        self.BankPwdFlag = BankPwdFlag
        self.SecuPwdFlag = SecuPwdFlag
        self.OperNo = OperNo
        self.TID = int(TID)
        self.UserID = UserID
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg
        self.LongCustomerName = LongCustomerName


class CancelAccountField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', Gender='', CountryCode='', CustType='',
                 Address='', ZipCode='', Telephone='', MobilePhone='', Fax='', EMail='', MoneyAccountStatus='',
                 BankAccount='', BankPassWord='', AccountID='', Password='', InstallID='', VerifyCertNoFlag='',
                 CurrencyID='', CashExchangeCode='', Digest='', BankAccType='', DeviceID='', BankSecuAccType='',
                 BrokerIDByBank='', BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='', OperNo='', TID='', UserID='',
                 ErrorID='', ErrorMsg='', LongCustomerName=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.CustomerName = CustomerName
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.Gender = Gender
        self.CountryCode = CountryCode
        self.CustType = CustType
        self.Address = Address
        self.ZipCode = ZipCode
        self.Telephone = Telephone
        self.MobilePhone = MobilePhone
        self.Fax = Fax
        self.EMail = EMail
        self.MoneyAccountStatus = MoneyAccountStatus
        self.BankAccount = BankAccount
        self.BankPassWord = BankPassWord
        self.AccountID = AccountID
        self.Password = Password
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = VerifyCertNoFlag
        self.CurrencyID = CurrencyID
        self.CashExchangeCode = CashExchangeCode
        self.Digest = Digest
        self.BankAccType = BankAccType
        self.DeviceID = DeviceID
        self.BankSecuAccType = BankSecuAccType
        self.BrokerIDByBank = BrokerIDByBank
        self.BankSecuAcc = BankSecuAcc
        self.BankPwdFlag = BankPwdFlag
        self.SecuPwdFlag = SecuPwdFlag
        self.OperNo = OperNo
        self.TID = int(TID)
        self.UserID = UserID
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg
        self.LongCustomerName = LongCustomerName


class ChangeAccountField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', Gender='', CountryCode='', CustType='',
                 Address='', ZipCode='', Telephone='', MobilePhone='', Fax='', EMail='', MoneyAccountStatus='',
                 BankAccount='', BankPassWord='', NewBankAccount='', NewBankPassWord='', AccountID='', Password='',
                 BankAccType='', InstallID='', VerifyCertNoFlag='', CurrencyID='', BrokerIDByBank='', BankPwdFlag='',
                 SecuPwdFlag='', TID='', Digest='', ErrorID='', ErrorMsg='', LongCustomerName=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.CustomerName = CustomerName
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.Gender = Gender
        self.CountryCode = CountryCode
        self.CustType = CustType
        self.Address = Address
        self.ZipCode = ZipCode
        self.Telephone = Telephone
        self.MobilePhone = MobilePhone
        self.Fax = Fax
        self.EMail = EMail
        self.MoneyAccountStatus = MoneyAccountStatus
        self.BankAccount = BankAccount
        self.BankPassWord = BankPassWord
        self.NewBankAccount = NewBankAccount
        self.NewBankPassWord = NewBankPassWord
        self.AccountID = AccountID
        self.Password = Password
        self.BankAccType = BankAccType
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = VerifyCertNoFlag
        self.CurrencyID = CurrencyID
        self.BrokerIDByBank = BrokerIDByBank
        self.BankPwdFlag = BankPwdFlag
        self.SecuPwdFlag = SecuPwdFlag
        self.TID = int(TID)
        self.Digest = Digest
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg
        self.LongCustomerName = LongCustomerName


class SecAgentACIDMapField(Base):
    def __init__(self, BrokerID='', UserID='', AccountID='', CurrencyID='', BrokerSecAgentID=''):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.AccountID = AccountID
        self.CurrencyID = CurrencyID
        self.BrokerSecAgentID = BrokerSecAgentID


class QrySecAgentACIDMapField(Base):
    def __init__(self, BrokerID='', UserID='', AccountID='', CurrencyID=''):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.AccountID = AccountID
        self.CurrencyID = CurrencyID


class UserRightsAssignField(Base):
    def __init__(self, BrokerID='', UserID='', DRIdentityID=''):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.DRIdentityID = int(DRIdentityID)


class BrokerUserRightAssignField(Base):
    def __init__(self, BrokerID='', DRIdentityID='', Tradeable=''):
        self.BrokerID = BrokerID
        self.DRIdentityID = int(DRIdentityID)
        self.Tradeable = int(Tradeable)


class DRTransferField(Base):
    def __init__(self, OrigDRIdentityID='', DestDRIdentityID='', OrigBrokerID='', DestBrokerID=''):
        self.OrigDRIdentityID = int(OrigDRIdentityID)
        self.DestDRIdentityID = int(DestDRIdentityID)
        self.OrigBrokerID = OrigBrokerID
        self.DestBrokerID = DestBrokerID


class FensUserInfoField(Base):
    def __init__(self, BrokerID='', UserID='', LoginMode=''):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.LoginMode = LoginMode


class CurrTransferIdentityField(Base):
    def __init__(self, IdentityID=''):
        self.IdentityID = int(IdentityID)


class LoginForbiddenUserField(Base):
    def __init__(self, BrokerID='', UserID='', IPAddress=''):
        self.BrokerID = BrokerID
        self.UserID = UserID
        self.IPAddress = IPAddress


class QryLoginForbiddenUserField(Base):
    def __init__(self, BrokerID='', UserID=''):
        self.BrokerID = BrokerID
        self.UserID = UserID


class MulticastGroupInfoField(Base):
    def __init__(self, GroupIP='', GroupPort='', SourceIP=''):
        self.GroupIP = GroupIP
        self.GroupPort = int(GroupPort)
        self.SourceIP = SourceIP


class TradingAccountReserveField(Base):
    def __init__(self, BrokerID='', AccountID='', Reserve='', CurrencyID=''):
        self.BrokerID = BrokerID
        self.AccountID = AccountID
        self.Reserve = float(Reserve)
        self.CurrencyID = CurrencyID


class ReserveOpenAccountConfirmField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', Gender='', CountryCode='', CustType='',
                 Address='', ZipCode='', Telephone='', MobilePhone='', Fax='', EMail='', MoneyAccountStatus='',
                 BankAccount='', BankPassWord='', InstallID='', VerifyCertNoFlag='', CurrencyID='', Digest='',
                 BankAccType='', BrokerIDByBank='', TID='', AccountID='', Password='', BankReserveOpenSeq='',
                 BookDate='', BookPsw='', ErrorID='', ErrorMsg=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.CustomerName = CustomerName
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.Gender = Gender
        self.CountryCode = CountryCode
        self.CustType = CustType
        self.Address = Address
        self.ZipCode = ZipCode
        self.Telephone = Telephone
        self.MobilePhone = MobilePhone
        self.Fax = Fax
        self.EMail = EMail
        self.MoneyAccountStatus = MoneyAccountStatus
        self.BankAccount = BankAccount
        self.BankPassWord = BankPassWord
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = VerifyCertNoFlag
        self.CurrencyID = CurrencyID
        self.Digest = Digest
        self.BankAccType = BankAccType
        self.BrokerIDByBank = BrokerIDByBank
        self.TID = int(TID)
        self.AccountID = AccountID
        self.Password = Password
        self.BankReserveOpenSeq = BankReserveOpenSeq
        self.BookDate = BookDate
        self.BookPsw = BookPsw
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg


class ReserveOpenAccountField(Base):
    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', Gender='', CountryCode='', CustType='',
                 Address='', ZipCode='', Telephone='', MobilePhone='', Fax='', EMail='', MoneyAccountStatus='',
                 BankAccount='', BankPassWord='', InstallID='', VerifyCertNoFlag='', CurrencyID='', Digest='',
                 BankAccType='', BrokerIDByBank='', TID='', ReserveOpenAccStas='', ErrorID='', ErrorMsg=''):
        self.TradeCode = TradeCode
        self.BankID = BankID
        self.BankBranchID = BankBranchID
        self.BrokerID = BrokerID
        self.BrokerBranchID = BrokerBranchID
        self.TradeDate = TradeDate
        self.TradeTime = TradeTime
        self.BankSerial = BankSerial
        self.TradingDay = TradingDay
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = LastFragment
        self.SessionID = int(SessionID)
        self.CustomerName = CustomerName
        self.IdCardType = IdCardType
        self.IdentifiedCardNo = IdentifiedCardNo
        self.Gender = Gender
        self.CountryCode = CountryCode
        self.CustType = CustType
        self.Address = Address
        self.ZipCode = ZipCode
        self.Telephone = Telephone
        self.MobilePhone = MobilePhone
        self.Fax = Fax
        self.EMail = EMail
        self.MoneyAccountStatus = MoneyAccountStatus
        self.BankAccount = BankAccount
        self.BankPassWord = BankPassWord
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = VerifyCertNoFlag
        self.CurrencyID = CurrencyID
        self.Digest = Digest
        self.BankAccType = BankAccType
        self.BrokerIDByBank = BrokerIDByBank
        self.TID = int(TID)
        self.ReserveOpenAccStas = ReserveOpenAccStas
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = ErrorMsg
