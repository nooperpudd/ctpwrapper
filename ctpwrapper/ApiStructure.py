# encoding=utf-8
import ctypes

from ctpwrapper.base import Base


class DisseminationField(Base):
    _fields_ = [
        ('SequenceSeries', ctypes.c_short),
        ('SequenceNo', ctypes.c_int),
    ]

    def __init__(self, SequenceSeries='', SequenceNo=''):
        super(DisseminationField, self).__init__()
        self.SequenceSeries = int(SequenceSeries)
        self.SequenceNo = int(SequenceNo)


class ReqUserLoginField(Base):
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('Password', ctypes.c_char * 41),
        ('UserProductInfo', ctypes.c_char * 11),
        ('InterfaceProductInfo', ctypes.c_char * 11),
        ('ProtocolInfo', ctypes.c_char * 11),
        ('MacAddress', ctypes.c_char * 21),
        ('OneTimePassword', ctypes.c_char * 41),
        ('ClientIPAddress', ctypes.c_char * 16),
        ('LoginRemark', ctypes.c_char * 36),
    ]

    def __init__(self, TradingDay='', BrokerID='', UserID='', Password='', UserProductInfo='', InterfaceProductInfo='',
                 ProtocolInfo='', MacAddress='', OneTimePassword='', ClientIPAddress='', LoginRemark=''):
        super(ReqUserLoginField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.Password = self._to_bytes(Password)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.InterfaceProductInfo = self._to_bytes(InterfaceProductInfo)
        self.ProtocolInfo = self._to_bytes(ProtocolInfo)
        self.MacAddress = self._to_bytes(MacAddress)
        self.OneTimePassword = self._to_bytes(OneTimePassword)
        self.ClientIPAddress = self._to_bytes(ClientIPAddress)
        self.LoginRemark = self._to_bytes(LoginRemark)


class RspUserLoginField(Base):
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),
        ('LoginTime', ctypes.c_char * 9),
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('SystemName', ctypes.c_char * 41),
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('MaxOrderRef', ctypes.c_char * 13),
        ('SHFETime', ctypes.c_char * 9),
        ('DCETime', ctypes.c_char * 9),
        ('CZCETime', ctypes.c_char * 9),
        ('FFEXTime', ctypes.c_char * 9),
        ('INETime', ctypes.c_char * 9),
    ]

    def __init__(self, TradingDay='', LoginTime='', BrokerID='', UserID='', SystemName='', FrontID='', SessionID='',
                 MaxOrderRef='', SHFETime='', DCETime='', CZCETime='', FFEXTime='', INETime=''):
        super(RspUserLoginField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.LoginTime = self._to_bytes(LoginTime)
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.SystemName = self._to_bytes(SystemName)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.MaxOrderRef = self._to_bytes(MaxOrderRef)
        self.SHFETime = self._to_bytes(SHFETime)
        self.DCETime = self._to_bytes(DCETime)
        self.CZCETime = self._to_bytes(CZCETime)
        self.FFEXTime = self._to_bytes(FFEXTime)
        self.INETime = self._to_bytes(INETime)


class UserLogoutField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
    ]

    def __init__(self, BrokerID='', UserID=''):
        super(UserLogoutField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)


class ForceUserLogoutField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
    ]

    def __init__(self, BrokerID='', UserID=''):
        super(ForceUserLogoutField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)


