### 用户接口

1. ReqUserLogin 用户登录接口
    
 a) 用户登录请求(ReqUserLogin)
    
    交易日 TradingDay --> STRING
    经纪公司代码 BrokerID --> STRING
    用户代码 UserID --> STRING
    密码 Password --> STRING
    用户端产品信息 UserProductInfo --> STRING
    接口端产品信息 InterfaceProductInfo --> STRING
    协议信息 ProtocolInfo --> STRING
    Mac地址 MacAddress --> STRING
    动态密码 OneTimePassword --> STRING
    终端IP地址 ClientIPAddress --> STRING
    登录备注 LoginRemark --> STRING
    
    请求ID requestID --> INT
    
 返回数据
    
    交易日 TradingDay
    登录成功时间 LoginTime
    经纪公司代码 BrokerID
    用户代码 UserID
    交易系统名称 SystemName
    前置编号 FrontID
    会话编号 SessionID
    最大报单引用 MaxOrderRef
    上期所时间 SHFETime
    大商所时间 DCETime
    郑商所时间 CZCETime
    中金所时间 FFEXTime
    能源中心时间 INETime
    
    # 相应信息
    错误代码 ErrorID
    错误信息 ErrorMsg
    
    requestID --> INT
 
 b) 用户登出请求(ReqUserLogout)
 
    经纪公司代码  BrokerID
    用户代码  UserID
    
    请求ID requestID --> INT
    
   返回数据
   
    经纪公司代码  BrokerID
    用户代码  UserID
    
    # 相应信息
    错误代码 ErrorID
    错误信息 ErrorMsg
    
    requestID --> INT
    
    
2. ReqUserLogout 用户登出接口


### 订阅行情接口

1. 订阅行情接口 （SubscribeMarketData）
    
    
    请求品种ID InstrumentID --> LIST
    
   返回数据 （推送行情多条数据）
    
    合约代码 InstrumentID --> STRING
     
    # 相应信息
    错误代码 ErrorID
    错误信息 ErrorMsg
    
    requestID --> INT
     
    
2. 退订行情接口（UnSubscribeMarketData）
    
    
    请求品种ID InstrumentID --> LIST
    
    
   返回数据 （推送行情多条数据）
    
    合约代码 InstrumentID --> STRING
     
    # 相应信息
    错误代码 ErrorID
    错误信息 ErrorMsg
    
    requestID --> INT
    

### 行情推送 （OnRtnDepthMarketData） -- 实时推送数据

    交易日 TradingDay
    合约代码 InstrumentID
    交易所代码 ExchangeID
    合约在交易所的代码 ExchangeInstID
    最新价 LastPrice
    上次结算价 PreSettlementPrice
    昨收盘 PreClosePrice
    昨持仓量PreOpenInterest
    今开盘 OpenPrice
    最高价 HighestPrice
    最低价 LowestPrice
    数量 Volume
    成交金额 Turnover
    持仓量 OpenInterest
    今收盘 ClosePrice
    本次结算价 SettlementPrice
    涨停板价 UpperLimitPrice
    跌停板价 LowerLimitPrice
    昨虚实度 PreDelta
    今虚实度 CurrDelta
    最后修改时间 UpdateTime
    最后修改毫秒 UpdateMillisec
    申买价一 BidPrice1
    申买量一 BidVolume1
    申卖价一 AskPrice1
    申卖量一 AskVolume1
    申买价二 BidPrice2
    申买量二 BidVolume2
    申卖价二 AskPrice2
    申卖量二 AskVolume2
    申买价三 BidPrice3
    申买量三 BidVolume3
    申卖价三 AskPrice3
    申卖量三 AskVolume3
    申买价四 BidPrice4
    申买量四 BidVolume4
    申卖价四 AskPrice4
    申卖量四 AskVolume4
    申买价五 BidPrice5
    申买量五 BidVolume5
    申卖价五 AskPrice5
    申卖量五 AskVolume5
    当日均价 AveragePrice
    业务日期 ActionDay


### 下单接口


    **以下请求都会包含（requestID）**
    ** 返回的接口都会包含
     
    错误代码  ErrorID  
    错误信息  ErrorMsg  


   
1. 报单录入请求 (ReqOrderInsert)
    
    (CThostFtdcInputOrderField *pInputOrder
   
   
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    合约代码  InstrumentID  
    报单引用  OrderRef  
    用户代码  UserID  
    报单价格条件  OrderPriceType  
    买卖方向  Direction  
    组合开平标志  CombOffsetFlag  
    组合投机套保标志  CombHedgeFlag  
    价格  LimitPrice  
    数量  VolumeTotalOriginal  
    有效期类型  TimeCondition  
    GTD日期  GTDDate  
    成交量类型  VolumeCondition  
    最小成交量  MinVolume  
    触发条件  ContingentCondition  
    止损价  StopPrice  
    强平原因  ForceCloseReason  
    自动挂起标志  IsAutoSuspend  
    业务单元  BusinessUnit  
    请求编号  RequestID  
    用户强评标志  UserForceClose  
    互换单标志  IsSwapOrder  
    交易所代码  ExchangeID  
    投资单元代码  InvestUnitID  
    资金账号  AccountID  
    币种代码  CurrencyID  
    交易编码  ClientID  
    IP地址  IPAddress  
    Mac地址  MacAddress  
    
    请求和返回数据一样
    
    

2. 预埋单录入请求 ReqParkedOrderInsert
    (CThostFtdcParkedOrderField *pParkedOrder, int nRequestID)
    
    
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    合约代码  InstrumentID  
    报单引用  OrderRef  
    用户代码  UserID  
    报单价格条件  OrderPriceType  
    买卖方向  Direction  
    组合开平标志  CombOffsetFlag  
    组合投机套保标志  CombHedgeFlag  
    价格  LimitPrice  
    数量  VolumeTotalOriginal  
    有效期类型  TimeCondition  
    GTD日期  GTDDate  
    成交量类型  VolumeCondition  
    最小成交量  MinVolume  
    触发条件  ContingentCondition  
    止损价  StopPrice  
    强平原因  ForceCloseReason  
    自动挂起标志  IsAutoSuspend  
    业务单元  BusinessUnit  
    请求编号  RequestID  
    用户强评标志  UserForceClose  
    交易所代码  ExchangeID  
    预埋报单编号  ParkedOrderID  
    用户类型  UserType  
    预埋单状态  Status  
    错误代码  ErrorID  
    错误信息  ErrorMsg  
    互换单标志  IsSwapOrder  
    资金账号  AccountID  
    币种代码  CurrencyID  
    交易编码  ClientID  
    投资单元代码  InvestUnitID  
    IP地址  IPAddress  
    Mac地址  MacAddress  
    
    请求和数据返回一样

3. 预埋撤单录入请求 ReqParkedOrderAction
    (CThostFtdcParkedOrderActionField *pParkedOrderAction, int nRequestID)
    
        
       经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    报单操作引用  OrderActionRef  
    报单引用  OrderRef  
    请求编号  RequestID  
    前置编号  FrontID  
    会话编号  SessionID  
    交易所代码  ExchangeID  
    报单编号  OrderSysID  
    操作标志  ActionFlag  
    价格  LimitPrice  
    数量变化  VolumeChange  
    用户代码  UserID  
    合约代码  InstrumentID  
    预埋撤单单编号  ParkedOrderActionID  
    用户类型  UserType  
    预埋撤单状态  Status  
    错误代码  ErrorID  
    错误信息  ErrorMsg  
    投资单元代码  InvestUnitID  
    IP地址  IPAddress  
    Mac地址  MacAddress  
    
    请求和返回数据一样
    
    
4. 报单操作请求 ReqOrderAction
    (CThostFtdcInputOrderActionField *pInputOrderAction, int nRequestID)
    
    
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    报单操作引用  OrderActionRef  
    报单引用  OrderRef  
    请求编号  RequestID  
    前置编号  FrontID  
    会话编号  SessionID  
    交易所代码  ExchangeID  
    报单编号  OrderSysID  
    操作标志  ActionFlag  
    价格  LimitPrice  
    数量变化  VolumeChange  
    用户代码  UserID  
    合约代码  InstrumentID  
    投资单元代码  InvestUnitID  
    IP地址  IPAddress  
    Mac地址  MacAddress  
    
    请求和返回数据一样
    
    

5. 查询最大报单数量请求 ReqQueryMaxOrderVolume
    (CThostFtdcQueryMaxOrderVolumeField *pQueryMaxOrderVolume, int nRequestID)
    
    
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    合约代码  InstrumentID  
    买卖方向  Direction  
    开平标志  OffsetFlag  
    投机套保标志  HedgeFlag  
    最大允许报单数量  MaxVolume  
    
    请求和返回数据一样
    
    
    
6. 投资者结算结果确认 ReqSettlementInfoConfirm
    (CThostFtdcSettlementInfoConfirmField *pSettlementInfoConfirm, int nRequestID)
    
    
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    确认日期  ConfirmDate  
    确认时间  ConfirmTime  
    
    请求和返回数据一样

7. 请求删除预埋单 ReqRemoveParkedOrder
    (CThostFtdcRemoveParkedOrderField *pRemoveParkedOrder, int nRequestID)
    
    
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    预埋报单编号  ParkedOrderID  
    
    请求和返回数据一样
    

8. 请求删除预埋撤单 ReqRemoveParkedOrderAction
    
    (CThostFtdcRemoveParkedOrderActionField *pRemoveParkedOrderAction, int nRequestID)

    
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    预埋撤单编号  ParkedOrderActionID  
    
    请求和返回数据一样

9. 报价录入请求 ReqQuoteInsert
    (CThostFtdcInputQuoteField *pInputQuote, int nRequestID)
    
    
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    合约代码  InstrumentID  
    报价引用  QuoteRef  
    用户代码  UserID  
    卖价格  AskPrice  
    买价格  BidPrice  
    卖数量  AskVolume  
    买数量  BidVolume  
    请求编号  RequestID  
    业务单元  BusinessUnit  
    卖开平标志  AskOffsetFlag  
    买开平标志  BidOffsetFlag  
    卖投机套保标志  AskHedgeFlag  
    买投机套保标志  BidHedgeFlag  
    衍生卖报单引用  AskOrderRef  
    衍生买报单引用  BidOrderRef  
    应价编号  ForQuoteSysID  
    交易所代码  ExchangeID  
    投资单元代码  InvestUnitID  
    交易编码  ClientID  
    IP地址  IPAddress  
    Mac地址  MacAddress  
    
    
    请求和返回数据一样

10.报价操作请求 ReqQuoteAction
    (CThostFtdcInputQuoteActionField *pInputQuoteAction, int nRequestID)
    
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    报价操作引用  QuoteActionRef  
    报价引用  QuoteRef  
    请求编号  RequestID  
    前置编号  FrontID  
    会话编号  SessionID  
    交易所代码  ExchangeID  
    报价操作编号  QuoteSysID  
    操作标志  ActionFlag  
    用户代码  UserID  
    合约代码  InstrumentID  
    投资单元代码  InvestUnitID  
    交易编码  ClientID  
    IP地址  IPAddress  
    Mac地址  MacAddress  
    
    ~

11.批量报单操作请求 ReqBatchOrderAction
    (CThostFtdcInputBatchOrderActionField *pInputBatchOrderAction, int nRequestID)
    
        经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    报单操作引用  OrderActionRef  
    请求编号  RequestID  
    前置编号  FrontID  
    会话编号  SessionID  
    交易所代码  ExchangeID  
    用户代码  UserID  
    投资单元代码  InvestUnitID  
    IP地址  IPAddress  
    Mac地址  MacAddress  
    
    ~
    
12.申请组合录入请求 ReqCombActionInsert
    (CThostFtdcInputCombActionField *pInputCombAction, int nRequestID)
    
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    合约代码  InstrumentID  
    组合引用  CombActionRef  
    用户代码  UserID  
    买卖方向  Direction  
    数量  Volume  
    组合指令方向  CombDirection  
    投机套保标志  HedgeFlag  
    交易所代码  ExchangeID  
    IP地址  IPAddress  
    Mac地址  MacAddress  
    
    ~

13.请求查询报单 ReqQryOrder
    (CThostFtdcQryOrderField *pQryOrder, int nRequestID)
    
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    合约代码  InstrumentID  
    交易所代码  ExchangeID  
    报单编号  OrderSysID  
    开始时间  InsertTimeStart  
    结束时间  InsertTimeEnd  
    
    
   返回数据
   
     经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    合约代码  InstrumentID  
    报单引用  OrderRef  
    用户代码  UserID  
    报单价格条件  OrderPriceType  
    买卖方向  Direction  
    组合开平标志  CombOffsetFlag  
    组合投机套保标志  CombHedgeFlag  
    价格  LimitPrice  
    数量  VolumeTotalOriginal  
    有效期类型  TimeCondition  
    GTD日期  GTDDate  
    成交量类型  VolumeCondition  
    最小成交量  MinVolume  
    触发条件  ContingentCondition  
    止损价  StopPrice  
    强平原因  ForceCloseReason  
    自动挂起标志  IsAutoSuspend  
    业务单元  BusinessUnit  
    请求编号  RequestID  
    本地报单编号  OrderLocalID  
    交易所代码  ExchangeID  
    会员代码  ParticipantID  
    客户代码  ClientID  
    合约在交易所的代码  ExchangeInstID  
    交易所交易员代码  TraderID  
    安装编号  InstallID  
    报单提交状态  OrderSubmitStatus  
    报单提示序号  NotifySequence  
    交易日  TradingDay  
    结算编号  SettlementID  
    报单编号  OrderSysID  
    报单来源  OrderSource  
    报单状态  OrderStatus  
    报单类型  OrderType  
    今成交数量  VolumeTraded  
    剩余数量  VolumeTotal  
    报单日期  InsertDate  
    委托时间  InsertTime  
    激活时间  ActiveTime  
    挂起时间  SuspendTime  
    最后修改时间  UpdateTime  
    撤销时间  CancelTime  
    最后修改交易所交易员代码  ActiveTraderID  
    结算会员编号  ClearingPartID  
    序号  SequenceNo  
    前置编号  FrontID  
    会话编号  SessionID  
    用户端产品信息  UserProductInfo  
    状态信息  StatusMsg  
    用户强评标志  UserForceClose  
    操作用户代码  ActiveUserID  
    经纪公司报单编号  BrokerOrderSeq  
    相关报单  RelativeOrderSysID  
    郑商所成交数量  ZCETotalTradedVolume  
    互换单标志  IsSwapOrder  
    营业部编号  BranchID  
    投资单元代码  InvestUnitID  
    资金账号  AccountID  
    币种代码  CurrencyID  
    IP地址  IPAddress  
    Mac地址  MacAddress  

14.请求查询成交 ReqQryTrade
    (CThostFtdcQryTradeField *pQryTrade, int nRequestID)
    
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    合约代码  InstrumentID  
    交易所代码  ExchangeID  
    成交编号  TradeID  
    开始时间  TradeTimeStart  
    结束时间  TradeTimeEnd  
    
    
    返回数据
    
      经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    合约代码  InstrumentID  
    报单引用  OrderRef  
    用户代码  UserID  
    交易所代码  ExchangeID  
    成交编号  TradeID  
    买卖方向  Direction  
    报单编号  OrderSysID  
    会员代码  ParticipantID  
    客户代码  ClientID  
    交易角色  TradingRole  
    合约在交易所的代码  ExchangeInstID  
    开平标志  OffsetFlag  
    投机套保标志  HedgeFlag  
    价格  Price  
    数量  Volume  
    成交时期  TradeDate  
    成交时间  TradeTime  
    成交类型  TradeType  
    成交价来源  PriceSource  
    交易所交易员代码  TraderID  
    本地报单编号  OrderLocalID  
    结算会员编号  ClearingPartID  
    业务单元  BusinessUnit  
    序号  SequenceNo  
    交易日  TradingDay  
    结算编号  SettlementID  
    经纪公司报单编号  BrokerOrderSeq  
    成交来源  TradeSource  

15.请求查询投资者持仓 ReqQryInvestorPosition
    (CThostFtdcQryInvestorPositionField *pQryInvestorPosition, int nRequestID)
    
    
       经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    合约代码  InstrumentID  
    
    
    返回数据
    
    
    合约代码  InstrumentID  
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    持仓多空方向  PosiDirection  
    投机套保标志  HedgeFlag  
    持仓日期  PositionDate  
    上日持仓  YdPosition  
    今日持仓  Position  
    多头冻结  LongFrozen  
    空头冻结  ShortFrozen  
    开仓冻结金额  LongFrozenAmount  
    开仓冻结金额  ShortFrozenAmount  
    开仓量  OpenVolume  
    平仓量  CloseVolume  
    开仓金额  OpenAmount  
    平仓金额  CloseAmount  
    持仓成本  PositionCost  
    上次占用的保证金  PreMargin  
    占用的保证金  UseMargin  
    冻结的保证金  FrozenMargin  
    冻结的资金  FrozenCash  
    冻结的手续费  FrozenCommission  
    资金差额  CashIn  
    手续费  Commission  
    平仓盈亏  CloseProfit  
    持仓盈亏  PositionProfit  
    上次结算价  PreSettlementPrice  
    本次结算价  SettlementPrice  
    交易日  TradingDay  
    结算编号  SettlementID  
    开仓成本  OpenCost  
    交易所保证金  ExchangeMargin  
    组合成交形成的持仓  CombPosition  
    组合多头冻结  CombLongFrozen  
    组合空头冻结  CombShortFrozen  
    逐日盯市平仓盈亏  CloseProfitByDate  
    逐笔对冲平仓盈亏  CloseProfitByTrade  
    今日持仓  TodayPosition  
    保证金率  MarginRateByMoney  
    保证金率(按手数)  MarginRateByVolume  
    执行冻结  StrikeFrozen  
    执行冻结金额  StrikeFrozenAmount  
    放弃执行冻结  AbandonFrozen  
    
16.请求查询资金账户 ReqQryTradingAccount
    (CThostFtdcQryTradingAccountField *pQryTradingAccount, int nRequestID)
    
    
     经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    币种代码  CurrencyID  
    
    
    返回数据
    
      经纪公司代码  BrokerID  
    投资者帐号  AccountID  
    上次质押金额  PreMortgage  
    上次信用额度  PreCredit  
    上次存款额  PreDeposit  
    上次结算准备金  PreBalance  
    上次占用的保证金  PreMargin  
    利息基数  InterestBase  
    利息收入  Interest  
    入金金额  Deposit  
    出金金额  Withdraw  
    冻结的保证金  FrozenMargin  
    冻结的资金  FrozenCash  
    冻结的手续费  FrozenCommission  
    当前保证金总额  CurrMargin  
    资金差额  CashIn  
    手续费  Commission  
    平仓盈亏  CloseProfit  
    持仓盈亏  PositionProfit  
    期货结算准备金  Balance  
    可用资金  Available  
    可取资金  WithdrawQuota  
    基本准备金  Reserve  
    交易日  TradingDay  
    结算编号  SettlementID  
    信用额度  Credit  
    质押金额  Mortgage  
    交易所保证金  ExchangeMargin  
    投资者交割保证金  DeliveryMargin  
    交易所交割保证金  ExchangeDeliveryMargin  
    保底期货结算准备金  ReserveBalance  
    币种代码  CurrencyID  
    上次货币质入金额  PreFundMortgageIn  
    上次货币质出金额  PreFundMortgageOut  
    货币质入金额  FundMortgageIn  
    货币质出金额  FundMortgageOut  
    货币质押余额  FundMortgageAvailable  
    可质押货币金额  MortgageableFund  
    特殊产品占用保证金  SpecProductMargin  
    特殊产品冻结保证金  SpecProductFrozenMargin  
    特殊产品手续费  SpecProductCommission  
    特殊产品冻结手续费  SpecProductFrozenCommission  
    特殊产品持仓盈亏  SpecProductPositionProfit  
    特殊产品平仓盈亏  SpecProductCloseProfit  
    根据持仓盈亏算法计算的特殊产品持仓盈亏  SpecProductPositionProfitByAlg  
    特殊产品交易所保证金  SpecProductExchangeMargin  
    

19.请求查询交易编码 ReqQryTradingCode
    (CThostFtdcQryTradingCodeField *pQryTradingCode, int nRequestID)
    
     经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    交易所代码  ExchangeID  
    客户代码  ClientID  
    交易编码类型  ClientIDType  
    
    
   返回数据
    
        投资者代码  InvestorID  
    经纪公司代码  BrokerID  
    交易所代码  ExchangeID  
    客户代码  ClientID  
    是否活跃  IsActive  
    交易编码类型  ClientIDType  

20.请求查询合约保证金率 ReqQryInstrumentMarginRate
    
    (CThostFtdcQryInstrumentMarginRateField *pQryInstrumentMarginRate, int nRequestID)
    
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    合约代码  InstrumentID  
    投机套保标志  HedgeFlag  
    
   返回数据
    
        合约代码  InstrumentID  
    投资者范围  InvestorRange  
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    投机套保标志  HedgeFlag  
    多头保证金率  LongMarginRatioByMoney  
    多头保证金费  LongMarginRatioByVolume  
    空头保证金率  ShortMarginRatioByMoney  
    空头保证金费  ShortMarginRatioByVolume  
    是否相对交易所收取  IsRelative  

21.请求查询合约手续费率 ReqQryInstrumentCommissionRate
    (CThostFtdcQryInstrumentCommissionRateField *pQryInstrumentCommissionRate,
                                               int nRequestID)
    
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    合约代码  InstrumentID  
    
   返回数据
    
    合约代码  InstrumentID  
    投资者范围  InvestorRange  
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    开仓手续费率  OpenRatioByMoney  
    开仓手续费  OpenRatioByVolume  
    平仓手续费率  CloseRatioByMoney  
    平仓手续费  CloseRatioByVolume  
    平今手续费率  CloseTodayRatioByMoney  
    平今手续费  CloseTodayRatioByVolume  
    


23.请求查询产品 ReqQryProduct
    (CThostFtdcQryProductField *pQryProduct, int nRequestID)
    
        产品代码  ProductID  
    产品类型  ProductClass  
    
    
   返回数据
    
       产品代码  ProductID  
    产品名称  ProductName  
    交易所代码  ExchangeID  
    产品类型  ProductClass  
    合约数量乘数  VolumeMultiple  
    最小变动价位  PriceTick  
    市价单最大下单量  MaxMarketOrderVolume  
    市价单最小下单量  MinMarketOrderVolume  
    限价单最大下单量  MaxLimitOrderVolume  
    限价单最小下单量  MinLimitOrderVolume  
    持仓类型  PositionType  
    持仓日期类型  PositionDateType  
    平仓处理类型  CloseDealType  
    交易币种类型  TradeCurrencyID  
    质押资金可用范围  MortgageFundUseRange  
    交易所产品代码  ExchangeProductID  
    合约基础商品乘数  UnderlyingMultiple  

24.请求查询合约 ReqQryInstrument
    (CThostFtdcQryInstrumentField *pQryInstrument, int nRequestID)
    
      合约代码  InstrumentID  
    交易所代码  ExchangeID  
    合约在交易所的代码  ExchangeInstID  
    产品代码  ProductID  
    
    
   返回数据
    
    合约代码 InstrumentID  
    交易所代码  ExchangeID  
    合约名称  InstrumentName  
    合约在交易所的代码  ExchangeInstID  
    产品代码  ProductID  
    产品类型  ProductClass  
    交割年份  DeliveryYear  
    交割月  DeliveryMonth  
    市价单最大下单量  MaxMarketOrderVolume  
    市价单最小下单量  MinMarketOrderVolume  
    限价单最大下单量  MaxLimitOrderVolume  
    限价单最小下单量  MinLimitOrderVolume  
    合约数量乘数  VolumeMultiple  
    最小变动价位  PriceTick  
    创建日  CreateDate  
    上市日  OpenDate  
    到期日  ExpireDate  
    开始交割日  StartDelivDate  
    结束交割日  EndDelivDate  
    合约生命周期状态  InstLifePhase  
    当前是否交易  IsTrading  
    持仓类型  PositionType  
    持仓日期类型  PositionDateType  
    多头保证金率  LongMarginRatio  
    空头保证金率  ShortMarginRatio  
    是否使用大额单边保证金算法  MaxMarginSideAlgorithm  
    基础商品代码  UnderlyingInstrID  
    执行价  StrikePrice  
    期权类型  OptionsType  
    合约基础商品乘数  UnderlyingMultiple  
    组合类型  CombinationType  


26.请求查询投资者结算结果 ReqQrySettlementInfo
    (CThostFtdcQrySettlementInfoField *pQrySettlementInfo, int nRequestID)
    
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    交易日  TradingDay  
    
    
    返回户籍
    
      交易日  TradingDay  
      结算编号  SettlementID  
      经纪公司代码  BrokerID  
      投资者代码  InvestorID  
      序号  SequenceNo  
      消息正文  Content  

    
27.请求查询投资者持仓明细 ReqQryInvestorPositionDetail
    (CThostFtdcQryInvestorPositionDetailField *pQryInvestorPositionDetail,
                                             int nRequestID)
                                             
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    合约代码  InstrumentID  
    
    返回数据
    
          合约代码  InstrumentID  
      经纪公司代码  BrokerID  
      投资者代码  InvestorID  
      投机套保标志  HedgeFlag  
      买卖  Direction  
      开仓日期  OpenDate  
      成交编号  TradeID  
      数量  Volume  
      开仓价  OpenPrice  
      交易日  TradingDay  
      结算编号  SettlementID  
      成交类型  TradeType  
      组合合约代码  CombInstrumentID  
      交易所代码  ExchangeID  
      逐日盯市平仓盈亏  CloseProfitByDate  
      逐笔对冲平仓盈亏  CloseProfitByTrade  
      逐日盯市持仓盈亏  PositionProfitByDate  
      逐笔对冲持仓盈亏  PositionProfitByTrade  
      投资者保证金  Margin  
      交易所保证金  ExchMargin  
      保证金率  MarginRateByMoney  
      保证金率(按手数)  MarginRateByVolume  
      昨结算价  LastSettlementPrice  
      结算价  SettlementPrice  
      平仓量  CloseVolume  
      平仓金额  CloseAmount  


30.请求查询投资者持仓明细 ReqQryInvestorPositionCombineDetail
    (CThostFtdcQryInvestorPositionCombineDetailField *pQryInvestorPositionCombineDetail, int nRequestID)
    
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    组合持仓合约编码  CombInstrumentID  
    
    
    返回数据
    
         交易日  TradingDay  
      开仓日期  OpenDate  
      交易所代码  ExchangeID  
      结算编号  SettlementID  
      经纪公司代码  BrokerID  
      投资者代码  InvestorID  
      组合编号  ComTradeID  
      撮合编号  TradeID  
      合约代码  InstrumentID  
      投机套保标志  HedgeFlag  
      买卖  Direction  
      持仓量  TotalAmt  
      投资者保证金  Margin  
      交易所保证金  ExchMargin  
      保证金率  MarginRateByMoney  
      保证金率(按手数)  MarginRateByVolume  
      单腿编号  LegID  
      单腿乘数  LegMultiple  
      组合持仓合约编码  CombInstrumentID  
      成交组号  TradeGroupID  

31.请求查询仓单折抵信息 ReqQryEWarrantOffset
    (CThostFtdcQryEWarrantOffsetField *pQryEWarrantOffset, int nRequestID)
    
    
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    交易所代码  ExchangeID  
    合约代码  InstrumentID 
    
    
    返回数据
    
    
      交易日期   TradingDay  
      经纪公司代码   BrokerID  
      投资者代码   InvestorID  
      交易所代码   ExchangeID  
      合约代码   InstrumentID  
      买卖方向   Direction  
      投机套保标志   HedgeFlag  
      数量   Volume   

32.请求查询投资者品种/跨品种保证金 ReqQryInvestorProductGroupMargin
    
    (CThostFtdcQryInvestorProductGroupMarginField *pQryInvestorProductGroupMargin,
                                     int nRequestID)
                                     
    经纪公司代码  BrokerID  
    投资者代码  InvestorID  
    品种/跨品种标示  ProductGroupID  
    投机套保标志  HedgeFlag     
    
    返回数据
    
      品种/跨品种标示  ProductGroupID  
      经纪公司代码  BrokerID  
      投资者代码  InvestorID  
      交易日  TradingDay  
      结算编号  SettlementID  
      冻结的保证金  FrozenMargin  
      多头冻结的保证金  LongFrozenMargin  
      空头冻结的保证金  ShortFrozenMargin  
      占用的保证金  UseMargin  
      多头保证金  LongUseMargin  
      空头保证金  ShortUseMargin  
      交易所保证金  ExchMargin  
      交易所多头保证金  LongExchMargin  
      交易所空头保证金  ShortExchMargin  
      平仓盈亏  CloseProfit  
      冻结的手续费  FrozenCommission  
      手续费  Commission  
      冻结的资金  FrozenCash  
      资金差额  CashIn  
      持仓盈亏  PositionProfit  
      折抵总金额  OffsetAmount  
      多头折抵总金额  LongOffsetAmount  
      空头折抵总金额  ShortOffsetAmount  
      交易所折抵总金额  ExchOffsetAmount  
      交易所多头折抵总金额  LongExchOffsetAmount  
      交易所空头折抵总金额  ShortExchOffsetAmount  
      投机套保标志  HedgeFlag                                

33.请求查询交易所保证金率 ReqQryExchangeMarginRate
    
    (CThostFtdcQryExchangeMarginRateField *pQryExchangeMarginRate, int nRequestID)
    
    经纪公司代码  BrokerID  
    合约代码  InstrumentID  
    投机套保标志  HedgeFlag  
    
    返回数据
    
        经纪公司代码  BrokerID  
      合约代码  InstrumentID  
      投机套保标志  HedgeFlag  
      多头保证金率  LongMarginRatioByMoney  
      多头保证金费  LongMarginRatioByVolume  
      空头保证金率  ShortMarginRatioByMoney  
      空头保证金费  ShortMarginRatioByVolume  

34.请求查询交易所调整保证金率 ReqQryExchangeMarginRateAdjust
    (CThostFtdcQryExchangeMarginRateAdjustField *pQryExchangeMarginRateAdjust,
                                               int nRequestID)
                                               
                                              
    经纪公司代码  BrokerID  
    合约代码  InstrumentID  
    投机套保标志  HedgeFlag 
    
    
    
    返回数据
    
        经纪公司代码  BrokerID  
      合约代码  InstrumentID  
      投机套保标志  HedgeFlag  
      跟随交易所投资者多头保证金率  LongMarginRatioByMoney  
      跟随交易所投资者多头保证金费  LongMarginRatioByVolume  
      跟随交易所投资者空头保证金率  ShortMarginRatioByMoney  
      跟随交易所投资者空头保证金费  ShortMarginRatioByVolume  
      交易所多头保证金率  ExchLongMarginRatioByMoney  
      交易所多头保证金费  ExchLongMarginRatioByVolume  
      交易所空头保证金率  ExchShortMarginRatioByMoney  
      交易所空头保证金费  ExchShortMarginRatioByVolume  
      不跟随交易所投资者多头保证金率  NoLongMarginRatioByMoney  
      不跟随交易所投资者多头保证金费  NoLongMarginRatioByVolume  
      不跟随交易所投资者空头保证金率  NoShortMarginRatioByMoney  
      不跟随交易所投资者空头保证金费  NoShortMarginRatioByVolume   
    


36. 请求查询报单手续费 ReqQryInstrumentOrderCommRate
    (CThostFtdcQryInstrumentOrderCommRateField *pQryInstrumentOrderCommRate,
                                              int nRequestID)

    
     经纪公司代码  BrokerID
    投资者代码  InvestorID
    合约代码  InstrumentID
    
    
    
   返回数据
    
       合约代码  InstrumentID
    投资者范围  InvestorRange
    经纪公司代码  BrokerID
    投资者代码  InvestorID
    投机套保标志  HedgeFlag
    报单手续费  OrderCommByVolume
    撤单手续费  OrderActionCommByVolume
   

37. 请求查询报价 ReqQryQuote
    (CThostFtdcQryQuoteField *pQryQuote, int nRequestID)
    
    
       经纪公司代码  BrokerID
    投资者代码  InvestorID
    合约代码  InstrumentID
    交易所代码  ExchangeID
    报价编号  QuoteSysID
    开始时间  InsertTimeStart
    结束时间  InsertTimeEnd
    
    
    返回数据
    
    
     经纪公司代码  BrokerID
    投资者代码  InvestorID
    合约代码  InstrumentID
    报价引用  QuoteRef
    用户代码  UserID
    卖价格  AskPrice
    买价格  BidPrice
    卖数量  AskVolume
    买数量  BidVolume
    请求编号  RequestID
    业务单元  BusinessUnit
    卖开平标志  AskOffsetFlag
    买开平标志  BidOffsetFlag
    卖投机套保标志  AskHedgeFlag
    买投机套保标志  BidHedgeFlag
    本地报价编号  QuoteLocalID
    交易所代码  ExchangeID
    会员代码  ParticipantID
    客户代码  ClientID
    合约在交易所的代码  ExchangeInstID
    交易所交易员代码  TraderID
    安装编号  InstallID
    报价提示序号  NotifySequence
    报价提交状态  OrderSubmitStatus
    交易日  TradingDay
    结算编号  SettlementID
    报价编号  QuoteSysID
    报单日期  InsertDate
    插入时间  InsertTime
    撤销时间  CancelTime
    报价状态  QuoteStatus
    结算会员编号  ClearingPartID
    序号  SequenceNo
    卖方报单编号  AskOrderSysID
    买方报单编号  BidOrderSysID
    前置编号  FrontID
    会话编号  SessionID
    用户端产品信息  UserProductInfo
    状态信息  StatusMsg
    操作用户代码  ActiveUserID
    经纪公司报价编号  BrokerQuoteSeq
    衍生卖报单引用  AskOrderRef
    衍生买报单引用  BidOrderRef
    应价编号  ForQuoteSysID
    营业部编号  BranchID
    投资单元代码  InvestUnitID
    资金账号  AccountID
    币种代码  CurrencyID
    IP地址  IPAddress
    Mac地址  MacAddress

38. 请求查询申请组合 ReqQryCombAction
    (CThostFtdcQryCombActionField *pQryCombAction, int nRequestID)
    
    
      经纪公司代码  BrokerID
    投资者代码  InvestorID
    合约代码  InstrumentID
    交易所代码  ExchangeID
    
    
   返回数据
    
        经纪公司代码  BrokerID
    投资者代码  InvestorID
    合约代码  InstrumentID
    组合引用  CombActionRef
    用户代码  UserID
    买卖方向  Direction
    数量  Volume
    组合指令方向  CombDirection
    投机套保标志  HedgeFlag
    本地申请组合编号  ActionLocalID
    交易所代码  ExchangeID
    会员代码  ParticipantID
    客户代码  ClientID
    合约在交易所的代码  ExchangeInstID
    交易所交易员代码  TraderID
    安装编号  InstallID
    组合状态  ActionStatus
    报单提示序号  NotifySequence
    交易日  TradingDay
    结算编号  SettlementID
    序号  SequenceNo
    前置编号  FrontID
    会话编号  SessionID
    用户端产品信息  UserProductInfo
    状态信息  StatusMsg
    IP地址  IPAddress
    Mac地址  MacAddress

    
39. 请求查询预埋单 ReqQryParkedOrder
    (CThostFtdcQryParkedOrderField *pQryParkedOrder, int nRequestID)
    
    
        经纪公司代码  BrokerID
    投资者代码  InvestorID
    合约代码  InstrumentID
    交易所代码  ExchangeID
    
    
    
    返回数据
    
    
     经纪公司代码  BrokerID
    投资者代码  InvestorID
    合约代码  InstrumentID
    报单引用  OrderRef
    用户代码  UserID
    报单价格条件  OrderPriceType
    买卖方向  Direction
    组合开平标志  CombOffsetFlag
    组合投机套保标志  CombHedgeFlag
    价格  LimitPrice
    数量  VolumeTotalOriginal
    有效期类型  TimeCondition
    GTD日期  GTDDate
    成交量类型  VolumeCondition
    最小成交量  MinVolume
    触发条件  ContingentCondition
    止损价  StopPrice
    强平原因  ForceCloseReason
    自动挂起标志  IsAutoSuspend
    业务单元  BusinessUnit
    请求编号  RequestID
    用户强评标志  UserForceClose
    交易所代码  ExchangeID
    预埋报单编号  ParkedOrderID
    用户类型  UserType
    预埋单状态  Status
    错误代码  ErrorID
    错误信息  ErrorMsg
    互换单标志  IsSwapOrder
    资金账号  AccountID
    币种代码  CurrencyID
    交易编码  ClientID
    投资单元代码  InvestUnitID
    IP地址  IPAddress
    Mac地址  MacAddress
    

40. 请求查询预埋撤单 ReqQryParkedOrderAction
    (CThostFtdcQryParkedOrderActionField *pQryParkedOrderAction, int nRequestID)
    
    
    经纪公司代码  BrokerID
    投资者代码  InvestorID
    合约代码  InstrumentID
    交易所代码  ExchangeID
    
    
    返回数据
    
    
        经纪公司代码  BrokerID
    投资者代码  InvestorID
    报单操作引用  OrderActionRef
    报单引用  OrderRef
    请求编号  RequestID
    前置编号  FrontID
    会话编号  SessionID
    交易所代码  ExchangeID
    报单编号  OrderSysID
    操作标志  ActionFlag
    价格  LimitPrice
    数量变化  VolumeChange
    用户代码  UserID
    合约代码  InstrumentID
    预埋撤单单编号  ParkedOrderActionID
    用户类型  UserType
    预埋撤单状态  Status
    错误代码  ErrorID
    错误信息  ErrorMsg
    投资单元代码  InvestUnitID
    IP地址  IPAddress
    Mac地址  MacAddress

    
    
    
    
## 待确认
     请求查询询价 ReqQryForQuote
    (CThostFtdcQryForQuoteField *pQryForQuote, int nRequestID)
    
        询价录入请求 ReqForQuoteInsert
    (CThostFtdcInputForQuoteField *pInputForQuote, int nRequestID)
    