class ReqAuthenticateField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('UserProductInfo', ctypes.c_char * 11),
        ('AuthCode', ctypes.c_char * 17),
    ]

    def __init__(self, BrokerID='', UserID='', UserProductInfo='', AuthCode=''):
        super(ReqAuthenticateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.AuthCode = self._to_bytes(AuthCode)


class RspAuthenticateField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('UserProductInfo', ctypes.c_char * 11),
    ]

    def __init__(self, BrokerID='', UserID='', UserProductInfo=''):
        super(RspAuthenticateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.UserProductInfo = self._to_bytes(UserProductInfo)


class AuthenticationInfoField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('UserProductInfo', ctypes.c_char * 11),
        ('AuthInfo', ctypes.c_char * 129),
        ('IsResult', ctypes.c_int),
    ]

    def __init__(self, BrokerID='', UserID='', UserProductInfo='', AuthInfo='', IsResult=''):
        super(AuthenticationInfoField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.AuthInfo = self._to_bytes(AuthInfo)
        self.IsResult = int(IsResult)


class TransferHeaderField(Base):
    _fields_ = [
        ('Version', ctypes.c_char * 4),
        ('TradeCode', ctypes.c_char * 7),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('TradeSerial', ctypes.c_char * 9),
        ('FutureID', ctypes.c_char * 11),
        ('BankID', ctypes.c_char * 4),
        ('BankBrchID', ctypes.c_char * 5),
        ('OperNo', ctypes.c_char * 17),
        ('DeviceID', ctypes.c_char * 3),
        ('RecordNum', ctypes.c_char * 7),
        ('SessionID', ctypes.c_int),
        ('RequestID', ctypes.c_int),
    ]

    def __init__(self, Version='', TradeCode='', TradeDate='', TradeTime='', TradeSerial='', FutureID='', BankID='',
                 BankBrchID='', OperNo='', DeviceID='', RecordNum='', SessionID='', RequestID=''):
        super(TransferHeaderField, self).__init__()
        self.Version = self._to_bytes(Version)
        self.TradeCode = self._to_bytes(TradeCode)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.TradeSerial = self._to_bytes(TradeSerial)
        self.FutureID = self._to_bytes(FutureID)
        self.BankID = self._to_bytes(BankID)
        self.BankBrchID = self._to_bytes(BankBrchID)
        self.OperNo = self._to_bytes(OperNo)
        self.DeviceID = self._to_bytes(DeviceID)
        self.RecordNum = self._to_bytes(RecordNum)
        self.SessionID = int(SessionID)
        self.RequestID = int(RequestID)


class TransferBankToFutureReqField(Base):
    _fields_ = [
        ('FutureAccount', ctypes.c_char * 13),
        ('FuturePwdFlag', ctypes.c_char),
        ('FutureAccPwd', ctypes.c_char * 17),
        ('TradeAmt', ctypes.c_double),
        ('CustFee', ctypes.c_double),
        ('CurrencyCode', ctypes.c_char * 4),
    ]

    def __init__(self, FutureAccount='', FuturePwdFlag='', FutureAccPwd='', TradeAmt='', CustFee='', CurrencyCode=''):
        super(TransferBankToFutureReqField, self).__init__()
        self.FutureAccount = self._to_bytes(FutureAccount)
        self.FuturePwdFlag = self._to_bytes(FuturePwdFlag)
        self.FutureAccPwd = self._to_bytes(FutureAccPwd)
        self.TradeAmt = float(TradeAmt)
        self.CustFee = float(CustFee)
        self.CurrencyCode = self._to_bytes(CurrencyCode)


class TransferBankToFutureRspField(Base):
    _fields_ = [
        ('RetCode', ctypes.c_char * 5),
        ('RetInfo', ctypes.c_char * 129),
        ('FutureAccount', ctypes.c_char * 13),
        ('TradeAmt', ctypes.c_double),
        ('CustFee', ctypes.c_double),
        ('CurrencyCode', ctypes.c_char * 4),
    ]

    def __init__(self, RetCode='', RetInfo='', FutureAccount='', TradeAmt='', CustFee='', CurrencyCode=''):
        super(TransferBankToFutureRspField, self).__init__()
        self.RetCode = self._to_bytes(RetCode)
        self.RetInfo = self._to_bytes(RetInfo)
        self.FutureAccount = self._to_bytes(FutureAccount)
        self.TradeAmt = float(TradeAmt)
        self.CustFee = float(CustFee)
        self.CurrencyCode = self._to_bytes(CurrencyCode)


class TransferFutureToBankReqField(Base):
    _fields_ = [
        ('FutureAccount', ctypes.c_char * 13),
        ('FuturePwdFlag', ctypes.c_char),
        ('FutureAccPwd', ctypes.c_char * 17),
        ('TradeAmt', ctypes.c_double),
        ('CustFee', ctypes.c_double),
        ('CurrencyCode', ctypes.c_char * 4),
    ]

    def __init__(self, FutureAccount='', FuturePwdFlag='', FutureAccPwd='', TradeAmt='', CustFee='', CurrencyCode=''):
        super(TransferFutureToBankReqField, self).__init__()
        self.FutureAccount = self._to_bytes(FutureAccount)
        self.FuturePwdFlag = self._to_bytes(FuturePwdFlag)
        self.FutureAccPwd = self._to_bytes(FutureAccPwd)
        self.TradeAmt = float(TradeAmt)
        self.CustFee = float(CustFee)
        self.CurrencyCode = self._to_bytes(CurrencyCode)


class TransferFutureToBankRspField(Base):
    _fields_ = [
        ('RetCode', ctypes.c_char * 5),
        ('RetInfo', ctypes.c_char * 129),
        ('FutureAccount', ctypes.c_char * 13),
        ('TradeAmt', ctypes.c_double),
        ('CustFee', ctypes.c_double),
        ('CurrencyCode', ctypes.c_char * 4),
    ]

    def __init__(self, RetCode='', RetInfo='', FutureAccount='', TradeAmt='', CustFee='', CurrencyCode=''):
        super(TransferFutureToBankRspField, self).__init__()
        self.RetCode = self._to_bytes(RetCode)
        self.RetInfo = self._to_bytes(RetInfo)
        self.FutureAccount = self._to_bytes(FutureAccount)
        self.TradeAmt = float(TradeAmt)
        self.CustFee = float(CustFee)
        self.CurrencyCode = self._to_bytes(CurrencyCode)


class TransferQryBankReqField(Base):
    _fields_ = [
        ('FutureAccount', ctypes.c_char * 13),
        ('FuturePwdFlag', ctypes.c_char),
        ('FutureAccPwd', ctypes.c_char * 17),
        ('CurrencyCode', ctypes.c_char * 4),
    ]

    def __init__(self, FutureAccount='', FuturePwdFlag='', FutureAccPwd='', CurrencyCode=''):
        super(TransferQryBankReqField, self).__init__()
        self.FutureAccount = self._to_bytes(FutureAccount)
        self.FuturePwdFlag = self._to_bytes(FuturePwdFlag)
        self.FutureAccPwd = self._to_bytes(FutureAccPwd)
        self.CurrencyCode = self._to_bytes(CurrencyCode)


class TransferQryBankRspField(Base):
    _fields_ = [
        ('RetCode', ctypes.c_char * 5),
        ('RetInfo', ctypes.c_char * 129),
        ('FutureAccount', ctypes.c_char * 13),
        ('TradeAmt', ctypes.c_double),
        ('UseAmt', ctypes.c_double),
        ('FetchAmt', ctypes.c_double),
        ('CurrencyCode', ctypes.c_char * 4),
    ]

    def __init__(self, RetCode='', RetInfo='', FutureAccount='', TradeAmt='', UseAmt='', FetchAmt='', CurrencyCode=''):
        super(TransferQryBankRspField, self).__init__()
        self.RetCode = self._to_bytes(RetCode)
        self.RetInfo = self._to_bytes(RetInfo)
        self.FutureAccount = self._to_bytes(FutureAccount)
        self.TradeAmt = float(TradeAmt)
        self.UseAmt = float(UseAmt)
        self.FetchAmt = float(FetchAmt)
        self.CurrencyCode = self._to_bytes(CurrencyCode)


class TransferQryDetailReqField(Base):
    _fields_ = [
        ('FutureAccount', ctypes.c_char * 13),
    ]

    def __init__(self, FutureAccount=''):
        super(TransferQryDetailReqField, self).__init__()
        self.FutureAccount = self._to_bytes(FutureAccount)


class TransferQryDetailRspField(Base):
    _fields_ = [
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('TradeCode', ctypes.c_char * 7),
        ('FutureSerial', ctypes.c_int),
        ('FutureID', ctypes.c_char * 11),
        ('FutureAccount', ctypes.c_char * 22),
        ('BankSerial', ctypes.c_int),
        ('BankID', ctypes.c_char * 4),
        ('BankBrchID', ctypes.c_char * 5),
        ('BankAccount', ctypes.c_char * 41),
        ('CertCode', ctypes.c_char * 21),
        ('CurrencyCode', ctypes.c_char * 4),
        ('TxAmount', ctypes.c_double),
        ('Flag', ctypes.c_char),
    ]

    def __init__(self, TradeDate='', TradeTime='', TradeCode='', FutureSerial='', FutureID='', FutureAccount='',
                 BankSerial='', BankID='', BankBrchID='', BankAccount='', CertCode='', CurrencyCode='', TxAmount='',
                 Flag=''):
        super(TransferQryDetailRspField, self).__init__()
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.TradeCode = self._to_bytes(TradeCode)
        self.FutureSerial = int(FutureSerial)
        self.FutureID = self._to_bytes(FutureID)
        self.FutureAccount = self._to_bytes(FutureAccount)
        self.BankSerial = int(BankSerial)
        self.BankID = self._to_bytes(BankID)
        self.BankBrchID = self._to_bytes(BankBrchID)
        self.BankAccount = self._to_bytes(BankAccount)
        self.CertCode = self._to_bytes(CertCode)
        self.CurrencyCode = self._to_bytes(CurrencyCode)
        self.TxAmount = float(TxAmount)
        self.Flag = self._to_bytes(Flag)


class RspInfoField(Base):
    _fields_ = [
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
    ]

    def __init__(self, ErrorID='', ErrorMsg=''):
        super(RspInfoField, self).__init__()
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class ExchangeField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('ExchangeName', ctypes.c_char * 61),
        ('ExchangeProperty', ctypes.c_char),
    ]

    def __init__(self, ExchangeID='', ExchangeName='', ExchangeProperty=''):
        super(ExchangeField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExchangeName = self._to_bytes(ExchangeName)
        self.ExchangeProperty = self._to_bytes(ExchangeProperty)


class ProductField(Base):
    _fields_ = [
        ('ProductID', ctypes.c_char * 31),
        ('ProductName', ctypes.c_char * 21),
        ('ExchangeID', ctypes.c_char * 9),
        ('ProductClass', ctypes.c_char),
        ('VolumeMultiple', ctypes.c_int),
        ('PriceTick', ctypes.c_double),
        ('MaxMarketOrderVolume', ctypes.c_int),
        ('MinMarketOrderVolume', ctypes.c_int),
        ('MaxLimitOrderVolume', ctypes.c_int),
        ('MinLimitOrderVolume', ctypes.c_int),
        ('PositionType', ctypes.c_char),
        ('PositionDateType', ctypes.c_char),
        ('CloseDealType', ctypes.c_char),
        ('TradeCurrencyID', ctypes.c_char * 4),
        ('MortgageFundUseRange', ctypes.c_char),
        ('ExchangeProductID', ctypes.c_char * 31),
        ('UnderlyingMultiple', ctypes.c_double),
    ]

    def __init__(self, ProductID='', ProductName='', ExchangeID='', ProductClass='', VolumeMultiple='', PriceTick='',
                 MaxMarketOrderVolume='', MinMarketOrderVolume='', MaxLimitOrderVolume='', MinLimitOrderVolume='',
                 PositionType='', PositionDateType='', CloseDealType='', TradeCurrencyID='', MortgageFundUseRange='',
                 ExchangeProductID='', UnderlyingMultiple=''):
        super(ProductField, self).__init__()
        self.ProductID = self._to_bytes(ProductID)
        self.ProductName = self._to_bytes(ProductName)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ProductClass = self._to_bytes(ProductClass)
        self.VolumeMultiple = int(VolumeMultiple)
        self.PriceTick = float(PriceTick)
        self.MaxMarketOrderVolume = int(MaxMarketOrderVolume)
        self.MinMarketOrderVolume = int(MinMarketOrderVolume)
        self.MaxLimitOrderVolume = int(MaxLimitOrderVolume)
        self.MinLimitOrderVolume = int(MinLimitOrderVolume)
        self.PositionType = self._to_bytes(PositionType)
        self.PositionDateType = self._to_bytes(PositionDateType)
        self.CloseDealType = self._to_bytes(CloseDealType)
        self.TradeCurrencyID = self._to_bytes(TradeCurrencyID)
        self.MortgageFundUseRange = self._to_bytes(MortgageFundUseRange)
        self.ExchangeProductID = self._to_bytes(ExchangeProductID)
        self.UnderlyingMultiple = float(UnderlyingMultiple)


class InstrumentField(Base):
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
        ('InstrumentName', ctypes.c_char * 21),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('ProductID', ctypes.c_char * 31),
        ('ProductClass', ctypes.c_char),
        ('DeliveryYear', ctypes.c_int),
        ('DeliveryMonth', ctypes.c_int),
        ('MaxMarketOrderVolume', ctypes.c_int),
        ('MinMarketOrderVolume', ctypes.c_int),
        ('MaxLimitOrderVolume', ctypes.c_int),
        ('MinLimitOrderVolume', ctypes.c_int),
        ('VolumeMultiple', ctypes.c_int),
        ('PriceTick', ctypes.c_double),
        ('CreateDate', ctypes.c_char * 9),
        ('OpenDate', ctypes.c_char * 9),
        ('ExpireDate', ctypes.c_char * 9),
        ('StartDelivDate', ctypes.c_char * 9),
        ('EndDelivDate', ctypes.c_char * 9),
        ('InstLifePhase', ctypes.c_char),
        ('IsTrading', ctypes.c_int),
        ('PositionType', ctypes.c_char),
        ('PositionDateType', ctypes.c_char),
        ('LongMarginRatio', ctypes.c_double),
        ('ShortMarginRatio', ctypes.c_double),
        ('MaxMarginSideAlgorithm', ctypes.c_char),
        ('UnderlyingInstrID', ctypes.c_char * 31),
        ('StrikePrice', ctypes.c_double),
        ('OptionsType', ctypes.c_char),
        ('UnderlyingMultiple', ctypes.c_double),
        ('CombinationType', ctypes.c_char),
    ]

    def __init__(self, InstrumentID='', ExchangeID='', InstrumentName='', ExchangeInstID='', ProductID='',
                 ProductClass='', DeliveryYear='', DeliveryMonth='', MaxMarketOrderVolume='', MinMarketOrderVolume='',
                 MaxLimitOrderVolume='', MinLimitOrderVolume='', VolumeMultiple='', PriceTick='', CreateDate='',
                 OpenDate='', ExpireDate='', StartDelivDate='', EndDelivDate='', InstLifePhase='', IsTrading='',
                 PositionType='', PositionDateType='', LongMarginRatio='', ShortMarginRatio='',
                 MaxMarginSideAlgorithm='', UnderlyingInstrID='', StrikePrice='', OptionsType='', UnderlyingMultiple='',
                 CombinationType=''):
        super(InstrumentField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentName = self._to_bytes(InstrumentName)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.ProductID = self._to_bytes(ProductID)
        self.ProductClass = self._to_bytes(ProductClass)
        self.DeliveryYear = int(DeliveryYear)
        self.DeliveryMonth = int(DeliveryMonth)
        self.MaxMarketOrderVolume = int(MaxMarketOrderVolume)
        self.MinMarketOrderVolume = int(MinMarketOrderVolume)
        self.MaxLimitOrderVolume = int(MaxLimitOrderVolume)
        self.MinLimitOrderVolume = int(MinLimitOrderVolume)
        self.VolumeMultiple = int(VolumeMultiple)
        self.PriceTick = float(PriceTick)
        self.CreateDate = self._to_bytes(CreateDate)
        self.OpenDate = self._to_bytes(OpenDate)
        self.ExpireDate = self._to_bytes(ExpireDate)
        self.StartDelivDate = self._to_bytes(StartDelivDate)
        self.EndDelivDate = self._to_bytes(EndDelivDate)
        self.InstLifePhase = self._to_bytes(InstLifePhase)
        self.IsTrading = int(IsTrading)
        self.PositionType = self._to_bytes(PositionType)
        self.PositionDateType = self._to_bytes(PositionDateType)
        self.LongMarginRatio = float(LongMarginRatio)
        self.ShortMarginRatio = float(ShortMarginRatio)
        self.MaxMarginSideAlgorithm = self._to_bytes(MaxMarginSideAlgorithm)
        self.UnderlyingInstrID = self._to_bytes(UnderlyingInstrID)
        self.StrikePrice = float(StrikePrice)
        self.OptionsType = self._to_bytes(OptionsType)
        self.UnderlyingMultiple = float(UnderlyingMultiple)
        self.CombinationType = self._to_bytes(CombinationType)


class BrokerField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerAbbr', ctypes.c_char * 9),
        ('BrokerName', ctypes.c_char * 81),
        ('IsActive', ctypes.c_int),
    ]

    def __init__(self, BrokerID='', BrokerAbbr='', BrokerName='', IsActive=''):
        super(BrokerField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerAbbr = self._to_bytes(BrokerAbbr)
        self.BrokerName = self._to_bytes(BrokerName)
        self.IsActive = int(IsActive)


class TraderField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
        ('ParticipantID', ctypes.c_char * 11),
        ('Password', ctypes.c_char * 41),
        ('InstallCount', ctypes.c_int),
        ('BrokerID', ctypes.c_char * 11),
    ]

    def __init__(self, ExchangeID='', TraderID='', ParticipantID='', Password='', InstallCount='', BrokerID=''):
        super(TraderField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.Password = self._to_bytes(Password)
        self.InstallCount = int(InstallCount)
        self.BrokerID = self._to_bytes(BrokerID)


class InvestorField(Base):
    _fields_ = [
        ('InvestorID', ctypes.c_char * 13),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorGroupID', ctypes.c_char * 13),
        ('InvestorName', ctypes.c_char * 81),
        ('IdentifiedCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('IsActive', ctypes.c_int),
        ('Telephone', ctypes.c_char * 41),
        ('Address', ctypes.c_char * 101),
        ('OpenDate', ctypes.c_char * 9),
        ('Mobile', ctypes.c_char * 41),
        ('CommModelID', ctypes.c_char * 13),
        ('MarginModelID', ctypes.c_char * 13),
    ]

    def __init__(self, InvestorID='', BrokerID='', InvestorGroupID='', InvestorName='', IdentifiedCardType='',
                 IdentifiedCardNo='', IsActive='', Telephone='', Address='', OpenDate='', Mobile='', CommModelID='',
                 MarginModelID=''):
        super(InvestorField, self).__init__()
        self.InvestorID = self._to_bytes(InvestorID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorGroupID = self._to_bytes(InvestorGroupID)
        self.InvestorName = self._to_bytes(InvestorName)
        self.IdentifiedCardType = self._to_bytes(IdentifiedCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.IsActive = int(IsActive)
        self.Telephone = self._to_bytes(Telephone)
        self.Address = self._to_bytes(Address)
        self.OpenDate = self._to_bytes(OpenDate)
        self.Mobile = self._to_bytes(Mobile)
        self.CommModelID = self._to_bytes(CommModelID)
        self.MarginModelID = self._to_bytes(MarginModelID)


class TradingCodeField(Base):
    _fields_ = [
        ('InvestorID', ctypes.c_char * 13),
        ('BrokerID', ctypes.c_char * 11),
        ('ExchangeID', ctypes.c_char * 9),
        ('ClientID', ctypes.c_char * 11),
        ('IsActive', ctypes.c_int),
        ('ClientIDType', ctypes.c_char),
    ]

    def __init__(self, InvestorID='', BrokerID='', ExchangeID='', ClientID='', IsActive='', ClientIDType=''):
        super(TradingCodeField, self).__init__()
        self.InvestorID = self._to_bytes(InvestorID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ClientID = self._to_bytes(ClientID)
        self.IsActive = int(IsActive)
        self.ClientIDType = self._to_bytes(ClientIDType)


class PartBrokerField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('ExchangeID', ctypes.c_char * 9),
        ('ParticipantID', ctypes.c_char * 11),
        ('IsActive', ctypes.c_int),
    ]

    def __init__(self, BrokerID='', ExchangeID='', ParticipantID='', IsActive=''):
        super(PartBrokerField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.IsActive = int(IsActive)


class SuperUserField(Base):
    _fields_ = [
        ('UserID', ctypes.c_char * 16),
        ('UserName', ctypes.c_char * 81),
        ('Password', ctypes.c_char * 41),
        ('IsActive', ctypes.c_int),
    ]

    def __init__(self, UserID='', UserName='', Password='', IsActive=''):
        super(SuperUserField, self).__init__()
        self.UserID = self._to_bytes(UserID)
        self.UserName = self._to_bytes(UserName)
        self.Password = self._to_bytes(Password)
        self.IsActive = int(IsActive)


class SuperUserFunctionField(Base):
    _fields_ = [
        ('UserID', ctypes.c_char * 16),
        ('FunctionCode', ctypes.c_char),
    ]

    def __init__(self, UserID='', FunctionCode=''):
        super(SuperUserFunctionField, self).__init__()
        self.UserID = self._to_bytes(UserID)
        self.FunctionCode = self._to_bytes(FunctionCode)


class InvestorGroupField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorGroupID', ctypes.c_char * 13),
        ('InvestorGroupName', ctypes.c_char * 41),
    ]

    def __init__(self, BrokerID='', InvestorGroupID='', InvestorGroupName=''):
        super(InvestorGroupField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorGroupID = self._to_bytes(InvestorGroupID)
        self.InvestorGroupName = self._to_bytes(InvestorGroupName)


class TradingAccountField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('AccountID', ctypes.c_char * 13),
        ('PreMortgage', ctypes.c_double),
        ('PreCredit', ctypes.c_double),
        ('PreDeposit', ctypes.c_double),
        ('PreBalance', ctypes.c_double),
        ('PreMargin', ctypes.c_double),
        ('InterestBase', ctypes.c_double),
        ('Interest', ctypes.c_double),
        ('Deposit', ctypes.c_double),
        ('Withdraw', ctypes.c_double),
        ('FrozenMargin', ctypes.c_double),
        ('FrozenCash', ctypes.c_double),
        ('FrozenCommission', ctypes.c_double),
        ('CurrMargin', ctypes.c_double),
        ('CashIn', ctypes.c_double),
        ('Commission', ctypes.c_double),
        ('CloseProfit', ctypes.c_double),
        ('PositionProfit', ctypes.c_double),
        ('Balance', ctypes.c_double),
        ('Available', ctypes.c_double),
        ('WithdrawQuota', ctypes.c_double),
        ('Reserve', ctypes.c_double),
        ('TradingDay', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
        ('Credit', ctypes.c_double),
        ('Mortgage', ctypes.c_double),
        ('ExchangeMargin', ctypes.c_double),
        ('DeliveryMargin', ctypes.c_double),
        ('ExchangeDeliveryMargin', ctypes.c_double),
        ('ReserveBalance', ctypes.c_double),
        ('CurrencyID', ctypes.c_char * 4),
        ('PreFundMortgageIn', ctypes.c_double),
        ('PreFundMortgageOut', ctypes.c_double),
        ('FundMortgageIn', ctypes.c_double),
        ('FundMortgageOut', ctypes.c_double),
        ('FundMortgageAvailable', ctypes.c_double),
        ('MortgageableFund', ctypes.c_double),
        ('SpecProductMargin', ctypes.c_double),
        ('SpecProductFrozenMargin', ctypes.c_double),
        ('SpecProductCommission', ctypes.c_double),
        ('SpecProductFrozenCommission', ctypes.c_double),
        ('SpecProductPositionProfit', ctypes.c_double),
        ('SpecProductCloseProfit', ctypes.c_double),
        ('SpecProductPositionProfitByAlg', ctypes.c_double),
        ('SpecProductExchangeMargin', ctypes.c_double),
    ]

    def __init__(self, BrokerID='', AccountID='', PreMortgage='', PreCredit='', PreDeposit='', PreBalance='',
                 PreMargin='', InterestBase='', Interest='', Deposit='', Withdraw='', FrozenMargin='', FrozenCash='',
                 FrozenCommission='', CurrMargin='', CashIn='', Commission='', CloseProfit='', PositionProfit='',
                 Balance='', Available='', WithdrawQuota='', Reserve='', TradingDay='', SettlementID='', Credit='',
                 Mortgage='', ExchangeMargin='', DeliveryMargin='', ExchangeDeliveryMargin='', ReserveBalance='',
                 CurrencyID='', PreFundMortgageIn='', PreFundMortgageOut='', FundMortgageIn='', FundMortgageOut='',
                 FundMortgageAvailable='', MortgageableFund='', SpecProductMargin='', SpecProductFrozenMargin='',
                 SpecProductCommission='', SpecProductFrozenCommission='', SpecProductPositionProfit='',
                 SpecProductCloseProfit='', SpecProductPositionProfitByAlg='', SpecProductExchangeMargin=''):
        super(TradingAccountField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AccountID = self._to_bytes(AccountID)
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
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.Credit = float(Credit)
        self.Mortgage = float(Mortgage)
        self.ExchangeMargin = float(ExchangeMargin)
        self.DeliveryMargin = float(DeliveryMargin)
        self.ExchangeDeliveryMargin = float(ExchangeDeliveryMargin)
        self.ReserveBalance = float(ReserveBalance)
        self.CurrencyID = self._to_bytes(CurrencyID)
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
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('PosiDirection', ctypes.c_char),
        ('HedgeFlag', ctypes.c_char),
        ('PositionDate', ctypes.c_char),
        ('YdPosition', ctypes.c_int),
        ('Position', ctypes.c_int),
        ('LongFrozen', ctypes.c_int),
        ('ShortFrozen', ctypes.c_int),
        ('LongFrozenAmount', ctypes.c_double),
        ('ShortFrozenAmount', ctypes.c_double),
        ('OpenVolume', ctypes.c_int),
        ('CloseVolume', ctypes.c_int),
        ('OpenAmount', ctypes.c_double),
        ('CloseAmount', ctypes.c_double),
        ('PositionCost', ctypes.c_double),
        ('PreMargin', ctypes.c_double),
        ('UseMargin', ctypes.c_double),
        ('FrozenMargin', ctypes.c_double),
        ('FrozenCash', ctypes.c_double),
        ('FrozenCommission', ctypes.c_double),
        ('CashIn', ctypes.c_double),
        ('Commission', ctypes.c_double),
        ('CloseProfit', ctypes.c_double),
        ('PositionProfit', ctypes.c_double),
        ('PreSettlementPrice', ctypes.c_double),
        ('SettlementPrice', ctypes.c_double),
        ('TradingDay', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
        ('OpenCost', ctypes.c_double),
        ('ExchangeMargin', ctypes.c_double),
        ('CombPosition', ctypes.c_int),
        ('CombLongFrozen', ctypes.c_int),
        ('CombShortFrozen', ctypes.c_int),
        ('CloseProfitByDate', ctypes.c_double),
        ('CloseProfitByTrade', ctypes.c_double),
        ('TodayPosition', ctypes.c_int),
        ('MarginRateByMoney', ctypes.c_double),
        ('MarginRateByVolume', ctypes.c_double),
        ('StrikeFrozen', ctypes.c_int),
        ('StrikeFrozenAmount', ctypes.c_double),
        ('AbandonFrozen', ctypes.c_int),
    ]

    def __init__(self, InstrumentID='', BrokerID='', InvestorID='', PosiDirection='', HedgeFlag='', PositionDate='',
                 YdPosition='', Position='', LongFrozen='', ShortFrozen='', LongFrozenAmount='', ShortFrozenAmount='',
                 OpenVolume='', CloseVolume='', OpenAmount='', CloseAmount='', PositionCost='', PreMargin='',
                 UseMargin='', FrozenMargin='', FrozenCash='', FrozenCommission='', CashIn='', Commission='',
                 CloseProfit='', PositionProfit='', PreSettlementPrice='', SettlementPrice='', TradingDay='',
                 SettlementID='', OpenCost='', ExchangeMargin='', CombPosition='', CombLongFrozen='',
                 CombShortFrozen='', CloseProfitByDate='', CloseProfitByTrade='', TodayPosition='',
                 MarginRateByMoney='', MarginRateByVolume='', StrikeFrozen='', StrikeFrozenAmount='', AbandonFrozen=''):
        super(InvestorPositionField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.PosiDirection = self._to_bytes(PosiDirection)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.PositionDate = self._to_bytes(PositionDate)
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
        self.TradingDay = self._to_bytes(TradingDay)
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
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestorRange', ctypes.c_char),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('HedgeFlag', ctypes.c_char),
        ('LongMarginRatioByMoney', ctypes.c_double),
        ('LongMarginRatioByVolume', ctypes.c_double),
        ('ShortMarginRatioByMoney', ctypes.c_double),
        ('ShortMarginRatioByVolume', ctypes.c_double),
        ('IsRelative', ctypes.c_int),
    ]

    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', HedgeFlag='',
                 LongMarginRatioByMoney='', LongMarginRatioByVolume='', ShortMarginRatioByMoney='',
                 ShortMarginRatioByVolume='', IsRelative=''):
        super(InstrumentMarginRateField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.LongMarginRatioByMoney = float(LongMarginRatioByMoney)
        self.LongMarginRatioByVolume = float(LongMarginRatioByVolume)
        self.ShortMarginRatioByMoney = float(ShortMarginRatioByMoney)
        self.ShortMarginRatioByVolume = float(ShortMarginRatioByVolume)
        self.IsRelative = int(IsRelative)


class InstrumentCommissionRateField(Base):
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestorRange', ctypes.c_char),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('OpenRatioByMoney', ctypes.c_double),
        ('OpenRatioByVolume', ctypes.c_double),
        ('CloseRatioByMoney', ctypes.c_double),
        ('CloseRatioByVolume', ctypes.c_double),
        ('CloseTodayRatioByMoney', ctypes.c_double),
        ('CloseTodayRatioByVolume', ctypes.c_double),
    ]

    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', OpenRatioByMoney='',
                 OpenRatioByVolume='', CloseRatioByMoney='', CloseRatioByVolume='', CloseTodayRatioByMoney='',
                 CloseTodayRatioByVolume=''):
        super(InstrumentCommissionRateField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OpenRatioByMoney = float(OpenRatioByMoney)
        self.OpenRatioByVolume = float(OpenRatioByVolume)
        self.CloseRatioByMoney = float(CloseRatioByMoney)
        self.CloseRatioByVolume = float(CloseRatioByVolume)
        self.CloseTodayRatioByMoney = float(CloseTodayRatioByMoney)
        self.CloseTodayRatioByVolume = float(CloseTodayRatioByVolume)


class DepthMarketDataField(Base):
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),
        ('InstrumentID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('LastPrice', ctypes.c_double),
        ('PreSettlementPrice', ctypes.c_double),
        ('PreClosePrice', ctypes.c_double),
        ('PreOpenInterest', ctypes.c_double),
        ('OpenPrice', ctypes.c_double),
        ('HighestPrice', ctypes.c_double),
        ('LowestPrice', ctypes.c_double),
        ('Volume', ctypes.c_int),
        ('Turnover', ctypes.c_double),
        ('OpenInterest', ctypes.c_double),
        ('ClosePrice', ctypes.c_double),
        ('SettlementPrice', ctypes.c_double),
        ('UpperLimitPrice', ctypes.c_double),
        ('LowerLimitPrice', ctypes.c_double),
        ('PreDelta', ctypes.c_double),
        ('CurrDelta', ctypes.c_double),
        ('UpdateTime', ctypes.c_char * 9),
        ('UpdateMillisec', ctypes.c_int),
        ('BidPrice1', ctypes.c_double),
        ('BidVolume1', ctypes.c_int),
        ('AskPrice1', ctypes.c_double),
        ('AskVolume1', ctypes.c_int),
        ('BidPrice2', ctypes.c_double),
        ('BidVolume2', ctypes.c_int),
        ('AskPrice2', ctypes.c_double),
        ('AskVolume2', ctypes.c_int),
        ('BidPrice3', ctypes.c_double),
        ('BidVolume3', ctypes.c_int),
        ('AskPrice3', ctypes.c_double),
        ('AskVolume3', ctypes.c_int),
        ('BidPrice4', ctypes.c_double),
        ('BidVolume4', ctypes.c_int),
        ('AskPrice4', ctypes.c_double),
        ('AskVolume4', ctypes.c_int),
        ('BidPrice5', ctypes.c_double),
        ('BidVolume5', ctypes.c_int),
        ('AskPrice5', ctypes.c_double),
        ('AskVolume5', ctypes.c_int),
        ('AveragePrice', ctypes.c_double),
        ('ActionDay', ctypes.c_char * 9),
    ]

    def __init__(self, TradingDay='', InstrumentID='', ExchangeID='', ExchangeInstID='', LastPrice='',
                 PreSettlementPrice='', PreClosePrice='', PreOpenInterest='', OpenPrice='', HighestPrice='',
                 LowestPrice='', Volume='', Turnover='', OpenInterest='', ClosePrice='', SettlementPrice='',
                 UpperLimitPrice='', LowerLimitPrice='', PreDelta='', CurrDelta='', UpdateTime='', UpdateMillisec='',
                 BidPrice1='', BidVolume1='', AskPrice1='', AskVolume1='', BidPrice2='', BidVolume2='', AskPrice2='',
                 AskVolume2='', BidPrice3='', BidVolume3='', AskPrice3='', AskVolume3='', BidPrice4='', BidVolume4='',
                 AskPrice4='', AskVolume4='', BidPrice5='', BidVolume5='', AskPrice5='', AskVolume5='', AveragePrice='',
                 ActionDay=''):
        super(DepthMarketDataField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
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
        self.UpdateTime = self._to_bytes(UpdateTime)
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
        self.ActionDay = self._to_bytes(ActionDay)


class InstrumentTradingRightField(Base):
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestorRange', ctypes.c_char),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('TradingRight', ctypes.c_char),
    ]

    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', TradingRight=''):
        super(InstrumentTradingRightField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.TradingRight = self._to_bytes(TradingRight)


class BrokerUserField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('UserName', ctypes.c_char * 81),
        ('UserType', ctypes.c_char),
        ('IsActive', ctypes.c_int),
        ('IsUsingOTP', ctypes.c_int),
    ]

    def __init__(self, BrokerID='', UserID='', UserName='', UserType='', IsActive='', IsUsingOTP=''):
        super(BrokerUserField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.UserName = self._to_bytes(UserName)
        self.UserType = self._to_bytes(UserType)
        self.IsActive = int(IsActive)
        self.IsUsingOTP = int(IsUsingOTP)


class BrokerUserPasswordField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('Password', ctypes.c_char * 41),
    ]

    def __init__(self, BrokerID='', UserID='', Password=''):
        super(BrokerUserPasswordField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.Password = self._to_bytes(Password)


class BrokerUserFunctionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('BrokerFunctionCode', ctypes.c_char),
    ]

    def __init__(self, BrokerID='', UserID='', BrokerFunctionCode=''):
        super(BrokerUserFunctionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.BrokerFunctionCode = self._to_bytes(BrokerFunctionCode)


class TraderOfferField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
        ('ParticipantID', ctypes.c_char * 11),
        ('Password', ctypes.c_char * 41),
        ('InstallID', ctypes.c_int),
        ('OrderLocalID', ctypes.c_char * 13),
        ('TraderConnectStatus', ctypes.c_char),
        ('ConnectRequestDate', ctypes.c_char * 9),
        ('ConnectRequestTime', ctypes.c_char * 9),
        ('LastReportDate', ctypes.c_char * 9),
        ('LastReportTime', ctypes.c_char * 9),
        ('ConnectDate', ctypes.c_char * 9),
        ('ConnectTime', ctypes.c_char * 9),
        ('StartDate', ctypes.c_char * 9),
        ('StartTime', ctypes.c_char * 9),
        ('TradingDay', ctypes.c_char * 9),
        ('BrokerID', ctypes.c_char * 11),
        ('MaxTradeID', ctypes.c_char * 21),
        ('MaxOrderMessageReference', ctypes.c_char * 7),
    ]

    def __init__(self, ExchangeID='', TraderID='', ParticipantID='', Password='', InstallID='', OrderLocalID='',
                 TraderConnectStatus='', ConnectRequestDate='', ConnectRequestTime='', LastReportDate='',
                 LastReportTime='', ConnectDate='', ConnectTime='', StartDate='', StartTime='', TradingDay='',
                 BrokerID='', MaxTradeID='', MaxOrderMessageReference=''):
        super(TraderOfferField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.TraderConnectStatus = self._to_bytes(TraderConnectStatus)
        self.ConnectRequestDate = self._to_bytes(ConnectRequestDate)
        self.ConnectRequestTime = self._to_bytes(ConnectRequestTime)
        self.LastReportDate = self._to_bytes(LastReportDate)
        self.LastReportTime = self._to_bytes(LastReportTime)
        self.ConnectDate = self._to_bytes(ConnectDate)
        self.ConnectTime = self._to_bytes(ConnectTime)
        self.StartDate = self._to_bytes(StartDate)
        self.StartTime = self._to_bytes(StartTime)
        self.TradingDay = self._to_bytes(TradingDay)
        self.BrokerID = self._to_bytes(BrokerID)
        self.MaxTradeID = self._to_bytes(MaxTradeID)
        self.MaxOrderMessageReference = self._to_bytes(MaxOrderMessageReference)


class SettlementInfoField(Base):
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('SequenceNo', ctypes.c_int),
        ('Content', ctypes.c_char * 501),
    ]

    def __init__(self, TradingDay='', SettlementID='', BrokerID='', InvestorID='', SequenceNo='', Content=''):
        super(SettlementInfoField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.SequenceNo = int(SequenceNo)
        self.Content = self._to_bytes(Content)


class InstrumentMarginRateAdjustField(Base):
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestorRange', ctypes.c_char),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('HedgeFlag', ctypes.c_char),
        ('LongMarginRatioByMoney', ctypes.c_double),
        ('LongMarginRatioByVolume', ctypes.c_double),
        ('ShortMarginRatioByMoney', ctypes.c_double),
        ('ShortMarginRatioByVolume', ctypes.c_double),
        ('IsRelative', ctypes.c_int),
    ]

    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', HedgeFlag='',
                 LongMarginRatioByMoney='', LongMarginRatioByVolume='', ShortMarginRatioByMoney='',
                 ShortMarginRatioByVolume='', IsRelative=''):
        super(InstrumentMarginRateAdjustField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.LongMarginRatioByMoney = float(LongMarginRatioByMoney)
        self.LongMarginRatioByVolume = float(LongMarginRatioByVolume)
        self.ShortMarginRatioByMoney = float(ShortMarginRatioByMoney)
        self.ShortMarginRatioByVolume = float(ShortMarginRatioByVolume)
        self.IsRelative = int(IsRelative)


class ExchangeMarginRateField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InstrumentID', ctypes.c_char * 31),
        ('HedgeFlag', ctypes.c_char),
        ('LongMarginRatioByMoney', ctypes.c_double),
        ('LongMarginRatioByVolume', ctypes.c_double),
        ('ShortMarginRatioByMoney', ctypes.c_double),
        ('ShortMarginRatioByVolume', ctypes.c_double),
    ]

    def __init__(self, BrokerID='', InstrumentID='', HedgeFlag='', LongMarginRatioByMoney='',
                 LongMarginRatioByVolume='', ShortMarginRatioByMoney='', ShortMarginRatioByVolume=''):
        super(ExchangeMarginRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.LongMarginRatioByMoney = float(LongMarginRatioByMoney)
        self.LongMarginRatioByVolume = float(LongMarginRatioByVolume)
        self.ShortMarginRatioByMoney = float(ShortMarginRatioByMoney)
        self.ShortMarginRatioByVolume = float(ShortMarginRatioByVolume)


class ExchangeMarginRateAdjustField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InstrumentID', ctypes.c_char * 31),
        ('HedgeFlag', ctypes.c_char),
        ('LongMarginRatioByMoney', ctypes.c_double),
        ('LongMarginRatioByVolume', ctypes.c_double),
        ('ShortMarginRatioByMoney', ctypes.c_double),
        ('ShortMarginRatioByVolume', ctypes.c_double),
        ('ExchLongMarginRatioByMoney', ctypes.c_double),
        ('ExchLongMarginRatioByVolume', ctypes.c_double),
        ('ExchShortMarginRatioByMoney', ctypes.c_double),
        ('ExchShortMarginRatioByVolume', ctypes.c_double),
        ('NoLongMarginRatioByMoney', ctypes.c_double),
        ('NoLongMarginRatioByVolume', ctypes.c_double),
        ('NoShortMarginRatioByMoney', ctypes.c_double),
        ('NoShortMarginRatioByVolume', ctypes.c_double),
    ]

    def __init__(self, BrokerID='', InstrumentID='', HedgeFlag='', LongMarginRatioByMoney='',
                 LongMarginRatioByVolume='', ShortMarginRatioByMoney='', ShortMarginRatioByVolume='',
                 ExchLongMarginRatioByMoney='', ExchLongMarginRatioByVolume='', ExchShortMarginRatioByMoney='',
                 ExchShortMarginRatioByVolume='', NoLongMarginRatioByMoney='', NoLongMarginRatioByVolume='',
                 NoShortMarginRatioByMoney='', NoShortMarginRatioByVolume=''):
        super(ExchangeMarginRateAdjustField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
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
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('FromCurrencyID', ctypes.c_char * 4),
        ('FromCurrencyUnit', ctypes.c_double),
        ('ToCurrencyID', ctypes.c_char * 4),
        ('ExchangeRate', ctypes.c_double),
    ]

    def __init__(self, BrokerID='', FromCurrencyID='', FromCurrencyUnit='', ToCurrencyID='', ExchangeRate=''):
        super(ExchangeRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.FromCurrencyID = self._to_bytes(FromCurrencyID)
        self.FromCurrencyUnit = float(FromCurrencyUnit)
        self.ToCurrencyID = self._to_bytes(ToCurrencyID)
        self.ExchangeRate = float(ExchangeRate)


class SettlementRefField(Base):
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
    ]

    def __init__(self, TradingDay='', SettlementID=''):
        super(SettlementRefField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)


class CurrentTimeField(Base):
    _fields_ = [
        ('CurrDate', ctypes.c_char * 9),
        ('CurrTime', ctypes.c_char * 9),
        ('CurrMillisec', ctypes.c_int),
        ('ActionDay', ctypes.c_char * 9),
    ]

    def __init__(self, CurrDate='', CurrTime='', CurrMillisec='', ActionDay=''):
        super(CurrentTimeField, self).__init__()
        self.CurrDate = self._to_bytes(CurrDate)
        self.CurrTime = self._to_bytes(CurrTime)
        self.CurrMillisec = int(CurrMillisec)
        self.ActionDay = self._to_bytes(ActionDay)


class CommPhaseField(Base):
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),
        ('CommPhaseNo', ctypes.c_short),
        ('SystemID', ctypes.c_char * 21),
    ]

    def __init__(self, TradingDay='', CommPhaseNo='', SystemID=''):
        super(CommPhaseField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.CommPhaseNo = int(CommPhaseNo)
        self.SystemID = self._to_bytes(SystemID)


class LoginInfoField(Base):
    _fields_ = [
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('LoginDate', ctypes.c_char * 9),
        ('LoginTime', ctypes.c_char * 9),
        ('IPAddress', ctypes.c_char * 16),
        ('UserProductInfo', ctypes.c_char * 11),
        ('InterfaceProductInfo', ctypes.c_char * 11),
        ('ProtocolInfo', ctypes.c_char * 11),
        ('SystemName', ctypes.c_char * 41),
        ('Password', ctypes.c_char * 41),
        ('MaxOrderRef', ctypes.c_char * 13),
        ('SHFETime', ctypes.c_char * 9),
        ('DCETime', ctypes.c_char * 9),
        ('CZCETime', ctypes.c_char * 9),
        ('FFEXTime', ctypes.c_char * 9),
        ('MacAddress', ctypes.c_char * 21),
        ('OneTimePassword', ctypes.c_char * 41),
        ('INETime', ctypes.c_char * 9),
        ('IsQryControl', ctypes.c_int),
        ('LoginRemark', ctypes.c_char * 36),
    ]

    def __init__(self, FrontID='', SessionID='', BrokerID='', UserID='', LoginDate='', LoginTime='', IPAddress='',
                 UserProductInfo='', InterfaceProductInfo='', ProtocolInfo='', SystemName='', Password='',
                 MaxOrderRef='', SHFETime='', DCETime='', CZCETime='', FFEXTime='', MacAddress='', OneTimePassword='',
                 INETime='', IsQryControl='', LoginRemark=''):
        super(LoginInfoField, self).__init__()
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.LoginDate = self._to_bytes(LoginDate)
        self.LoginTime = self._to_bytes(LoginTime)
        self.IPAddress = self._to_bytes(IPAddress)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.InterfaceProductInfo = self._to_bytes(InterfaceProductInfo)
        self.ProtocolInfo = self._to_bytes(ProtocolInfo)
        self.SystemName = self._to_bytes(SystemName)
        self.Password = self._to_bytes(Password)
        self.MaxOrderRef = self._to_bytes(MaxOrderRef)
        self.SHFETime = self._to_bytes(SHFETime)
        self.DCETime = self._to_bytes(DCETime)
        self.CZCETime = self._to_bytes(CZCETime)
        self.FFEXTime = self._to_bytes(FFEXTime)
        self.MacAddress = self._to_bytes(MacAddress)
        self.OneTimePassword = self._to_bytes(OneTimePassword)
        self.INETime = self._to_bytes(INETime)
        self.IsQryControl = int(IsQryControl)
        self.LoginRemark = self._to_bytes(LoginRemark)


class LogoutAllField(Base):
    _fields_ = [
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('SystemName', ctypes.c_char * 41),
    ]

    def __init__(self, FrontID='', SessionID='', SystemName=''):
        super(LogoutAllField, self).__init__()
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.SystemName = self._to_bytes(SystemName)


class FrontStatusField(Base):
    _fields_ = [
        ('FrontID', ctypes.c_int),
        ('LastReportDate', ctypes.c_char * 9),
        ('LastReportTime', ctypes.c_char * 9),
        ('IsActive', ctypes.c_int),
    ]

    def __init__(self, FrontID='', LastReportDate='', LastReportTime='', IsActive=''):
        super(FrontStatusField, self).__init__()
        self.FrontID = int(FrontID)
        self.LastReportDate = self._to_bytes(LastReportDate)
        self.LastReportTime = self._to_bytes(LastReportTime)
        self.IsActive = int(IsActive)


class UserPasswordUpdateField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('OldPassword', ctypes.c_char * 41),
        ('NewPassword', ctypes.c_char * 41),
    ]

    def __init__(self, BrokerID='', UserID='', OldPassword='', NewPassword=''):
        super(UserPasswordUpdateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.OldPassword = self._to_bytes(OldPassword)
        self.NewPassword = self._to_bytes(NewPassword)


class InputOrderField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('OrderRef', ctypes.c_char * 13),
        ('UserID', ctypes.c_char * 16),
        ('OrderPriceType', ctypes.c_char),
        ('Direction', ctypes.c_char),
        ('CombOffsetFlag', ctypes.c_char * 5),
        ('CombHedgeFlag', ctypes.c_char * 5),
        ('LimitPrice', ctypes.c_double),
        ('VolumeTotalOriginal', ctypes.c_int),
        ('TimeCondition', ctypes.c_char),
        ('GTDDate', ctypes.c_char * 9),
        ('VolumeCondition', ctypes.c_char),
        ('MinVolume', ctypes.c_int),
        ('ContingentCondition', ctypes.c_char),
        ('StopPrice', ctypes.c_double),
        ('ForceCloseReason', ctypes.c_char),
        ('IsAutoSuspend', ctypes.c_int),
        ('BusinessUnit', ctypes.c_char * 21),
        ('RequestID', ctypes.c_int),
        ('UserForceClose', ctypes.c_int),
        ('IsSwapOrder', ctypes.c_int),
        ('ExchangeID', ctypes.c_char * 9),
        ('InvestUnitID', ctypes.c_char * 17),
        ('AccountID', ctypes.c_char * 13),
        ('CurrencyID', ctypes.c_char * 4),
        ('ClientID', ctypes.c_char * 11),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', OrderRef='', UserID='', OrderPriceType='',
                 Direction='', CombOffsetFlag='', CombHedgeFlag='', LimitPrice='', VolumeTotalOriginal='',
                 TimeCondition='', GTDDate='', VolumeCondition='', MinVolume='', ContingentCondition='', StopPrice='',
                 ForceCloseReason='', IsAutoSuspend='', BusinessUnit='', RequestID='', UserForceClose='',
                 IsSwapOrder='', ExchangeID='', InvestUnitID='', AccountID='', CurrencyID='', ClientID='', IPAddress='',
                 MacAddress=''):
        super(InputOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.OrderRef = self._to_bytes(OrderRef)
        self.UserID = self._to_bytes(UserID)
        self.OrderPriceType = self._to_bytes(OrderPriceType)
        self.Direction = self._to_bytes(Direction)
        self.CombOffsetFlag = self._to_bytes(CombOffsetFlag)
        self.CombHedgeFlag = self._to_bytes(CombHedgeFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = self._to_bytes(TimeCondition)
        self.GTDDate = self._to_bytes(GTDDate)
        self.VolumeCondition = self._to_bytes(VolumeCondition)
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = self._to_bytes(ContingentCondition)
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = self._to_bytes(ForceCloseReason)
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.RequestID = int(RequestID)
        self.UserForceClose = int(UserForceClose)
        self.IsSwapOrder = int(IsSwapOrder)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.ClientID = self._to_bytes(ClientID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class OrderField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('OrderRef', ctypes.c_char * 13),
        ('UserID', ctypes.c_char * 16),
        ('OrderPriceType', ctypes.c_char),
        ('Direction', ctypes.c_char),
        ('CombOffsetFlag', ctypes.c_char * 5),
        ('CombHedgeFlag', ctypes.c_char * 5),
        ('LimitPrice', ctypes.c_double),
        ('VolumeTotalOriginal', ctypes.c_int),
        ('TimeCondition', ctypes.c_char),
        ('GTDDate', ctypes.c_char * 9),
        ('VolumeCondition', ctypes.c_char),
        ('MinVolume', ctypes.c_int),
        ('ContingentCondition', ctypes.c_char),
        ('StopPrice', ctypes.c_double),
        ('ForceCloseReason', ctypes.c_char),
        ('IsAutoSuspend', ctypes.c_int),
        ('BusinessUnit', ctypes.c_char * 21),
        ('RequestID', ctypes.c_int),
        ('OrderLocalID', ctypes.c_char * 13),
        ('ExchangeID', ctypes.c_char * 9),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('OrderSubmitStatus', ctypes.c_char),
        ('NotifySequence', ctypes.c_int),
        ('TradingDay', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
        ('OrderSysID', ctypes.c_char * 21),
        ('OrderSource', ctypes.c_char),
        ('OrderStatus', ctypes.c_char),
        ('OrderType', ctypes.c_char),
        ('VolumeTraded', ctypes.c_int),
        ('VolumeTotal', ctypes.c_int),
        ('InsertDate', ctypes.c_char * 9),
        ('InsertTime', ctypes.c_char * 9),
        ('ActiveTime', ctypes.c_char * 9),
        ('SuspendTime', ctypes.c_char * 9),
        ('UpdateTime', ctypes.c_char * 9),
        ('CancelTime', ctypes.c_char * 9),
        ('ActiveTraderID', ctypes.c_char * 21),
        ('ClearingPartID', ctypes.c_char * 11),
        ('SequenceNo', ctypes.c_int),
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('UserProductInfo', ctypes.c_char * 11),
        ('StatusMsg', ctypes.c_char * 81),
        ('UserForceClose', ctypes.c_int),
        ('ActiveUserID', ctypes.c_char * 16),
        ('BrokerOrderSeq', ctypes.c_int),
        ('RelativeOrderSysID', ctypes.c_char * 21),
        ('ZCETotalTradedVolume', ctypes.c_int),
        ('IsSwapOrder', ctypes.c_int),
        ('BranchID', ctypes.c_char * 9),
        ('InvestUnitID', ctypes.c_char * 17),
        ('AccountID', ctypes.c_char * 13),
        ('CurrencyID', ctypes.c_char * 4),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

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
        super(OrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.OrderRef = self._to_bytes(OrderRef)
        self.UserID = self._to_bytes(UserID)
        self.OrderPriceType = self._to_bytes(OrderPriceType)
        self.Direction = self._to_bytes(Direction)
        self.CombOffsetFlag = self._to_bytes(CombOffsetFlag)
        self.CombHedgeFlag = self._to_bytes(CombHedgeFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = self._to_bytes(TimeCondition)
        self.GTDDate = self._to_bytes(GTDDate)
        self.VolumeCondition = self._to_bytes(VolumeCondition)
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = self._to_bytes(ContingentCondition)
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = self._to_bytes(ForceCloseReason)
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.RequestID = int(RequestID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderSubmitStatus = self._to_bytes(OrderSubmitStatus)
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.OrderSource = self._to_bytes(OrderSource)
        self.OrderStatus = self._to_bytes(OrderStatus)
        self.OrderType = self._to_bytes(OrderType)
        self.VolumeTraded = int(VolumeTraded)
        self.VolumeTotal = int(VolumeTotal)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.ActiveTime = self._to_bytes(ActiveTime)
        self.SuspendTime = self._to_bytes(SuspendTime)
        self.UpdateTime = self._to_bytes(UpdateTime)
        self.CancelTime = self._to_bytes(CancelTime)
        self.ActiveTraderID = self._to_bytes(ActiveTraderID)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.SequenceNo = int(SequenceNo)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.UserForceClose = int(UserForceClose)
        self.ActiveUserID = self._to_bytes(ActiveUserID)
        self.BrokerOrderSeq = int(BrokerOrderSeq)
        self.RelativeOrderSysID = self._to_bytes(RelativeOrderSysID)
        self.ZCETotalTradedVolume = int(ZCETotalTradedVolume)
        self.IsSwapOrder = int(IsSwapOrder)
        self.BranchID = self._to_bytes(BranchID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class ExchangeOrderField(Base):
    _fields_ = [
        ('OrderPriceType', ctypes.c_char),
        ('Direction', ctypes.c_char),
        ('CombOffsetFlag', ctypes.c_char * 5),
        ('CombHedgeFlag', ctypes.c_char * 5),
        ('LimitPrice', ctypes.c_double),
        ('VolumeTotalOriginal', ctypes.c_int),
        ('TimeCondition', ctypes.c_char),
        ('GTDDate', ctypes.c_char * 9),
        ('VolumeCondition', ctypes.c_char),
        ('MinVolume', ctypes.c_int),
        ('ContingentCondition', ctypes.c_char),
        ('StopPrice', ctypes.c_double),
        ('ForceCloseReason', ctypes.c_char),
        ('IsAutoSuspend', ctypes.c_int),
        ('BusinessUnit', ctypes.c_char * 21),
        ('RequestID', ctypes.c_int),
        ('OrderLocalID', ctypes.c_char * 13),
        ('ExchangeID', ctypes.c_char * 9),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('OrderSubmitStatus', ctypes.c_char),
        ('NotifySequence', ctypes.c_int),
        ('TradingDay', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
        ('OrderSysID', ctypes.c_char * 21),
        ('OrderSource', ctypes.c_char),
        ('OrderStatus', ctypes.c_char),
        ('OrderType', ctypes.c_char),
        ('VolumeTraded', ctypes.c_int),
        ('VolumeTotal', ctypes.c_int),
        ('InsertDate', ctypes.c_char * 9),
        ('InsertTime', ctypes.c_char * 9),
        ('ActiveTime', ctypes.c_char * 9),
        ('SuspendTime', ctypes.c_char * 9),
        ('UpdateTime', ctypes.c_char * 9),
        ('CancelTime', ctypes.c_char * 9),
        ('ActiveTraderID', ctypes.c_char * 21),
        ('ClearingPartID', ctypes.c_char * 11),
        ('SequenceNo', ctypes.c_int),
        ('BranchID', ctypes.c_char * 9),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, OrderPriceType='', Direction='', CombOffsetFlag='', CombHedgeFlag='', LimitPrice='',
                 VolumeTotalOriginal='', TimeCondition='', GTDDate='', VolumeCondition='', MinVolume='',
                 ContingentCondition='', StopPrice='', ForceCloseReason='', IsAutoSuspend='', BusinessUnit='',
                 RequestID='', OrderLocalID='', ExchangeID='', ParticipantID='', ClientID='', ExchangeInstID='',
                 TraderID='', InstallID='', OrderSubmitStatus='', NotifySequence='', TradingDay='', SettlementID='',
                 OrderSysID='', OrderSource='', OrderStatus='', OrderType='', VolumeTraded='', VolumeTotal='',
                 InsertDate='', InsertTime='', ActiveTime='', SuspendTime='', UpdateTime='', CancelTime='',
                 ActiveTraderID='', ClearingPartID='', SequenceNo='', BranchID='', IPAddress='', MacAddress=''):
        super(ExchangeOrderField, self).__init__()
        self.OrderPriceType = self._to_bytes(OrderPriceType)
        self.Direction = self._to_bytes(Direction)
        self.CombOffsetFlag = self._to_bytes(CombOffsetFlag)
        self.CombHedgeFlag = self._to_bytes(CombHedgeFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = self._to_bytes(TimeCondition)
        self.GTDDate = self._to_bytes(GTDDate)
        self.VolumeCondition = self._to_bytes(VolumeCondition)
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = self._to_bytes(ContingentCondition)
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = self._to_bytes(ForceCloseReason)
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.RequestID = int(RequestID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderSubmitStatus = self._to_bytes(OrderSubmitStatus)
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.OrderSource = self._to_bytes(OrderSource)
        self.OrderStatus = self._to_bytes(OrderStatus)
        self.OrderType = self._to_bytes(OrderType)
        self.VolumeTraded = int(VolumeTraded)
        self.VolumeTotal = int(VolumeTotal)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.ActiveTime = self._to_bytes(ActiveTime)
        self.SuspendTime = self._to_bytes(SuspendTime)
        self.UpdateTime = self._to_bytes(UpdateTime)
        self.CancelTime = self._to_bytes(CancelTime)
        self.ActiveTraderID = self._to_bytes(ActiveTraderID)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.SequenceNo = int(SequenceNo)
        self.BranchID = self._to_bytes(BranchID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class ExchangeOrderInsertErrorField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('ParticipantID', ctypes.c_char * 11),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('OrderLocalID', ctypes.c_char * 13),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
    ]

    def __init__(self, ExchangeID='', ParticipantID='', TraderID='', InstallID='', OrderLocalID='', ErrorID='',
                 ErrorMsg=''):
        super(ExchangeOrderInsertErrorField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class InputOrderActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('OrderActionRef', ctypes.c_int),
        ('OrderRef', ctypes.c_char * 13),
        ('RequestID', ctypes.c_int),
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('ExchangeID', ctypes.c_char * 9),
        ('OrderSysID', ctypes.c_char * 21),
        ('ActionFlag', ctypes.c_char),
        ('LimitPrice', ctypes.c_double),
        ('VolumeChange', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestUnitID', ctypes.c_char * 17),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', OrderActionRef='', OrderRef='', RequestID='', FrontID='',
                 SessionID='', ExchangeID='', OrderSysID='', ActionFlag='', LimitPrice='', VolumeChange='', UserID='',
                 InstrumentID='', InvestUnitID='', IPAddress='', MacAddress=''):
        super(InputOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OrderActionRef = int(OrderActionRef)
        self.OrderRef = self._to_bytes(OrderRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeChange = int(VolumeChange)
        self.UserID = self._to_bytes(UserID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class OrderActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('OrderActionRef', ctypes.c_int),
        ('OrderRef', ctypes.c_char * 13),
        ('RequestID', ctypes.c_int),
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('ExchangeID', ctypes.c_char * 9),
        ('OrderSysID', ctypes.c_char * 21),
        ('ActionFlag', ctypes.c_char),
        ('LimitPrice', ctypes.c_double),
        ('VolumeChange', ctypes.c_int),
        ('ActionDate', ctypes.c_char * 9),
        ('ActionTime', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('OrderLocalID', ctypes.c_char * 13),
        ('ActionLocalID', ctypes.c_char * 13),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('BusinessUnit', ctypes.c_char * 21),
        ('OrderActionStatus', ctypes.c_char),
        ('UserID', ctypes.c_char * 16),
        ('StatusMsg', ctypes.c_char * 81),
        ('InstrumentID', ctypes.c_char * 31),
        ('BranchID', ctypes.c_char * 9),
        ('InvestUnitID', ctypes.c_char * 17),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', OrderActionRef='', OrderRef='', RequestID='', FrontID='',
                 SessionID='', ExchangeID='', OrderSysID='', ActionFlag='', LimitPrice='', VolumeChange='',
                 ActionDate='', ActionTime='', TraderID='', InstallID='', OrderLocalID='', ActionLocalID='',
                 ParticipantID='', ClientID='', BusinessUnit='', OrderActionStatus='', UserID='', StatusMsg='',
                 InstrumentID='', BranchID='', InvestUnitID='', IPAddress='', MacAddress=''):
        super(OrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OrderActionRef = int(OrderActionRef)
        self.OrderRef = self._to_bytes(OrderRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeChange = int(VolumeChange)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.BranchID = self._to_bytes(BranchID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class ExchangeOrderActionField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('OrderSysID', ctypes.c_char * 21),
        ('ActionFlag', ctypes.c_char),
        ('LimitPrice', ctypes.c_double),
        ('VolumeChange', ctypes.c_int),
        ('ActionDate', ctypes.c_char * 9),
        ('ActionTime', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('OrderLocalID', ctypes.c_char * 13),
        ('ActionLocalID', ctypes.c_char * 13),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('BusinessUnit', ctypes.c_char * 21),
        ('OrderActionStatus', ctypes.c_char),
        ('UserID', ctypes.c_char * 16),
        ('BranchID', ctypes.c_char * 9),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, ExchangeID='', OrderSysID='', ActionFlag='', LimitPrice='', VolumeChange='', ActionDate='',
                 ActionTime='', TraderID='', InstallID='', OrderLocalID='', ActionLocalID='', ParticipantID='',
                 ClientID='', BusinessUnit='', OrderActionStatus='', UserID='', BranchID='', IPAddress='',
                 MacAddress=''):
        super(ExchangeOrderActionField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeChange = int(VolumeChange)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.BranchID = self._to_bytes(BranchID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class ExchangeOrderActionErrorField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('OrderSysID', ctypes.c_char * 21),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('OrderLocalID', ctypes.c_char * 13),
        ('ActionLocalID', ctypes.c_char * 13),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
    ]

    def __init__(self, ExchangeID='', OrderSysID='', TraderID='', InstallID='', OrderLocalID='', ActionLocalID='',
                 ErrorID='', ErrorMsg=''):
        super(ExchangeOrderActionErrorField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class ExchangeTradeField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('TradeID', ctypes.c_char * 21),
        ('Direction', ctypes.c_char),
        ('OrderSysID', ctypes.c_char * 21),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('TradingRole', ctypes.c_char),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('OffsetFlag', ctypes.c_char),
        ('HedgeFlag', ctypes.c_char),
        ('Price', ctypes.c_double),
        ('Volume', ctypes.c_int),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('TradeType', ctypes.c_char),
        ('PriceSource', ctypes.c_char),
        ('TraderID', ctypes.c_char * 21),
        ('OrderLocalID', ctypes.c_char * 13),
        ('ClearingPartID', ctypes.c_char * 11),
        ('BusinessUnit', ctypes.c_char * 21),
        ('SequenceNo', ctypes.c_int),
        ('TradeSource', ctypes.c_char),
    ]

    def __init__(self, ExchangeID='', TradeID='', Direction='', OrderSysID='', ParticipantID='', ClientID='',
                 TradingRole='', ExchangeInstID='', OffsetFlag='', HedgeFlag='', Price='', Volume='', TradeDate='',
                 TradeTime='', TradeType='', PriceSource='', TraderID='', OrderLocalID='', ClearingPartID='',
                 BusinessUnit='', SequenceNo='', TradeSource=''):
        super(ExchangeTradeField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TradeID = self._to_bytes(TradeID)
        self.Direction = self._to_bytes(Direction)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.TradingRole = self._to_bytes(TradingRole)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.OffsetFlag = self._to_bytes(OffsetFlag)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.Price = float(Price)
        self.Volume = int(Volume)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.TradeType = self._to_bytes(TradeType)
        self.PriceSource = self._to_bytes(PriceSource)
        self.TraderID = self._to_bytes(TraderID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.SequenceNo = int(SequenceNo)
        self.TradeSource = self._to_bytes(TradeSource)


class TradeField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('OrderRef', ctypes.c_char * 13),
        ('UserID', ctypes.c_char * 16),
        ('ExchangeID', ctypes.c_char * 9),
        ('TradeID', ctypes.c_char * 21),
        ('Direction', ctypes.c_char),
        ('OrderSysID', ctypes.c_char * 21),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('TradingRole', ctypes.c_char),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('OffsetFlag', ctypes.c_char),
        ('HedgeFlag', ctypes.c_char),
        ('Price', ctypes.c_double),
        ('Volume', ctypes.c_int),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('TradeType', ctypes.c_char),
        ('PriceSource', ctypes.c_char),
        ('TraderID', ctypes.c_char * 21),
        ('OrderLocalID', ctypes.c_char * 13),
        ('ClearingPartID', ctypes.c_char * 11),
        ('BusinessUnit', ctypes.c_char * 21),
        ('SequenceNo', ctypes.c_int),
        ('TradingDay', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
        ('BrokerOrderSeq', ctypes.c_int),
        ('TradeSource', ctypes.c_char),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', OrderRef='', UserID='', ExchangeID='', TradeID='',
                 Direction='', OrderSysID='', ParticipantID='', ClientID='', TradingRole='', ExchangeInstID='',
                 OffsetFlag='', HedgeFlag='', Price='', Volume='', TradeDate='', TradeTime='', TradeType='',
                 PriceSource='', TraderID='', OrderLocalID='', ClearingPartID='', BusinessUnit='', SequenceNo='',
                 TradingDay='', SettlementID='', BrokerOrderSeq='', TradeSource=''):
        super(TradeField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.OrderRef = self._to_bytes(OrderRef)
        self.UserID = self._to_bytes(UserID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TradeID = self._to_bytes(TradeID)
        self.Direction = self._to_bytes(Direction)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.TradingRole = self._to_bytes(TradingRole)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.OffsetFlag = self._to_bytes(OffsetFlag)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.Price = float(Price)
        self.Volume = int(Volume)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.TradeType = self._to_bytes(TradeType)
        self.PriceSource = self._to_bytes(PriceSource)
        self.TraderID = self._to_bytes(TraderID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.SequenceNo = int(SequenceNo)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.BrokerOrderSeq = int(BrokerOrderSeq)
        self.TradeSource = self._to_bytes(TradeSource)


class UserSessionField(Base):
    _fields_ = [
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('LoginDate', ctypes.c_char * 9),
        ('LoginTime', ctypes.c_char * 9),
        ('IPAddress', ctypes.c_char * 16),
        ('UserProductInfo', ctypes.c_char * 11),
        ('InterfaceProductInfo', ctypes.c_char * 11),
        ('ProtocolInfo', ctypes.c_char * 11),
        ('MacAddress', ctypes.c_char * 21),
        ('LoginRemark', ctypes.c_char * 36),
    ]

    def __init__(self, FrontID='', SessionID='', BrokerID='', UserID='', LoginDate='', LoginTime='', IPAddress='',
                 UserProductInfo='', InterfaceProductInfo='', ProtocolInfo='', MacAddress='', LoginRemark=''):
        super(UserSessionField, self).__init__()
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.LoginDate = self._to_bytes(LoginDate)
        self.LoginTime = self._to_bytes(LoginTime)
        self.IPAddress = self._to_bytes(IPAddress)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.InterfaceProductInfo = self._to_bytes(InterfaceProductInfo)
        self.ProtocolInfo = self._to_bytes(ProtocolInfo)
        self.MacAddress = self._to_bytes(MacAddress)
        self.LoginRemark = self._to_bytes(LoginRemark)


class QueryMaxOrderVolumeField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('Direction', ctypes.c_char),
        ('OffsetFlag', ctypes.c_char),
        ('HedgeFlag', ctypes.c_char),
        ('MaxVolume', ctypes.c_int),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', Direction='', OffsetFlag='', HedgeFlag='',
                 MaxVolume=''):
        super(QueryMaxOrderVolumeField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.Direction = self._to_bytes(Direction)
        self.OffsetFlag = self._to_bytes(OffsetFlag)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.MaxVolume = int(MaxVolume)


class SettlementInfoConfirmField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('ConfirmDate', ctypes.c_char * 9),
        ('ConfirmTime', ctypes.c_char * 9),
    ]

    def __init__(self, BrokerID='', InvestorID='', ConfirmDate='', ConfirmTime=''):
        super(SettlementInfoConfirmField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ConfirmDate = self._to_bytes(ConfirmDate)
        self.ConfirmTime = self._to_bytes(ConfirmTime)


class SyncDepositField(Base):
    _fields_ = [
        ('DepositSeqNo', ctypes.c_char * 15),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('Deposit', ctypes.c_double),
        ('IsForce', ctypes.c_int),
        ('CurrencyID', ctypes.c_char * 4),
    ]

    def __init__(self, DepositSeqNo='', BrokerID='', InvestorID='', Deposit='', IsForce='', CurrencyID=''):
        super(SyncDepositField, self).__init__()
        self.DepositSeqNo = self._to_bytes(DepositSeqNo)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.Deposit = float(Deposit)
        self.IsForce = int(IsForce)
        self.CurrencyID = self._to_bytes(CurrencyID)


class SyncFundMortgageField(Base):
    _fields_ = [
        ('MortgageSeqNo', ctypes.c_char * 15),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('FromCurrencyID', ctypes.c_char * 4),
        ('MortgageAmount', ctypes.c_double),
        ('ToCurrencyID', ctypes.c_char * 4),
    ]

    def __init__(self, MortgageSeqNo='', BrokerID='', InvestorID='', FromCurrencyID='', MortgageAmount='',
                 ToCurrencyID=''):
        super(SyncFundMortgageField, self).__init__()
        self.MortgageSeqNo = self._to_bytes(MortgageSeqNo)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.FromCurrencyID = self._to_bytes(FromCurrencyID)
        self.MortgageAmount = float(MortgageAmount)
        self.ToCurrencyID = self._to_bytes(ToCurrencyID)


class BrokerSyncField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
    ]

    def __init__(self, BrokerID=''):
        super(BrokerSyncField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)


class SyncingInvestorField(Base):
    _fields_ = [
        ('InvestorID', ctypes.c_char * 13),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorGroupID', ctypes.c_char * 13),
        ('InvestorName', ctypes.c_char * 81),
        ('IdentifiedCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('IsActive', ctypes.c_int),
        ('Telephone', ctypes.c_char * 41),
        ('Address', ctypes.c_char * 101),
        ('OpenDate', ctypes.c_char * 9),
        ('Mobile', ctypes.c_char * 41),
        ('CommModelID', ctypes.c_char * 13),
        ('MarginModelID', ctypes.c_char * 13),
    ]

    def __init__(self, InvestorID='', BrokerID='', InvestorGroupID='', InvestorName='', IdentifiedCardType='',
                 IdentifiedCardNo='', IsActive='', Telephone='', Address='', OpenDate='', Mobile='', CommModelID='',
                 MarginModelID=''):
        super(SyncingInvestorField, self).__init__()
        self.InvestorID = self._to_bytes(InvestorID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorGroupID = self._to_bytes(InvestorGroupID)
        self.InvestorName = self._to_bytes(InvestorName)
        self.IdentifiedCardType = self._to_bytes(IdentifiedCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.IsActive = int(IsActive)
        self.Telephone = self._to_bytes(Telephone)
        self.Address = self._to_bytes(Address)
        self.OpenDate = self._to_bytes(OpenDate)
        self.Mobile = self._to_bytes(Mobile)
        self.CommModelID = self._to_bytes(CommModelID)
        self.MarginModelID = self._to_bytes(MarginModelID)


class SyncingTradingCodeField(Base):
    _fields_ = [
        ('InvestorID', ctypes.c_char * 13),
        ('BrokerID', ctypes.c_char * 11),
        ('ExchangeID', ctypes.c_char * 9),
        ('ClientID', ctypes.c_char * 11),
        ('IsActive', ctypes.c_int),
        ('ClientIDType', ctypes.c_char),
    ]

    def __init__(self, InvestorID='', BrokerID='', ExchangeID='', ClientID='', IsActive='', ClientIDType=''):
        super(SyncingTradingCodeField, self).__init__()
        self.InvestorID = self._to_bytes(InvestorID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ClientID = self._to_bytes(ClientID)
        self.IsActive = int(IsActive)
        self.ClientIDType = self._to_bytes(ClientIDType)


class SyncingInvestorGroupField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorGroupID', ctypes.c_char * 13),
        ('InvestorGroupName', ctypes.c_char * 41),
    ]

    def __init__(self, BrokerID='', InvestorGroupID='', InvestorGroupName=''):
        super(SyncingInvestorGroupField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorGroupID = self._to_bytes(InvestorGroupID)
        self.InvestorGroupName = self._to_bytes(InvestorGroupName)


class SyncingTradingAccountField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('AccountID', ctypes.c_char * 13),
        ('PreMortgage', ctypes.c_double),
        ('PreCredit', ctypes.c_double),
        ('PreDeposit', ctypes.c_double),
        ('PreBalance', ctypes.c_double),
        ('PreMargin', ctypes.c_double),
        ('InterestBase', ctypes.c_double),
        ('Interest', ctypes.c_double),
        ('Deposit', ctypes.c_double),
        ('Withdraw', ctypes.c_double),
        ('FrozenMargin', ctypes.c_double),
        ('FrozenCash', ctypes.c_double),
        ('FrozenCommission', ctypes.c_double),
        ('CurrMargin', ctypes.c_double),
        ('CashIn', ctypes.c_double),
        ('Commission', ctypes.c_double),
        ('CloseProfit', ctypes.c_double),
        ('PositionProfit', ctypes.c_double),
        ('Balance', ctypes.c_double),
        ('Available', ctypes.c_double),
        ('WithdrawQuota', ctypes.c_double),
        ('Reserve', ctypes.c_double),
        ('TradingDay', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
        ('Credit', ctypes.c_double),
        ('Mortgage', ctypes.c_double),
        ('ExchangeMargin', ctypes.c_double),
        ('DeliveryMargin', ctypes.c_double),
        ('ExchangeDeliveryMargin', ctypes.c_double),
        ('ReserveBalance', ctypes.c_double),
        ('CurrencyID', ctypes.c_char * 4),
        ('PreFundMortgageIn', ctypes.c_double),
        ('PreFundMortgageOut', ctypes.c_double),
        ('FundMortgageIn', ctypes.c_double),
        ('FundMortgageOut', ctypes.c_double),
        ('FundMortgageAvailable', ctypes.c_double),
        ('MortgageableFund', ctypes.c_double),
        ('SpecProductMargin', ctypes.c_double),
        ('SpecProductFrozenMargin', ctypes.c_double),
        ('SpecProductCommission', ctypes.c_double),
        ('SpecProductFrozenCommission', ctypes.c_double),
        ('SpecProductPositionProfit', ctypes.c_double),
        ('SpecProductCloseProfit', ctypes.c_double),
        ('SpecProductPositionProfitByAlg', ctypes.c_double),
        ('SpecProductExchangeMargin', ctypes.c_double),
    ]

    def __init__(self, BrokerID='', AccountID='', PreMortgage='', PreCredit='', PreDeposit='', PreBalance='',
                 PreMargin='', InterestBase='', Interest='', Deposit='', Withdraw='', FrozenMargin='', FrozenCash='',
                 FrozenCommission='', CurrMargin='', CashIn='', Commission='', CloseProfit='', PositionProfit='',
                 Balance='', Available='', WithdrawQuota='', Reserve='', TradingDay='', SettlementID='', Credit='',
                 Mortgage='', ExchangeMargin='', DeliveryMargin='', ExchangeDeliveryMargin='', ReserveBalance='',
                 CurrencyID='', PreFundMortgageIn='', PreFundMortgageOut='', FundMortgageIn='', FundMortgageOut='',
                 FundMortgageAvailable='', MortgageableFund='', SpecProductMargin='', SpecProductFrozenMargin='',
                 SpecProductCommission='', SpecProductFrozenCommission='', SpecProductPositionProfit='',
                 SpecProductCloseProfit='', SpecProductPositionProfitByAlg='', SpecProductExchangeMargin=''):
        super(SyncingTradingAccountField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AccountID = self._to_bytes(AccountID)
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
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.Credit = float(Credit)
        self.Mortgage = float(Mortgage)
        self.ExchangeMargin = float(ExchangeMargin)
        self.DeliveryMargin = float(DeliveryMargin)
        self.ExchangeDeliveryMargin = float(ExchangeDeliveryMargin)
        self.ReserveBalance = float(ReserveBalance)
        self.CurrencyID = self._to_bytes(CurrencyID)
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
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('PosiDirection', ctypes.c_char),
        ('HedgeFlag', ctypes.c_char),
        ('PositionDate', ctypes.c_char),
        ('YdPosition', ctypes.c_int),
        ('Position', ctypes.c_int),
        ('LongFrozen', ctypes.c_int),
        ('ShortFrozen', ctypes.c_int),
        ('LongFrozenAmount', ctypes.c_double),
        ('ShortFrozenAmount', ctypes.c_double),
        ('OpenVolume', ctypes.c_int),
        ('CloseVolume', ctypes.c_int),
        ('OpenAmount', ctypes.c_double),
        ('CloseAmount', ctypes.c_double),
        ('PositionCost', ctypes.c_double),
        ('PreMargin', ctypes.c_double),
        ('UseMargin', ctypes.c_double),
        ('FrozenMargin', ctypes.c_double),
        ('FrozenCash', ctypes.c_double),
        ('FrozenCommission', ctypes.c_double),
        ('CashIn', ctypes.c_double),
        ('Commission', ctypes.c_double),
        ('CloseProfit', ctypes.c_double),
        ('PositionProfit', ctypes.c_double),
        ('PreSettlementPrice', ctypes.c_double),
        ('SettlementPrice', ctypes.c_double),
        ('TradingDay', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
        ('OpenCost', ctypes.c_double),
        ('ExchangeMargin', ctypes.c_double),
        ('CombPosition', ctypes.c_int),
        ('CombLongFrozen', ctypes.c_int),
        ('CombShortFrozen', ctypes.c_int),
        ('CloseProfitByDate', ctypes.c_double),
        ('CloseProfitByTrade', ctypes.c_double),
        ('TodayPosition', ctypes.c_int),
        ('MarginRateByMoney', ctypes.c_double),
        ('MarginRateByVolume', ctypes.c_double),
        ('StrikeFrozen', ctypes.c_int),
        ('StrikeFrozenAmount', ctypes.c_double),
        ('AbandonFrozen', ctypes.c_int),
    ]

    def __init__(self, InstrumentID='', BrokerID='', InvestorID='', PosiDirection='', HedgeFlag='', PositionDate='',
                 YdPosition='', Position='', LongFrozen='', ShortFrozen='', LongFrozenAmount='', ShortFrozenAmount='',
                 OpenVolume='', CloseVolume='', OpenAmount='', CloseAmount='', PositionCost='', PreMargin='',
                 UseMargin='', FrozenMargin='', FrozenCash='', FrozenCommission='', CashIn='', Commission='',
                 CloseProfit='', PositionProfit='', PreSettlementPrice='', SettlementPrice='', TradingDay='',
                 SettlementID='', OpenCost='', ExchangeMargin='', CombPosition='', CombLongFrozen='',
                 CombShortFrozen='', CloseProfitByDate='', CloseProfitByTrade='', TodayPosition='',
                 MarginRateByMoney='', MarginRateByVolume='', StrikeFrozen='', StrikeFrozenAmount='', AbandonFrozen=''):
        super(SyncingInvestorPositionField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.PosiDirection = self._to_bytes(PosiDirection)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.PositionDate = self._to_bytes(PositionDate)
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
        self.TradingDay = self._to_bytes(TradingDay)
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
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestorRange', ctypes.c_char),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('HedgeFlag', ctypes.c_char),
        ('LongMarginRatioByMoney', ctypes.c_double),
        ('LongMarginRatioByVolume', ctypes.c_double),
        ('ShortMarginRatioByMoney', ctypes.c_double),
        ('ShortMarginRatioByVolume', ctypes.c_double),
        ('IsRelative', ctypes.c_int),
    ]

    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', HedgeFlag='',
                 LongMarginRatioByMoney='', LongMarginRatioByVolume='', ShortMarginRatioByMoney='',
                 ShortMarginRatioByVolume='', IsRelative=''):
        super(SyncingInstrumentMarginRateField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.LongMarginRatioByMoney = float(LongMarginRatioByMoney)
        self.LongMarginRatioByVolume = float(LongMarginRatioByVolume)
        self.ShortMarginRatioByMoney = float(ShortMarginRatioByMoney)
        self.ShortMarginRatioByVolume = float(ShortMarginRatioByVolume)
        self.IsRelative = int(IsRelative)


class SyncingInstrumentCommissionRateField(Base):
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestorRange', ctypes.c_char),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('OpenRatioByMoney', ctypes.c_double),
        ('OpenRatioByVolume', ctypes.c_double),
        ('CloseRatioByMoney', ctypes.c_double),
        ('CloseRatioByVolume', ctypes.c_double),
        ('CloseTodayRatioByMoney', ctypes.c_double),
        ('CloseTodayRatioByVolume', ctypes.c_double),
    ]

    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', OpenRatioByMoney='',
                 OpenRatioByVolume='', CloseRatioByMoney='', CloseRatioByVolume='', CloseTodayRatioByMoney='',
                 CloseTodayRatioByVolume=''):
        super(SyncingInstrumentCommissionRateField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OpenRatioByMoney = float(OpenRatioByMoney)
        self.OpenRatioByVolume = float(OpenRatioByVolume)
        self.CloseRatioByMoney = float(CloseRatioByMoney)
        self.CloseRatioByVolume = float(CloseRatioByVolume)
        self.CloseTodayRatioByMoney = float(CloseTodayRatioByMoney)
        self.CloseTodayRatioByVolume = float(CloseTodayRatioByVolume)


class SyncingInstrumentTradingRightField(Base):
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestorRange', ctypes.c_char),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('TradingRight', ctypes.c_char),
    ]

    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', TradingRight=''):
        super(SyncingInstrumentTradingRightField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.TradingRight = self._to_bytes(TradingRight)


class QryOrderField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
        ('OrderSysID', ctypes.c_char * 21),
        ('InsertTimeStart', ctypes.c_char * 9),
        ('InsertTimeEnd', ctypes.c_char * 9),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID='', OrderSysID='', InsertTimeStart='',
                 InsertTimeEnd=''):
        super(QryOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.InsertTimeStart = self._to_bytes(InsertTimeStart)
        self.InsertTimeEnd = self._to_bytes(InsertTimeEnd)


class QryTradeField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
        ('TradeID', ctypes.c_char * 21),
        ('TradeTimeStart', ctypes.c_char * 9),
        ('TradeTimeEnd', ctypes.c_char * 9),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID='', TradeID='', TradeTimeStart='',
                 TradeTimeEnd=''):
        super(QryTradeField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TradeID = self._to_bytes(TradeID)
        self.TradeTimeStart = self._to_bytes(TradeTimeStart)
        self.TradeTimeEnd = self._to_bytes(TradeTimeEnd)


class QryInvestorPositionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        super(QryInvestorPositionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryTradingAccountField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('CurrencyID', ctypes.c_char * 4),
    ]

    def __init__(self, BrokerID='', InvestorID='', CurrencyID=''):
        super(QryTradingAccountField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.CurrencyID = self._to_bytes(CurrencyID)


class QryInvestorField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
    ]

    def __init__(self, BrokerID='', InvestorID=''):
        super(QryInvestorField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)


class QryTradingCodeField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('ExchangeID', ctypes.c_char * 9),
        ('ClientID', ctypes.c_char * 11),
        ('ClientIDType', ctypes.c_char),
    ]

    def __init__(self, BrokerID='', InvestorID='', ExchangeID='', ClientID='', ClientIDType=''):
        super(QryTradingCodeField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ClientID = self._to_bytes(ClientID)
        self.ClientIDType = self._to_bytes(ClientIDType)


class QryInvestorGroupField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
    ]

    def __init__(self, BrokerID=''):
        super(QryInvestorGroupField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)


class QryInstrumentMarginRateField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('HedgeFlag', ctypes.c_char),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', HedgeFlag=''):
        super(QryInstrumentMarginRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)


class QryInstrumentCommissionRateField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        super(QryInstrumentCommissionRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryInstrumentTradingRightField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        super(QryInstrumentTradingRightField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryBrokerField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
    ]

    def __init__(self, BrokerID=''):
        super(QryBrokerField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)


class QryTraderField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('ParticipantID', ctypes.c_char * 11),
        ('TraderID', ctypes.c_char * 21),
    ]

    def __init__(self, ExchangeID='', ParticipantID='', TraderID=''):
        super(QryTraderField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.TraderID = self._to_bytes(TraderID)


class QrySuperUserFunctionField(Base):
    _fields_ = [
        ('UserID', ctypes.c_char * 16),
    ]

    def __init__(self, UserID=''):
        super(QrySuperUserFunctionField, self).__init__()
        self.UserID = self._to_bytes(UserID)


class QryUserSessionField(Base):
    _fields_ = [
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
    ]

    def __init__(self, FrontID='', SessionID='', BrokerID='', UserID=''):
        super(QryUserSessionField, self).__init__()
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)


class QryPartBrokerField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('BrokerID', ctypes.c_char * 11),
        ('ParticipantID', ctypes.c_char * 11),
    ]

    def __init__(self, ExchangeID='', BrokerID='', ParticipantID=''):
        super(QryPartBrokerField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.ParticipantID = self._to_bytes(ParticipantID)


class QryFrontStatusField(Base):
    _fields_ = [
        ('FrontID', ctypes.c_int),
    ]

    def __init__(self, FrontID=''):
        super(QryFrontStatusField, self).__init__()
        self.FrontID = int(FrontID)


class QryExchangeOrderField(Base):
    _fields_ = [
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
    ]

    def __init__(self, ParticipantID='', ClientID='', ExchangeInstID='', ExchangeID='', TraderID=''):
        super(QryExchangeOrderField, self).__init__()
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)


class QryOrderActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('ExchangeID', ctypes.c_char * 9),
    ]

    def __init__(self, BrokerID='', InvestorID='', ExchangeID=''):
        super(QryOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExchangeID = self._to_bytes(ExchangeID)


class QryExchangeOrderActionField(Base):
    _fields_ = [
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('ExchangeID', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
    ]

    def __init__(self, ParticipantID='', ClientID='', ExchangeID='', TraderID=''):
        super(QryExchangeOrderActionField, self).__init__()
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)


class QrySuperUserField(Base):
    _fields_ = [
        ('UserID', ctypes.c_char * 16),
    ]

    def __init__(self, UserID=''):
        super(QrySuperUserField, self).__init__()
        self.UserID = self._to_bytes(UserID)


class QryExchangeField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
    ]

    def __init__(self, ExchangeID=''):
        super(QryExchangeField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)


class QryProductField(Base):
    _fields_ = [
        ('ProductID', ctypes.c_char * 31),
        ('ProductClass', ctypes.c_char),
    ]

    def __init__(self, ProductID='', ProductClass=''):
        super(QryProductField, self).__init__()
        self.ProductID = self._to_bytes(ProductID)
        self.ProductClass = self._to_bytes(ProductClass)


class QryInstrumentField(Base):
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('ProductID', ctypes.c_char * 31),
    ]

    def __init__(self, InstrumentID='', ExchangeID='', ExchangeInstID='', ProductID=''):
        super(QryInstrumentField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.ProductID = self._to_bytes(ProductID)


class QryDepthMarketDataField(Base):
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
    ]

    def __init__(self, InstrumentID=''):
        super(QryDepthMarketDataField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryBrokerUserField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
    ]

    def __init__(self, BrokerID='', UserID=''):
        super(QryBrokerUserField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)


class QryBrokerUserFunctionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
    ]

    def __init__(self, BrokerID='', UserID=''):
        super(QryBrokerUserFunctionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)


class QryTraderOfferField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('ParticipantID', ctypes.c_char * 11),
        ('TraderID', ctypes.c_char * 21),
    ]

    def __init__(self, ExchangeID='', ParticipantID='', TraderID=''):
        super(QryTraderOfferField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.TraderID = self._to_bytes(TraderID)


class QrySyncDepositField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('DepositSeqNo', ctypes.c_char * 15),
    ]

    def __init__(self, BrokerID='', DepositSeqNo=''):
        super(QrySyncDepositField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.DepositSeqNo = self._to_bytes(DepositSeqNo)


class QrySettlementInfoField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
    ]

    def __init__(self, BrokerID='', InvestorID='', TradingDay=''):
        super(QrySettlementInfoField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.TradingDay = self._to_bytes(TradingDay)


class QryExchangeMarginRateField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InstrumentID', ctypes.c_char * 31),
        ('HedgeFlag', ctypes.c_char),
    ]

    def __init__(self, BrokerID='', InstrumentID='', HedgeFlag=''):
        super(QryExchangeMarginRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)


class QryExchangeMarginRateAdjustField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InstrumentID', ctypes.c_char * 31),
        ('HedgeFlag', ctypes.c_char),
    ]

    def __init__(self, BrokerID='', InstrumentID='', HedgeFlag=''):
        super(QryExchangeMarginRateAdjustField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)


class QryExchangeRateField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('FromCurrencyID', ctypes.c_char * 4),
        ('ToCurrencyID', ctypes.c_char * 4),
    ]

    def __init__(self, BrokerID='', FromCurrencyID='', ToCurrencyID=''):
        super(QryExchangeRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.FromCurrencyID = self._to_bytes(FromCurrencyID)
        self.ToCurrencyID = self._to_bytes(ToCurrencyID)


class QrySyncFundMortgageField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('MortgageSeqNo', ctypes.c_char * 15),
    ]

    def __init__(self, BrokerID='', MortgageSeqNo=''):
        super(QrySyncFundMortgageField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.MortgageSeqNo = self._to_bytes(MortgageSeqNo)


class QryHisOrderField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
        ('OrderSysID', ctypes.c_char * 21),
        ('InsertTimeStart', ctypes.c_char * 9),
        ('InsertTimeEnd', ctypes.c_char * 9),
        ('TradingDay', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID='', OrderSysID='', InsertTimeStart='',
                 InsertTimeEnd='', TradingDay='', SettlementID=''):
        super(QryHisOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.InsertTimeStart = self._to_bytes(InsertTimeStart)
        self.InsertTimeEnd = self._to_bytes(InsertTimeEnd)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)


class OptionInstrMiniMarginField(Base):
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestorRange', ctypes.c_char),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('MinMargin', ctypes.c_double),
        ('ValueMethod', ctypes.c_char),
        ('IsRelative', ctypes.c_int),
    ]

    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', MinMargin='', ValueMethod='',
                 IsRelative=''):
        super(OptionInstrMiniMarginField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.MinMargin = float(MinMargin)
        self.ValueMethod = self._to_bytes(ValueMethod)
        self.IsRelative = int(IsRelative)


class OptionInstrMarginAdjustField(Base):
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestorRange', ctypes.c_char),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('SShortMarginRatioByMoney', ctypes.c_double),
        ('SShortMarginRatioByVolume', ctypes.c_double),
        ('HShortMarginRatioByMoney', ctypes.c_double),
        ('HShortMarginRatioByVolume', ctypes.c_double),
        ('AShortMarginRatioByMoney', ctypes.c_double),
        ('AShortMarginRatioByVolume', ctypes.c_double),
        ('IsRelative', ctypes.c_int),
        ('MShortMarginRatioByMoney', ctypes.c_double),
        ('MShortMarginRatioByVolume', ctypes.c_double),
    ]

    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', SShortMarginRatioByMoney='',
                 SShortMarginRatioByVolume='', HShortMarginRatioByMoney='', HShortMarginRatioByVolume='',
                 AShortMarginRatioByMoney='', AShortMarginRatioByVolume='', IsRelative='', MShortMarginRatioByMoney='',
                 MShortMarginRatioByVolume=''):
        super(OptionInstrMarginAdjustField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
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
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestorRange', ctypes.c_char),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('OpenRatioByMoney', ctypes.c_double),
        ('OpenRatioByVolume', ctypes.c_double),
        ('CloseRatioByMoney', ctypes.c_double),
        ('CloseRatioByVolume', ctypes.c_double),
        ('CloseTodayRatioByMoney', ctypes.c_double),
        ('CloseTodayRatioByVolume', ctypes.c_double),
        ('StrikeRatioByMoney', ctypes.c_double),
        ('StrikeRatioByVolume', ctypes.c_double),
    ]

    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', OpenRatioByMoney='',
                 OpenRatioByVolume='', CloseRatioByMoney='', CloseRatioByVolume='', CloseTodayRatioByMoney='',
                 CloseTodayRatioByVolume='', StrikeRatioByMoney='', StrikeRatioByVolume=''):
        super(OptionInstrCommRateField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OpenRatioByMoney = float(OpenRatioByMoney)
        self.OpenRatioByVolume = float(OpenRatioByVolume)
        self.CloseRatioByMoney = float(CloseRatioByMoney)
        self.CloseRatioByVolume = float(CloseRatioByVolume)
        self.CloseTodayRatioByMoney = float(CloseTodayRatioByMoney)
        self.CloseTodayRatioByVolume = float(CloseTodayRatioByVolume)
        self.StrikeRatioByMoney = float(StrikeRatioByMoney)
        self.StrikeRatioByVolume = float(StrikeRatioByVolume)


class OptionInstrTradeCostField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('HedgeFlag', ctypes.c_char),
        ('FixedMargin', ctypes.c_double),
        ('MiniMargin', ctypes.c_double),
        ('Royalty', ctypes.c_double),
        ('ExchFixedMargin', ctypes.c_double),
        ('ExchMiniMargin', ctypes.c_double),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', HedgeFlag='', FixedMargin='', MiniMargin='',
                 Royalty='', ExchFixedMargin='', ExchMiniMargin=''):
        super(OptionInstrTradeCostField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.FixedMargin = float(FixedMargin)
        self.MiniMargin = float(MiniMargin)
        self.Royalty = float(Royalty)
        self.ExchFixedMargin = float(ExchFixedMargin)
        self.ExchMiniMargin = float(ExchMiniMargin)


class QryOptionInstrTradeCostField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('HedgeFlag', ctypes.c_char),
        ('InputPrice', ctypes.c_double),
        ('UnderlyingPrice', ctypes.c_double),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', HedgeFlag='', InputPrice='', UnderlyingPrice=''):
        super(QryOptionInstrTradeCostField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.InputPrice = float(InputPrice)
        self.UnderlyingPrice = float(UnderlyingPrice)


class QryOptionInstrCommRateField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        super(QryOptionInstrCommRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class IndexPriceField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InstrumentID', ctypes.c_char * 31),
        ('ClosePrice', ctypes.c_double),
    ]

    def __init__(self, BrokerID='', InstrumentID='', ClosePrice=''):
        super(IndexPriceField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ClosePrice = float(ClosePrice)


class InputExecOrderField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('ExecOrderRef', ctypes.c_char * 13),
        ('UserID', ctypes.c_char * 16),
        ('Volume', ctypes.c_int),
        ('RequestID', ctypes.c_int),
        ('BusinessUnit', ctypes.c_char * 21),
        ('OffsetFlag', ctypes.c_char),
        ('HedgeFlag', ctypes.c_char),
        ('ActionType', ctypes.c_char),
        ('PosiDirection', ctypes.c_char),
        ('ReservePositionFlag', ctypes.c_char),
        ('CloseFlag', ctypes.c_char),
        ('ExchangeID', ctypes.c_char * 9),
        ('InvestUnitID', ctypes.c_char * 17),
        ('AccountID', ctypes.c_char * 13),
        ('CurrencyID', ctypes.c_char * 4),
        ('ClientID', ctypes.c_char * 11),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExecOrderRef='', UserID='', Volume='', RequestID='',
                 BusinessUnit='', OffsetFlag='', HedgeFlag='', ActionType='', PosiDirection='', ReservePositionFlag='',
                 CloseFlag='', ExchangeID='', InvestUnitID='', AccountID='', CurrencyID='', ClientID='', IPAddress='',
                 MacAddress=''):
        super(InputExecOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExecOrderRef = self._to_bytes(ExecOrderRef)
        self.UserID = self._to_bytes(UserID)
        self.Volume = int(Volume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OffsetFlag = self._to_bytes(OffsetFlag)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.ActionType = self._to_bytes(ActionType)
        self.PosiDirection = self._to_bytes(PosiDirection)
        self.ReservePositionFlag = self._to_bytes(ReservePositionFlag)
        self.CloseFlag = self._to_bytes(CloseFlag)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.ClientID = self._to_bytes(ClientID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class InputExecOrderActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('ExecOrderActionRef', ctypes.c_int),
        ('ExecOrderRef', ctypes.c_char * 13),
        ('RequestID', ctypes.c_int),
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('ExchangeID', ctypes.c_char * 9),
        ('ExecOrderSysID', ctypes.c_char * 21),
        ('ActionFlag', ctypes.c_char),
        ('UserID', ctypes.c_char * 16),
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestUnitID', ctypes.c_char * 17),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', ExecOrderActionRef='', ExecOrderRef='', RequestID='', FrontID='',
                 SessionID='', ExchangeID='', ExecOrderSysID='', ActionFlag='', UserID='', InstrumentID='',
                 InvestUnitID='', IPAddress='', MacAddress=''):
        super(InputExecOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExecOrderActionRef = int(ExecOrderActionRef)
        self.ExecOrderRef = self._to_bytes(ExecOrderRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExecOrderSysID = self._to_bytes(ExecOrderSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.UserID = self._to_bytes(UserID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class ExecOrderField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('ExecOrderRef', ctypes.c_char * 13),
        ('UserID', ctypes.c_char * 16),
        ('Volume', ctypes.c_int),
        ('RequestID', ctypes.c_int),
        ('BusinessUnit', ctypes.c_char * 21),
        ('OffsetFlag', ctypes.c_char),
        ('HedgeFlag', ctypes.c_char),
        ('ActionType', ctypes.c_char),
        ('PosiDirection', ctypes.c_char),
        ('ReservePositionFlag', ctypes.c_char),
        ('CloseFlag', ctypes.c_char),
        ('ExecOrderLocalID', ctypes.c_char * 13),
        ('ExchangeID', ctypes.c_char * 9),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('OrderSubmitStatus', ctypes.c_char),
        ('NotifySequence', ctypes.c_int),
        ('TradingDay', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
        ('ExecOrderSysID', ctypes.c_char * 21),
        ('InsertDate', ctypes.c_char * 9),
        ('InsertTime', ctypes.c_char * 9),
        ('CancelTime', ctypes.c_char * 9),
        ('ExecResult', ctypes.c_char),
        ('ClearingPartID', ctypes.c_char * 11),
        ('SequenceNo', ctypes.c_int),
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('UserProductInfo', ctypes.c_char * 11),
        ('StatusMsg', ctypes.c_char * 81),
        ('ActiveUserID', ctypes.c_char * 16),
        ('BrokerExecOrderSeq', ctypes.c_int),
        ('BranchID', ctypes.c_char * 9),
        ('InvestUnitID', ctypes.c_char * 17),
        ('AccountID', ctypes.c_char * 13),
        ('CurrencyID', ctypes.c_char * 4),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExecOrderRef='', UserID='', Volume='', RequestID='',
                 BusinessUnit='', OffsetFlag='', HedgeFlag='', ActionType='', PosiDirection='', ReservePositionFlag='',
                 CloseFlag='', ExecOrderLocalID='', ExchangeID='', ParticipantID='', ClientID='', ExchangeInstID='',
                 TraderID='', InstallID='', OrderSubmitStatus='', NotifySequence='', TradingDay='', SettlementID='',
                 ExecOrderSysID='', InsertDate='', InsertTime='', CancelTime='', ExecResult='', ClearingPartID='',
                 SequenceNo='', FrontID='', SessionID='', UserProductInfo='', StatusMsg='', ActiveUserID='',
                 BrokerExecOrderSeq='', BranchID='', InvestUnitID='', AccountID='', CurrencyID='', IPAddress='',
                 MacAddress=''):
        super(ExecOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExecOrderRef = self._to_bytes(ExecOrderRef)
        self.UserID = self._to_bytes(UserID)
        self.Volume = int(Volume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OffsetFlag = self._to_bytes(OffsetFlag)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.ActionType = self._to_bytes(ActionType)
        self.PosiDirection = self._to_bytes(PosiDirection)
        self.ReservePositionFlag = self._to_bytes(ReservePositionFlag)
        self.CloseFlag = self._to_bytes(CloseFlag)
        self.ExecOrderLocalID = self._to_bytes(ExecOrderLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderSubmitStatus = self._to_bytes(OrderSubmitStatus)
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.ExecOrderSysID = self._to_bytes(ExecOrderSysID)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.CancelTime = self._to_bytes(CancelTime)
        self.ExecResult = self._to_bytes(ExecResult)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.SequenceNo = int(SequenceNo)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.ActiveUserID = self._to_bytes(ActiveUserID)
        self.BrokerExecOrderSeq = int(BrokerExecOrderSeq)
        self.BranchID = self._to_bytes(BranchID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class ExecOrderActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('ExecOrderActionRef', ctypes.c_int),
        ('ExecOrderRef', ctypes.c_char * 13),
        ('RequestID', ctypes.c_int),
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('ExchangeID', ctypes.c_char * 9),
        ('ExecOrderSysID', ctypes.c_char * 21),
        ('ActionFlag', ctypes.c_char),
        ('ActionDate', ctypes.c_char * 9),
        ('ActionTime', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('ExecOrderLocalID', ctypes.c_char * 13),
        ('ActionLocalID', ctypes.c_char * 13),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('BusinessUnit', ctypes.c_char * 21),
        ('OrderActionStatus', ctypes.c_char),
        ('UserID', ctypes.c_char * 16),
        ('ActionType', ctypes.c_char),
        ('StatusMsg', ctypes.c_char * 81),
        ('InstrumentID', ctypes.c_char * 31),
        ('BranchID', ctypes.c_char * 9),
        ('InvestUnitID', ctypes.c_char * 17),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', ExecOrderActionRef='', ExecOrderRef='', RequestID='', FrontID='',
                 SessionID='', ExchangeID='', ExecOrderSysID='', ActionFlag='', ActionDate='', ActionTime='',
                 TraderID='', InstallID='', ExecOrderLocalID='', ActionLocalID='', ParticipantID='', ClientID='',
                 BusinessUnit='', OrderActionStatus='', UserID='', ActionType='', StatusMsg='', InstrumentID='',
                 BranchID='', InvestUnitID='', IPAddress='', MacAddress=''):
        super(ExecOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExecOrderActionRef = int(ExecOrderActionRef)
        self.ExecOrderRef = self._to_bytes(ExecOrderRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExecOrderSysID = self._to_bytes(ExecOrderSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.ExecOrderLocalID = self._to_bytes(ExecOrderLocalID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.ActionType = self._to_bytes(ActionType)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.BranchID = self._to_bytes(BranchID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class QryExecOrderField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
        ('ExecOrderSysID', ctypes.c_char * 21),
        ('InsertTimeStart', ctypes.c_char * 9),
        ('InsertTimeEnd', ctypes.c_char * 9),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID='', ExecOrderSysID='',
                 InsertTimeStart='', InsertTimeEnd=''):
        super(QryExecOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExecOrderSysID = self._to_bytes(ExecOrderSysID)
        self.InsertTimeStart = self._to_bytes(InsertTimeStart)
        self.InsertTimeEnd = self._to_bytes(InsertTimeEnd)


class ExchangeExecOrderField(Base):
    _fields_ = [
        ('Volume', ctypes.c_int),
        ('RequestID', ctypes.c_int),
        ('BusinessUnit', ctypes.c_char * 21),
        ('OffsetFlag', ctypes.c_char),
        ('HedgeFlag', ctypes.c_char),
        ('ActionType', ctypes.c_char),
        ('PosiDirection', ctypes.c_char),
        ('ReservePositionFlag', ctypes.c_char),
        ('CloseFlag', ctypes.c_char),
        ('ExecOrderLocalID', ctypes.c_char * 13),
        ('ExchangeID', ctypes.c_char * 9),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('OrderSubmitStatus', ctypes.c_char),
        ('NotifySequence', ctypes.c_int),
        ('TradingDay', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
        ('ExecOrderSysID', ctypes.c_char * 21),
        ('InsertDate', ctypes.c_char * 9),
        ('InsertTime', ctypes.c_char * 9),
        ('CancelTime', ctypes.c_char * 9),
        ('ExecResult', ctypes.c_char),
        ('ClearingPartID', ctypes.c_char * 11),
        ('SequenceNo', ctypes.c_int),
        ('BranchID', ctypes.c_char * 9),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, Volume='', RequestID='', BusinessUnit='', OffsetFlag='', HedgeFlag='', ActionType='',
                 PosiDirection='', ReservePositionFlag='', CloseFlag='', ExecOrderLocalID='', ExchangeID='',
                 ParticipantID='', ClientID='', ExchangeInstID='', TraderID='', InstallID='', OrderSubmitStatus='',
                 NotifySequence='', TradingDay='', SettlementID='', ExecOrderSysID='', InsertDate='', InsertTime='',
                 CancelTime='', ExecResult='', ClearingPartID='', SequenceNo='', BranchID='', IPAddress='',
                 MacAddress=''):
        super(ExchangeExecOrderField, self).__init__()
        self.Volume = int(Volume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OffsetFlag = self._to_bytes(OffsetFlag)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.ActionType = self._to_bytes(ActionType)
        self.PosiDirection = self._to_bytes(PosiDirection)
        self.ReservePositionFlag = self._to_bytes(ReservePositionFlag)
        self.CloseFlag = self._to_bytes(CloseFlag)
        self.ExecOrderLocalID = self._to_bytes(ExecOrderLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderSubmitStatus = self._to_bytes(OrderSubmitStatus)
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.ExecOrderSysID = self._to_bytes(ExecOrderSysID)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.CancelTime = self._to_bytes(CancelTime)
        self.ExecResult = self._to_bytes(ExecResult)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.SequenceNo = int(SequenceNo)
        self.BranchID = self._to_bytes(BranchID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class QryExchangeExecOrderField(Base):
    _fields_ = [
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
    ]

    def __init__(self, ParticipantID='', ClientID='', ExchangeInstID='', ExchangeID='', TraderID=''):
        super(QryExchangeExecOrderField, self).__init__()
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)


class QryExecOrderActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('ExchangeID', ctypes.c_char * 9),
    ]

    def __init__(self, BrokerID='', InvestorID='', ExchangeID=''):
        super(QryExecOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExchangeID = self._to_bytes(ExchangeID)


class ExchangeExecOrderActionField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('ExecOrderSysID', ctypes.c_char * 21),
        ('ActionFlag', ctypes.c_char),
        ('ActionDate', ctypes.c_char * 9),
        ('ActionTime', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('ExecOrderLocalID', ctypes.c_char * 13),
        ('ActionLocalID', ctypes.c_char * 13),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('BusinessUnit', ctypes.c_char * 21),
        ('OrderActionStatus', ctypes.c_char),
        ('UserID', ctypes.c_char * 16),
        ('ActionType', ctypes.c_char),
        ('BranchID', ctypes.c_char * 9),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, ExchangeID='', ExecOrderSysID='', ActionFlag='', ActionDate='', ActionTime='', TraderID='',
                 InstallID='', ExecOrderLocalID='', ActionLocalID='', ParticipantID='', ClientID='', BusinessUnit='',
                 OrderActionStatus='', UserID='', ActionType='', BranchID='', IPAddress='', MacAddress=''):
        super(ExchangeExecOrderActionField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExecOrderSysID = self._to_bytes(ExecOrderSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.ExecOrderLocalID = self._to_bytes(ExecOrderLocalID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.ActionType = self._to_bytes(ActionType)
        self.BranchID = self._to_bytes(BranchID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class QryExchangeExecOrderActionField(Base):
    _fields_ = [
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('ExchangeID', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
    ]

    def __init__(self, ParticipantID='', ClientID='', ExchangeID='', TraderID=''):
        super(QryExchangeExecOrderActionField, self).__init__()
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)


class ErrExecOrderField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('ExecOrderRef', ctypes.c_char * 13),
        ('UserID', ctypes.c_char * 16),
        ('Volume', ctypes.c_int),
        ('RequestID', ctypes.c_int),
        ('BusinessUnit', ctypes.c_char * 21),
        ('OffsetFlag', ctypes.c_char),
        ('HedgeFlag', ctypes.c_char),
        ('ActionType', ctypes.c_char),
        ('PosiDirection', ctypes.c_char),
        ('ReservePositionFlag', ctypes.c_char),
        ('CloseFlag', ctypes.c_char),
        ('ExchangeID', ctypes.c_char * 9),
        ('InvestUnitID', ctypes.c_char * 17),
        ('AccountID', ctypes.c_char * 13),
        ('CurrencyID', ctypes.c_char * 4),
        ('ClientID', ctypes.c_char * 11),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExecOrderRef='', UserID='', Volume='', RequestID='',
                 BusinessUnit='', OffsetFlag='', HedgeFlag='', ActionType='', PosiDirection='', ReservePositionFlag='',
                 CloseFlag='', ExchangeID='', InvestUnitID='', AccountID='', CurrencyID='', ClientID='', IPAddress='',
                 MacAddress='', ErrorID='', ErrorMsg=''):
        super(ErrExecOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExecOrderRef = self._to_bytes(ExecOrderRef)
        self.UserID = self._to_bytes(UserID)
        self.Volume = int(Volume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OffsetFlag = self._to_bytes(OffsetFlag)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.ActionType = self._to_bytes(ActionType)
        self.PosiDirection = self._to_bytes(PosiDirection)
        self.ReservePositionFlag = self._to_bytes(ReservePositionFlag)
        self.CloseFlag = self._to_bytes(CloseFlag)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.ClientID = self._to_bytes(ClientID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class QryErrExecOrderField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
    ]

    def __init__(self, BrokerID='', InvestorID=''):
        super(QryErrExecOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)


class ErrExecOrderActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('ExecOrderActionRef', ctypes.c_int),
        ('ExecOrderRef', ctypes.c_char * 13),
        ('RequestID', ctypes.c_int),
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('ExchangeID', ctypes.c_char * 9),
        ('ExecOrderSysID', ctypes.c_char * 21),
        ('ActionFlag', ctypes.c_char),
        ('UserID', ctypes.c_char * 16),
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestUnitID', ctypes.c_char * 17),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
    ]

    def __init__(self, BrokerID='', InvestorID='', ExecOrderActionRef='', ExecOrderRef='', RequestID='', FrontID='',
                 SessionID='', ExchangeID='', ExecOrderSysID='', ActionFlag='', UserID='', InstrumentID='',
                 InvestUnitID='', IPAddress='', MacAddress='', ErrorID='', ErrorMsg=''):
        super(ErrExecOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExecOrderActionRef = int(ExecOrderActionRef)
        self.ExecOrderRef = self._to_bytes(ExecOrderRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExecOrderSysID = self._to_bytes(ExecOrderSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.UserID = self._to_bytes(UserID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class QryErrExecOrderActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
    ]

    def __init__(self, BrokerID='', InvestorID=''):
        super(QryErrExecOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)


class OptionInstrTradingRightField(Base):
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestorRange', ctypes.c_char),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('Direction', ctypes.c_char),
        ('TradingRight', ctypes.c_char),
    ]

    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', Direction='', TradingRight=''):
        super(OptionInstrTradingRightField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.Direction = self._to_bytes(Direction)
        self.TradingRight = self._to_bytes(TradingRight)


class QryOptionInstrTradingRightField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('Direction', ctypes.c_char),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', Direction=''):
        super(QryOptionInstrTradingRightField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.Direction = self._to_bytes(Direction)


class InputForQuoteField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('ForQuoteRef', ctypes.c_char * 13),
        ('UserID', ctypes.c_char * 16),
        ('ExchangeID', ctypes.c_char * 9),
        ('InvestUnitID', ctypes.c_char * 17),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ForQuoteRef='', UserID='', ExchangeID='',
                 InvestUnitID='', IPAddress='', MacAddress=''):
        super(InputForQuoteField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ForQuoteRef = self._to_bytes(ForQuoteRef)
        self.UserID = self._to_bytes(UserID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class ForQuoteField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('ForQuoteRef', ctypes.c_char * 13),
        ('UserID', ctypes.c_char * 16),
        ('ForQuoteLocalID', ctypes.c_char * 13),
        ('ExchangeID', ctypes.c_char * 9),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('InsertDate', ctypes.c_char * 9),
        ('InsertTime', ctypes.c_char * 9),
        ('ForQuoteStatus', ctypes.c_char),
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('StatusMsg', ctypes.c_char * 81),
        ('ActiveUserID', ctypes.c_char * 16),
        ('BrokerForQutoSeq', ctypes.c_int),
        ('InvestUnitID', ctypes.c_char * 17),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ForQuoteRef='', UserID='', ForQuoteLocalID='',
                 ExchangeID='', ParticipantID='', ClientID='', ExchangeInstID='', TraderID='', InstallID='',
                 InsertDate='', InsertTime='', ForQuoteStatus='', FrontID='', SessionID='', StatusMsg='',
                 ActiveUserID='', BrokerForQutoSeq='', InvestUnitID='', IPAddress='', MacAddress=''):
        super(ForQuoteField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ForQuoteRef = self._to_bytes(ForQuoteRef)
        self.UserID = self._to_bytes(UserID)
        self.ForQuoteLocalID = self._to_bytes(ForQuoteLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.ForQuoteStatus = self._to_bytes(ForQuoteStatus)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.ActiveUserID = self._to_bytes(ActiveUserID)
        self.BrokerForQutoSeq = int(BrokerForQutoSeq)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class QryForQuoteField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
        ('InsertTimeStart', ctypes.c_char * 9),
        ('InsertTimeEnd', ctypes.c_char * 9),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID='', InsertTimeStart='',
                 InsertTimeEnd=''):
        super(QryForQuoteField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InsertTimeStart = self._to_bytes(InsertTimeStart)
        self.InsertTimeEnd = self._to_bytes(InsertTimeEnd)


class ExchangeForQuoteField(Base):
    _fields_ = [
        ('ForQuoteLocalID', ctypes.c_char * 13),
        ('ExchangeID', ctypes.c_char * 9),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('InsertDate', ctypes.c_char * 9),
        ('InsertTime', ctypes.c_char * 9),
        ('ForQuoteStatus', ctypes.c_char),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, ForQuoteLocalID='', ExchangeID='', ParticipantID='', ClientID='', ExchangeInstID='', TraderID='',
                 InstallID='', InsertDate='', InsertTime='', ForQuoteStatus='', IPAddress='', MacAddress=''):
        super(ExchangeForQuoteField, self).__init__()
        self.ForQuoteLocalID = self._to_bytes(ForQuoteLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.ForQuoteStatus = self._to_bytes(ForQuoteStatus)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class QryExchangeForQuoteField(Base):
    _fields_ = [
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
    ]

    def __init__(self, ParticipantID='', ClientID='', ExchangeInstID='', ExchangeID='', TraderID=''):
        super(QryExchangeForQuoteField, self).__init__()
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)


class InputQuoteField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('QuoteRef', ctypes.c_char * 13),
        ('UserID', ctypes.c_char * 16),
        ('AskPrice', ctypes.c_double),
        ('BidPrice', ctypes.c_double),
        ('AskVolume', ctypes.c_int),
        ('BidVolume', ctypes.c_int),
        ('RequestID', ctypes.c_int),
        ('BusinessUnit', ctypes.c_char * 21),
        ('AskOffsetFlag', ctypes.c_char),
        ('BidOffsetFlag', ctypes.c_char),
        ('AskHedgeFlag', ctypes.c_char),
        ('BidHedgeFlag', ctypes.c_char),
        ('AskOrderRef', ctypes.c_char * 13),
        ('BidOrderRef', ctypes.c_char * 13),
        ('ForQuoteSysID', ctypes.c_char * 21),
        ('ExchangeID', ctypes.c_char * 9),
        ('InvestUnitID', ctypes.c_char * 17),
        ('ClientID', ctypes.c_char * 11),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', QuoteRef='', UserID='', AskPrice='', BidPrice='',
                 AskVolume='', BidVolume='', RequestID='', BusinessUnit='', AskOffsetFlag='', BidOffsetFlag='',
                 AskHedgeFlag='', BidHedgeFlag='', AskOrderRef='', BidOrderRef='', ForQuoteSysID='', ExchangeID='',
                 InvestUnitID='', ClientID='', IPAddress='', MacAddress=''):
        super(InputQuoteField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.QuoteRef = self._to_bytes(QuoteRef)
        self.UserID = self._to_bytes(UserID)
        self.AskPrice = float(AskPrice)
        self.BidPrice = float(BidPrice)
        self.AskVolume = int(AskVolume)
        self.BidVolume = int(BidVolume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.AskOffsetFlag = self._to_bytes(AskOffsetFlag)
        self.BidOffsetFlag = self._to_bytes(BidOffsetFlag)
        self.AskHedgeFlag = self._to_bytes(AskHedgeFlag)
        self.BidHedgeFlag = self._to_bytes(BidHedgeFlag)
        self.AskOrderRef = self._to_bytes(AskOrderRef)
        self.BidOrderRef = self._to_bytes(BidOrderRef)
        self.ForQuoteSysID = self._to_bytes(ForQuoteSysID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.ClientID = self._to_bytes(ClientID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class InputQuoteActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('QuoteActionRef', ctypes.c_int),
        ('QuoteRef', ctypes.c_char * 13),
        ('RequestID', ctypes.c_int),
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('ExchangeID', ctypes.c_char * 9),
        ('QuoteSysID', ctypes.c_char * 21),
        ('ActionFlag', ctypes.c_char),
        ('UserID', ctypes.c_char * 16),
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestUnitID', ctypes.c_char * 17),
        ('ClientID', ctypes.c_char * 11),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', QuoteActionRef='', QuoteRef='', RequestID='', FrontID='',
                 SessionID='', ExchangeID='', QuoteSysID='', ActionFlag='', UserID='', InstrumentID='', InvestUnitID='',
                 ClientID='', IPAddress='', MacAddress=''):
        super(InputQuoteActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.QuoteActionRef = int(QuoteActionRef)
        self.QuoteRef = self._to_bytes(QuoteRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.QuoteSysID = self._to_bytes(QuoteSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.UserID = self._to_bytes(UserID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.ClientID = self._to_bytes(ClientID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class QuoteField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('QuoteRef', ctypes.c_char * 13),
        ('UserID', ctypes.c_char * 16),
        ('AskPrice', ctypes.c_double),
        ('BidPrice', ctypes.c_double),
        ('AskVolume', ctypes.c_int),
        ('BidVolume', ctypes.c_int),
        ('RequestID', ctypes.c_int),
        ('BusinessUnit', ctypes.c_char * 21),
        ('AskOffsetFlag', ctypes.c_char),
        ('BidOffsetFlag', ctypes.c_char),
        ('AskHedgeFlag', ctypes.c_char),
        ('BidHedgeFlag', ctypes.c_char),
        ('QuoteLocalID', ctypes.c_char * 13),
        ('ExchangeID', ctypes.c_char * 9),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('NotifySequence', ctypes.c_int),
        ('OrderSubmitStatus', ctypes.c_char),
        ('TradingDay', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
        ('QuoteSysID', ctypes.c_char * 21),
        ('InsertDate', ctypes.c_char * 9),
        ('InsertTime', ctypes.c_char * 9),
        ('CancelTime', ctypes.c_char * 9),
        ('QuoteStatus', ctypes.c_char),
        ('ClearingPartID', ctypes.c_char * 11),
        ('SequenceNo', ctypes.c_int),
        ('AskOrderSysID', ctypes.c_char * 21),
        ('BidOrderSysID', ctypes.c_char * 21),
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('UserProductInfo', ctypes.c_char * 11),
        ('StatusMsg', ctypes.c_char * 81),
        ('ActiveUserID', ctypes.c_char * 16),
        ('BrokerQuoteSeq', ctypes.c_int),
        ('AskOrderRef', ctypes.c_char * 13),
        ('BidOrderRef', ctypes.c_char * 13),
        ('ForQuoteSysID', ctypes.c_char * 21),
        ('BranchID', ctypes.c_char * 9),
        ('InvestUnitID', ctypes.c_char * 17),
        ('AccountID', ctypes.c_char * 13),
        ('CurrencyID', ctypes.c_char * 4),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', QuoteRef='', UserID='', AskPrice='', BidPrice='',
                 AskVolume='', BidVolume='', RequestID='', BusinessUnit='', AskOffsetFlag='', BidOffsetFlag='',
                 AskHedgeFlag='', BidHedgeFlag='', QuoteLocalID='', ExchangeID='', ParticipantID='', ClientID='',
                 ExchangeInstID='', TraderID='', InstallID='', NotifySequence='', OrderSubmitStatus='', TradingDay='',
                 SettlementID='', QuoteSysID='', InsertDate='', InsertTime='', CancelTime='', QuoteStatus='',
                 ClearingPartID='', SequenceNo='', AskOrderSysID='', BidOrderSysID='', FrontID='', SessionID='',
                 UserProductInfo='', StatusMsg='', ActiveUserID='', BrokerQuoteSeq='', AskOrderRef='', BidOrderRef='',
                 ForQuoteSysID='', BranchID='', InvestUnitID='', AccountID='', CurrencyID='', IPAddress='',
                 MacAddress=''):
        super(QuoteField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.QuoteRef = self._to_bytes(QuoteRef)
        self.UserID = self._to_bytes(UserID)
        self.AskPrice = float(AskPrice)
        self.BidPrice = float(BidPrice)
        self.AskVolume = int(AskVolume)
        self.BidVolume = int(BidVolume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.AskOffsetFlag = self._to_bytes(AskOffsetFlag)
        self.BidOffsetFlag = self._to_bytes(BidOffsetFlag)
        self.AskHedgeFlag = self._to_bytes(AskHedgeFlag)
        self.BidHedgeFlag = self._to_bytes(BidHedgeFlag)
        self.QuoteLocalID = self._to_bytes(QuoteLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.NotifySequence = int(NotifySequence)
        self.OrderSubmitStatus = self._to_bytes(OrderSubmitStatus)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.QuoteSysID = self._to_bytes(QuoteSysID)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.CancelTime = self._to_bytes(CancelTime)
        self.QuoteStatus = self._to_bytes(QuoteStatus)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.SequenceNo = int(SequenceNo)
        self.AskOrderSysID = self._to_bytes(AskOrderSysID)
        self.BidOrderSysID = self._to_bytes(BidOrderSysID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.ActiveUserID = self._to_bytes(ActiveUserID)
        self.BrokerQuoteSeq = int(BrokerQuoteSeq)
        self.AskOrderRef = self._to_bytes(AskOrderRef)
        self.BidOrderRef = self._to_bytes(BidOrderRef)
        self.ForQuoteSysID = self._to_bytes(ForQuoteSysID)
        self.BranchID = self._to_bytes(BranchID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class QuoteActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('QuoteActionRef', ctypes.c_int),
        ('QuoteRef', ctypes.c_char * 13),
        ('RequestID', ctypes.c_int),
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('ExchangeID', ctypes.c_char * 9),
        ('QuoteSysID', ctypes.c_char * 21),
        ('ActionFlag', ctypes.c_char),
        ('ActionDate', ctypes.c_char * 9),
        ('ActionTime', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('QuoteLocalID', ctypes.c_char * 13),
        ('ActionLocalID', ctypes.c_char * 13),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('BusinessUnit', ctypes.c_char * 21),
        ('OrderActionStatus', ctypes.c_char),
        ('UserID', ctypes.c_char * 16),
        ('StatusMsg', ctypes.c_char * 81),
        ('InstrumentID', ctypes.c_char * 31),
        ('BranchID', ctypes.c_char * 9),
        ('InvestUnitID', ctypes.c_char * 17),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', QuoteActionRef='', QuoteRef='', RequestID='', FrontID='',
                 SessionID='', ExchangeID='', QuoteSysID='', ActionFlag='', ActionDate='', ActionTime='', TraderID='',
                 InstallID='', QuoteLocalID='', ActionLocalID='', ParticipantID='', ClientID='', BusinessUnit='',
                 OrderActionStatus='', UserID='', StatusMsg='', InstrumentID='', BranchID='', InvestUnitID='',
                 IPAddress='', MacAddress=''):
        super(QuoteActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.QuoteActionRef = int(QuoteActionRef)
        self.QuoteRef = self._to_bytes(QuoteRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.QuoteSysID = self._to_bytes(QuoteSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.QuoteLocalID = self._to_bytes(QuoteLocalID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.BranchID = self._to_bytes(BranchID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class QryQuoteField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
        ('QuoteSysID', ctypes.c_char * 21),
        ('InsertTimeStart', ctypes.c_char * 9),
        ('InsertTimeEnd', ctypes.c_char * 9),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID='', QuoteSysID='', InsertTimeStart='',
                 InsertTimeEnd=''):
        super(QryQuoteField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.QuoteSysID = self._to_bytes(QuoteSysID)
        self.InsertTimeStart = self._to_bytes(InsertTimeStart)
        self.InsertTimeEnd = self._to_bytes(InsertTimeEnd)


class ExchangeQuoteField(Base):
    _fields_ = [
        ('AskPrice', ctypes.c_double),
        ('BidPrice', ctypes.c_double),
        ('AskVolume', ctypes.c_int),
        ('BidVolume', ctypes.c_int),
        ('RequestID', ctypes.c_int),
        ('BusinessUnit', ctypes.c_char * 21),
        ('AskOffsetFlag', ctypes.c_char),
        ('BidOffsetFlag', ctypes.c_char),
        ('AskHedgeFlag', ctypes.c_char),
        ('BidHedgeFlag', ctypes.c_char),
        ('QuoteLocalID', ctypes.c_char * 13),
        ('ExchangeID', ctypes.c_char * 9),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('NotifySequence', ctypes.c_int),
        ('OrderSubmitStatus', ctypes.c_char),
        ('TradingDay', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
        ('QuoteSysID', ctypes.c_char * 21),
        ('InsertDate', ctypes.c_char * 9),
        ('InsertTime', ctypes.c_char * 9),
        ('CancelTime', ctypes.c_char * 9),
        ('QuoteStatus', ctypes.c_char),
        ('ClearingPartID', ctypes.c_char * 11),
        ('SequenceNo', ctypes.c_int),
        ('AskOrderSysID', ctypes.c_char * 21),
        ('BidOrderSysID', ctypes.c_char * 21),
        ('ForQuoteSysID', ctypes.c_char * 21),
        ('BranchID', ctypes.c_char * 9),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, AskPrice='', BidPrice='', AskVolume='', BidVolume='', RequestID='', BusinessUnit='',
                 AskOffsetFlag='', BidOffsetFlag='', AskHedgeFlag='', BidHedgeFlag='', QuoteLocalID='', ExchangeID='',
                 ParticipantID='', ClientID='', ExchangeInstID='', TraderID='', InstallID='', NotifySequence='',
                 OrderSubmitStatus='', TradingDay='', SettlementID='', QuoteSysID='', InsertDate='', InsertTime='',
                 CancelTime='', QuoteStatus='', ClearingPartID='', SequenceNo='', AskOrderSysID='', BidOrderSysID='',
                 ForQuoteSysID='', BranchID='', IPAddress='', MacAddress=''):
        super(ExchangeQuoteField, self).__init__()
        self.AskPrice = float(AskPrice)
        self.BidPrice = float(BidPrice)
        self.AskVolume = int(AskVolume)
        self.BidVolume = int(BidVolume)
        self.RequestID = int(RequestID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.AskOffsetFlag = self._to_bytes(AskOffsetFlag)
        self.BidOffsetFlag = self._to_bytes(BidOffsetFlag)
        self.AskHedgeFlag = self._to_bytes(AskHedgeFlag)
        self.BidHedgeFlag = self._to_bytes(BidHedgeFlag)
        self.QuoteLocalID = self._to_bytes(QuoteLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.NotifySequence = int(NotifySequence)
        self.OrderSubmitStatus = self._to_bytes(OrderSubmitStatus)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.QuoteSysID = self._to_bytes(QuoteSysID)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.CancelTime = self._to_bytes(CancelTime)
        self.QuoteStatus = self._to_bytes(QuoteStatus)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.SequenceNo = int(SequenceNo)
        self.AskOrderSysID = self._to_bytes(AskOrderSysID)
        self.BidOrderSysID = self._to_bytes(BidOrderSysID)
        self.ForQuoteSysID = self._to_bytes(ForQuoteSysID)
        self.BranchID = self._to_bytes(BranchID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class QryExchangeQuoteField(Base):
    _fields_ = [
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
    ]

    def __init__(self, ParticipantID='', ClientID='', ExchangeInstID='', ExchangeID='', TraderID=''):
        super(QryExchangeQuoteField, self).__init__()
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)


class QryQuoteActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('ExchangeID', ctypes.c_char * 9),
    ]

    def __init__(self, BrokerID='', InvestorID='', ExchangeID=''):
        super(QryQuoteActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExchangeID = self._to_bytes(ExchangeID)


class ExchangeQuoteActionField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('QuoteSysID', ctypes.c_char * 21),
        ('ActionFlag', ctypes.c_char),
        ('ActionDate', ctypes.c_char * 9),
        ('ActionTime', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('QuoteLocalID', ctypes.c_char * 13),
        ('ActionLocalID', ctypes.c_char * 13),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('BusinessUnit', ctypes.c_char * 21),
        ('OrderActionStatus', ctypes.c_char),
        ('UserID', ctypes.c_char * 16),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, ExchangeID='', QuoteSysID='', ActionFlag='', ActionDate='', ActionTime='', TraderID='',
                 InstallID='', QuoteLocalID='', ActionLocalID='', ParticipantID='', ClientID='', BusinessUnit='',
                 OrderActionStatus='', UserID='', IPAddress='', MacAddress=''):
        super(ExchangeQuoteActionField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.QuoteSysID = self._to_bytes(QuoteSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.QuoteLocalID = self._to_bytes(QuoteLocalID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class QryExchangeQuoteActionField(Base):
    _fields_ = [
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('ExchangeID', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
    ]

    def __init__(self, ParticipantID='', ClientID='', ExchangeID='', TraderID=''):
        super(QryExchangeQuoteActionField, self).__init__()
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)


class OptionInstrDeltaField(Base):
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestorRange', ctypes.c_char),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('Delta', ctypes.c_double),
    ]

    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', Delta=''):
        super(OptionInstrDeltaField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.Delta = float(Delta)


class ForQuoteRspField(Base):
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),
        ('InstrumentID', ctypes.c_char * 31),
        ('ForQuoteSysID', ctypes.c_char * 21),
        ('ForQuoteTime', ctypes.c_char * 9),
        ('ActionDay', ctypes.c_char * 9),
        ('ExchangeID', ctypes.c_char * 9),
    ]

    def __init__(self, TradingDay='', InstrumentID='', ForQuoteSysID='', ForQuoteTime='', ActionDay='', ExchangeID=''):
        super(ForQuoteRspField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ForQuoteSysID = self._to_bytes(ForQuoteSysID)
        self.ForQuoteTime = self._to_bytes(ForQuoteTime)
        self.ActionDay = self._to_bytes(ActionDay)
        self.ExchangeID = self._to_bytes(ExchangeID)


class StrikeOffsetField(Base):
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestorRange', ctypes.c_char),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('Offset', ctypes.c_double),
        ('OffsetType', ctypes.c_char),
    ]

    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', Offset='', OffsetType=''):
        super(StrikeOffsetField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.Offset = float(Offset)
        self.OffsetType = self._to_bytes(OffsetType)


class QryStrikeOffsetField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        super(QryStrikeOffsetField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class InputBatchOrderActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('OrderActionRef', ctypes.c_int),
        ('RequestID', ctypes.c_int),
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('ExchangeID', ctypes.c_char * 9),
        ('UserID', ctypes.c_char * 16),
        ('InvestUnitID', ctypes.c_char * 17),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', OrderActionRef='', RequestID='', FrontID='', SessionID='',
                 ExchangeID='', UserID='', InvestUnitID='', IPAddress='', MacAddress=''):
        super(InputBatchOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OrderActionRef = int(OrderActionRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.UserID = self._to_bytes(UserID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class BatchOrderActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('OrderActionRef', ctypes.c_int),
        ('RequestID', ctypes.c_int),
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('ExchangeID', ctypes.c_char * 9),
        ('ActionDate', ctypes.c_char * 9),
        ('ActionTime', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('ActionLocalID', ctypes.c_char * 13),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('BusinessUnit', ctypes.c_char * 21),
        ('OrderActionStatus', ctypes.c_char),
        ('UserID', ctypes.c_char * 16),
        ('StatusMsg', ctypes.c_char * 81),
        ('InvestUnitID', ctypes.c_char * 17),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', OrderActionRef='', RequestID='', FrontID='', SessionID='',
                 ExchangeID='', ActionDate='', ActionTime='', TraderID='', InstallID='', ActionLocalID='',
                 ParticipantID='', ClientID='', BusinessUnit='', OrderActionStatus='', UserID='', StatusMsg='',
                 InvestUnitID='', IPAddress='', MacAddress=''):
        super(BatchOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OrderActionRef = int(OrderActionRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class ExchangeBatchOrderActionField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('ActionDate', ctypes.c_char * 9),
        ('ActionTime', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('ActionLocalID', ctypes.c_char * 13),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('BusinessUnit', ctypes.c_char * 21),
        ('OrderActionStatus', ctypes.c_char),
        ('UserID', ctypes.c_char * 16),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, ExchangeID='', ActionDate='', ActionTime='', TraderID='', InstallID='', ActionLocalID='',
                 ParticipantID='', ClientID='', BusinessUnit='', OrderActionStatus='', UserID='', IPAddress='',
                 MacAddress=''):
        super(ExchangeBatchOrderActionField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class QryBatchOrderActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('ExchangeID', ctypes.c_char * 9),
    ]

    def __init__(self, BrokerID='', InvestorID='', ExchangeID=''):
        super(QryBatchOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExchangeID = self._to_bytes(ExchangeID)


class CombInstrumentGuardField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InstrumentID', ctypes.c_char * 31),
        ('GuarantRatio', ctypes.c_double),
    ]

    def __init__(self, BrokerID='', InstrumentID='', GuarantRatio=''):
        super(CombInstrumentGuardField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.GuarantRatio = float(GuarantRatio)


class QryCombInstrumentGuardField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InstrumentID', ctypes.c_char * 31),
    ]

    def __init__(self, BrokerID='', InstrumentID=''):
        super(QryCombInstrumentGuardField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class InputCombActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('CombActionRef', ctypes.c_char * 13),
        ('UserID', ctypes.c_char * 16),
        ('Direction', ctypes.c_char),
        ('Volume', ctypes.c_int),
        ('CombDirection', ctypes.c_char),
        ('HedgeFlag', ctypes.c_char),
        ('ExchangeID', ctypes.c_char * 9),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', CombActionRef='', UserID='', Direction='',
                 Volume='', CombDirection='', HedgeFlag='', ExchangeID='', IPAddress='', MacAddress=''):
        super(InputCombActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.CombActionRef = self._to_bytes(CombActionRef)
        self.UserID = self._to_bytes(UserID)
        self.Direction = self._to_bytes(Direction)
        self.Volume = int(Volume)
        self.CombDirection = self._to_bytes(CombDirection)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class CombActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('CombActionRef', ctypes.c_char * 13),
        ('UserID', ctypes.c_char * 16),
        ('Direction', ctypes.c_char),
        ('Volume', ctypes.c_int),
        ('CombDirection', ctypes.c_char),
        ('HedgeFlag', ctypes.c_char),
        ('ActionLocalID', ctypes.c_char * 13),
        ('ExchangeID', ctypes.c_char * 9),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('ActionStatus', ctypes.c_char),
        ('NotifySequence', ctypes.c_int),
        ('TradingDay', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
        ('SequenceNo', ctypes.c_int),
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('UserProductInfo', ctypes.c_char * 11),
        ('StatusMsg', ctypes.c_char * 81),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', CombActionRef='', UserID='', Direction='',
                 Volume='', CombDirection='', HedgeFlag='', ActionLocalID='', ExchangeID='', ParticipantID='',
                 ClientID='', ExchangeInstID='', TraderID='', InstallID='', ActionStatus='', NotifySequence='',
                 TradingDay='', SettlementID='', SequenceNo='', FrontID='', SessionID='', UserProductInfo='',
                 StatusMsg='', IPAddress='', MacAddress=''):
        super(CombActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.CombActionRef = self._to_bytes(CombActionRef)
        self.UserID = self._to_bytes(UserID)
        self.Direction = self._to_bytes(Direction)
        self.Volume = int(Volume)
        self.CombDirection = self._to_bytes(CombDirection)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.ActionStatus = self._to_bytes(ActionStatus)
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.SequenceNo = int(SequenceNo)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class QryCombActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID=''):
        super(QryCombActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)


class ExchangeCombActionField(Base):
    _fields_ = [
        ('Direction', ctypes.c_char),
        ('Volume', ctypes.c_int),
        ('CombDirection', ctypes.c_char),
        ('HedgeFlag', ctypes.c_char),
        ('ActionLocalID', ctypes.c_char * 13),
        ('ExchangeID', ctypes.c_char * 9),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('ActionStatus', ctypes.c_char),
        ('NotifySequence', ctypes.c_int),
        ('TradingDay', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
        ('SequenceNo', ctypes.c_int),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, Direction='', Volume='', CombDirection='', HedgeFlag='', ActionLocalID='', ExchangeID='',
                 ParticipantID='', ClientID='', ExchangeInstID='', TraderID='', InstallID='', ActionStatus='',
                 NotifySequence='', TradingDay='', SettlementID='', SequenceNo='', IPAddress='', MacAddress=''):
        super(ExchangeCombActionField, self).__init__()
        self.Direction = self._to_bytes(Direction)
        self.Volume = int(Volume)
        self.CombDirection = self._to_bytes(CombDirection)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.ActionStatus = self._to_bytes(ActionStatus)
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.SequenceNo = int(SequenceNo)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class QryExchangeCombActionField(Base):
    _fields_ = [
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
    ]

    def __init__(self, ParticipantID='', ClientID='', ExchangeInstID='', ExchangeID='', TraderID=''):
        super(QryExchangeCombActionField, self).__init__()
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)


class ProductExchRateField(Base):
    _fields_ = [
        ('ProductID', ctypes.c_char * 31),
        ('QuoteCurrencyID', ctypes.c_char * 4),
        ('ExchangeRate', ctypes.c_double),
    ]

    def __init__(self, ProductID='', QuoteCurrencyID='', ExchangeRate=''):
        super(ProductExchRateField, self).__init__()
        self.ProductID = self._to_bytes(ProductID)
        self.QuoteCurrencyID = self._to_bytes(QuoteCurrencyID)
        self.ExchangeRate = float(ExchangeRate)


class QryProductExchRateField(Base):
    _fields_ = [
        ('ProductID', ctypes.c_char * 31),
    ]

    def __init__(self, ProductID=''):
        super(QryProductExchRateField, self).__init__()
        self.ProductID = self._to_bytes(ProductID)


class QryForQuoteParamField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InstrumentID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
    ]

    def __init__(self, BrokerID='', InstrumentID='', ExchangeID=''):
        super(QryForQuoteParamField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)


class ForQuoteParamField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InstrumentID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
        ('LastPrice', ctypes.c_double),
        ('PriceInterval', ctypes.c_double),
    ]

    def __init__(self, BrokerID='', InstrumentID='', ExchangeID='', LastPrice='', PriceInterval=''):
        super(ForQuoteParamField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.LastPrice = float(LastPrice)
        self.PriceInterval = float(PriceInterval)


class MMOptionInstrCommRateField(Base):
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestorRange', ctypes.c_char),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('OpenRatioByMoney', ctypes.c_double),
        ('OpenRatioByVolume', ctypes.c_double),
        ('CloseRatioByMoney', ctypes.c_double),
        ('CloseRatioByVolume', ctypes.c_double),
        ('CloseTodayRatioByMoney', ctypes.c_double),
        ('CloseTodayRatioByVolume', ctypes.c_double),
        ('StrikeRatioByMoney', ctypes.c_double),
        ('StrikeRatioByVolume', ctypes.c_double),
    ]

    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', OpenRatioByMoney='',
                 OpenRatioByVolume='', CloseRatioByMoney='', CloseRatioByVolume='', CloseTodayRatioByMoney='',
                 CloseTodayRatioByVolume='', StrikeRatioByMoney='', StrikeRatioByVolume=''):
        super(MMOptionInstrCommRateField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OpenRatioByMoney = float(OpenRatioByMoney)
        self.OpenRatioByVolume = float(OpenRatioByVolume)
        self.CloseRatioByMoney = float(CloseRatioByMoney)
        self.CloseRatioByVolume = float(CloseRatioByVolume)
        self.CloseTodayRatioByMoney = float(CloseTodayRatioByMoney)
        self.CloseTodayRatioByVolume = float(CloseTodayRatioByVolume)
        self.StrikeRatioByMoney = float(StrikeRatioByMoney)
        self.StrikeRatioByVolume = float(StrikeRatioByVolume)


class QryMMOptionInstrCommRateField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        super(QryMMOptionInstrCommRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class MMInstrumentCommissionRateField(Base):
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestorRange', ctypes.c_char),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('OpenRatioByMoney', ctypes.c_double),
        ('OpenRatioByVolume', ctypes.c_double),
        ('CloseRatioByMoney', ctypes.c_double),
        ('CloseRatioByVolume', ctypes.c_double),
        ('CloseTodayRatioByMoney', ctypes.c_double),
        ('CloseTodayRatioByVolume', ctypes.c_double),
    ]

    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', OpenRatioByMoney='',
                 OpenRatioByVolume='', CloseRatioByMoney='', CloseRatioByVolume='', CloseTodayRatioByMoney='',
                 CloseTodayRatioByVolume=''):
        super(MMInstrumentCommissionRateField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OpenRatioByMoney = float(OpenRatioByMoney)
        self.OpenRatioByVolume = float(OpenRatioByVolume)
        self.CloseRatioByMoney = float(CloseRatioByMoney)
        self.CloseRatioByVolume = float(CloseRatioByVolume)
        self.CloseTodayRatioByMoney = float(CloseTodayRatioByMoney)
        self.CloseTodayRatioByVolume = float(CloseTodayRatioByVolume)


class QryMMInstrumentCommissionRateField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        super(QryMMInstrumentCommissionRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class InstrumentOrderCommRateField(Base):
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('InvestorRange', ctypes.c_char),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('HedgeFlag', ctypes.c_char),
        ('OrderCommByVolume', ctypes.c_double),
        ('OrderActionCommByVolume', ctypes.c_double),
    ]

    def __init__(self, InstrumentID='', InvestorRange='', BrokerID='', InvestorID='', HedgeFlag='',
                 OrderCommByVolume='', OrderActionCommByVolume=''):
        super(InstrumentOrderCommRateField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.OrderCommByVolume = float(OrderCommByVolume)
        self.OrderActionCommByVolume = float(OrderActionCommByVolume)


class QryInstrumentOrderCommRateField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        super(QryInstrumentOrderCommRateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class MarketDataField(Base):
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),
        ('InstrumentID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('LastPrice', ctypes.c_double),
        ('PreSettlementPrice', ctypes.c_double),
        ('PreClosePrice', ctypes.c_double),
        ('PreOpenInterest', ctypes.c_double),
        ('OpenPrice', ctypes.c_double),
        ('HighestPrice', ctypes.c_double),
        ('LowestPrice', ctypes.c_double),
        ('Volume', ctypes.c_int),
        ('Turnover', ctypes.c_double),
        ('OpenInterest', ctypes.c_double),
        ('ClosePrice', ctypes.c_double),
        ('SettlementPrice', ctypes.c_double),
        ('UpperLimitPrice', ctypes.c_double),
        ('LowerLimitPrice', ctypes.c_double),
        ('PreDelta', ctypes.c_double),
        ('CurrDelta', ctypes.c_double),
        ('UpdateTime', ctypes.c_char * 9),
        ('UpdateMillisec', ctypes.c_int),
        ('ActionDay', ctypes.c_char * 9),
    ]

    def __init__(self, TradingDay='', InstrumentID='', ExchangeID='', ExchangeInstID='', LastPrice='',
                 PreSettlementPrice='', PreClosePrice='', PreOpenInterest='', OpenPrice='', HighestPrice='',
                 LowestPrice='', Volume='', Turnover='', OpenInterest='', ClosePrice='', SettlementPrice='',
                 UpperLimitPrice='', LowerLimitPrice='', PreDelta='', CurrDelta='', UpdateTime='', UpdateMillisec='',
                 ActionDay=''):
        super(MarketDataField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
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
        self.UpdateTime = self._to_bytes(UpdateTime)
        self.UpdateMillisec = int(UpdateMillisec)
        self.ActionDay = self._to_bytes(ActionDay)


class MarketDataBaseField(Base):
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),
        ('PreSettlementPrice', ctypes.c_double),
        ('PreClosePrice', ctypes.c_double),
        ('PreOpenInterest', ctypes.c_double),
        ('PreDelta', ctypes.c_double),
    ]

    def __init__(self, TradingDay='', PreSettlementPrice='', PreClosePrice='', PreOpenInterest='', PreDelta=''):
        super(MarketDataBaseField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.PreSettlementPrice = float(PreSettlementPrice)
        self.PreClosePrice = float(PreClosePrice)
        self.PreOpenInterest = float(PreOpenInterest)
        self.PreDelta = float(PreDelta)


class MarketDataStaticField(Base):
    _fields_ = [
        ('OpenPrice', ctypes.c_double),
        ('HighestPrice', ctypes.c_double),
        ('LowestPrice', ctypes.c_double),
        ('ClosePrice', ctypes.c_double),
        ('UpperLimitPrice', ctypes.c_double),
        ('LowerLimitPrice', ctypes.c_double),
        ('SettlementPrice', ctypes.c_double),
        ('CurrDelta', ctypes.c_double),
    ]

    def __init__(self, OpenPrice='', HighestPrice='', LowestPrice='', ClosePrice='', UpperLimitPrice='',
                 LowerLimitPrice='', SettlementPrice='', CurrDelta=''):
        super(MarketDataStaticField, self).__init__()
        self.OpenPrice = float(OpenPrice)
        self.HighestPrice = float(HighestPrice)
        self.LowestPrice = float(LowestPrice)
        self.ClosePrice = float(ClosePrice)
        self.UpperLimitPrice = float(UpperLimitPrice)
        self.LowerLimitPrice = float(LowerLimitPrice)
        self.SettlementPrice = float(SettlementPrice)
        self.CurrDelta = float(CurrDelta)


class MarketDataLastMatchField(Base):
    _fields_ = [
        ('LastPrice', ctypes.c_double),
        ('Volume', ctypes.c_int),
        ('Turnover', ctypes.c_double),
        ('OpenInterest', ctypes.c_double),
    ]

    def __init__(self, LastPrice='', Volume='', Turnover='', OpenInterest=''):
        super(MarketDataLastMatchField, self).__init__()
        self.LastPrice = float(LastPrice)
        self.Volume = int(Volume)
        self.Turnover = float(Turnover)
        self.OpenInterest = float(OpenInterest)


class MarketDataBestPriceField(Base):
    _fields_ = [
        ('BidPrice1', ctypes.c_double),
        ('BidVolume1', ctypes.c_int),
        ('AskPrice1', ctypes.c_double),
        ('AskVolume1', ctypes.c_int),
    ]

    def __init__(self, BidPrice1='', BidVolume1='', AskPrice1='', AskVolume1=''):
        super(MarketDataBestPriceField, self).__init__()
        self.BidPrice1 = float(BidPrice1)
        self.BidVolume1 = int(BidVolume1)
        self.AskPrice1 = float(AskPrice1)
        self.AskVolume1 = int(AskVolume1)


class MarketDataBid23Field(Base):
    _fields_ = [
        ('BidPrice2', ctypes.c_double),
        ('BidVolume2', ctypes.c_int),
        ('BidPrice3', ctypes.c_double),
        ('BidVolume3', ctypes.c_int),
    ]

    def __init__(self, BidPrice2='', BidVolume2='', BidPrice3='', BidVolume3=''):
        super(MarketDataBid23Field, self).__init__()
        self.BidPrice2 = float(BidPrice2)
        self.BidVolume2 = int(BidVolume2)
        self.BidPrice3 = float(BidPrice3)
        self.BidVolume3 = int(BidVolume3)


class MarketDataAsk23Field(Base):
    _fields_ = [
        ('AskPrice2', ctypes.c_double),
        ('AskVolume2', ctypes.c_int),
        ('AskPrice3', ctypes.c_double),
        ('AskVolume3', ctypes.c_int),
    ]

    def __init__(self, AskPrice2='', AskVolume2='', AskPrice3='', AskVolume3=''):
        super(MarketDataAsk23Field, self).__init__()
        self.AskPrice2 = float(AskPrice2)
        self.AskVolume2 = int(AskVolume2)
        self.AskPrice3 = float(AskPrice3)
        self.AskVolume3 = int(AskVolume3)


class MarketDataBid45Field(Base):
    _fields_ = [
        ('BidPrice4', ctypes.c_double),
        ('BidVolume4', ctypes.c_int),
        ('BidPrice5', ctypes.c_double),
        ('BidVolume5', ctypes.c_int),
    ]

    def __init__(self, BidPrice4='', BidVolume4='', BidPrice5='', BidVolume5=''):
        super(MarketDataBid45Field, self).__init__()
        self.BidPrice4 = float(BidPrice4)
        self.BidVolume4 = int(BidVolume4)
        self.BidPrice5 = float(BidPrice5)
        self.BidVolume5 = int(BidVolume5)


class MarketDataAsk45Field(Base):
    _fields_ = [
        ('AskPrice4', ctypes.c_double),
        ('AskVolume4', ctypes.c_int),
        ('AskPrice5', ctypes.c_double),
        ('AskVolume5', ctypes.c_int),
    ]

    def __init__(self, AskPrice4='', AskVolume4='', AskPrice5='', AskVolume5=''):
        super(MarketDataAsk45Field, self).__init__()
        self.AskPrice4 = float(AskPrice4)
        self.AskVolume4 = int(AskVolume4)
        self.AskPrice5 = float(AskPrice5)
        self.AskVolume5 = int(AskVolume5)


class MarketDataUpdateTimeField(Base):
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('UpdateTime', ctypes.c_char * 9),
        ('UpdateMillisec', ctypes.c_int),
        ('ActionDay', ctypes.c_char * 9),
    ]

    def __init__(self, InstrumentID='', UpdateTime='', UpdateMillisec='', ActionDay=''):
        super(MarketDataUpdateTimeField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.UpdateTime = self._to_bytes(UpdateTime)
        self.UpdateMillisec = int(UpdateMillisec)
        self.ActionDay = self._to_bytes(ActionDay)


class MarketDataExchangeField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
    ]

    def __init__(self, ExchangeID=''):
        super(MarketDataExchangeField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)


class SpecificInstrumentField(Base):
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
    ]

    def __init__(self, InstrumentID=''):
        super(SpecificInstrumentField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)


class InstrumentStatusField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('SettlementGroupID', ctypes.c_char * 9),
        ('InstrumentID', ctypes.c_char * 31),
        ('InstrumentStatus', ctypes.c_char),
        ('TradingSegmentSN', ctypes.c_int),
        ('EnterTime', ctypes.c_char * 9),
        ('EnterReason', ctypes.c_char),
    ]

    def __init__(self, ExchangeID='', ExchangeInstID='', SettlementGroupID='', InstrumentID='', InstrumentStatus='',
                 TradingSegmentSN='', EnterTime='', EnterReason=''):
        super(InstrumentStatusField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.SettlementGroupID = self._to_bytes(SettlementGroupID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.InstrumentStatus = self._to_bytes(InstrumentStatus)
        self.TradingSegmentSN = int(TradingSegmentSN)
        self.EnterTime = self._to_bytes(EnterTime)
        self.EnterReason = self._to_bytes(EnterReason)


class QryInstrumentStatusField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('ExchangeInstID', ctypes.c_char * 31),
    ]

    def __init__(self, ExchangeID='', ExchangeInstID=''):
        super(QryInstrumentStatusField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)


class InvestorAccountField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('AccountID', ctypes.c_char * 13),
        ('CurrencyID', ctypes.c_char * 4),
    ]

    def __init__(self, BrokerID='', InvestorID='', AccountID='', CurrencyID=''):
        super(InvestorAccountField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)


class PositionProfitAlgorithmField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('AccountID', ctypes.c_char * 13),
        ('Algorithm', ctypes.c_char),
        ('Memo', ctypes.c_char * 161),
        ('CurrencyID', ctypes.c_char * 4),
    ]

    def __init__(self, BrokerID='', AccountID='', Algorithm='', Memo='', CurrencyID=''):
        super(PositionProfitAlgorithmField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AccountID = self._to_bytes(AccountID)
        self.Algorithm = self._to_bytes(Algorithm)
        self.Memo = self._to_bytes(Memo)
        self.CurrencyID = self._to_bytes(CurrencyID)


class DiscountField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorRange', ctypes.c_char),
        ('InvestorID', ctypes.c_char * 13),
        ('Discount', ctypes.c_double),
    ]

    def __init__(self, BrokerID='', InvestorRange='', InvestorID='', Discount=''):
        super(DiscountField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.InvestorID = self._to_bytes(InvestorID)
        self.Discount = float(Discount)


class QryTransferBankField(Base):
    _fields_ = [
        ('BankID', ctypes.c_char * 4),
        ('BankBrchID', ctypes.c_char * 5),
    ]

    def __init__(self, BankID='', BankBrchID=''):
        super(QryTransferBankField, self).__init__()
        self.BankID = self._to_bytes(BankID)
        self.BankBrchID = self._to_bytes(BankBrchID)


class TransferBankField(Base):
    _fields_ = [
        ('BankID', ctypes.c_char * 4),
        ('BankBrchID', ctypes.c_char * 5),
        ('BankName', ctypes.c_char * 101),
        ('IsActive', ctypes.c_int),
    ]

    def __init__(self, BankID='', BankBrchID='', BankName='', IsActive=''):
        super(TransferBankField, self).__init__()
        self.BankID = self._to_bytes(BankID)
        self.BankBrchID = self._to_bytes(BankBrchID)
        self.BankName = self._to_bytes(BankName)
        self.IsActive = int(IsActive)


class QryInvestorPositionDetailField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID=''):
        super(QryInvestorPositionDetailField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class InvestorPositionDetailField(Base):
    _fields_ = [
        ('InstrumentID', ctypes.c_char * 31),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('HedgeFlag', ctypes.c_char),
        ('Direction', ctypes.c_char),
        ('OpenDate', ctypes.c_char * 9),
        ('TradeID', ctypes.c_char * 21),
        ('Volume', ctypes.c_int),
        ('OpenPrice', ctypes.c_double),
        ('TradingDay', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
        ('TradeType', ctypes.c_char),
        ('CombInstrumentID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
        ('CloseProfitByDate', ctypes.c_double),
        ('CloseProfitByTrade', ctypes.c_double),
        ('PositionProfitByDate', ctypes.c_double),
        ('PositionProfitByTrade', ctypes.c_double),
        ('Margin', ctypes.c_double),
        ('ExchMargin', ctypes.c_double),
        ('MarginRateByMoney', ctypes.c_double),
        ('MarginRateByVolume', ctypes.c_double),
        ('LastSettlementPrice', ctypes.c_double),
        ('SettlementPrice', ctypes.c_double),
        ('CloseVolume', ctypes.c_int),
        ('CloseAmount', ctypes.c_double),
    ]

    def __init__(self, InstrumentID='', BrokerID='', InvestorID='', HedgeFlag='', Direction='', OpenDate='', TradeID='',
                 Volume='', OpenPrice='', TradingDay='', SettlementID='', TradeType='', CombInstrumentID='',
                 ExchangeID='', CloseProfitByDate='', CloseProfitByTrade='', PositionProfitByDate='',
                 PositionProfitByTrade='', Margin='', ExchMargin='', MarginRateByMoney='', MarginRateByVolume='',
                 LastSettlementPrice='', SettlementPrice='', CloseVolume='', CloseAmount=''):
        super(InvestorPositionDetailField, self).__init__()
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.Direction = self._to_bytes(Direction)
        self.OpenDate = self._to_bytes(OpenDate)
        self.TradeID = self._to_bytes(TradeID)
        self.Volume = int(Volume)
        self.OpenPrice = float(OpenPrice)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.TradeType = self._to_bytes(TradeType)
        self.CombInstrumentID = self._to_bytes(CombInstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)
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
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('AccountID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
        ('CurrencyID', ctypes.c_char * 4),
    ]

    def __init__(self, BrokerID='', AccountID='', Password='', CurrencyID=''):
        super(TradingAccountPasswordField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.CurrencyID = self._to_bytes(CurrencyID)


class MDTraderOfferField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
        ('ParticipantID', ctypes.c_char * 11),
        ('Password', ctypes.c_char * 41),
        ('InstallID', ctypes.c_int),
        ('OrderLocalID', ctypes.c_char * 13),
        ('TraderConnectStatus', ctypes.c_char),
        ('ConnectRequestDate', ctypes.c_char * 9),
        ('ConnectRequestTime', ctypes.c_char * 9),
        ('LastReportDate', ctypes.c_char * 9),
        ('LastReportTime', ctypes.c_char * 9),
        ('ConnectDate', ctypes.c_char * 9),
        ('ConnectTime', ctypes.c_char * 9),
        ('StartDate', ctypes.c_char * 9),
        ('StartTime', ctypes.c_char * 9),
        ('TradingDay', ctypes.c_char * 9),
        ('BrokerID', ctypes.c_char * 11),
        ('MaxTradeID', ctypes.c_char * 21),
        ('MaxOrderMessageReference', ctypes.c_char * 7),
    ]

    def __init__(self, ExchangeID='', TraderID='', ParticipantID='', Password='', InstallID='', OrderLocalID='',
                 TraderConnectStatus='', ConnectRequestDate='', ConnectRequestTime='', LastReportDate='',
                 LastReportTime='', ConnectDate='', ConnectTime='', StartDate='', StartTime='', TradingDay='',
                 BrokerID='', MaxTradeID='', MaxOrderMessageReference=''):
        super(MDTraderOfferField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TraderID = self._to_bytes(TraderID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.TraderConnectStatus = self._to_bytes(TraderConnectStatus)
        self.ConnectRequestDate = self._to_bytes(ConnectRequestDate)
        self.ConnectRequestTime = self._to_bytes(ConnectRequestTime)
        self.LastReportDate = self._to_bytes(LastReportDate)
        self.LastReportTime = self._to_bytes(LastReportTime)
        self.ConnectDate = self._to_bytes(ConnectDate)
        self.ConnectTime = self._to_bytes(ConnectTime)
        self.StartDate = self._to_bytes(StartDate)
        self.StartTime = self._to_bytes(StartTime)
        self.TradingDay = self._to_bytes(TradingDay)
        self.BrokerID = self._to_bytes(BrokerID)
        self.MaxTradeID = self._to_bytes(MaxTradeID)
        self.MaxOrderMessageReference = self._to_bytes(MaxOrderMessageReference)


class QryMDTraderOfferField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('ParticipantID', ctypes.c_char * 11),
        ('TraderID', ctypes.c_char * 21),
    ]

    def __init__(self, ExchangeID='', ParticipantID='', TraderID=''):
        super(QryMDTraderOfferField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.TraderID = self._to_bytes(TraderID)


class QryNoticeField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
    ]

    def __init__(self, BrokerID=''):
        super(QryNoticeField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)


class NoticeField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('Content', ctypes.c_char * 501),
        ('SequenceLabel', ctypes.c_char * 2),
    ]

    def __init__(self, BrokerID='', Content='', SequenceLabel=''):
        super(NoticeField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.Content = self._to_bytes(Content)
        self.SequenceLabel = self._to_bytes(SequenceLabel)


class UserRightField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('UserRightType', ctypes.c_char),
        ('IsForbidden', ctypes.c_int),
    ]

    def __init__(self, BrokerID='', UserID='', UserRightType='', IsForbidden=''):
        super(UserRightField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.UserRightType = self._to_bytes(UserRightType)
        self.IsForbidden = int(IsForbidden)


class QrySettlementInfoConfirmField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
    ]

    def __init__(self, BrokerID='', InvestorID=''):
        super(QrySettlementInfoConfirmField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)


class LoadSettlementInfoField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
    ]

    def __init__(self, BrokerID=''):
        super(LoadSettlementInfoField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)


class BrokerWithdrawAlgorithmField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('WithdrawAlgorithm', ctypes.c_char),
        ('UsingRatio', ctypes.c_double),
        ('IncludeCloseProfit', ctypes.c_char),
        ('AllWithoutTrade', ctypes.c_char),
        ('AvailIncludeCloseProfit', ctypes.c_char),
        ('IsBrokerUserEvent', ctypes.c_int),
        ('CurrencyID', ctypes.c_char * 4),
        ('FundMortgageRatio', ctypes.c_double),
        ('BalanceAlgorithm', ctypes.c_char),
    ]

    def __init__(self, BrokerID='', WithdrawAlgorithm='', UsingRatio='', IncludeCloseProfit='', AllWithoutTrade='',
                 AvailIncludeCloseProfit='', IsBrokerUserEvent='', CurrencyID='', FundMortgageRatio='',
                 BalanceAlgorithm=''):
        super(BrokerWithdrawAlgorithmField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.WithdrawAlgorithm = self._to_bytes(WithdrawAlgorithm)
        self.UsingRatio = float(UsingRatio)
        self.IncludeCloseProfit = self._to_bytes(IncludeCloseProfit)
        self.AllWithoutTrade = self._to_bytes(AllWithoutTrade)
        self.AvailIncludeCloseProfit = self._to_bytes(AvailIncludeCloseProfit)
        self.IsBrokerUserEvent = int(IsBrokerUserEvent)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.FundMortgageRatio = float(FundMortgageRatio)
        self.BalanceAlgorithm = self._to_bytes(BalanceAlgorithm)


class TradingAccountPasswordUpdateV1Field(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('OldPassword', ctypes.c_char * 41),
        ('NewPassword', ctypes.c_char * 41),
    ]

    def __init__(self, BrokerID='', InvestorID='', OldPassword='', NewPassword=''):
        super(TradingAccountPasswordUpdateV1Field, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OldPassword = self._to_bytes(OldPassword)
        self.NewPassword = self._to_bytes(NewPassword)


class TradingAccountPasswordUpdateField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('AccountID', ctypes.c_char * 13),
        ('OldPassword', ctypes.c_char * 41),
        ('NewPassword', ctypes.c_char * 41),
        ('CurrencyID', ctypes.c_char * 4),
    ]

    def __init__(self, BrokerID='', AccountID='', OldPassword='', NewPassword='', CurrencyID=''):
        super(TradingAccountPasswordUpdateField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AccountID = self._to_bytes(AccountID)
        self.OldPassword = self._to_bytes(OldPassword)
        self.NewPassword = self._to_bytes(NewPassword)
        self.CurrencyID = self._to_bytes(CurrencyID)


class QryCombinationLegField(Base):
    _fields_ = [
        ('CombInstrumentID', ctypes.c_char * 31),
        ('LegID', ctypes.c_int),
        ('LegInstrumentID', ctypes.c_char * 31),
    ]

    def __init__(self, CombInstrumentID='', LegID='', LegInstrumentID=''):
        super(QryCombinationLegField, self).__init__()
        self.CombInstrumentID = self._to_bytes(CombInstrumentID)
        self.LegID = int(LegID)
        self.LegInstrumentID = self._to_bytes(LegInstrumentID)


class QrySyncStatusField(Base):
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),
    ]

    def __init__(self, TradingDay=''):
        super(QrySyncStatusField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)


class CombinationLegField(Base):
    _fields_ = [
        ('CombInstrumentID', ctypes.c_char * 31),
        ('LegID', ctypes.c_int),
        ('LegInstrumentID', ctypes.c_char * 31),
        ('Direction', ctypes.c_char),
        ('LegMultiple', ctypes.c_int),
        ('ImplyLevel', ctypes.c_int),
    ]

    def __init__(self, CombInstrumentID='', LegID='', LegInstrumentID='', Direction='', LegMultiple='', ImplyLevel=''):
        super(CombinationLegField, self).__init__()
        self.CombInstrumentID = self._to_bytes(CombInstrumentID)
        self.LegID = int(LegID)
        self.LegInstrumentID = self._to_bytes(LegInstrumentID)
        self.Direction = self._to_bytes(Direction)
        self.LegMultiple = int(LegMultiple)
        self.ImplyLevel = int(ImplyLevel)


class SyncStatusField(Base):
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),
        ('DataSyncStatus', ctypes.c_char),
    ]

    def __init__(self, TradingDay='', DataSyncStatus=''):
        super(SyncStatusField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.DataSyncStatus = self._to_bytes(DataSyncStatus)


class QryLinkManField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
    ]

    def __init__(self, BrokerID='', InvestorID=''):
        super(QryLinkManField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)


class LinkManField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('PersonType', ctypes.c_char),
        ('IdentifiedCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('PersonName', ctypes.c_char * 81),
        ('Telephone', ctypes.c_char * 41),
        ('Address', ctypes.c_char * 101),
        ('ZipCode', ctypes.c_char * 7),
        ('Priority', ctypes.c_int),
        ('UOAZipCode', ctypes.c_char * 11),
        ('PersonFullName', ctypes.c_char * 101),
    ]

    def __init__(self, BrokerID='', InvestorID='', PersonType='', IdentifiedCardType='', IdentifiedCardNo='',
                 PersonName='', Telephone='', Address='', ZipCode='', Priority='', UOAZipCode='', PersonFullName=''):
        super(LinkManField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.PersonType = self._to_bytes(PersonType)
        self.IdentifiedCardType = self._to_bytes(IdentifiedCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.PersonName = self._to_bytes(PersonName)
        self.Telephone = self._to_bytes(Telephone)
        self.Address = self._to_bytes(Address)
        self.ZipCode = self._to_bytes(ZipCode)
        self.Priority = int(Priority)
        self.UOAZipCode = self._to_bytes(UOAZipCode)
        self.PersonFullName = self._to_bytes(PersonFullName)


class QryBrokerUserEventField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('UserEventType', ctypes.c_char),
    ]

    def __init__(self, BrokerID='', UserID='', UserEventType=''):
        super(QryBrokerUserEventField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.UserEventType = self._to_bytes(UserEventType)


class BrokerUserEventField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('UserEventType', ctypes.c_char),
        ('EventSequenceNo', ctypes.c_int),
        ('EventDate', ctypes.c_char * 9),
        ('EventTime', ctypes.c_char * 9),
        ('UserEventInfo', ctypes.c_char * 1025),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
    ]

    def __init__(self, BrokerID='', UserID='', UserEventType='', EventSequenceNo='', EventDate='', EventTime='',
                 UserEventInfo='', InvestorID='', InstrumentID=''):
        super(BrokerUserEventField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.UserEventType = self._to_bytes(UserEventType)
        self.EventSequenceNo = int(EventSequenceNo)
        self.EventDate = self._to_bytes(EventDate)
        self.EventTime = self._to_bytes(EventTime)
        self.UserEventInfo = self._to_bytes(UserEventInfo)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryContractBankField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('BankID', ctypes.c_char * 4),
        ('BankBrchID', ctypes.c_char * 5),
    ]

    def __init__(self, BrokerID='', BankID='', BankBrchID=''):
        super(QryContractBankField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.BankID = self._to_bytes(BankID)
        self.BankBrchID = self._to_bytes(BankBrchID)


class ContractBankField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('BankID', ctypes.c_char * 4),
        ('BankBrchID', ctypes.c_char * 5),
        ('BankName', ctypes.c_char * 101),
    ]

    def __init__(self, BrokerID='', BankID='', BankBrchID='', BankName=''):
        super(ContractBankField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.BankID = self._to_bytes(BankID)
        self.BankBrchID = self._to_bytes(BankBrchID)
        self.BankName = self._to_bytes(BankName)


class InvestorPositionCombineDetailField(Base):
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),
        ('OpenDate', ctypes.c_char * 9),
        ('ExchangeID', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('ComTradeID', ctypes.c_char * 21),
        ('TradeID', ctypes.c_char * 21),
        ('InstrumentID', ctypes.c_char * 31),
        ('HedgeFlag', ctypes.c_char),
        ('Direction', ctypes.c_char),
        ('TotalAmt', ctypes.c_int),
        ('Margin', ctypes.c_double),
        ('ExchMargin', ctypes.c_double),
        ('MarginRateByMoney', ctypes.c_double),
        ('MarginRateByVolume', ctypes.c_double),
        ('LegID', ctypes.c_int),
        ('LegMultiple', ctypes.c_int),
        ('CombInstrumentID', ctypes.c_char * 31),
        ('TradeGroupID', ctypes.c_int),
    ]

    def __init__(self, TradingDay='', OpenDate='', ExchangeID='', SettlementID='', BrokerID='', InvestorID='',
                 ComTradeID='', TradeID='', InstrumentID='', HedgeFlag='', Direction='', TotalAmt='', Margin='',
                 ExchMargin='', MarginRateByMoney='', MarginRateByVolume='', LegID='', LegMultiple='',
                 CombInstrumentID='', TradeGroupID=''):
        super(InvestorPositionCombineDetailField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.OpenDate = self._to_bytes(OpenDate)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.SettlementID = int(SettlementID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ComTradeID = self._to_bytes(ComTradeID)
        self.TradeID = self._to_bytes(TradeID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.Direction = self._to_bytes(Direction)
        self.TotalAmt = int(TotalAmt)
        self.Margin = float(Margin)
        self.ExchMargin = float(ExchMargin)
        self.MarginRateByMoney = float(MarginRateByMoney)
        self.MarginRateByVolume = float(MarginRateByVolume)
        self.LegID = int(LegID)
        self.LegMultiple = int(LegMultiple)
        self.CombInstrumentID = self._to_bytes(CombInstrumentID)
        self.TradeGroupID = int(TradeGroupID)


class ParkedOrderField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('OrderRef', ctypes.c_char * 13),
        ('UserID', ctypes.c_char * 16),
        ('OrderPriceType', ctypes.c_char),
        ('Direction', ctypes.c_char),
        ('CombOffsetFlag', ctypes.c_char * 5),
        ('CombHedgeFlag', ctypes.c_char * 5),
        ('LimitPrice', ctypes.c_double),
        ('VolumeTotalOriginal', ctypes.c_int),
        ('TimeCondition', ctypes.c_char),
        ('GTDDate', ctypes.c_char * 9),
        ('VolumeCondition', ctypes.c_char),
        ('MinVolume', ctypes.c_int),
        ('ContingentCondition', ctypes.c_char),
        ('StopPrice', ctypes.c_double),
        ('ForceCloseReason', ctypes.c_char),
        ('IsAutoSuspend', ctypes.c_int),
        ('BusinessUnit', ctypes.c_char * 21),
        ('RequestID', ctypes.c_int),
        ('UserForceClose', ctypes.c_int),
        ('ExchangeID', ctypes.c_char * 9),
        ('ParkedOrderID', ctypes.c_char * 13),
        ('UserType', ctypes.c_char),
        ('Status', ctypes.c_char),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
        ('IsSwapOrder', ctypes.c_int),
        ('AccountID', ctypes.c_char * 13),
        ('CurrencyID', ctypes.c_char * 4),
        ('ClientID', ctypes.c_char * 11),
        ('InvestUnitID', ctypes.c_char * 17),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', OrderRef='', UserID='', OrderPriceType='',
                 Direction='', CombOffsetFlag='', CombHedgeFlag='', LimitPrice='', VolumeTotalOriginal='',
                 TimeCondition='', GTDDate='', VolumeCondition='', MinVolume='', ContingentCondition='', StopPrice='',
                 ForceCloseReason='', IsAutoSuspend='', BusinessUnit='', RequestID='', UserForceClose='', ExchangeID='',
                 ParkedOrderID='', UserType='', Status='', ErrorID='', ErrorMsg='', IsSwapOrder='', AccountID='',
                 CurrencyID='', ClientID='', InvestUnitID='', IPAddress='', MacAddress=''):
        super(ParkedOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.OrderRef = self._to_bytes(OrderRef)
        self.UserID = self._to_bytes(UserID)
        self.OrderPriceType = self._to_bytes(OrderPriceType)
        self.Direction = self._to_bytes(Direction)
        self.CombOffsetFlag = self._to_bytes(CombOffsetFlag)
        self.CombHedgeFlag = self._to_bytes(CombHedgeFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = self._to_bytes(TimeCondition)
        self.GTDDate = self._to_bytes(GTDDate)
        self.VolumeCondition = self._to_bytes(VolumeCondition)
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = self._to_bytes(ContingentCondition)
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = self._to_bytes(ForceCloseReason)
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.RequestID = int(RequestID)
        self.UserForceClose = int(UserForceClose)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParkedOrderID = self._to_bytes(ParkedOrderID)
        self.UserType = self._to_bytes(UserType)
        self.Status = self._to_bytes(Status)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.IsSwapOrder = int(IsSwapOrder)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.ClientID = self._to_bytes(ClientID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class ParkedOrderActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('OrderActionRef', ctypes.c_int),
        ('OrderRef', ctypes.c_char * 13),
        ('RequestID', ctypes.c_int),
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('ExchangeID', ctypes.c_char * 9),
        ('OrderSysID', ctypes.c_char * 21),
        ('ActionFlag', ctypes.c_char),
        ('LimitPrice', ctypes.c_double),
        ('VolumeChange', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('InstrumentID', ctypes.c_char * 31),
        ('ParkedOrderActionID', ctypes.c_char * 13),
        ('UserType', ctypes.c_char),
        ('Status', ctypes.c_char),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
        ('InvestUnitID', ctypes.c_char * 17),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', OrderActionRef='', OrderRef='', RequestID='', FrontID='',
                 SessionID='', ExchangeID='', OrderSysID='', ActionFlag='', LimitPrice='', VolumeChange='', UserID='',
                 InstrumentID='', ParkedOrderActionID='', UserType='', Status='', ErrorID='', ErrorMsg='',
                 InvestUnitID='', IPAddress='', MacAddress=''):
        super(ParkedOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OrderActionRef = int(OrderActionRef)
        self.OrderRef = self._to_bytes(OrderRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeChange = int(VolumeChange)
        self.UserID = self._to_bytes(UserID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ParkedOrderActionID = self._to_bytes(ParkedOrderActionID)
        self.UserType = self._to_bytes(UserType)
        self.Status = self._to_bytes(Status)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class QryParkedOrderField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID=''):
        super(QryParkedOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)


class QryParkedOrderActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', ExchangeID=''):
        super(QryParkedOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.ExchangeID = self._to_bytes(ExchangeID)


class RemoveParkedOrderField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('ParkedOrderID', ctypes.c_char * 13),
    ]

    def __init__(self, BrokerID='', InvestorID='', ParkedOrderID=''):
        super(RemoveParkedOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ParkedOrderID = self._to_bytes(ParkedOrderID)


class RemoveParkedOrderActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('ParkedOrderActionID', ctypes.c_char * 13),
    ]

    def __init__(self, BrokerID='', InvestorID='', ParkedOrderActionID=''):
        super(RemoveParkedOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ParkedOrderActionID = self._to_bytes(ParkedOrderActionID)


class InvestorWithdrawAlgorithmField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorRange', ctypes.c_char),
        ('InvestorID', ctypes.c_char * 13),
        ('UsingRatio', ctypes.c_double),
        ('CurrencyID', ctypes.c_char * 4),
        ('FundMortgageRatio', ctypes.c_double),
    ]

    def __init__(self, BrokerID='', InvestorRange='', InvestorID='', UsingRatio='', CurrencyID='',
                 FundMortgageRatio=''):
        super(InvestorWithdrawAlgorithmField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.InvestorID = self._to_bytes(InvestorID)
        self.UsingRatio = float(UsingRatio)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.FundMortgageRatio = float(FundMortgageRatio)


class QryInvestorPositionCombineDetailField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('CombInstrumentID', ctypes.c_char * 31),
    ]

    def __init__(self, BrokerID='', InvestorID='', CombInstrumentID=''):
        super(QryInvestorPositionCombineDetailField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.CombInstrumentID = self._to_bytes(CombInstrumentID)


class MarketDataAveragePriceField(Base):
    _fields_ = [
        ('AveragePrice', ctypes.c_double),
    ]

    def __init__(self, AveragePrice=''):
        super(MarketDataAveragePriceField, self).__init__()
        self.AveragePrice = float(AveragePrice)


class VerifyInvestorPasswordField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
    ]

    def __init__(self, BrokerID='', InvestorID='', Password=''):
        super(VerifyInvestorPasswordField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.Password = self._to_bytes(Password)


class UserIPField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('IPAddress', ctypes.c_char * 16),
        ('IPMask', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', UserID='', IPAddress='', IPMask='', MacAddress=''):
        super(UserIPField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.IPMask = self._to_bytes(IPMask)
        self.MacAddress = self._to_bytes(MacAddress)


class TradingNoticeInfoField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('SendTime', ctypes.c_char * 9),
        ('FieldContent', ctypes.c_char * 501),
        ('SequenceSeries', ctypes.c_short),
        ('SequenceNo', ctypes.c_int),
    ]

    def __init__(self, BrokerID='', InvestorID='', SendTime='', FieldContent='', SequenceSeries='', SequenceNo=''):
        super(TradingNoticeInfoField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.SendTime = self._to_bytes(SendTime)
        self.FieldContent = self._to_bytes(FieldContent)
        self.SequenceSeries = int(SequenceSeries)
        self.SequenceNo = int(SequenceNo)


class TradingNoticeField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorRange', ctypes.c_char),
        ('InvestorID', ctypes.c_char * 13),
        ('SequenceSeries', ctypes.c_short),
        ('UserID', ctypes.c_char * 16),
        ('SendTime', ctypes.c_char * 9),
        ('SequenceNo', ctypes.c_int),
        ('FieldContent', ctypes.c_char * 501),
    ]

    def __init__(self, BrokerID='', InvestorRange='', InvestorID='', SequenceSeries='', UserID='', SendTime='',
                 SequenceNo='', FieldContent=''):
        super(TradingNoticeField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorRange = self._to_bytes(InvestorRange)
        self.InvestorID = self._to_bytes(InvestorID)
        self.SequenceSeries = int(SequenceSeries)
        self.UserID = self._to_bytes(UserID)
        self.SendTime = self._to_bytes(SendTime)
        self.SequenceNo = int(SequenceNo)
        self.FieldContent = self._to_bytes(FieldContent)


class QryTradingNoticeField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
    ]

    def __init__(self, BrokerID='', InvestorID=''):
        super(QryTradingNoticeField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)


class QryErrOrderField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
    ]

    def __init__(self, BrokerID='', InvestorID=''):
        super(QryErrOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)


class ErrOrderField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('OrderRef', ctypes.c_char * 13),
        ('UserID', ctypes.c_char * 16),
        ('OrderPriceType', ctypes.c_char),
        ('Direction', ctypes.c_char),
        ('CombOffsetFlag', ctypes.c_char * 5),
        ('CombHedgeFlag', ctypes.c_char * 5),
        ('LimitPrice', ctypes.c_double),
        ('VolumeTotalOriginal', ctypes.c_int),
        ('TimeCondition', ctypes.c_char),
        ('GTDDate', ctypes.c_char * 9),
        ('VolumeCondition', ctypes.c_char),
        ('MinVolume', ctypes.c_int),
        ('ContingentCondition', ctypes.c_char),
        ('StopPrice', ctypes.c_double),
        ('ForceCloseReason', ctypes.c_char),
        ('IsAutoSuspend', ctypes.c_int),
        ('BusinessUnit', ctypes.c_char * 21),
        ('RequestID', ctypes.c_int),
        ('UserForceClose', ctypes.c_int),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
        ('IsSwapOrder', ctypes.c_int),
        ('ExchangeID', ctypes.c_char * 9),
        ('InvestUnitID', ctypes.c_char * 17),
        ('AccountID', ctypes.c_char * 13),
        ('CurrencyID', ctypes.c_char * 4),
        ('ClientID', ctypes.c_char * 11),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', OrderRef='', UserID='', OrderPriceType='',
                 Direction='', CombOffsetFlag='', CombHedgeFlag='', LimitPrice='', VolumeTotalOriginal='',
                 TimeCondition='', GTDDate='', VolumeCondition='', MinVolume='', ContingentCondition='', StopPrice='',
                 ForceCloseReason='', IsAutoSuspend='', BusinessUnit='', RequestID='', UserForceClose='', ErrorID='',
                 ErrorMsg='', IsSwapOrder='', ExchangeID='', InvestUnitID='', AccountID='', CurrencyID='', ClientID='',
                 IPAddress='', MacAddress=''):
        super(ErrOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.OrderRef = self._to_bytes(OrderRef)
        self.UserID = self._to_bytes(UserID)
        self.OrderPriceType = self._to_bytes(OrderPriceType)
        self.Direction = self._to_bytes(Direction)
        self.CombOffsetFlag = self._to_bytes(CombOffsetFlag)
        self.CombHedgeFlag = self._to_bytes(CombHedgeFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = self._to_bytes(TimeCondition)
        self.GTDDate = self._to_bytes(GTDDate)
        self.VolumeCondition = self._to_bytes(VolumeCondition)
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = self._to_bytes(ContingentCondition)
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = self._to_bytes(ForceCloseReason)
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.RequestID = int(RequestID)
        self.UserForceClose = int(UserForceClose)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.IsSwapOrder = int(IsSwapOrder)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.ClientID = self._to_bytes(ClientID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class ErrorConditionalOrderField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('OrderRef', ctypes.c_char * 13),
        ('UserID', ctypes.c_char * 16),
        ('OrderPriceType', ctypes.c_char),
        ('Direction', ctypes.c_char),
        ('CombOffsetFlag', ctypes.c_char * 5),
        ('CombHedgeFlag', ctypes.c_char * 5),
        ('LimitPrice', ctypes.c_double),
        ('VolumeTotalOriginal', ctypes.c_int),
        ('TimeCondition', ctypes.c_char),
        ('GTDDate', ctypes.c_char * 9),
        ('VolumeCondition', ctypes.c_char),
        ('MinVolume', ctypes.c_int),
        ('ContingentCondition', ctypes.c_char),
        ('StopPrice', ctypes.c_double),
        ('ForceCloseReason', ctypes.c_char),
        ('IsAutoSuspend', ctypes.c_int),
        ('BusinessUnit', ctypes.c_char * 21),
        ('RequestID', ctypes.c_int),
        ('OrderLocalID', ctypes.c_char * 13),
        ('ExchangeID', ctypes.c_char * 9),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('ExchangeInstID', ctypes.c_char * 31),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('OrderSubmitStatus', ctypes.c_char),
        ('NotifySequence', ctypes.c_int),
        ('TradingDay', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
        ('OrderSysID', ctypes.c_char * 21),
        ('OrderSource', ctypes.c_char),
        ('OrderStatus', ctypes.c_char),
        ('OrderType', ctypes.c_char),
        ('VolumeTraded', ctypes.c_int),
        ('VolumeTotal', ctypes.c_int),
        ('InsertDate', ctypes.c_char * 9),
        ('InsertTime', ctypes.c_char * 9),
        ('ActiveTime', ctypes.c_char * 9),
        ('SuspendTime', ctypes.c_char * 9),
        ('UpdateTime', ctypes.c_char * 9),
        ('CancelTime', ctypes.c_char * 9),
        ('ActiveTraderID', ctypes.c_char * 21),
        ('ClearingPartID', ctypes.c_char * 11),
        ('SequenceNo', ctypes.c_int),
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('UserProductInfo', ctypes.c_char * 11),
        ('StatusMsg', ctypes.c_char * 81),
        ('UserForceClose', ctypes.c_int),
        ('ActiveUserID', ctypes.c_char * 16),
        ('BrokerOrderSeq', ctypes.c_int),
        ('RelativeOrderSysID', ctypes.c_char * 21),
        ('ZCETotalTradedVolume', ctypes.c_int),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
        ('IsSwapOrder', ctypes.c_int),
        ('BranchID', ctypes.c_char * 9),
        ('InvestUnitID', ctypes.c_char * 17),
        ('AccountID', ctypes.c_char * 13),
        ('CurrencyID', ctypes.c_char * 4),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
    ]

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
        super(ErrorConditionalOrderField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.OrderRef = self._to_bytes(OrderRef)
        self.UserID = self._to_bytes(UserID)
        self.OrderPriceType = self._to_bytes(OrderPriceType)
        self.Direction = self._to_bytes(Direction)
        self.CombOffsetFlag = self._to_bytes(CombOffsetFlag)
        self.CombHedgeFlag = self._to_bytes(CombHedgeFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeTotalOriginal = int(VolumeTotalOriginal)
        self.TimeCondition = self._to_bytes(TimeCondition)
        self.GTDDate = self._to_bytes(GTDDate)
        self.VolumeCondition = self._to_bytes(VolumeCondition)
        self.MinVolume = int(MinVolume)
        self.ContingentCondition = self._to_bytes(ContingentCondition)
        self.StopPrice = float(StopPrice)
        self.ForceCloseReason = self._to_bytes(ForceCloseReason)
        self.IsAutoSuspend = int(IsAutoSuspend)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.RequestID = int(RequestID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.ExchangeInstID = self._to_bytes(ExchangeInstID)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderSubmitStatus = self._to_bytes(OrderSubmitStatus)
        self.NotifySequence = int(NotifySequence)
        self.TradingDay = self._to_bytes(TradingDay)
        self.SettlementID = int(SettlementID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.OrderSource = self._to_bytes(OrderSource)
        self.OrderStatus = self._to_bytes(OrderStatus)
        self.OrderType = self._to_bytes(OrderType)
        self.VolumeTraded = int(VolumeTraded)
        self.VolumeTotal = int(VolumeTotal)
        self.InsertDate = self._to_bytes(InsertDate)
        self.InsertTime = self._to_bytes(InsertTime)
        self.ActiveTime = self._to_bytes(ActiveTime)
        self.SuspendTime = self._to_bytes(SuspendTime)
        self.UpdateTime = self._to_bytes(UpdateTime)
        self.CancelTime = self._to_bytes(CancelTime)
        self.ActiveTraderID = self._to_bytes(ActiveTraderID)
        self.ClearingPartID = self._to_bytes(ClearingPartID)
        self.SequenceNo = int(SequenceNo)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.UserProductInfo = self._to_bytes(UserProductInfo)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.UserForceClose = int(UserForceClose)
        self.ActiveUserID = self._to_bytes(ActiveUserID)
        self.BrokerOrderSeq = int(BrokerOrderSeq)
        self.RelativeOrderSysID = self._to_bytes(RelativeOrderSysID)
        self.ZCETotalTradedVolume = int(ZCETotalTradedVolume)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.IsSwapOrder = int(IsSwapOrder)
        self.BranchID = self._to_bytes(BranchID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)


class QryErrOrderActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
    ]

    def __init__(self, BrokerID='', InvestorID=''):
        super(QryErrOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)


class ErrOrderActionField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('OrderActionRef', ctypes.c_int),
        ('OrderRef', ctypes.c_char * 13),
        ('RequestID', ctypes.c_int),
        ('FrontID', ctypes.c_int),
        ('SessionID', ctypes.c_int),
        ('ExchangeID', ctypes.c_char * 9),
        ('OrderSysID', ctypes.c_char * 21),
        ('ActionFlag', ctypes.c_char),
        ('LimitPrice', ctypes.c_double),
        ('VolumeChange', ctypes.c_int),
        ('ActionDate', ctypes.c_char * 9),
        ('ActionTime', ctypes.c_char * 9),
        ('TraderID', ctypes.c_char * 21),
        ('InstallID', ctypes.c_int),
        ('OrderLocalID', ctypes.c_char * 13),
        ('ActionLocalID', ctypes.c_char * 13),
        ('ParticipantID', ctypes.c_char * 11),
        ('ClientID', ctypes.c_char * 11),
        ('BusinessUnit', ctypes.c_char * 21),
        ('OrderActionStatus', ctypes.c_char),
        ('UserID', ctypes.c_char * 16),
        ('StatusMsg', ctypes.c_char * 81),
        ('InstrumentID', ctypes.c_char * 31),
        ('BranchID', ctypes.c_char * 9),
        ('InvestUnitID', ctypes.c_char * 17),
        ('IPAddress', ctypes.c_char * 16),
        ('MacAddress', ctypes.c_char * 21),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
    ]

    def __init__(self, BrokerID='', InvestorID='', OrderActionRef='', OrderRef='', RequestID='', FrontID='',
                 SessionID='', ExchangeID='', OrderSysID='', ActionFlag='', LimitPrice='', VolumeChange='',
                 ActionDate='', ActionTime='', TraderID='', InstallID='', OrderLocalID='', ActionLocalID='',
                 ParticipantID='', ClientID='', BusinessUnit='', OrderActionStatus='', UserID='', StatusMsg='',
                 InstrumentID='', BranchID='', InvestUnitID='', IPAddress='', MacAddress='', ErrorID='', ErrorMsg=''):
        super(ErrOrderActionField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.OrderActionRef = int(OrderActionRef)
        self.OrderRef = self._to_bytes(OrderRef)
        self.RequestID = int(RequestID)
        self.FrontID = int(FrontID)
        self.SessionID = int(SessionID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.OrderSysID = self._to_bytes(OrderSysID)
        self.ActionFlag = self._to_bytes(ActionFlag)
        self.LimitPrice = float(LimitPrice)
        self.VolumeChange = int(VolumeChange)
        self.ActionDate = self._to_bytes(ActionDate)
        self.ActionTime = self._to_bytes(ActionTime)
        self.TraderID = self._to_bytes(TraderID)
        self.InstallID = int(InstallID)
        self.OrderLocalID = self._to_bytes(OrderLocalID)
        self.ActionLocalID = self._to_bytes(ActionLocalID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ClientID = self._to_bytes(ClientID)
        self.BusinessUnit = self._to_bytes(BusinessUnit)
        self.OrderActionStatus = self._to_bytes(OrderActionStatus)
        self.UserID = self._to_bytes(UserID)
        self.StatusMsg = self._to_bytes(StatusMsg)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.BranchID = self._to_bytes(BranchID)
        self.InvestUnitID = self._to_bytes(InvestUnitID)
        self.IPAddress = self._to_bytes(IPAddress)
        self.MacAddress = self._to_bytes(MacAddress)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class QryExchangeSequenceField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
    ]

    def __init__(self, ExchangeID=''):
        super(QryExchangeSequenceField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)


class ExchangeSequenceField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('SequenceNo', ctypes.c_int),
        ('MarketStatus', ctypes.c_char),
    ]

    def __init__(self, ExchangeID='', SequenceNo='', MarketStatus=''):
        super(ExchangeSequenceField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.SequenceNo = int(SequenceNo)
        self.MarketStatus = self._to_bytes(MarketStatus)


class QueryMaxOrderVolumeWithPriceField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('InstrumentID', ctypes.c_char * 31),
        ('Direction', ctypes.c_char),
        ('OffsetFlag', ctypes.c_char),
        ('HedgeFlag', ctypes.c_char),
        ('MaxVolume', ctypes.c_int),
        ('Price', ctypes.c_double),
    ]

    def __init__(self, BrokerID='', InvestorID='', InstrumentID='', Direction='', OffsetFlag='', HedgeFlag='',
                 MaxVolume='', Price=''):
        super(QueryMaxOrderVolumeWithPriceField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.Direction = self._to_bytes(Direction)
        self.OffsetFlag = self._to_bytes(OffsetFlag)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.MaxVolume = int(MaxVolume)
        self.Price = float(Price)


class QryBrokerTradingParamsField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('CurrencyID', ctypes.c_char * 4),
    ]

    def __init__(self, BrokerID='', InvestorID='', CurrencyID=''):
        super(QryBrokerTradingParamsField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.CurrencyID = self._to_bytes(CurrencyID)


class BrokerTradingParamsField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('MarginPriceType', ctypes.c_char),
        ('Algorithm', ctypes.c_char),
        ('AvailIncludeCloseProfit', ctypes.c_char),
        ('CurrencyID', ctypes.c_char * 4),
        ('OptionRoyaltyPriceType', ctypes.c_char),
    ]

    def __init__(self, BrokerID='', InvestorID='', MarginPriceType='', Algorithm='', AvailIncludeCloseProfit='',
                 CurrencyID='', OptionRoyaltyPriceType=''):
        super(BrokerTradingParamsField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.MarginPriceType = self._to_bytes(MarginPriceType)
        self.Algorithm = self._to_bytes(Algorithm)
        self.AvailIncludeCloseProfit = self._to_bytes(AvailIncludeCloseProfit)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.OptionRoyaltyPriceType = self._to_bytes(OptionRoyaltyPriceType)


class QryBrokerTradingAlgosField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('ExchangeID', ctypes.c_char * 9),
        ('InstrumentID', ctypes.c_char * 31),
    ]

    def __init__(self, BrokerID='', ExchangeID='', InstrumentID=''):
        super(QryBrokerTradingAlgosField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class BrokerTradingAlgosField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('ExchangeID', ctypes.c_char * 9),
        ('InstrumentID', ctypes.c_char * 31),
        ('HandlePositionAlgoID', ctypes.c_char),
        ('FindMarginRateAlgoID', ctypes.c_char),
        ('HandleTradingAccountAlgoID', ctypes.c_char),
    ]

    def __init__(self, BrokerID='', ExchangeID='', InstrumentID='', HandlePositionAlgoID='', FindMarginRateAlgoID='',
                 HandleTradingAccountAlgoID=''):
        super(BrokerTradingAlgosField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.HandlePositionAlgoID = self._to_bytes(HandlePositionAlgoID)
        self.FindMarginRateAlgoID = self._to_bytes(FindMarginRateAlgoID)
        self.HandleTradingAccountAlgoID = self._to_bytes(HandleTradingAccountAlgoID)


class QueryBrokerDepositField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('ExchangeID', ctypes.c_char * 9),
    ]

    def __init__(self, BrokerID='', ExchangeID=''):
        super(QueryBrokerDepositField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.ExchangeID = self._to_bytes(ExchangeID)


class BrokerDepositField(Base):
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),
        ('BrokerID', ctypes.c_char * 11),
        ('ParticipantID', ctypes.c_char * 11),
        ('ExchangeID', ctypes.c_char * 9),
        ('PreBalance', ctypes.c_double),
        ('CurrMargin', ctypes.c_double),
        ('CloseProfit', ctypes.c_double),
        ('Balance', ctypes.c_double),
        ('Deposit', ctypes.c_double),
        ('Withdraw', ctypes.c_double),
        ('Available', ctypes.c_double),
        ('Reserve', ctypes.c_double),
        ('FrozenMargin', ctypes.c_double),
    ]

    def __init__(self, TradingDay='', BrokerID='', ParticipantID='', ExchangeID='', PreBalance='', CurrMargin='',
                 CloseProfit='', Balance='', Deposit='', Withdraw='', Available='', Reserve='', FrozenMargin=''):
        super(BrokerDepositField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.BrokerID = self._to_bytes(BrokerID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.ExchangeID = self._to_bytes(ExchangeID)
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
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
    ]

    def __init__(self, BrokerID=''):
        super(QryCFMMCBrokerKeyField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)


class CFMMCBrokerKeyField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('ParticipantID', ctypes.c_char * 11),
        ('CreateDate', ctypes.c_char * 9),
        ('CreateTime', ctypes.c_char * 9),
        ('KeyID', ctypes.c_int),
        ('CurrentKey', ctypes.c_char * 21),
        ('KeyKind', ctypes.c_char),
    ]

    def __init__(self, BrokerID='', ParticipantID='', CreateDate='', CreateTime='', KeyID='', CurrentKey='',
                 KeyKind=''):
        super(CFMMCBrokerKeyField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.CreateDate = self._to_bytes(CreateDate)
        self.CreateTime = self._to_bytes(CreateTime)
        self.KeyID = int(KeyID)
        self.CurrentKey = self._to_bytes(CurrentKey)
        self.KeyKind = self._to_bytes(KeyKind)


class CFMMCTradingAccountKeyField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('ParticipantID', ctypes.c_char * 11),
        ('AccountID', ctypes.c_char * 13),
        ('KeyID', ctypes.c_int),
        ('CurrentKey', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', ParticipantID='', AccountID='', KeyID='', CurrentKey=''):
        super(CFMMCTradingAccountKeyField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.AccountID = self._to_bytes(AccountID)
        self.KeyID = int(KeyID)
        self.CurrentKey = self._to_bytes(CurrentKey)


class QryCFMMCTradingAccountKeyField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
    ]

    def __init__(self, BrokerID='', InvestorID=''):
        super(QryCFMMCTradingAccountKeyField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)


class BrokerUserOTPParamField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('OTPVendorsID', ctypes.c_char * 2),
        ('SerialNumber', ctypes.c_char * 17),
        ('AuthKey', ctypes.c_char * 41),
        ('LastDrift', ctypes.c_int),
        ('LastSuccess', ctypes.c_int),
        ('OTPType', ctypes.c_char),
    ]

    def __init__(self, BrokerID='', UserID='', OTPVendorsID='', SerialNumber='', AuthKey='', LastDrift='',
                 LastSuccess='', OTPType=''):
        super(BrokerUserOTPParamField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.OTPVendorsID = self._to_bytes(OTPVendorsID)
        self.SerialNumber = self._to_bytes(SerialNumber)
        self.AuthKey = self._to_bytes(AuthKey)
        self.LastDrift = int(LastDrift)
        self.LastSuccess = int(LastSuccess)
        self.OTPType = self._to_bytes(OTPType)


class ManualSyncBrokerUserOTPField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('OTPType', ctypes.c_char),
        ('FirstOTP', ctypes.c_char * 41),
        ('SecondOTP', ctypes.c_char * 41),
    ]

    def __init__(self, BrokerID='', UserID='', OTPType='', FirstOTP='', SecondOTP=''):
        super(ManualSyncBrokerUserOTPField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.OTPType = self._to_bytes(OTPType)
        self.FirstOTP = self._to_bytes(FirstOTP)
        self.SecondOTP = self._to_bytes(SecondOTP)


class CommRateModelField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('CommModelID', ctypes.c_char * 13),
        ('CommModelName', ctypes.c_char * 161),
    ]

    def __init__(self, BrokerID='', CommModelID='', CommModelName=''):
        super(CommRateModelField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.CommModelID = self._to_bytes(CommModelID)
        self.CommModelName = self._to_bytes(CommModelName)


class QryCommRateModelField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('CommModelID', ctypes.c_char * 13),
    ]

    def __init__(self, BrokerID='', CommModelID=''):
        super(QryCommRateModelField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.CommModelID = self._to_bytes(CommModelID)


class MarginModelField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('MarginModelID', ctypes.c_char * 13),
        ('MarginModelName', ctypes.c_char * 161),
    ]

    def __init__(self, BrokerID='', MarginModelID='', MarginModelName=''):
        super(MarginModelField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.MarginModelID = self._to_bytes(MarginModelID)
        self.MarginModelName = self._to_bytes(MarginModelName)


class QryMarginModelField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('MarginModelID', ctypes.c_char * 13),
    ]

    def __init__(self, BrokerID='', MarginModelID=''):
        super(QryMarginModelField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.MarginModelID = self._to_bytes(MarginModelID)


class EWarrantOffsetField(Base):
    _fields_ = [
        ('TradingDay', ctypes.c_char * 9),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('ExchangeID', ctypes.c_char * 9),
        ('InstrumentID', ctypes.c_char * 31),
        ('Direction', ctypes.c_char),
        ('HedgeFlag', ctypes.c_char),
        ('Volume', ctypes.c_int),
    ]

    def __init__(self, TradingDay='', BrokerID='', InvestorID='', ExchangeID='', InstrumentID='', Direction='',
                 HedgeFlag='', Volume=''):
        super(EWarrantOffsetField, self).__init__()
        self.TradingDay = self._to_bytes(TradingDay)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentID = self._to_bytes(InstrumentID)
        self.Direction = self._to_bytes(Direction)
        self.HedgeFlag = self._to_bytes(HedgeFlag)
        self.Volume = int(Volume)


class QryEWarrantOffsetField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('ExchangeID', ctypes.c_char * 9),
        ('InstrumentID', ctypes.c_char * 31),
    ]

    def __init__(self, BrokerID='', InvestorID='', ExchangeID='', InstrumentID=''):
        super(QryEWarrantOffsetField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.InstrumentID = self._to_bytes(InstrumentID)


class QryInvestorProductGroupMarginField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('ProductGroupID', ctypes.c_char * 31),
        ('HedgeFlag', ctypes.c_char),
    ]

    def __init__(self, BrokerID='', InvestorID='', ProductGroupID='', HedgeFlag=''):
        super(QryInvestorProductGroupMarginField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.ProductGroupID = self._to_bytes(ProductGroupID)
        self.HedgeFlag = self._to_bytes(HedgeFlag)


class InvestorProductGroupMarginField(Base):
    _fields_ = [
        ('ProductGroupID', ctypes.c_char * 31),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('SettlementID', ctypes.c_int),
        ('FrozenMargin', ctypes.c_double),
        ('LongFrozenMargin', ctypes.c_double),
        ('ShortFrozenMargin', ctypes.c_double),
        ('UseMargin', ctypes.c_double),
        ('LongUseMargin', ctypes.c_double),
        ('ShortUseMargin', ctypes.c_double),
        ('ExchMargin', ctypes.c_double),
        ('LongExchMargin', ctypes.c_double),
        ('ShortExchMargin', ctypes.c_double),
        ('CloseProfit', ctypes.c_double),
        ('FrozenCommission', ctypes.c_double),
        ('Commission', ctypes.c_double),
        ('FrozenCash', ctypes.c_double),
        ('CashIn', ctypes.c_double),
        ('PositionProfit', ctypes.c_double),
        ('OffsetAmount', ctypes.c_double),
        ('LongOffsetAmount', ctypes.c_double),
        ('ShortOffsetAmount', ctypes.c_double),
        ('ExchOffsetAmount', ctypes.c_double),
        ('LongExchOffsetAmount', ctypes.c_double),
        ('ShortExchOffsetAmount', ctypes.c_double),
        ('HedgeFlag', ctypes.c_char),
    ]

    def __init__(self, ProductGroupID='', BrokerID='', InvestorID='', TradingDay='', SettlementID='', FrozenMargin='',
                 LongFrozenMargin='', ShortFrozenMargin='', UseMargin='', LongUseMargin='', ShortUseMargin='',
                 ExchMargin='', LongExchMargin='', ShortExchMargin='', CloseProfit='', FrozenCommission='',
                 Commission='', FrozenCash='', CashIn='', PositionProfit='', OffsetAmount='', LongOffsetAmount='',
                 ShortOffsetAmount='', ExchOffsetAmount='', LongExchOffsetAmount='', ShortExchOffsetAmount='',
                 HedgeFlag=''):
        super(InvestorProductGroupMarginField, self).__init__()
        self.ProductGroupID = self._to_bytes(ProductGroupID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.TradingDay = self._to_bytes(TradingDay)
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
        self.HedgeFlag = self._to_bytes(HedgeFlag)


class QueryCFMMCTradingAccountTokenField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
    ]

    def __init__(self, BrokerID='', InvestorID=''):
        super(QueryCFMMCTradingAccountTokenField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)


class CFMMCTradingAccountTokenField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('ParticipantID', ctypes.c_char * 11),
        ('AccountID', ctypes.c_char * 13),
        ('KeyID', ctypes.c_int),
        ('Token', ctypes.c_char * 21),
    ]

    def __init__(self, BrokerID='', ParticipantID='', AccountID='', KeyID='', Token=''):
        super(CFMMCTradingAccountTokenField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.ParticipantID = self._to_bytes(ParticipantID)
        self.AccountID = self._to_bytes(AccountID)
        self.KeyID = int(KeyID)
        self.Token = self._to_bytes(Token)


class QryProductGroupField(Base):
    _fields_ = [
        ('ProductID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
    ]

    def __init__(self, ProductID='', ExchangeID=''):
        super(QryProductGroupField, self).__init__()
        self.ProductID = self._to_bytes(ProductID)
        self.ExchangeID = self._to_bytes(ExchangeID)


class ProductGroupField(Base):
    _fields_ = [
        ('ProductID', ctypes.c_char * 31),
        ('ExchangeID', ctypes.c_char * 9),
        ('ProductGroupID', ctypes.c_char * 31),
    ]

    def __init__(self, ProductID='', ExchangeID='', ProductGroupID=''):
        super(ProductGroupField, self).__init__()
        self.ProductID = self._to_bytes(ProductID)
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.ProductGroupID = self._to_bytes(ProductGroupID)


class BulletinField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('TradingDay', ctypes.c_char * 9),
        ('BulletinID', ctypes.c_int),
        ('SequenceNo', ctypes.c_int),
        ('NewsType', ctypes.c_char * 3),
        ('NewsUrgency', ctypes.c_char),
        ('SendTime', ctypes.c_char * 9),
        ('Abstract', ctypes.c_char * 81),
        ('ComeFrom', ctypes.c_char * 21),
        ('Content', ctypes.c_char * 501),
        ('URLLink', ctypes.c_char * 201),
        ('MarketID', ctypes.c_char * 31),
    ]

    def __init__(self, ExchangeID='', TradingDay='', BulletinID='', SequenceNo='', NewsType='', NewsUrgency='',
                 SendTime='', Abstract='', ComeFrom='', Content='', URLLink='', MarketID=''):
        super(BulletinField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.TradingDay = self._to_bytes(TradingDay)
        self.BulletinID = int(BulletinID)
        self.SequenceNo = int(SequenceNo)
        self.NewsType = self._to_bytes(NewsType)
        self.NewsUrgency = self._to_bytes(NewsUrgency)
        self.SendTime = self._to_bytes(SendTime)
        self.Abstract = self._to_bytes(Abstract)
        self.ComeFrom = self._to_bytes(ComeFrom)
        self.Content = self._to_bytes(Content)
        self.URLLink = self._to_bytes(URLLink)
        self.MarketID = self._to_bytes(MarketID)


class QryBulletinField(Base):
    _fields_ = [
        ('ExchangeID', ctypes.c_char * 9),
        ('BulletinID', ctypes.c_int),
        ('SequenceNo', ctypes.c_int),
        ('NewsType', ctypes.c_char * 3),
        ('NewsUrgency', ctypes.c_char),
    ]

    def __init__(self, ExchangeID='', BulletinID='', SequenceNo='', NewsType='', NewsUrgency=''):
        super(QryBulletinField, self).__init__()
        self.ExchangeID = self._to_bytes(ExchangeID)
        self.BulletinID = int(BulletinID)
        self.SequenceNo = int(SequenceNo)
        self.NewsType = self._to_bytes(NewsType)
        self.NewsUrgency = self._to_bytes(NewsUrgency)


class ReqOpenAccountField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('CustomerName', ctypes.c_char * 51),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('Gender', ctypes.c_char),
        ('CountryCode', ctypes.c_char * 21),
        ('CustType', ctypes.c_char),
        ('Address', ctypes.c_char * 101),
        ('ZipCode', ctypes.c_char * 7),
        ('Telephone', ctypes.c_char * 41),
        ('MobilePhone', ctypes.c_char * 21),
        ('Fax', ctypes.c_char * 41),
        ('EMail', ctypes.c_char * 41),
        ('MoneyAccountStatus', ctypes.c_char),
        ('BankAccount', ctypes.c_char * 41),
        ('BankPassWord', ctypes.c_char * 41),
        ('AccountID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
        ('InstallID', ctypes.c_int),
        ('VerifyCertNoFlag', ctypes.c_char),
        ('CurrencyID', ctypes.c_char * 4),
        ('CashExchangeCode', ctypes.c_char),
        ('Digest', ctypes.c_char * 36),
        ('BankAccType', ctypes.c_char),
        ('DeviceID', ctypes.c_char * 3),
        ('BankSecuAccType', ctypes.c_char),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('BankSecuAcc', ctypes.c_char * 41),
        ('BankPwdFlag', ctypes.c_char),
        ('SecuPwdFlag', ctypes.c_char),
        ('OperNo', ctypes.c_char * 17),
        ('TID', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('LongCustomerName', ctypes.c_char * 161),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', Gender='', CountryCode='', CustType='',
                 Address='', ZipCode='', Telephone='', MobilePhone='', Fax='', EMail='', MoneyAccountStatus='',
                 BankAccount='', BankPassWord='', AccountID='', Password='', InstallID='', VerifyCertNoFlag='',
                 CurrencyID='', CashExchangeCode='', Digest='', BankAccType='', DeviceID='', BankSecuAccType='',
                 BrokerIDByBank='', BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='', OperNo='', TID='', UserID='',
                 LongCustomerName=''):
        super(ReqOpenAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.Gender = self._to_bytes(Gender)
        self.CountryCode = self._to_bytes(CountryCode)
        self.CustType = self._to_bytes(CustType)
        self.Address = self._to_bytes(Address)
        self.ZipCode = self._to_bytes(ZipCode)
        self.Telephone = self._to_bytes(Telephone)
        self.MobilePhone = self._to_bytes(MobilePhone)
        self.Fax = self._to_bytes(Fax)
        self.EMail = self._to_bytes(EMail)
        self.MoneyAccountStatus = self._to_bytes(MoneyAccountStatus)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.CashExchangeCode = self._to_bytes(CashExchangeCode)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.TID = int(TID)
        self.UserID = self._to_bytes(UserID)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class ReqCancelAccountField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('CustomerName', ctypes.c_char * 51),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('Gender', ctypes.c_char),
        ('CountryCode', ctypes.c_char * 21),
        ('CustType', ctypes.c_char),
        ('Address', ctypes.c_char * 101),
        ('ZipCode', ctypes.c_char * 7),
        ('Telephone', ctypes.c_char * 41),
        ('MobilePhone', ctypes.c_char * 21),
        ('Fax', ctypes.c_char * 41),
        ('EMail', ctypes.c_char * 41),
        ('MoneyAccountStatus', ctypes.c_char),
        ('BankAccount', ctypes.c_char * 41),
        ('BankPassWord', ctypes.c_char * 41),
        ('AccountID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
        ('InstallID', ctypes.c_int),
        ('VerifyCertNoFlag', ctypes.c_char),
        ('CurrencyID', ctypes.c_char * 4),
        ('CashExchangeCode', ctypes.c_char),
        ('Digest', ctypes.c_char * 36),
        ('BankAccType', ctypes.c_char),
        ('DeviceID', ctypes.c_char * 3),
        ('BankSecuAccType', ctypes.c_char),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('BankSecuAcc', ctypes.c_char * 41),
        ('BankPwdFlag', ctypes.c_char),
        ('SecuPwdFlag', ctypes.c_char),
        ('OperNo', ctypes.c_char * 17),
        ('TID', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('LongCustomerName', ctypes.c_char * 161),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', Gender='', CountryCode='', CustType='',
                 Address='', ZipCode='', Telephone='', MobilePhone='', Fax='', EMail='', MoneyAccountStatus='',
                 BankAccount='', BankPassWord='', AccountID='', Password='', InstallID='', VerifyCertNoFlag='',
                 CurrencyID='', CashExchangeCode='', Digest='', BankAccType='', DeviceID='', BankSecuAccType='',
                 BrokerIDByBank='', BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='', OperNo='', TID='', UserID='',
                 LongCustomerName=''):
        super(ReqCancelAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.Gender = self._to_bytes(Gender)
        self.CountryCode = self._to_bytes(CountryCode)
        self.CustType = self._to_bytes(CustType)
        self.Address = self._to_bytes(Address)
        self.ZipCode = self._to_bytes(ZipCode)
        self.Telephone = self._to_bytes(Telephone)
        self.MobilePhone = self._to_bytes(MobilePhone)
        self.Fax = self._to_bytes(Fax)
        self.EMail = self._to_bytes(EMail)
        self.MoneyAccountStatus = self._to_bytes(MoneyAccountStatus)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.CashExchangeCode = self._to_bytes(CashExchangeCode)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.TID = int(TID)
        self.UserID = self._to_bytes(UserID)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class ReqChangeAccountField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('CustomerName', ctypes.c_char * 51),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('Gender', ctypes.c_char),
        ('CountryCode', ctypes.c_char * 21),
        ('CustType', ctypes.c_char),
        ('Address', ctypes.c_char * 101),
        ('ZipCode', ctypes.c_char * 7),
        ('Telephone', ctypes.c_char * 41),
        ('MobilePhone', ctypes.c_char * 21),
        ('Fax', ctypes.c_char * 41),
        ('EMail', ctypes.c_char * 41),
        ('MoneyAccountStatus', ctypes.c_char),
        ('BankAccount', ctypes.c_char * 41),
        ('BankPassWord', ctypes.c_char * 41),
        ('NewBankAccount', ctypes.c_char * 41),
        ('NewBankPassWord', ctypes.c_char * 41),
        ('AccountID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
        ('BankAccType', ctypes.c_char),
        ('InstallID', ctypes.c_int),
        ('VerifyCertNoFlag', ctypes.c_char),
        ('CurrencyID', ctypes.c_char * 4),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('BankPwdFlag', ctypes.c_char),
        ('SecuPwdFlag', ctypes.c_char),
        ('TID', ctypes.c_int),
        ('Digest', ctypes.c_char * 36),
        ('LongCustomerName', ctypes.c_char * 161),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', Gender='', CountryCode='', CustType='',
                 Address='', ZipCode='', Telephone='', MobilePhone='', Fax='', EMail='', MoneyAccountStatus='',
                 BankAccount='', BankPassWord='', NewBankAccount='', NewBankPassWord='', AccountID='', Password='',
                 BankAccType='', InstallID='', VerifyCertNoFlag='', CurrencyID='', BrokerIDByBank='', BankPwdFlag='',
                 SecuPwdFlag='', TID='', Digest='', LongCustomerName=''):
        super(ReqChangeAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.Gender = self._to_bytes(Gender)
        self.CountryCode = self._to_bytes(CountryCode)
        self.CustType = self._to_bytes(CustType)
        self.Address = self._to_bytes(Address)
        self.ZipCode = self._to_bytes(ZipCode)
        self.Telephone = self._to_bytes(Telephone)
        self.MobilePhone = self._to_bytes(MobilePhone)
        self.Fax = self._to_bytes(Fax)
        self.EMail = self._to_bytes(EMail)
        self.MoneyAccountStatus = self._to_bytes(MoneyAccountStatus)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.NewBankAccount = self._to_bytes(NewBankAccount)
        self.NewBankPassWord = self._to_bytes(NewBankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.BankAccType = self._to_bytes(BankAccType)
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.TID = int(TID)
        self.Digest = self._to_bytes(Digest)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class ReqTransferField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('CustomerName', ctypes.c_char * 51),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('CustType', ctypes.c_char),
        ('BankAccount', ctypes.c_char * 41),
        ('BankPassWord', ctypes.c_char * 41),
        ('AccountID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
        ('InstallID', ctypes.c_int),
        ('FutureSerial', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('VerifyCertNoFlag', ctypes.c_char),
        ('CurrencyID', ctypes.c_char * 4),
        ('TradeAmount', ctypes.c_double),
        ('FutureFetchAmount', ctypes.c_double),
        ('FeePayFlag', ctypes.c_char),
        ('CustFee', ctypes.c_double),
        ('BrokerFee', ctypes.c_double),
        ('Message', ctypes.c_char * 129),
        ('Digest', ctypes.c_char * 36),
        ('BankAccType', ctypes.c_char),
        ('DeviceID', ctypes.c_char * 3),
        ('BankSecuAccType', ctypes.c_char),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('BankSecuAcc', ctypes.c_char * 41),
        ('BankPwdFlag', ctypes.c_char),
        ('SecuPwdFlag', ctypes.c_char),
        ('OperNo', ctypes.c_char * 17),
        ('RequestID', ctypes.c_int),
        ('TID', ctypes.c_int),
        ('TransferStatus', ctypes.c_char),
        ('LongCustomerName', ctypes.c_char * 161),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', CustType='', BankAccount='', BankPassWord='',
                 AccountID='', Password='', InstallID='', FutureSerial='', UserID='', VerifyCertNoFlag='',
                 CurrencyID='', TradeAmount='', FutureFetchAmount='', FeePayFlag='', CustFee='', BrokerFee='',
                 Message='', Digest='', BankAccType='', DeviceID='', BankSecuAccType='', BrokerIDByBank='',
                 BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='', OperNo='', RequestID='', TID='', TransferStatus='',
                 LongCustomerName=''):
        super(ReqTransferField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.FutureSerial = int(FutureSerial)
        self.UserID = self._to_bytes(UserID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.TradeAmount = float(TradeAmount)
        self.FutureFetchAmount = float(FutureFetchAmount)
        self.FeePayFlag = self._to_bytes(FeePayFlag)
        self.CustFee = float(CustFee)
        self.BrokerFee = float(BrokerFee)
        self.Message = self._to_bytes(Message)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.TransferStatus = self._to_bytes(TransferStatus)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class RspTransferField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('CustomerName', ctypes.c_char * 51),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('CustType', ctypes.c_char),
        ('BankAccount', ctypes.c_char * 41),
        ('BankPassWord', ctypes.c_char * 41),
        ('AccountID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
        ('InstallID', ctypes.c_int),
        ('FutureSerial', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('VerifyCertNoFlag', ctypes.c_char),
        ('CurrencyID', ctypes.c_char * 4),
        ('TradeAmount', ctypes.c_double),
        ('FutureFetchAmount', ctypes.c_double),
        ('FeePayFlag', ctypes.c_char),
        ('CustFee', ctypes.c_double),
        ('BrokerFee', ctypes.c_double),
        ('Message', ctypes.c_char * 129),
        ('Digest', ctypes.c_char * 36),
        ('BankAccType', ctypes.c_char),
        ('DeviceID', ctypes.c_char * 3),
        ('BankSecuAccType', ctypes.c_char),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('BankSecuAcc', ctypes.c_char * 41),
        ('BankPwdFlag', ctypes.c_char),
        ('SecuPwdFlag', ctypes.c_char),
        ('OperNo', ctypes.c_char * 17),
        ('RequestID', ctypes.c_int),
        ('TID', ctypes.c_int),
        ('TransferStatus', ctypes.c_char),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
        ('LongCustomerName', ctypes.c_char * 161),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', CustType='', BankAccount='', BankPassWord='',
                 AccountID='', Password='', InstallID='', FutureSerial='', UserID='', VerifyCertNoFlag='',
                 CurrencyID='', TradeAmount='', FutureFetchAmount='', FeePayFlag='', CustFee='', BrokerFee='',
                 Message='', Digest='', BankAccType='', DeviceID='', BankSecuAccType='', BrokerIDByBank='',
                 BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='', OperNo='', RequestID='', TID='', TransferStatus='',
                 ErrorID='', ErrorMsg='', LongCustomerName=''):
        super(RspTransferField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.FutureSerial = int(FutureSerial)
        self.UserID = self._to_bytes(UserID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.TradeAmount = float(TradeAmount)
        self.FutureFetchAmount = float(FutureFetchAmount)
        self.FeePayFlag = self._to_bytes(FeePayFlag)
        self.CustFee = float(CustFee)
        self.BrokerFee = float(BrokerFee)
        self.Message = self._to_bytes(Message)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.TransferStatus = self._to_bytes(TransferStatus)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class ReqRepealField(Base):
    _fields_ = [
        ('RepealTimeInterval', ctypes.c_int),
        ('RepealedTimes', ctypes.c_int),
        ('BankRepealFlag', ctypes.c_char),
        ('BrokerRepealFlag', ctypes.c_char),
        ('PlateRepealSerial', ctypes.c_int),
        ('BankRepealSerial', ctypes.c_char * 13),
        ('FutureRepealSerial', ctypes.c_int),
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('CustomerName', ctypes.c_char * 51),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('CustType', ctypes.c_char),
        ('BankAccount', ctypes.c_char * 41),
        ('BankPassWord', ctypes.c_char * 41),
        ('AccountID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
        ('InstallID', ctypes.c_int),
        ('FutureSerial', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('VerifyCertNoFlag', ctypes.c_char),
        ('CurrencyID', ctypes.c_char * 4),
        ('TradeAmount', ctypes.c_double),
        ('FutureFetchAmount', ctypes.c_double),
        ('FeePayFlag', ctypes.c_char),
        ('CustFee', ctypes.c_double),
        ('BrokerFee', ctypes.c_double),
        ('Message', ctypes.c_char * 129),
        ('Digest', ctypes.c_char * 36),
        ('BankAccType', ctypes.c_char),
        ('DeviceID', ctypes.c_char * 3),
        ('BankSecuAccType', ctypes.c_char),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('BankSecuAcc', ctypes.c_char * 41),
        ('BankPwdFlag', ctypes.c_char),
        ('SecuPwdFlag', ctypes.c_char),
        ('OperNo', ctypes.c_char * 17),
        ('RequestID', ctypes.c_int),
        ('TID', ctypes.c_int),
        ('TransferStatus', ctypes.c_char),
        ('LongCustomerName', ctypes.c_char * 161),
    ]

    def __init__(self, RepealTimeInterval='', RepealedTimes='', BankRepealFlag='', BrokerRepealFlag='',
                 PlateRepealSerial='', BankRepealSerial='', FutureRepealSerial='', TradeCode='', BankID='',
                 BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='',
                 TradingDay='', PlateSerial='', LastFragment='', SessionID='', CustomerName='', IdCardType='',
                 IdentifiedCardNo='', CustType='', BankAccount='', BankPassWord='', AccountID='', Password='',
                 InstallID='', FutureSerial='', UserID='', VerifyCertNoFlag='', CurrencyID='', TradeAmount='',
                 FutureFetchAmount='', FeePayFlag='', CustFee='', BrokerFee='', Message='', Digest='', BankAccType='',
                 DeviceID='', BankSecuAccType='', BrokerIDByBank='', BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='',
                 OperNo='', RequestID='', TID='', TransferStatus='', LongCustomerName=''):
        super(ReqRepealField, self).__init__()
        self.RepealTimeInterval = int(RepealTimeInterval)
        self.RepealedTimes = int(RepealedTimes)
        self.BankRepealFlag = self._to_bytes(BankRepealFlag)
        self.BrokerRepealFlag = self._to_bytes(BrokerRepealFlag)
        self.PlateRepealSerial = int(PlateRepealSerial)
        self.BankRepealSerial = self._to_bytes(BankRepealSerial)
        self.FutureRepealSerial = int(FutureRepealSerial)
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.FutureSerial = int(FutureSerial)
        self.UserID = self._to_bytes(UserID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.TradeAmount = float(TradeAmount)
        self.FutureFetchAmount = float(FutureFetchAmount)
        self.FeePayFlag = self._to_bytes(FeePayFlag)
        self.CustFee = float(CustFee)
        self.BrokerFee = float(BrokerFee)
        self.Message = self._to_bytes(Message)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.TransferStatus = self._to_bytes(TransferStatus)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class RspRepealField(Base):
    _fields_ = [
        ('RepealTimeInterval', ctypes.c_int),
        ('RepealedTimes', ctypes.c_int),
        ('BankRepealFlag', ctypes.c_char),
        ('BrokerRepealFlag', ctypes.c_char),
        ('PlateRepealSerial', ctypes.c_int),
        ('BankRepealSerial', ctypes.c_char * 13),
        ('FutureRepealSerial', ctypes.c_int),
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('CustomerName', ctypes.c_char * 51),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('CustType', ctypes.c_char),
        ('BankAccount', ctypes.c_char * 41),
        ('BankPassWord', ctypes.c_char * 41),
        ('AccountID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
        ('InstallID', ctypes.c_int),
        ('FutureSerial', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('VerifyCertNoFlag', ctypes.c_char),
        ('CurrencyID', ctypes.c_char * 4),
        ('TradeAmount', ctypes.c_double),
        ('FutureFetchAmount', ctypes.c_double),
        ('FeePayFlag', ctypes.c_char),
        ('CustFee', ctypes.c_double),
        ('BrokerFee', ctypes.c_double),
        ('Message', ctypes.c_char * 129),
        ('Digest', ctypes.c_char * 36),
        ('BankAccType', ctypes.c_char),
        ('DeviceID', ctypes.c_char * 3),
        ('BankSecuAccType', ctypes.c_char),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('BankSecuAcc', ctypes.c_char * 41),
        ('BankPwdFlag', ctypes.c_char),
        ('SecuPwdFlag', ctypes.c_char),
        ('OperNo', ctypes.c_char * 17),
        ('RequestID', ctypes.c_int),
        ('TID', ctypes.c_int),
        ('TransferStatus', ctypes.c_char),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
        ('LongCustomerName', ctypes.c_char * 161),
    ]

    def __init__(self, RepealTimeInterval='', RepealedTimes='', BankRepealFlag='', BrokerRepealFlag='',
                 PlateRepealSerial='', BankRepealSerial='', FutureRepealSerial='', TradeCode='', BankID='',
                 BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='', TradeTime='', BankSerial='',
                 TradingDay='', PlateSerial='', LastFragment='', SessionID='', CustomerName='', IdCardType='',
                 IdentifiedCardNo='', CustType='', BankAccount='', BankPassWord='', AccountID='', Password='',
                 InstallID='', FutureSerial='', UserID='', VerifyCertNoFlag='', CurrencyID='', TradeAmount='',
                 FutureFetchAmount='', FeePayFlag='', CustFee='', BrokerFee='', Message='', Digest='', BankAccType='',
                 DeviceID='', BankSecuAccType='', BrokerIDByBank='', BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='',
                 OperNo='', RequestID='', TID='', TransferStatus='', ErrorID='', ErrorMsg='', LongCustomerName=''):
        super(RspRepealField, self).__init__()
        self.RepealTimeInterval = int(RepealTimeInterval)
        self.RepealedTimes = int(RepealedTimes)
        self.BankRepealFlag = self._to_bytes(BankRepealFlag)
        self.BrokerRepealFlag = self._to_bytes(BrokerRepealFlag)
        self.PlateRepealSerial = int(PlateRepealSerial)
        self.BankRepealSerial = self._to_bytes(BankRepealSerial)
        self.FutureRepealSerial = int(FutureRepealSerial)
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.FutureSerial = int(FutureSerial)
        self.UserID = self._to_bytes(UserID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.TradeAmount = float(TradeAmount)
        self.FutureFetchAmount = float(FutureFetchAmount)
        self.FeePayFlag = self._to_bytes(FeePayFlag)
        self.CustFee = float(CustFee)
        self.BrokerFee = float(BrokerFee)
        self.Message = self._to_bytes(Message)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.TransferStatus = self._to_bytes(TransferStatus)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class ReqQueryAccountField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('CustomerName', ctypes.c_char * 51),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('CustType', ctypes.c_char),
        ('BankAccount', ctypes.c_char * 41),
        ('BankPassWord', ctypes.c_char * 41),
        ('AccountID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
        ('FutureSerial', ctypes.c_int),
        ('InstallID', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('VerifyCertNoFlag', ctypes.c_char),
        ('CurrencyID', ctypes.c_char * 4),
        ('Digest', ctypes.c_char * 36),
        ('BankAccType', ctypes.c_char),
        ('DeviceID', ctypes.c_char * 3),
        ('BankSecuAccType', ctypes.c_char),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('BankSecuAcc', ctypes.c_char * 41),
        ('BankPwdFlag', ctypes.c_char),
        ('SecuPwdFlag', ctypes.c_char),
        ('OperNo', ctypes.c_char * 17),
        ('RequestID', ctypes.c_int),
        ('TID', ctypes.c_int),
        ('LongCustomerName', ctypes.c_char * 161),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', CustType='', BankAccount='', BankPassWord='',
                 AccountID='', Password='', FutureSerial='', InstallID='', UserID='', VerifyCertNoFlag='',
                 CurrencyID='', Digest='', BankAccType='', DeviceID='', BankSecuAccType='', BrokerIDByBank='',
                 BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='', OperNo='', RequestID='', TID='', LongCustomerName=''):
        super(ReqQueryAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.FutureSerial = int(FutureSerial)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class RspQueryAccountField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('CustomerName', ctypes.c_char * 51),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('CustType', ctypes.c_char),
        ('BankAccount', ctypes.c_char * 41),
        ('BankPassWord', ctypes.c_char * 41),
        ('AccountID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
        ('FutureSerial', ctypes.c_int),
        ('InstallID', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('VerifyCertNoFlag', ctypes.c_char),
        ('CurrencyID', ctypes.c_char * 4),
        ('Digest', ctypes.c_char * 36),
        ('BankAccType', ctypes.c_char),
        ('DeviceID', ctypes.c_char * 3),
        ('BankSecuAccType', ctypes.c_char),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('BankSecuAcc', ctypes.c_char * 41),
        ('BankPwdFlag', ctypes.c_char),
        ('SecuPwdFlag', ctypes.c_char),
        ('OperNo', ctypes.c_char * 17),
        ('RequestID', ctypes.c_int),
        ('TID', ctypes.c_int),
        ('BankUseAmount', ctypes.c_double),
        ('BankFetchAmount', ctypes.c_double),
        ('LongCustomerName', ctypes.c_char * 161),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', CustType='', BankAccount='', BankPassWord='',
                 AccountID='', Password='', FutureSerial='', InstallID='', UserID='', VerifyCertNoFlag='',
                 CurrencyID='', Digest='', BankAccType='', DeviceID='', BankSecuAccType='', BrokerIDByBank='',
                 BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='', OperNo='', RequestID='', TID='', BankUseAmount='',
                 BankFetchAmount='', LongCustomerName=''):
        super(RspQueryAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.FutureSerial = int(FutureSerial)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.BankUseAmount = float(BankUseAmount)
        self.BankFetchAmount = float(BankFetchAmount)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class FutureSignIOField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('InstallID', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('Digest', ctypes.c_char * 36),
        ('CurrencyID', ctypes.c_char * 4),
        ('DeviceID', ctypes.c_char * 3),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('OperNo', ctypes.c_char * 17),
        ('RequestID', ctypes.c_int),
        ('TID', ctypes.c_int),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 InstallID='', UserID='', Digest='', CurrencyID='', DeviceID='', BrokerIDByBank='', OperNo='',
                 RequestID='', TID=''):
        super(FutureSignIOField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.Digest = self._to_bytes(Digest)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)


class RspFutureSignInField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('InstallID', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('Digest', ctypes.c_char * 36),
        ('CurrencyID', ctypes.c_char * 4),
        ('DeviceID', ctypes.c_char * 3),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('OperNo', ctypes.c_char * 17),
        ('RequestID', ctypes.c_int),
        ('TID', ctypes.c_int),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
        ('PinKey', ctypes.c_char * 129),
        ('MacKey', ctypes.c_char * 129),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 InstallID='', UserID='', Digest='', CurrencyID='', DeviceID='', BrokerIDByBank='', OperNo='',
                 RequestID='', TID='', ErrorID='', ErrorMsg='', PinKey='', MacKey=''):
        super(RspFutureSignInField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.Digest = self._to_bytes(Digest)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.PinKey = self._to_bytes(PinKey)
        self.MacKey = self._to_bytes(MacKey)


class ReqFutureSignOutField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('InstallID', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('Digest', ctypes.c_char * 36),
        ('CurrencyID', ctypes.c_char * 4),
        ('DeviceID', ctypes.c_char * 3),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('OperNo', ctypes.c_char * 17),
        ('RequestID', ctypes.c_int),
        ('TID', ctypes.c_int),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 InstallID='', UserID='', Digest='', CurrencyID='', DeviceID='', BrokerIDByBank='', OperNo='',
                 RequestID='', TID=''):
        super(ReqFutureSignOutField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.Digest = self._to_bytes(Digest)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)


class RspFutureSignOutField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('InstallID', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('Digest', ctypes.c_char * 36),
        ('CurrencyID', ctypes.c_char * 4),
        ('DeviceID', ctypes.c_char * 3),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('OperNo', ctypes.c_char * 17),
        ('RequestID', ctypes.c_int),
        ('TID', ctypes.c_int),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 InstallID='', UserID='', Digest='', CurrencyID='', DeviceID='', BrokerIDByBank='', OperNo='',
                 RequestID='', TID='', ErrorID='', ErrorMsg=''):
        super(RspFutureSignOutField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.Digest = self._to_bytes(Digest)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class ReqQueryTradeResultBySerialField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('Reference', ctypes.c_int),
        ('RefrenceIssureType', ctypes.c_char),
        ('RefrenceIssure', ctypes.c_char * 36),
        ('CustomerName', ctypes.c_char * 51),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('CustType', ctypes.c_char),
        ('BankAccount', ctypes.c_char * 41),
        ('BankPassWord', ctypes.c_char * 41),
        ('AccountID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
        ('CurrencyID', ctypes.c_char * 4),
        ('TradeAmount', ctypes.c_double),
        ('Digest', ctypes.c_char * 36),
        ('LongCustomerName', ctypes.c_char * 161),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 Reference='', RefrenceIssureType='', RefrenceIssure='', CustomerName='', IdCardType='',
                 IdentifiedCardNo='', CustType='', BankAccount='', BankPassWord='', AccountID='', Password='',
                 CurrencyID='', TradeAmount='', Digest='', LongCustomerName=''):
        super(ReqQueryTradeResultBySerialField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.Reference = int(Reference)
        self.RefrenceIssureType = self._to_bytes(RefrenceIssureType)
        self.RefrenceIssure = self._to_bytes(RefrenceIssure)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.TradeAmount = float(TradeAmount)
        self.Digest = self._to_bytes(Digest)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class RspQueryTradeResultBySerialField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
        ('Reference', ctypes.c_int),
        ('RefrenceIssureType', ctypes.c_char),
        ('RefrenceIssure', ctypes.c_char * 36),
        ('OriginReturnCode', ctypes.c_char * 7),
        ('OriginDescrInfoForReturnCode', ctypes.c_char * 129),
        ('BankAccount', ctypes.c_char * 41),
        ('BankPassWord', ctypes.c_char * 41),
        ('AccountID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
        ('CurrencyID', ctypes.c_char * 4),
        ('TradeAmount', ctypes.c_double),
        ('Digest', ctypes.c_char * 36),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='', ErrorID='',
                 ErrorMsg='', Reference='', RefrenceIssureType='', RefrenceIssure='', OriginReturnCode='',
                 OriginDescrInfoForReturnCode='', BankAccount='', BankPassWord='', AccountID='', Password='',
                 CurrencyID='', TradeAmount='', Digest=''):
        super(RspQueryTradeResultBySerialField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.Reference = int(Reference)
        self.RefrenceIssureType = self._to_bytes(RefrenceIssureType)
        self.RefrenceIssure = self._to_bytes(RefrenceIssure)
        self.OriginReturnCode = self._to_bytes(OriginReturnCode)
        self.OriginDescrInfoForReturnCode = self._to_bytes(OriginDescrInfoForReturnCode)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.TradeAmount = float(TradeAmount)
        self.Digest = self._to_bytes(Digest)


class ReqDayEndFileReadyField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('FileBusinessCode', ctypes.c_char),
        ('Digest', ctypes.c_char * 36),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 FileBusinessCode='', Digest=''):
        super(ReqDayEndFileReadyField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.FileBusinessCode = self._to_bytes(FileBusinessCode)
        self.Digest = self._to_bytes(Digest)


class ReturnResultField(Base):
    _fields_ = [
        ('ReturnCode', ctypes.c_char * 7),
        ('DescrInfoForReturnCode', ctypes.c_char * 129),
    ]

    def __init__(self, ReturnCode='', DescrInfoForReturnCode=''):
        super(ReturnResultField, self).__init__()
        self.ReturnCode = self._to_bytes(ReturnCode)
        self.DescrInfoForReturnCode = self._to_bytes(DescrInfoForReturnCode)


class VerifyFuturePasswordField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('AccountID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
        ('BankAccount', ctypes.c_char * 41),
        ('BankPassWord', ctypes.c_char * 41),
        ('InstallID', ctypes.c_int),
        ('TID', ctypes.c_int),
        ('CurrencyID', ctypes.c_char * 4),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 AccountID='', Password='', BankAccount='', BankPassWord='', InstallID='', TID='', CurrencyID=''):
        super(VerifyFuturePasswordField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.InstallID = int(InstallID)
        self.TID = int(TID)
        self.CurrencyID = self._to_bytes(CurrencyID)


class VerifyCustInfoField(Base):
    _fields_ = [
        ('CustomerName', ctypes.c_char * 51),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('CustType', ctypes.c_char),
        ('LongCustomerName', ctypes.c_char * 161),
    ]

    def __init__(self, CustomerName='', IdCardType='', IdentifiedCardNo='', CustType='', LongCustomerName=''):
        super(VerifyCustInfoField, self).__init__()
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class VerifyFuturePasswordAndCustInfoField(Base):
    _fields_ = [
        ('CustomerName', ctypes.c_char * 51),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('CustType', ctypes.c_char),
        ('AccountID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
        ('CurrencyID', ctypes.c_char * 4),
        ('LongCustomerName', ctypes.c_char * 161),
    ]

    def __init__(self, CustomerName='', IdCardType='', IdentifiedCardNo='', CustType='', AccountID='', Password='',
                 CurrencyID='', LongCustomerName=''):
        super(VerifyFuturePasswordAndCustInfoField, self).__init__()
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class DepositResultInformField(Base):
    _fields_ = [
        ('DepositSeqNo', ctypes.c_char * 15),
        ('BrokerID', ctypes.c_char * 11),
        ('InvestorID', ctypes.c_char * 13),
        ('Deposit', ctypes.c_double),
        ('RequestID', ctypes.c_int),
        ('ReturnCode', ctypes.c_char * 7),
        ('DescrInfoForReturnCode', ctypes.c_char * 129),
    ]

    def __init__(self, DepositSeqNo='', BrokerID='', InvestorID='', Deposit='', RequestID='', ReturnCode='',
                 DescrInfoForReturnCode=''):
        super(DepositResultInformField, self).__init__()
        self.DepositSeqNo = self._to_bytes(DepositSeqNo)
        self.BrokerID = self._to_bytes(BrokerID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.Deposit = float(Deposit)
        self.RequestID = int(RequestID)
        self.ReturnCode = self._to_bytes(ReturnCode)
        self.DescrInfoForReturnCode = self._to_bytes(DescrInfoForReturnCode)


class ReqSyncKeyField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('InstallID', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('Message', ctypes.c_char * 129),
        ('DeviceID', ctypes.c_char * 3),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('OperNo', ctypes.c_char * 17),
        ('RequestID', ctypes.c_int),
        ('TID', ctypes.c_int),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 InstallID='', UserID='', Message='', DeviceID='', BrokerIDByBank='', OperNo='', RequestID='', TID=''):
        super(ReqSyncKeyField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.Message = self._to_bytes(Message)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)


class RspSyncKeyField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('InstallID', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('Message', ctypes.c_char * 129),
        ('DeviceID', ctypes.c_char * 3),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('OperNo', ctypes.c_char * 17),
        ('RequestID', ctypes.c_int),
        ('TID', ctypes.c_int),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 InstallID='', UserID='', Message='', DeviceID='', BrokerIDByBank='', OperNo='', RequestID='', TID='',
                 ErrorID='', ErrorMsg=''):
        super(RspSyncKeyField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.Message = self._to_bytes(Message)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class NotifyQueryAccountField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('CustomerName', ctypes.c_char * 51),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('CustType', ctypes.c_char),
        ('BankAccount', ctypes.c_char * 41),
        ('BankPassWord', ctypes.c_char * 41),
        ('AccountID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
        ('FutureSerial', ctypes.c_int),
        ('InstallID', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('VerifyCertNoFlag', ctypes.c_char),
        ('CurrencyID', ctypes.c_char * 4),
        ('Digest', ctypes.c_char * 36),
        ('BankAccType', ctypes.c_char),
        ('DeviceID', ctypes.c_char * 3),
        ('BankSecuAccType', ctypes.c_char),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('BankSecuAcc', ctypes.c_char * 41),
        ('BankPwdFlag', ctypes.c_char),
        ('SecuPwdFlag', ctypes.c_char),
        ('OperNo', ctypes.c_char * 17),
        ('RequestID', ctypes.c_int),
        ('TID', ctypes.c_int),
        ('BankUseAmount', ctypes.c_double),
        ('BankFetchAmount', ctypes.c_double),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
        ('LongCustomerName', ctypes.c_char * 161),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', CustType='', BankAccount='', BankPassWord='',
                 AccountID='', Password='', FutureSerial='', InstallID='', UserID='', VerifyCertNoFlag='',
                 CurrencyID='', Digest='', BankAccType='', DeviceID='', BankSecuAccType='', BrokerIDByBank='',
                 BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='', OperNo='', RequestID='', TID='', BankUseAmount='',
                 BankFetchAmount='', ErrorID='', ErrorMsg='', LongCustomerName=''):
        super(NotifyQueryAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustType = self._to_bytes(CustType)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.FutureSerial = int(FutureSerial)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.BankUseAmount = float(BankUseAmount)
        self.BankFetchAmount = float(BankFetchAmount)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class TransferSerialField(Base):
    _fields_ = [
        ('PlateSerial', ctypes.c_int),
        ('TradeDate', ctypes.c_char * 9),
        ('TradingDay', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('TradeCode', ctypes.c_char * 7),
        ('SessionID', ctypes.c_int),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BankAccType', ctypes.c_char),
        ('BankAccount', ctypes.c_char * 41),
        ('BankSerial', ctypes.c_char * 13),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('FutureAccType', ctypes.c_char),
        ('AccountID', ctypes.c_char * 13),
        ('InvestorID', ctypes.c_char * 13),
        ('FutureSerial', ctypes.c_int),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('CurrencyID', ctypes.c_char * 4),
        ('TradeAmount', ctypes.c_double),
        ('CustFee', ctypes.c_double),
        ('BrokerFee', ctypes.c_double),
        ('AvailabilityFlag', ctypes.c_char),
        ('OperatorCode', ctypes.c_char * 17),
        ('BankNewAccount', ctypes.c_char * 41),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
    ]

    def __init__(self, PlateSerial='', TradeDate='', TradingDay='', TradeTime='', TradeCode='', SessionID='', BankID='',
                 BankBranchID='', BankAccType='', BankAccount='', BankSerial='', BrokerID='', BrokerBranchID='',
                 FutureAccType='', AccountID='', InvestorID='', FutureSerial='', IdCardType='', IdentifiedCardNo='',
                 CurrencyID='', TradeAmount='', CustFee='', BrokerFee='', AvailabilityFlag='', OperatorCode='',
                 BankNewAccount='', ErrorID='', ErrorMsg=''):
        super(TransferSerialField, self).__init__()
        self.PlateSerial = int(PlateSerial)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradingDay = self._to_bytes(TradingDay)
        self.TradeTime = self._to_bytes(TradeTime)
        self.TradeCode = self._to_bytes(TradeCode)
        self.SessionID = int(SessionID)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BankAccType = self._to_bytes(BankAccType)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankSerial = self._to_bytes(BankSerial)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.FutureAccType = self._to_bytes(FutureAccType)
        self.AccountID = self._to_bytes(AccountID)
        self.InvestorID = self._to_bytes(InvestorID)
        self.FutureSerial = int(FutureSerial)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.TradeAmount = float(TradeAmount)
        self.CustFee = float(CustFee)
        self.BrokerFee = float(BrokerFee)
        self.AvailabilityFlag = self._to_bytes(AvailabilityFlag)
        self.OperatorCode = self._to_bytes(OperatorCode)
        self.BankNewAccount = self._to_bytes(BankNewAccount)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class QryTransferSerialField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('AccountID', ctypes.c_char * 13),
        ('BankID', ctypes.c_char * 4),
        ('CurrencyID', ctypes.c_char * 4),
    ]

    def __init__(self, BrokerID='', AccountID='', BankID='', CurrencyID=''):
        super(QryTransferSerialField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AccountID = self._to_bytes(AccountID)
        self.BankID = self._to_bytes(BankID)
        self.CurrencyID = self._to_bytes(CurrencyID)


class NotifyFutureSignInField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('InstallID', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('Digest', ctypes.c_char * 36),
        ('CurrencyID', ctypes.c_char * 4),
        ('DeviceID', ctypes.c_char * 3),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('OperNo', ctypes.c_char * 17),
        ('RequestID', ctypes.c_int),
        ('TID', ctypes.c_int),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
        ('PinKey', ctypes.c_char * 129),
        ('MacKey', ctypes.c_char * 129),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 InstallID='', UserID='', Digest='', CurrencyID='', DeviceID='', BrokerIDByBank='', OperNo='',
                 RequestID='', TID='', ErrorID='', ErrorMsg='', PinKey='', MacKey=''):
        super(NotifyFutureSignInField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.Digest = self._to_bytes(Digest)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.PinKey = self._to_bytes(PinKey)
        self.MacKey = self._to_bytes(MacKey)


class NotifyFutureSignOutField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('InstallID', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('Digest', ctypes.c_char * 36),
        ('CurrencyID', ctypes.c_char * 4),
        ('DeviceID', ctypes.c_char * 3),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('OperNo', ctypes.c_char * 17),
        ('RequestID', ctypes.c_int),
        ('TID', ctypes.c_int),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 InstallID='', UserID='', Digest='', CurrencyID='', DeviceID='', BrokerIDByBank='', OperNo='',
                 RequestID='', TID='', ErrorID='', ErrorMsg=''):
        super(NotifyFutureSignOutField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.Digest = self._to_bytes(Digest)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class NotifySyncKeyField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('InstallID', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('Message', ctypes.c_char * 129),
        ('DeviceID', ctypes.c_char * 3),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('OperNo', ctypes.c_char * 17),
        ('RequestID', ctypes.c_int),
        ('TID', ctypes.c_int),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 InstallID='', UserID='', Message='', DeviceID='', BrokerIDByBank='', OperNo='', RequestID='', TID='',
                 ErrorID='', ErrorMsg=''):
        super(NotifySyncKeyField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.InstallID = int(InstallID)
        self.UserID = self._to_bytes(UserID)
        self.Message = self._to_bytes(Message)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.OperNo = self._to_bytes(OperNo)
        self.RequestID = int(RequestID)
        self.TID = int(TID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class QryAccountregisterField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('AccountID', ctypes.c_char * 13),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('CurrencyID', ctypes.c_char * 4),
    ]

    def __init__(self, BrokerID='', AccountID='', BankID='', BankBranchID='', CurrencyID=''):
        super(QryAccountregisterField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AccountID = self._to_bytes(AccountID)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.CurrencyID = self._to_bytes(CurrencyID)


class AccountregisterField(Base):
    _fields_ = [
        ('TradeDay', ctypes.c_char * 9),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BankAccount', ctypes.c_char * 41),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('AccountID', ctypes.c_char * 13),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('CustomerName', ctypes.c_char * 51),
        ('CurrencyID', ctypes.c_char * 4),
        ('OpenOrDestroy', ctypes.c_char),
        ('RegDate', ctypes.c_char * 9),
        ('OutDate', ctypes.c_char * 9),
        ('TID', ctypes.c_int),
        ('CustType', ctypes.c_char),
        ('BankAccType', ctypes.c_char),
        ('LongCustomerName', ctypes.c_char * 161),
    ]

    def __init__(self, TradeDay='', BankID='', BankBranchID='', BankAccount='', BrokerID='', BrokerBranchID='',
                 AccountID='', IdCardType='', IdentifiedCardNo='', CustomerName='', CurrencyID='', OpenOrDestroy='',
                 RegDate='', OutDate='', TID='', CustType='', BankAccType='', LongCustomerName=''):
        super(AccountregisterField, self).__init__()
        self.TradeDay = self._to_bytes(TradeDay)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.AccountID = self._to_bytes(AccountID)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.CustomerName = self._to_bytes(CustomerName)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.OpenOrDestroy = self._to_bytes(OpenOrDestroy)
        self.RegDate = self._to_bytes(RegDate)
        self.OutDate = self._to_bytes(OutDate)
        self.TID = int(TID)
        self.CustType = self._to_bytes(CustType)
        self.BankAccType = self._to_bytes(BankAccType)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class OpenAccountField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('CustomerName', ctypes.c_char * 51),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('Gender', ctypes.c_char),
        ('CountryCode', ctypes.c_char * 21),
        ('CustType', ctypes.c_char),
        ('Address', ctypes.c_char * 101),
        ('ZipCode', ctypes.c_char * 7),
        ('Telephone', ctypes.c_char * 41),
        ('MobilePhone', ctypes.c_char * 21),
        ('Fax', ctypes.c_char * 41),
        ('EMail', ctypes.c_char * 41),
        ('MoneyAccountStatus', ctypes.c_char),
        ('BankAccount', ctypes.c_char * 41),
        ('BankPassWord', ctypes.c_char * 41),
        ('AccountID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
        ('InstallID', ctypes.c_int),
        ('VerifyCertNoFlag', ctypes.c_char),
        ('CurrencyID', ctypes.c_char * 4),
        ('CashExchangeCode', ctypes.c_char),
        ('Digest', ctypes.c_char * 36),
        ('BankAccType', ctypes.c_char),
        ('DeviceID', ctypes.c_char * 3),
        ('BankSecuAccType', ctypes.c_char),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('BankSecuAcc', ctypes.c_char * 41),
        ('BankPwdFlag', ctypes.c_char),
        ('SecuPwdFlag', ctypes.c_char),
        ('OperNo', ctypes.c_char * 17),
        ('TID', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
        ('LongCustomerName', ctypes.c_char * 161),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', Gender='', CountryCode='', CustType='',
                 Address='', ZipCode='', Telephone='', MobilePhone='', Fax='', EMail='', MoneyAccountStatus='',
                 BankAccount='', BankPassWord='', AccountID='', Password='', InstallID='', VerifyCertNoFlag='',
                 CurrencyID='', CashExchangeCode='', Digest='', BankAccType='', DeviceID='', BankSecuAccType='',
                 BrokerIDByBank='', BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='', OperNo='', TID='', UserID='',
                 ErrorID='', ErrorMsg='', LongCustomerName=''):
        super(OpenAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.Gender = self._to_bytes(Gender)
        self.CountryCode = self._to_bytes(CountryCode)
        self.CustType = self._to_bytes(CustType)
        self.Address = self._to_bytes(Address)
        self.ZipCode = self._to_bytes(ZipCode)
        self.Telephone = self._to_bytes(Telephone)
        self.MobilePhone = self._to_bytes(MobilePhone)
        self.Fax = self._to_bytes(Fax)
        self.EMail = self._to_bytes(EMail)
        self.MoneyAccountStatus = self._to_bytes(MoneyAccountStatus)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.CashExchangeCode = self._to_bytes(CashExchangeCode)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.TID = int(TID)
        self.UserID = self._to_bytes(UserID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class CancelAccountField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('CustomerName', ctypes.c_char * 51),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('Gender', ctypes.c_char),
        ('CountryCode', ctypes.c_char * 21),
        ('CustType', ctypes.c_char),
        ('Address', ctypes.c_char * 101),
        ('ZipCode', ctypes.c_char * 7),
        ('Telephone', ctypes.c_char * 41),
        ('MobilePhone', ctypes.c_char * 21),
        ('Fax', ctypes.c_char * 41),
        ('EMail', ctypes.c_char * 41),
        ('MoneyAccountStatus', ctypes.c_char),
        ('BankAccount', ctypes.c_char * 41),
        ('BankPassWord', ctypes.c_char * 41),
        ('AccountID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
        ('InstallID', ctypes.c_int),
        ('VerifyCertNoFlag', ctypes.c_char),
        ('CurrencyID', ctypes.c_char * 4),
        ('CashExchangeCode', ctypes.c_char),
        ('Digest', ctypes.c_char * 36),
        ('BankAccType', ctypes.c_char),
        ('DeviceID', ctypes.c_char * 3),
        ('BankSecuAccType', ctypes.c_char),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('BankSecuAcc', ctypes.c_char * 41),
        ('BankPwdFlag', ctypes.c_char),
        ('SecuPwdFlag', ctypes.c_char),
        ('OperNo', ctypes.c_char * 17),
        ('TID', ctypes.c_int),
        ('UserID', ctypes.c_char * 16),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
        ('LongCustomerName', ctypes.c_char * 161),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', Gender='', CountryCode='', CustType='',
                 Address='', ZipCode='', Telephone='', MobilePhone='', Fax='', EMail='', MoneyAccountStatus='',
                 BankAccount='', BankPassWord='', AccountID='', Password='', InstallID='', VerifyCertNoFlag='',
                 CurrencyID='', CashExchangeCode='', Digest='', BankAccType='', DeviceID='', BankSecuAccType='',
                 BrokerIDByBank='', BankSecuAcc='', BankPwdFlag='', SecuPwdFlag='', OperNo='', TID='', UserID='',
                 ErrorID='', ErrorMsg='', LongCustomerName=''):
        super(CancelAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.Gender = self._to_bytes(Gender)
        self.CountryCode = self._to_bytes(CountryCode)
        self.CustType = self._to_bytes(CustType)
        self.Address = self._to_bytes(Address)
        self.ZipCode = self._to_bytes(ZipCode)
        self.Telephone = self._to_bytes(Telephone)
        self.MobilePhone = self._to_bytes(MobilePhone)
        self.Fax = self._to_bytes(Fax)
        self.EMail = self._to_bytes(EMail)
        self.MoneyAccountStatus = self._to_bytes(MoneyAccountStatus)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.CashExchangeCode = self._to_bytes(CashExchangeCode)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.DeviceID = self._to_bytes(DeviceID)
        self.BankSecuAccType = self._to_bytes(BankSecuAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankSecuAcc = self._to_bytes(BankSecuAcc)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.OperNo = self._to_bytes(OperNo)
        self.TID = int(TID)
        self.UserID = self._to_bytes(UserID)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class ChangeAccountField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('CustomerName', ctypes.c_char * 51),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('Gender', ctypes.c_char),
        ('CountryCode', ctypes.c_char * 21),
        ('CustType', ctypes.c_char),
        ('Address', ctypes.c_char * 101),
        ('ZipCode', ctypes.c_char * 7),
        ('Telephone', ctypes.c_char * 41),
        ('MobilePhone', ctypes.c_char * 21),
        ('Fax', ctypes.c_char * 41),
        ('EMail', ctypes.c_char * 41),
        ('MoneyAccountStatus', ctypes.c_char),
        ('BankAccount', ctypes.c_char * 41),
        ('BankPassWord', ctypes.c_char * 41),
        ('NewBankAccount', ctypes.c_char * 41),
        ('NewBankPassWord', ctypes.c_char * 41),
        ('AccountID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
        ('BankAccType', ctypes.c_char),
        ('InstallID', ctypes.c_int),
        ('VerifyCertNoFlag', ctypes.c_char),
        ('CurrencyID', ctypes.c_char * 4),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('BankPwdFlag', ctypes.c_char),
        ('SecuPwdFlag', ctypes.c_char),
        ('TID', ctypes.c_int),
        ('Digest', ctypes.c_char * 36),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
        ('LongCustomerName', ctypes.c_char * 161),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', Gender='', CountryCode='', CustType='',
                 Address='', ZipCode='', Telephone='', MobilePhone='', Fax='', EMail='', MoneyAccountStatus='',
                 BankAccount='', BankPassWord='', NewBankAccount='', NewBankPassWord='', AccountID='', Password='',
                 BankAccType='', InstallID='', VerifyCertNoFlag='', CurrencyID='', BrokerIDByBank='', BankPwdFlag='',
                 SecuPwdFlag='', TID='', Digest='', ErrorID='', ErrorMsg='', LongCustomerName=''):
        super(ChangeAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.Gender = self._to_bytes(Gender)
        self.CountryCode = self._to_bytes(CountryCode)
        self.CustType = self._to_bytes(CustType)
        self.Address = self._to_bytes(Address)
        self.ZipCode = self._to_bytes(ZipCode)
        self.Telephone = self._to_bytes(Telephone)
        self.MobilePhone = self._to_bytes(MobilePhone)
        self.Fax = self._to_bytes(Fax)
        self.EMail = self._to_bytes(EMail)
        self.MoneyAccountStatus = self._to_bytes(MoneyAccountStatus)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.NewBankAccount = self._to_bytes(NewBankAccount)
        self.NewBankPassWord = self._to_bytes(NewBankPassWord)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.BankAccType = self._to_bytes(BankAccType)
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.BankPwdFlag = self._to_bytes(BankPwdFlag)
        self.SecuPwdFlag = self._to_bytes(SecuPwdFlag)
        self.TID = int(TID)
        self.Digest = self._to_bytes(Digest)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
        self.LongCustomerName = self._to_bytes(LongCustomerName)


class SecAgentACIDMapField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('AccountID', ctypes.c_char * 13),
        ('CurrencyID', ctypes.c_char * 4),
        ('BrokerSecAgentID', ctypes.c_char * 13),
    ]

    def __init__(self, BrokerID='', UserID='', AccountID='', CurrencyID='', BrokerSecAgentID=''):
        super(SecAgentACIDMapField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.BrokerSecAgentID = self._to_bytes(BrokerSecAgentID)


class QrySecAgentACIDMapField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('AccountID', ctypes.c_char * 13),
        ('CurrencyID', ctypes.c_char * 4),
    ]

    def __init__(self, BrokerID='', UserID='', AccountID='', CurrencyID=''):
        super(QrySecAgentACIDMapField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.AccountID = self._to_bytes(AccountID)
        self.CurrencyID = self._to_bytes(CurrencyID)


class UserRightsAssignField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('DRIdentityID', ctypes.c_int),
    ]

    def __init__(self, BrokerID='', UserID='', DRIdentityID=''):
        super(UserRightsAssignField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.DRIdentityID = int(DRIdentityID)


class BrokerUserRightAssignField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('DRIdentityID', ctypes.c_int),
        ('Tradeable', ctypes.c_int),
    ]

    def __init__(self, BrokerID='', DRIdentityID='', Tradeable=''):
        super(BrokerUserRightAssignField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.DRIdentityID = int(DRIdentityID)
        self.Tradeable = int(Tradeable)


class DRTransferField(Base):
    _fields_ = [
        ('OrigDRIdentityID', ctypes.c_int),
        ('DestDRIdentityID', ctypes.c_int),
        ('OrigBrokerID', ctypes.c_char * 11),
        ('DestBrokerID', ctypes.c_char * 11),
    ]

    def __init__(self, OrigDRIdentityID='', DestDRIdentityID='', OrigBrokerID='', DestBrokerID=''):
        super(DRTransferField, self).__init__()
        self.OrigDRIdentityID = int(OrigDRIdentityID)
        self.DestDRIdentityID = int(DestDRIdentityID)
        self.OrigBrokerID = self._to_bytes(OrigBrokerID)
        self.DestBrokerID = self._to_bytes(DestBrokerID)


class FensUserInfoField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('LoginMode', ctypes.c_char),
    ]

    def __init__(self, BrokerID='', UserID='', LoginMode=''):
        super(FensUserInfoField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.LoginMode = self._to_bytes(LoginMode)


class CurrTransferIdentityField(Base):
    _fields_ = [
        ('IdentityID', ctypes.c_int),
    ]

    def __init__(self, IdentityID=''):
        super(CurrTransferIdentityField, self).__init__()
        self.IdentityID = int(IdentityID)


class LoginForbiddenUserField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
        ('IPAddress', ctypes.c_char * 16),
    ]

    def __init__(self, BrokerID='', UserID='', IPAddress=''):
        super(LoginForbiddenUserField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)
        self.IPAddress = self._to_bytes(IPAddress)


class QryLoginForbiddenUserField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('UserID', ctypes.c_char * 16),
    ]

    def __init__(self, BrokerID='', UserID=''):
        super(QryLoginForbiddenUserField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.UserID = self._to_bytes(UserID)


class MulticastGroupInfoField(Base):
    _fields_ = [
        ('GroupIP', ctypes.c_char * 16),
        ('GroupPort', ctypes.c_int),
        ('SourceIP', ctypes.c_char * 16),
    ]

    def __init__(self, GroupIP='', GroupPort='', SourceIP=''):
        super(MulticastGroupInfoField, self).__init__()
        self.GroupIP = self._to_bytes(GroupIP)
        self.GroupPort = int(GroupPort)
        self.SourceIP = self._to_bytes(SourceIP)


class TradingAccountReserveField(Base):
    _fields_ = [
        ('BrokerID', ctypes.c_char * 11),
        ('AccountID', ctypes.c_char * 13),
        ('Reserve', ctypes.c_double),
        ('CurrencyID', ctypes.c_char * 4),
    ]

    def __init__(self, BrokerID='', AccountID='', Reserve='', CurrencyID=''):
        super(TradingAccountReserveField, self).__init__()
        self.BrokerID = self._to_bytes(BrokerID)
        self.AccountID = self._to_bytes(AccountID)
        self.Reserve = float(Reserve)
        self.CurrencyID = self._to_bytes(CurrencyID)


class ReserveOpenAccountConfirmField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('CustomerName', ctypes.c_char * 161),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('Gender', ctypes.c_char),
        ('CountryCode', ctypes.c_char * 21),
        ('CustType', ctypes.c_char),
        ('Address', ctypes.c_char * 101),
        ('ZipCode', ctypes.c_char * 7),
        ('Telephone', ctypes.c_char * 41),
        ('MobilePhone', ctypes.c_char * 21),
        ('Fax', ctypes.c_char * 41),
        ('EMail', ctypes.c_char * 41),
        ('MoneyAccountStatus', ctypes.c_char),
        ('BankAccount', ctypes.c_char * 41),
        ('BankPassWord', ctypes.c_char * 41),
        ('InstallID', ctypes.c_int),
        ('VerifyCertNoFlag', ctypes.c_char),
        ('CurrencyID', ctypes.c_char * 4),
        ('Digest', ctypes.c_char * 36),
        ('BankAccType', ctypes.c_char),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('TID', ctypes.c_int),
        ('AccountID', ctypes.c_char * 13),
        ('Password', ctypes.c_char * 41),
        ('BankReserveOpenSeq', ctypes.c_char * 13),
        ('BookDate', ctypes.c_char * 9),
        ('BookPsw', ctypes.c_char * 41),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', Gender='', CountryCode='', CustType='',
                 Address='', ZipCode='', Telephone='', MobilePhone='', Fax='', EMail='', MoneyAccountStatus='',
                 BankAccount='', BankPassWord='', InstallID='', VerifyCertNoFlag='', CurrencyID='', Digest='',
                 BankAccType='', BrokerIDByBank='', TID='', AccountID='', Password='', BankReserveOpenSeq='',
                 BookDate='', BookPsw='', ErrorID='', ErrorMsg=''):
        super(ReserveOpenAccountConfirmField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.Gender = self._to_bytes(Gender)
        self.CountryCode = self._to_bytes(CountryCode)
        self.CustType = self._to_bytes(CustType)
        self.Address = self._to_bytes(Address)
        self.ZipCode = self._to_bytes(ZipCode)
        self.Telephone = self._to_bytes(Telephone)
        self.MobilePhone = self._to_bytes(MobilePhone)
        self.Fax = self._to_bytes(Fax)
        self.EMail = self._to_bytes(EMail)
        self.MoneyAccountStatus = self._to_bytes(MoneyAccountStatus)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.TID = int(TID)
        self.AccountID = self._to_bytes(AccountID)
        self.Password = self._to_bytes(Password)
        self.BankReserveOpenSeq = self._to_bytes(BankReserveOpenSeq)
        self.BookDate = self._to_bytes(BookDate)
        self.BookPsw = self._to_bytes(BookPsw)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)


class ReserveOpenAccountField(Base):
    _fields_ = [
        ('TradeCode', ctypes.c_char * 7),
        ('BankID', ctypes.c_char * 4),
        ('BankBranchID', ctypes.c_char * 5),
        ('BrokerID', ctypes.c_char * 11),
        ('BrokerBranchID', ctypes.c_char * 31),
        ('TradeDate', ctypes.c_char * 9),
        ('TradeTime', ctypes.c_char * 9),
        ('BankSerial', ctypes.c_char * 13),
        ('TradingDay', ctypes.c_char * 9),
        ('PlateSerial', ctypes.c_int),
        ('LastFragment', ctypes.c_char),
        ('SessionID', ctypes.c_int),
        ('CustomerName', ctypes.c_char * 161),
        ('IdCardType', ctypes.c_char),
        ('IdentifiedCardNo', ctypes.c_char * 51),
        ('Gender', ctypes.c_char),
        ('CountryCode', ctypes.c_char * 21),
        ('CustType', ctypes.c_char),
        ('Address', ctypes.c_char * 101),
        ('ZipCode', ctypes.c_char * 7),
        ('Telephone', ctypes.c_char * 41),
        ('MobilePhone', ctypes.c_char * 21),
        ('Fax', ctypes.c_char * 41),
        ('EMail', ctypes.c_char * 41),
        ('MoneyAccountStatus', ctypes.c_char),
        ('BankAccount', ctypes.c_char * 41),
        ('BankPassWord', ctypes.c_char * 41),
        ('InstallID', ctypes.c_int),
        ('VerifyCertNoFlag', ctypes.c_char),
        ('CurrencyID', ctypes.c_char * 4),
        ('Digest', ctypes.c_char * 36),
        ('BankAccType', ctypes.c_char),
        ('BrokerIDByBank', ctypes.c_char * 33),
        ('TID', ctypes.c_int),
        ('ReserveOpenAccStas', ctypes.c_char),
        ('ErrorID', ctypes.c_int),
        ('ErrorMsg', ctypes.c_char * 81),
    ]

    def __init__(self, TradeCode='', BankID='', BankBranchID='', BrokerID='', BrokerBranchID='', TradeDate='',
                 TradeTime='', BankSerial='', TradingDay='', PlateSerial='', LastFragment='', SessionID='',
                 CustomerName='', IdCardType='', IdentifiedCardNo='', Gender='', CountryCode='', CustType='',
                 Address='', ZipCode='', Telephone='', MobilePhone='', Fax='', EMail='', MoneyAccountStatus='',
                 BankAccount='', BankPassWord='', InstallID='', VerifyCertNoFlag='', CurrencyID='', Digest='',
                 BankAccType='', BrokerIDByBank='', TID='', ReserveOpenAccStas='', ErrorID='', ErrorMsg=''):
        super(ReserveOpenAccountField, self).__init__()
        self.TradeCode = self._to_bytes(TradeCode)
        self.BankID = self._to_bytes(BankID)
        self.BankBranchID = self._to_bytes(BankBranchID)
        self.BrokerID = self._to_bytes(BrokerID)
        self.BrokerBranchID = self._to_bytes(BrokerBranchID)
        self.TradeDate = self._to_bytes(TradeDate)
        self.TradeTime = self._to_bytes(TradeTime)
        self.BankSerial = self._to_bytes(BankSerial)
        self.TradingDay = self._to_bytes(TradingDay)
        self.PlateSerial = int(PlateSerial)
        self.LastFragment = self._to_bytes(LastFragment)
        self.SessionID = int(SessionID)
        self.CustomerName = self._to_bytes(CustomerName)
        self.IdCardType = self._to_bytes(IdCardType)
        self.IdentifiedCardNo = self._to_bytes(IdentifiedCardNo)
        self.Gender = self._to_bytes(Gender)
        self.CountryCode = self._to_bytes(CountryCode)
        self.CustType = self._to_bytes(CustType)
        self.Address = self._to_bytes(Address)
        self.ZipCode = self._to_bytes(ZipCode)
        self.Telephone = self._to_bytes(Telephone)
        self.MobilePhone = self._to_bytes(MobilePhone)
        self.Fax = self._to_bytes(Fax)
        self.EMail = self._to_bytes(EMail)
        self.MoneyAccountStatus = self._to_bytes(MoneyAccountStatus)
        self.BankAccount = self._to_bytes(BankAccount)
        self.BankPassWord = self._to_bytes(BankPassWord)
        self.InstallID = int(InstallID)
        self.VerifyCertNoFlag = self._to_bytes(VerifyCertNoFlag)
        self.CurrencyID = self._to_bytes(CurrencyID)
        self.Digest = self._to_bytes(Digest)
        self.BankAccType = self._to_bytes(BankAccType)
        self.BrokerIDByBank = self._to_bytes(BrokerIDByBank)
        self.TID = int(TID)
        self.ReserveOpenAccStas = self._to_bytes(ReserveOpenAccStas)
        self.ErrorID = int(ErrorID)
        self.ErrorMsg = self._to_bytes(ErrorMsg)
