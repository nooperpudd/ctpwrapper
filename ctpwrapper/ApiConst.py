# encoding:utf-8

#///正常
ExchangeProperty_Normal = '0'
#///根据成交生成报单
ExchangeProperty_GenOrderByTrade = '1'
#///组织机构代码
IdCardType_EID = '0'
#///中国公民身份证
IdCardType_IDCard = '1'
#///军官证
IdCardType_OfficerIDCard = '2'
#///警官证
IdCardType_PoliceIDCard = '3'
#///士兵证
IdCardType_SoldierIDCard = '4'
#///户口簿
IdCardType_HouseholdRegister =  '5'
#///护照
IdCardType_Passport = '6'
#///台胞证
IdCardType_TaiwanCompatriotIDCard = '7'
#///回乡证
IdCardType_HomeComingCard = '8'
#///营业执照号
IdCardType_LicenseNo = '9'
#///税务登记号/当地纳税ID
IdCardType_TaxNo = 'A'
#///港澳居民来往内地通行证
IdCardType_HMMainlandTravelPermit = 'B'
#///台湾居民来往大陆通行证
IdCardType_TwMainlandTravelPermit = 'C'
#///驾照
IdCardType_DrivingLicense = 'D'
#///当地社保ID
IdCardType_SocialID = 'F'
#///当地身份证
IdCardType_LocalID = 'G'
#///商业登记证
IdCardType_BusinessRegistration = 'H'
#///港澳永久性居民身份证
IdCardType_HKMCIDCard = 'I'
#///人行开户许可证
IdCardType_AccountsPermits = 'J'
#///外国人永久居留证
IdCardType_FrgPrmtRdCard = 'K'
#///资管产品备案函
IdCardType_CptMngPrdLetter = 'L'
#///其他证件
IdCardType_OtherCard = 'x'
#///所有
InvestorRange_All = '1'
#///投资者组
InvestorRange_Group = '2'
#///单一投资者
InvestorRange_Single = '3'
#///所有
DepartmentRange_All = '1'
#///组织架构
DepartmentRange_Group = '2'
#///单一投资者
DepartmentRange_Single = '3'
#///未同步
DataSyncStatus_Asynchronous = '1'
#///同步中
DataSyncStatus_Synchronizing = '2'
#///已同步
DataSyncStatus_Synchronized = '3'
#///已同步
BrokerDataSyncStatus_Synchronized = '1'
#///同步中
BrokerDataSyncStatus_Synchronizing = '2'
#///没有任何连接
ExchangeConnectStatus_NoConnection = '1'
#///已经发出合约查询请求
ExchangeConnectStatus_QryInstrumentSent = '2'
#///已经获取信息
ExchangeConnectStatus_GotInformation = '9'
#///没有任何连接
TraderConnectStatus_NotConnected = '1'
#///已经连接
TraderConnectStatus_Connected = '2'
#///已经发出合约查询请求
TraderConnectStatus_QryInstrumentSent = '3'
#///订阅私有流
TraderConnectStatus_SubPrivateFlow = '4'
#///数据异步化
FunctionCode_DataAsync = '1'
#///强制用户登出
FunctionCode_ForceUserLogout = '2'
#///变更管理用户口令
FunctionCode_UserPasswordUpdate = '3'
#///变更经纪公司口令
FunctionCode_BrokerPasswordUpdate = '4'
#///变更投资者口令
FunctionCode_InvestorPasswordUpdate = '5'
#///报单插入
FunctionCode_OrderInsert = '6'
#///报单操作
FunctionCode_OrderAction = '7'
#///同步系统数据
FunctionCode_SyncSystemData = '8'
#///同步经纪公司数据
FunctionCode_SyncBrokerData = '9'
#///批量同步经纪公司数据
FunctionCode_BachSyncBrokerData = 'A'
#///超级查询
FunctionCode_SuperQuery = 'B'
#///预埋报单插入
FunctionCode_ParkedOrderInsert = 'C'
#///预埋报单操作
FunctionCode_ParkedOrderAction = 'D'
#///同步动态令牌
FunctionCode_SyncOTP = 'E'
#///删除未知单
FunctionCode_DeleteOrder = 'F'
#///强制用户登出
BrokerFunctionCode_ForceUserLogout = '1'
#///变更用户口令
BrokerFunctionCode_UserPasswordUpdate = '2'
#///同步经纪公司数据
BrokerFunctionCode_SyncBrokerData = '3'
#///批量同步经纪公司数据
BrokerFunctionCode_BachSyncBrokerData = '4'
#///报单插入
BrokerFunctionCode_OrderInsert = '5'
#///报单操作
BrokerFunctionCode_OrderAction = '6'
#///全部查询
BrokerFunctionCode_AllQuery = '7'
#///系统功能：登入/登出/修改密码等
BrokerFunctionCode_log = 'a'
#///基本查询：查询基础数据，如合约，交易所等常量
BrokerFunctionCode_BaseQry = 'b'
#///交易查询：如查成交，委托
BrokerFunctionCode_TradeQry = 'c'
#///交易功能：报单，撤单
BrokerFunctionCode_Trade = 'd'
#///银期转账
BrokerFunctionCode_Virement = 'e'
#///风险监控
BrokerFunctionCode_Risk = 'f'
#///查询/管理：查询会话，踢人等
BrokerFunctionCode_Session = 'g'
#///风控通知控制
BrokerFunctionCode_RiskNoticeCtl = 'h'
#///风控通知发送
BrokerFunctionCode_RiskNotice = 'i'
#///察看经纪公司资金权限
BrokerFunctionCode_BrokerDeposit = 'j'
#///资金查询
BrokerFunctionCode_QueryFund = 'k'
#///报单查询
BrokerFunctionCode_QueryOrder = 'l'
#///成交查询
BrokerFunctionCode_QueryTrade = 'm'
#///持仓查询
BrokerFunctionCode_QueryPosition = 'n'
#///行情查询
BrokerFunctionCode_QueryMarketData = 'o'
#///用户事件查询
BrokerFunctionCode_QueryUserEvent = 'p'
#///风险通知查询
BrokerFunctionCode_QueryRiskNotify = 'q'
#///出入金查询
BrokerFunctionCode_QueryFundChange = 'r'
#///投资者信息查询
BrokerFunctionCode_QueryInvestor = 's'
#///交易编码查询
BrokerFunctionCode_QueryTradingCode = 't'
#///强平
BrokerFunctionCode_ForceClose = 'u'
#///压力测试
BrokerFunctionCode_PressTest = 'v'
#///权益反算
BrokerFunctionCode_RemainCalc = 'w'
#///净持仓保证金指标
BrokerFunctionCode_NetPositionInd = 'x'
#///风险预算
BrokerFunctionCode_RiskPredict = 'y'
#///数据导出
BrokerFunctionCode_DataExport = 'z'
#///风控指标设置
BrokerFunctionCode_RiskTargetSetup = 'A'
#///行情预警
BrokerFunctionCode_MarketDataWarn = 'B'
#///业务通知查询
BrokerFunctionCode_QryBizNotice = 'C'
#///业务通知模板设置
BrokerFunctionCode_CfgBizNotice = 'D'
#///同步动态令牌
BrokerFunctionCode_SyncOTP = 'E'
#///发送业务通知
BrokerFunctionCode_SendBizNotice = 'F'
#///风险级别标准设置
BrokerFunctionCode_CfgRiskLevelStd = 'G'
#///交易终端应急功能
BrokerFunctionCode_TbCommand = 'H'
#///删除未知单
BrokerFunctionCode_DeleteOrder = 'J'
#///预埋报单插入
BrokerFunctionCode_ParkedOrderInsert = 'K'
#///预埋报单操作
BrokerFunctionCode_ParkedOrderAction = 'L'
#///资金不够仍允许行权
BrokerFunctionCode_ExecOrderNoCheck = 'M'
#///指定
BrokerFunctionCode_Designate = 'N'
#///证券处置
BrokerFunctionCode_StockDisposal = 'O'
#///席位资金预警
BrokerFunctionCode_BrokerDepositWarn = 'Q'
#///备兑不足预警
BrokerFunctionCode_CoverWarn = 'S'
#///行权试算
BrokerFunctionCode_PreExecOrder = 'T'
#///行权交收风险
BrokerFunctionCode_ExecOrderRisk = 'P'
#///持仓限额预警
BrokerFunctionCode_PosiLimitWarn = 'U'
#///持仓限额查询
BrokerFunctionCode_QryPosiLimit = 'V'
#///银期签到签退
BrokerFunctionCode_FBSign = 'W'
#///银期签约解约
BrokerFunctionCode_FBAccount = 'X'
#///已经提交
OrderActionStatus_Submitted = 'a'
#///已经接受
OrderActionStatus_Accepted = 'b'
#///已经被拒绝
OrderActionStatus_Rejected = 'c'
#///全部成交
OrderStatus_AllTraded = '0'
#///部分成交还在队列中
OrderStatus_PartTradedQueueing = '1'
#///部分成交不在队列中
OrderStatus_PartTradedNotQueueing = '2'
#///未成交还在队列中
OrderStatus_NoTradeQueueing = '3'
#///未成交不在队列中
OrderStatus_NoTradeNotQueueing = '4'
#///撤单
OrderStatus_Canceled = '5'
#///未知
OrderStatus_Unknown = 'a'
#///尚未触发
OrderStatus_NotTouched = 'b'
#///已触发
OrderStatus_Touched = 'c'
#///已经提交
OrderSubmitStatus_InsertSubmitted = '0'
#///撤单已经提交
OrderSubmitStatus_CancelSubmitted = '1'
#///修改已经提交
OrderSubmitStatus_ModifySubmitted = '2'
#///已经接受
OrderSubmitStatus_Accepted = '3'
#///报单已经被拒绝
OrderSubmitStatus_InsertRejected = '4'
#///撤单已经被拒绝
OrderSubmitStatus_CancelRejected = '5'
#///改单已经被拒绝
OrderSubmitStatus_ModifyRejected = '6'
#///今日持仓
PositionDate_Today = '1'
#///历史持仓
PositionDate_History = '2'
#///使用历史持仓
PositionDateType_UseHistory = '1'
#///不使用历史持仓
PositionDateType_NoUseHistory = '2'
#///代理
TradingRole_Broker = '1'
#///自营
TradingRole_Host = '2'
#///做市商
TradingRole_Maker = '3'
#///期货
ProductClass_Futures = '1'
#///期货期权
ProductClass_Options = '2'
#///组合
ProductClass_Combination = '3'
#///即期
ProductClass_Spot = '4'
#///期转现
ProductClass_EFP = '5'
#///现货期权
ProductClass_SpotOption = '6'
#///未上市
InstLifePhase_NotStart = '0'
#///上市
InstLifePhase_Started = '1'
#///停牌
InstLifePhase_Pause = '2'
#///到期
InstLifePhase_Expired = '3'
#///买
Direction_Buy = '0'
#///卖
Direction_Sell = '1'
#///净持仓
PositionType_Net = '1'
#///综合持仓
PositionType_Gross = '2'
#///净
PosiDirection_Net = '1'
#///多头
PosiDirection_Long = '2'
#///空头
PosiDirection_Short = '3'
#///不活跃
SysSettlementStatus_NonActive = '1'
#///启动
SysSettlementStatus_Startup = '2'
#///操作
SysSettlementStatus_Operating = '3'
#///结算
SysSettlementStatus_Settlement = '4'
#///结算完成
SysSettlementStatus_SettlementFinished = '5'
#///交易费率
RatioAttr_Trade = '0'
#///结算费率
RatioAttr_Settlement = '1'
#///投机
HedgeFlag_Speculation = '1'
#///套利
HedgeFlag_Arbitrage = '2'
#///套保
HedgeFlag_Hedge = '3'
#///做市商
HedgeFlag_MarketMaker = '5'
#///第一腿投机第二腿套保 大商所专用
HedgeFlag_SpecHedge = '6'
#///第一腿套保第二腿投机  大商所专用
HedgeFlag_HedgeSpec = '7'
#///投机
BillHedgeFlag_Speculation = '1'
#///套利
BillHedgeFlag_Arbitrage = '2'
#///套保
BillHedgeFlag_Hedge = '3'
#///投机
ClientIDType_Speculation = '1'
#///套利
ClientIDType_Arbitrage = '2'
#///套保
ClientIDType_Hedge = '3'
#///做市商
ClientIDType_MarketMaker = '5'
#///任意价
OrderPriceType_AnyPrice = '1'
#///限价
OrderPriceType_LimitPrice = '2'
#///最优价
OrderPriceType_BestPrice = '3'
#///最新价
OrderPriceType_LastPrice = '4'
#///最新价浮动上浮1个ticks
OrderPriceType_LastPricePlusOneTicks = '5'
#///最新价浮动上浮2个ticks
OrderPriceType_LastPricePlusTwoTicks = '6'
#///最新价浮动上浮3个ticks
OrderPriceType_LastPricePlusThreeTicks = '7'
#///卖一价
OrderPriceType_AskPrice1 = '8'
#///卖一价浮动上浮1个ticks
OrderPriceType_AskPrice1PlusOneTicks = '9'
#///卖一价浮动上浮2个ticks
OrderPriceType_AskPrice1PlusTwoTicks = 'A'
#///卖一价浮动上浮3个ticks
OrderPriceType_AskPrice1PlusThreeTicks = 'B'
#///买一价
OrderPriceType_BidPrice1 = 'C'
#///买一价浮动上浮1个ticks
OrderPriceType_BidPrice1PlusOneTicks = 'D'
#///买一价浮动上浮2个ticks
OrderPriceType_BidPrice1PlusTwoTicks = 'E'
#///买一价浮动上浮3个ticks
OrderPriceType_BidPrice1PlusThreeTicks = 'F'
#///五档价
OrderPriceType_FiveLevelPrice = 'G'
#///开仓
OffsetFlag_Open = '0'
#///平仓
OffsetFlag_Close = '1'
#///强平
OffsetFlag_ForceClose = '2'
#///平今
OffsetFlag_CloseToday = '3'
#///平昨
OffsetFlag_CloseYesterday = '4'
#///强减
OffsetFlag_ForceOff = '5'
#///本地强平
OffsetFlag_LocalForceClose = '6'
#///非强平
ForceCloseReason_NotForceClose = '0'
#///资金不足
ForceCloseReason_LackDeposit = '1'
#///客户超仓
ForceCloseReason_ClientOverPositionLimit = '2'
#///会员超仓
ForceCloseReason_MemberOverPositionLimit = '3'
#///持仓非整数倍
ForceCloseReason_NotMultiple = '4'
#///违规
ForceCloseReason_Violation = '5'
#///其它
ForceCloseReason_Other = '6'
#///自然人临近交割
ForceCloseReason_PersonDeliv = '7'
#///正常
OrderType_Normal = '0'
#///报价衍生
OrderType_DeriveFromQuote = '1'
#///组合衍生
OrderType_DeriveFromCombination = '2'
#///组合报单
OrderType_Combination = '3'
#///条件单
OrderType_ConditionalOrder = '4'
#///互换单
OrderType_Swap = '5'
#///大宗交易成交衍生
OrderType_DeriveFromBlockTrade = '6'
#///期转现成交衍生
OrderType_DeriveFromEFPTrade = '7'
#///立即完成，否则撤销
TimeCondition_IOC = '1'
#///本节有效
TimeCondition_GFS = '2'
#///当日有效
TimeCondition_GFD = '3'
#///指定日期前有效
TimeCondition_GTD = '4'
#///撤销前有效
TimeCondition_GTC = '5'
#///集合竞价有效
TimeCondition_GFA = '6'
#///任何数量
VolumeCondition_AV = '1'
#///最小数量
VolumeCondition_MV = '2'
#///全部数量
VolumeCondition_CV = '3'
#///立即
ContingentCondition_Immediately = '1'
#///止损
ContingentCondition_Touch = '2'
#///止赢
ContingentCondition_TouchProfit = '3'
#///预埋单
ContingentCondition_ParkedOrder = '4'
#///最新价大于条件价
ContingentCondition_LastPriceGreaterThanStopPrice = '5'
#///最新价大于等于条件价
ContingentCondition_LastPriceGreaterEqualStopPrice = '6'
#///最新价小于条件价
ContingentCondition_LastPriceLesserThanStopPrice = '7'
#///最新价小于等于条件价
ContingentCondition_LastPriceLesserEqualStopPrice = '8'
#///卖一价大于条件价
ContingentCondition_AskPriceGreaterThanStopPrice = '9'
#///卖一价大于等于条件价
ContingentCondition_AskPriceGreaterEqualStopPrice = 'A'
#///卖一价小于条件价
ContingentCondition_AskPriceLesserThanStopPrice = 'B'
#///卖一价小于等于条件价
ContingentCondition_AskPriceLesserEqualStopPrice = 'C'
#///买一价大于条件价
ContingentCondition_BidPriceGreaterThanStopPrice = 'D'
#///买一价大于等于条件价
ContingentCondition_BidPriceGreaterEqualStopPrice = 'E'
#///买一价小于条件价
ContingentCondition_BidPriceLesserThanStopPrice = 'F'
#///买一价小于等于条件价
ContingentCondition_BidPriceLesserEqualStopPrice = 'H'
#///删除
ActionFlag_Delete = '0'
#///修改
ActionFlag_Modify = '3'
#///可以交易
TradingRight_Allow = '0'
#///只能平仓
TradingRight_CloseOnly = '1'
#///不能交易
TradingRight_Forbidden = '2'
#///来自参与者
OrderSource_Participant = '0'
#///来自管理员
OrderSource_Administrator = '1'
#///组合持仓拆分为单一持仓,初始化不应包含该类型的持仓
TradeType_SplitCombination = '#'
#///普通成交
TradeType_Common = '0'
#///期权执行
TradeType_OptionsExecution = '1'
#///OTC成交
TradeType_OTC = '2'
#///期转现衍生成交
TradeType_EFPDerived = '3'
#///组合衍生成交
TradeType_CombinationDerived = '4'
#///大宗交易成交
TradeType_BlockTrade = '5'
#///前成交价
PriceSource_LastPrice = '0'
#///买委托价
PriceSource_Buy = '1'
#///卖委托价
PriceSource_Sell = '2'
#///场外成交价
PriceSource_OTC = '3'
#///开盘前
InstrumentStatus_BeforeTrading = '0'
#///非交易
InstrumentStatus_NoTrading = '1'
#///连续交易
InstrumentStatus_Continous = '2'
#///集合竞价报单
InstrumentStatus_AuctionOrdering = '3'
#///集合竞价价格平衡
InstrumentStatus_AuctionBalance = '4'
#///集合竞价撮合
InstrumentStatus_AuctionMatch = '5'
#///收盘
InstrumentStatus_Closed = '6'
#///自动切换
InstStatusEnterReason_Automatic = '1'
#///手动切换
InstStatusEnterReason_Manual = '2'
#///熔断
InstStatusEnterReason_Fuse = '3'
#///未上传
BatchStatus_NoUpload = '1'
#///已上传
BatchStatus_Uploaded = '2'
#///审核失败
BatchStatus_Failed = '3'
#///按所有品种
ReturnStyle_All = '1'
#///按品种
ReturnStyle_ByProduct = '2'
#///按成交手数
ReturnPattern_ByVolume = '1'
#///按留存手续费
ReturnPattern_ByFeeOnHand = '2'
#///级别1
ReturnLevel_Level1 = '1'
#///级别2
ReturnLevel_Level2 = '2'
#///级别3
ReturnLevel_Level3 = '3'
#///级别4
ReturnLevel_Level4 = '4'
#///级别5
ReturnLevel_Level5 = '5'
#///级别6
ReturnLevel_Level6 = '6'
#///级别7
ReturnLevel_Level7 = '7'
#///级别8
ReturnLevel_Level8 = '8'
#///级别9
ReturnLevel_Level9 = '9'
#///分阶段返还
ReturnStandard_ByPeriod = '1'
#///按某一标准
ReturnStandard_ByStandard = '2'
#///质出
MortgageType_Out = '0'
#///质入
MortgageType_In = '1'
#///质押比例
InvestorSettlementParamID_MortgageRatio = '4'
#///保证金算法
InvestorSettlementParamID_MarginWay = '5'
#///结算单结存是否包含质押
InvestorSettlementParamID_BillDeposit = '9'
#///质押比例
ExchangeSettlementParamID_MortgageRatio = '1'
#///分项资金导入项
ExchangeSettlementParamID_OtherFundItem = '2'
#///分项资金入交易所出入金
ExchangeSettlementParamID_OtherFundImport = '3'
#///中金所开户最低可用金额
ExchangeSettlementParamID_CFFEXMinPrepa = '6'
#///郑商所结算方式
ExchangeSettlementParamID_CZCESettlementType = '7'
#///交易所交割手续费收取方式
ExchangeSettlementParamID_ExchDelivFeeMode = '9'
#///投资者交割手续费收取方式
ExchangeSettlementParamID_DelivFeeMode = '0'
#///郑商所组合持仓保证金收取方式
ExchangeSettlementParamID_CZCEComMarginType = 'A'
#///大商所套利保证金是否优惠
ExchangeSettlementParamID_DceComMarginType = 'B'
#///虚值期权保证金优惠比率
ExchangeSettlementParamID_OptOutDisCountRate = 'a'
#///最低保障系数
ExchangeSettlementParamID_OptMiniGuarantee = 'b'
#///投资者代码最小长度
SystemParamID_InvestorIDMinLength = '1'
#///投资者帐号代码最小长度
SystemParamID_AccountIDMinLength = '2'
#///投资者开户默认登录权限
SystemParamID_UserRightLogon = '3'
#///投资者交易结算单成交汇总方式
SystemParamID_SettlementBillTrade = '4'
#///统一开户更新交易编码方式
SystemParamID_TradingCode = '5'
#///结算是否判断存在未复核的出入金和分项资金
SystemParamID_CheckFund = '6'
#///是否启用手续费模板数据权限
SystemParamID_CommModelRight = '7'
#///是否启用保证金率模板数据权限
SystemParamID_MarginModelRight = '9'
#///是否规范用户才能激活
SystemParamID_IsStandardActive = '8'
#///上传的交易所结算文件路径
SystemParamID_UploadSettlementFile = 'U'
#///上报保证金监控中心文件路径
SystemParamID_DownloadCSRCFile = 'D'
#///生成的结算单文件路径
SystemParamID_SettlementBillFile = 'S'
#///证监会文件标识
SystemParamID_CSRCOthersFile = 'C'
#///投资者照片路径
SystemParamID_InvestorPhoto = 'P'
#///全结经纪公司上传文件路径
SystemParamID_CSRCData = 'R'
#///开户密码录入方式
SystemParamID_InvestorPwdModel = 'I'
#///投资者中金所结算文件下载路径
SystemParamID_CFFEXInvestorSettleFile = 'F'
#///投资者代码编码方式
SystemParamID_InvestorIDType = 'a'
#///休眠户最高权益
SystemParamID_FreezeMaxReMain = 'r'
#///手续费相关操作实时上场开关
SystemParamID_IsSync = 'A'
#///解除开仓权限限制
SystemParamID_RelieveOpenLimit = 'O'
#///是否规范用户才能休眠
SystemParamID_IsStandardFreeze = 'X'
#///郑商所是否开放所有品种套保交易
SystemParamID_CZCENormalProductHedge = 'B'
#///系统加密算法
TradeParamID_EncryptionStandard = 'E'
#///系统风险算法
TradeParamID_RiskMode = 'R'
#///系统风险算法是否全局 0-否 1-是
TradeParamID_RiskModeGlobal = 'G'
#///密码加密算法
TradeParamID_modeEncode = 'P'
#///价格小数位数参数
TradeParamID_tickMode = 'T'
#///用户最大会话数
TradeParamID_SingleUserSessionMaxNum = 'S'
#///最大连续登录失败数
TradeParamID_LoginFailMaxNum = 'L'
#///是否强制认证
TradeParamID_IsAuthForce = 'A'
#///是否冻结证券持仓
TradeParamID_IsPosiFreeze = 'F'
#///是否限仓
TradeParamID_IsPosiLimit = 'M'
#///郑商所询价时间间隔
TradeParamID_ForQuoteTimeInterval = 'Q'
#///是否期货限仓
TradeParamID_IsFuturePosiLimit = 'B'
#///是否期货下单频率限制
TradeParamID_IsFutureOrderFreq = 'C'
#///行权冻结是否计算盈利
TradeParamID_IsExecOrderProfit = 'H'
#///银期开户是否验证开户银行卡号是否是预留银行账户
TradeParamID_IsCheckBankAcc = 'I'
#///弱密码最后修改日期
TradeParamID_PasswordDeadLine = 'J'
#///强密码校验
TradeParamID_IsStrongPassword = 'K'
#///自有资金质押比
TradeParamID_BalanceMorgage = 'a'
#///最小密码长度
TradeParamID_MinPwdLen = 'O'
#///IP当日最大登陆失败次数
TradeParamID_LoginFailMaxNumForIP = 'U'
#///密码有效期
TradeParamID_PasswordPeriod = 'V'
#///资金数据
FileID_SettlementFund = 'F'
#///成交数据
FileID_Trade = 'T'
#///投资者持仓数据
FileID_InvestorPosition = 'P'
#///投资者分项资金数据
FileID_SubEntryFund = 'O'
#///组合持仓数据
FileID_CZCECombinationPos = 'C'
#///上报保证金监控中心数据
FileID_CSRCData = 'R'
#///郑商所平仓了结数据
FileID_CZCEClose = 'L'
#///郑商所非平仓了结数据
FileID_CZCENoClose = 'N'
#///持仓明细数据
FileID_PositionDtl = 'D'
#///期权执行文件
FileID_OptionStrike = 'S'
#///结算价比对文件
FileID_SettlementPriceComparison = 'M'
#///上期所非持仓变动明细
FileID_NonTradePosChange = 'B'
#///结算
FileType_Settlement = '0'
#///核对
FileType_Check = '1'
#///文本文件(.txt)
FileFormat_Txt = '0'
#///压缩文件(.zip)
FileFormat_Zip = '1'
#///DBF文件(.dbf)
FileFormat_DBF = '2'
#///上传成功
FileUploadStatus_SucceedUpload = '1'
#///上传失败
FileUploadStatus_FailedUpload = '2'
#///导入成功
FileUploadStatus_SucceedLoad = '3'
#///导入部分成功
FileUploadStatus_PartSucceedLoad = '4'
#///导入失败
FileUploadStatus_FailedLoad = '5'
#///移出
TransferDirection_Out = '0'
#///移入
TransferDirection_In = '1'
#///没有特殊创建规则
SpecialCreateRule_NoSpecialRule = '0'
#///不包含春节
SpecialCreateRule_NoSpringFestival = '1'
#///上一合约结算价
BasisPriceType_LastSettlement = '1'
#///上一合约收盘价
BasisPriceType_LaseClose = '2'
#///活跃
ProductLifePhase_Active = '1'
#///不活跃
ProductLifePhase_NonActive = '2'
#///注销
ProductLifePhase_Canceled = '3'
#///现金交割
DeliveryMode_CashDeliv = '1'
#///实物交割
DeliveryMode_CommodityDeliv = '2'
#///出入金
FundIOType_FundIO = '1'
#///银期转帐
FundIOType_Transfer = '2'
#///银期换汇
FundIOType_SwapCurrency = '3'
#///银行存款
FundType_Deposite = '1'
#///分项资金
FundType_ItemFund = '2'
#///公司调整
FundType_Company = '3'
#///资金内转
FundType_InnerTransfer = '4'
#///入金
FundDirection_In = '1'
#///出金
FundDirection_Out = '2'
#///已录入
FundStatus_Record = '1'
#///已复核
FundStatus_Check = '2'
#///已冲销
FundStatus_Charge = '3'
#///未发布
PublishStatus_None = '1'
#///正在发布
PublishStatus_Publishing = '2'
#///已发布
PublishStatus_Published = '3'
#///不活跃
SystemStatus_NonActive = '1'
#///启动
SystemStatus_Startup = '2'
#///交易开始初始化
SystemStatus_Initialize = '3'
#///交易完成初始化
SystemStatus_Initialized = '4'
#///收市开始
SystemStatus_Close = '5'
#///收市完成
SystemStatus_Closed = '6'
#///结算
SystemStatus_Settlement = '7'
#///初始
SettlementStatus_Initialize = '0'
#///结算中
SettlementStatus_Settlementing = '1'
#///已结算
SettlementStatus_Settlemented = '2'
#///结算完成
SettlementStatus_Finished = '3'
#///自然人
InvestorType_Person = '0'
#///法人
InvestorType_Company = '1'
#///投资基金
InvestorType_Fund = '2'
#///特殊法人
InvestorType_SpecialOrgan = '3'
#///资管户
InvestorType_Asset = '4'
#///交易会员
BrokerType_Trade = '0'
#///交易结算会员
BrokerType_TradeSettle = '1'
#///低风险客户
RiskLevel_Low = '1'
#///普通客户
RiskLevel_Normal = '2'
#///关注客户
RiskLevel_Focus = '3'
#///风险客户
RiskLevel_Risk = '4'
#///按交易收取
FeeAcceptStyle_ByTrade = '1'
#///按交割收取
FeeAcceptStyle_ByDeliv = '2'
#///不收
FeeAcceptStyle_None = '3'
#///按指定手续费收取
FeeAcceptStyle_FixFee = '4'
#///交易密码
PasswordType_Trade = '1'
#///资金密码
PasswordType_Account = '2'
#///浮盈浮亏都计算
Algorithm_All = '1'
#///浮盈不计，浮亏计
Algorithm_OnlyLost = '2'
#///浮盈计，浮亏不计
Algorithm_OnlyGain = '3'
#///浮盈浮亏都不计算
Algorithm_None = '4'
#///包含平仓盈利
IncludeCloseProfit_Include = '0'
#///不包含平仓盈利
IncludeCloseProfit_NotInclude = '2'
#///无仓无成交不受可提比例限制
AllWithoutTrade_Enable = '0'
#///受可提比例限制
AllWithoutTrade_Disable = '2'
#///无仓不受可提比例限制
AllWithoutTrade_NoHoldEnable = '3'
#///不核对
FuturePwdFlag_UnCheck = '0'
#///核对
FuturePwdFlag_Check = '1'
#///银行转期货
TransferType_BankToFuture = '0'
#///期货转银行
TransferType_FutureToBank = '1'
#///无效或失败
TransferValidFlag_Invalid = '0'
#///有效
TransferValidFlag_Valid = '1'
#///冲正
TransferValidFlag_Reverse = '2'
#///错单
Reason_CD = '0'
#///资金在途
Reason_ZT = '1'
#///其它
Reason_QT = '2'
#///未知
Sex_None = '0'
#///男
Sex_Man = '1'
#///女
Sex_Woman = '2'
#///投资者
UserType_Investor = '0'
#///操作员
UserType_Operator = '1'
#///管理员
UserType_SuperUser = '2'
#///保证金率
RateType_MarginRate = '2'
#///交易结算单
NoteType_TradeSettleBill = '1'
#///交易结算月报
NoteType_TradeSettleMonth = '2'
#///追加保证金通知书
NoteType_CallMarginNotes = '3'
#///强行平仓通知书
NoteType_ForceCloseNotes = '4'
#///成交通知书
NoteType_TradeNotes = '5'
#///交割通知书
NoteType_DelivNotes = '6'
#///逐日盯市
SettlementStyle_Day = '1'
#///逐笔对冲
SettlementStyle_Volume = '2'
#///日报
SettlementBillType_Day = '0'
#///月报
SettlementBillType_Month = '1'
#///登录
UserRightType_Logon = '1'
#///银期转帐
UserRightType_Transfer = '2'
#///邮寄结算单
UserRightType_EMail = '3'
#///传真结算单
UserRightType_Fax = '4'
#///条件单
UserRightType_ConditionOrder = '5'
#///昨结算价
MarginPriceType_PreSettlementPrice = '1'
#///最新价
MarginPriceType_SettlementPrice = '2'
#///成交均价
MarginPriceType_AveragePrice = '3'
#///开仓价
MarginPriceType_OpenPrice = '4'
#///未生成
BillGenStatus_None = '0'
#///生成中
BillGenStatus_NoGenerated = '1'
#///已生成
BillGenStatus_Generated = '2'
#///持仓处理算法
AlgoType_HandlePositionAlgo = '1'
#///寻找保证金率算法
AlgoType_FindMarginRateAlgo = '2'
#///基本
HandlePositionAlgoID_Base = '1'
#///大连商品交易所
HandlePositionAlgoID_DCE = '2'
#///郑州商品交易所
HandlePositionAlgoID_CZCE = '3'
#///基本
FindMarginRateAlgoID_Base = '1'
#///大连商品交易所
FindMarginRateAlgoID_DCE = '2'
#///郑州商品交易所
FindMarginRateAlgoID_CZCE = '3'
#///基本
HandleTradingAccountAlgoID_Base = '1'
#///大连商品交易所
HandleTradingAccountAlgoID_DCE = '2'
#///郑州商品交易所
HandleTradingAccountAlgoID_CZCE = '3'
#///指定下单人
PersonType_Order = '1'
#///开户授权人
PersonType_Open = '2'
#///资金调拨人
PersonType_Fund = '3'
#///结算单确认人
PersonType_Settlement = '4'
#///法人
PersonType_Company = '5'
#///法人代表
PersonType_Corporation = '6'
#///投资者联系人
PersonType_LinkMan = '7'
#///分户管理资产负责人
PersonType_Ledger = '8'
#///托（保）管人
PersonType_Trustee = '9'
#///托（保）管机构法人代表
PersonType_TrusteeCorporation = 'A'
#///托（保）管机构开户授权人
PersonType_TrusteeOpen = 'B'
#///托（保）管机构联系人
PersonType_TrusteeContact = 'C'
#///境外自然人参考证件
PersonType_ForeignerRefer = 'D'
#///法人代表参考证件
PersonType_CorporationRefer = 'E'
#///所有
QueryInvestorRange_All = '1'
#///查询分类
QueryInvestorRange_Group = '2'
#///单一投资者
QueryInvestorRange_Single = '3'
#///正常
InvestorRiskStatus_Normal = '1'
#///警告
InvestorRiskStatus_Warn = '2'
#///追保
InvestorRiskStatus_Call = '3'
#///强平
InvestorRiskStatus_Force = '4'
#///异常
InvestorRiskStatus_Exception = '5'
#///登录
UserEventType_Login = '1'
#///登出
UserEventType_Logout = '2'
#///交易成功
UserEventType_Trading = '3'
#///交易失败
UserEventType_TradingError = '4'
#///修改密码
UserEventType_UpdatePassword = '5'
#///客户端认证
UserEventType_Authenticate = '6'
#///其他
UserEventType_Other = '9'
#///先开先平
CloseStyle_Close = '0'
#///先平今再平昨
CloseStyle_CloseToday = '1'
#///----
StatMode_Non = '0'
#///按合约统计
StatMode_Instrument = '1'
#///按产品统计
StatMode_Product = '2'
#///按投资者统计
StatMode_Investor = '3'
#///未发送
ParkedOrderStatus_NotSend = '1'
#///已发送
ParkedOrderStatus_Send = '2'
#///已删除
ParkedOrderStatus_Deleted = '3'
#///正在处理
VirDealStatus_Dealing = '1'
#///处理成功
VirDealStatus_DeaclSucceed = '2'
#///综合交易平台
OrgSystemID_Standard = '0'
#///易盛系统
OrgSystemID_ESunny = '1'
#///金仕达V6系统
OrgSystemID_KingStarV6 = '2'
#///正常处理中
VirTradeStatus_NaturalDeal = '0'
#///成功结束
VirTradeStatus_SucceedEnd = '1'
#///失败结束
VirTradeStatus_FailedEND = '2'
#///异常中
VirTradeStatus_Exception = '3'
#///已人工异常处理
VirTradeStatus_ManualDeal = '4'
#///通讯异常 ，请人工处理
VirTradeStatus_MesException = '5'
#///系统出错，请人工处理
VirTradeStatus_SysException = '6'
#///存折
VirBankAccType_BankBook = '1'
#///储蓄卡
VirBankAccType_BankCard = '2'
#///信用卡
VirBankAccType_CreditCard = '3'
#///正常
VirementStatus_Natural = '0'
#///销户
VirementStatus_Canceled = '9'
#///未确认
VirementAvailAbility_NoAvailAbility = '0'
#///有效
VirementAvailAbility_AvailAbility = '1'
#///冲正
VirementAvailAbility_Repeal = '2'
#///银行发起银行资金转期货
VirementTradeCode_BankBankToFuture = '102001'
#///银行发起期货资金转银行
VirementTradeCode_BankFutureToBank = '102002'
#///期货发起银行资金转期货
VirementTradeCode_FutureBankToFuture = '202001'
#///期货发起期货资金转银行
VirementTradeCode_FutureFutureToBank = '202002'
#///程序生成
AMLGenStatus_Program = '0'
#///人工生成
AMLGenStatus_HandWork = '1'
#///主动请求更新
CFMMCKeyKind_REQUEST = 'R'
#///CFMMC自动更新
CFMMCKeyKind_AUTO = 'A'
#///CFMMC手动更新
CFMMCKeyKind_MANUAL = 'M'
#///身份证
CertificationType_IDCard = '0'
#///护照
CertificationType_Passport = '1'
#///军官证
CertificationType_OfficerIDCard = '2'
#///士兵证
CertificationType_SoldierIDCard = '3'
#///回乡证
CertificationType_HomeComingCard = '4'
#///户口簿
CertificationType_HouseholdRegister = '5'
#///营业执照号
CertificationType_LicenseNo = '6'
#///组织机构代码证
CertificationType_InstitutionCodeCard = '7'
#///临时营业执照号
CertificationType_TempLicenseNo = '8'
#///民办非企业登记证书
CertificationType_NoEnterpriseLicenseNo = '9'
#///其他证件
CertificationType_OtherCard = 'x'
#///主管部门批文
CertificationType_SuperDepAgree = 'a'
#///其他
FileBusinessCode_Others = '0'
#///转账交易明细对账
FileBusinessCode_TransferDetails = '1'
#///客户账户状态对账
FileBusinessCode_CustAccStatus = '2'
#///账户类交易明细对账
FileBusinessCode_AccountTradeDetails = '3'
#///期货账户信息变更明细对账
FileBusinessCode_FutureAccountChangeInfoDetails = '4'
#///客户资金台账余额明细对账
FileBusinessCode_CustMoneyDetail = '5'
#///客户销户结息明细对账
FileBusinessCode_CustCancelAccountInfo = '6'
#///客户资金余额对账结果
FileBusinessCode_CustMoneyResult = '7'
#///其它对账异常结果文件
FileBusinessCode_OthersExceptionResult = '8'
#///客户结息净额明细
FileBusinessCode_CustInterestNetMoneyDetails = '9'
#///客户资金交收明细
FileBusinessCode_CustMoneySendAndReceiveDetails = 'a'
#///法人存管银行资金交收汇总
FileBusinessCode_CorporationMoneyTotal = 'b'
#///主体间资金交收汇总
FileBusinessCode_MainbodyMoneyTotal = 'c'
#///总分平衡监管数据
FileBusinessCode_MainPartMonitorData = 'd'
#///存管银行备付金余额
FileBusinessCode_PreparationMoney = 'e'
#///协办存管银行资金监管数据
FileBusinessCode_BankMoneyMonitorData = 'f'
#///汇
CashExchangeCode_Exchange = '1'
#///钞
CashExchangeCode_Cash = '2'
#///是
YesNoIndicator_Yes = '0'
#///否
YesNoIndicator_No = '1'
#///当前余额
BanlanceType_CurrentMoney = '0'
#///可用余额
BanlanceType_UsableMoney = '1'
#///可取余额
BanlanceType_FetchableMoney = '2'
#///冻结余额
BanlanceType_FreezeMoney = '3'
#///未知状态
Gender_Unknown = '0'
#///男
Gender_Male = '1'
#///女
Gender_Female = '2'
#///由受益方支付费用
FeePayFlag_BEN = '0'
#///由发送方支付费用
FeePayFlag_OUR = '1'
#///由发送方支付发起的费用，受益方支付接受的费用
FeePayFlag_SHA = '2'
#///交换密钥
PassWordKeyType_ExchangeKey = '0'
#///密码密钥
PassWordKeyType_PassWordKey = '1'
#///MAC密钥
PassWordKeyType_MACKey = '2'
#///报文密钥
PassWordKeyType_MessageKey = '3'
#///查询
FBTPassWordType_Query = '0'
#///取款
FBTPassWordType_Fetch = '1'
#///转帐
FBTPassWordType_Transfer = '2'
#///交易
FBTPassWordType_Trade = '3'
#///不加密
FBTEncryMode_NoEncry = '0'
#///DES
FBTEncryMode_DES = '1'
#///3DES
FBTEncryMode_3DES = '2'
#///银行无需自动冲正
BankRepealFlag_BankNotNeedRepeal = '0'
#///银行待自动冲正
BankRepealFlag_BankWaitingRepeal = '1'
#///银行已自动冲正
BankRepealFlag_BankBeenRepealed = '2'
#///期商无需自动冲正
BrokerRepealFlag_BrokerNotNeedRepeal = '0'
#///期商待自动冲正
BrokerRepealFlag_BrokerWaitingRepeal = '1'
#///期商已自动冲正
BrokerRepealFlag_BrokerBeenRepealed = '2'
#///银行
InstitutionType_Bank = '0'
#///期商
InstitutionType_Future = '1'
#///券商
InstitutionType_Store = '2'
#///是最后分片
LastFragment_Yes = '0'
#///不是最后分片
LastFragment_No = '1'
#///正常
BankAccStatus_Normal = '0'
#///冻结
BankAccStatus_Freeze = '1'
#///挂失
BankAccStatus_ReportLoss = '2'
#///正常
MoneyAccountStatus_Normal = '0'
#///销户
MoneyAccountStatus_Cancel = '1'
#///指定存管
ManageStatus_Point = '0'
#///预指定
ManageStatus_PrePoint = '1'
#///撤销指定
ManageStatus_CancelPoint = '2'
#///银期转帐
SystemType_FutureBankTransfer = '0'
#///银证转帐
SystemType_StockBankTransfer = '1'
#///第三方存管
SystemType_TheThirdPartStore = '2'
#///正常处理中
TxnEndFlag_NormalProcessing = '0'
#///成功结束
TxnEndFlag_Success = '1'
#///失败结束
TxnEndFlag_Failed = '2'
#///异常中
TxnEndFlag_Abnormal = '3'
#///已人工异常处理
TxnEndFlag_ManualProcessedForException = '4'
#///通讯异常 ，请人工处理
TxnEndFlag_CommuFailedNeedManualProcess = '5'
#///系统出错，请人工处理
TxnEndFlag_SysErrorNeedManualProcess = '6'
#///未处理
ProcessStatus_NotProcess = '0'
#///开始处理
ProcessStatus_StartProcess = '1'
#///处理完成
ProcessStatus_Finished = '2'
#///自然人
CustType_Person = '0'
#///机构户
CustType_Institution = '1'
#///入金，银行转期货
FBTTransferDirection_FromBankToFuture = '1'
#///出金，期货转银行
FBTTransferDirection_FromFutureToBank = '2'
#///开户
OpenOrDestroy_Open = '1'
#///销户
OpenOrDestroy_Destroy = '0'
#///未确认
AvailabilityFlag_Invalid = '0'
#///有效
AvailabilityFlag_Valid = '1'
#///冲正
AvailabilityFlag_Repeal = '2'
#///银行代理
OrganType_Bank = '1'
#///交易前置
OrganType_Future = '2'
#///银期转帐平台管理
OrganType_PlateForm = '9'
#///银行总行或期商总部
OrganLevel_HeadQuarters = '1'
#///银行分中心或期货公司营业部
OrganLevel_Branch = '2'
#///期商协议
ProtocalID_FutureProtocal = '0'
#///工行协议
ProtocalID_ICBCProtocal = '1'
#///农行协议
ProtocalID_ABCProtocal = '2'
#///中国银行协议
ProtocalID_CBCProtocal = '3'
#///建行协议
ProtocalID_CCBProtocal = '4'
#///交行协议
ProtocalID_BOCOMProtocal = '5'
#///银期转帐平台协议
ProtocalID_FBTPlateFormProtocal = 'X'
#///短连接
ConnectMode_ShortConnect = '0'
#///长连接
ConnectMode_LongConnect = '1'
#///异步
SyncMode_ASync = '0'
#///同步
SyncMode_Sync = '1'
#///银行存折
BankAccType_BankBook = '1'
#///储蓄卡
BankAccType_SavingCard = '2'
#///信用卡
BankAccType_CreditCard = '3'
#///银行存折
FutureAccType_BankBook = '1'
#///储蓄卡
FutureAccType_SavingCard = '2'
#///信用卡
FutureAccType_CreditCard = '3'
#///启用
OrganStatus_Ready = '0'
#///签到
OrganStatus_CheckIn = '1'
#///签退
OrganStatus_CheckOut = '2'
#///对帐文件到达
OrganStatus_CheckFileArrived = '3'
#///对帐
OrganStatus_CheckDetail = '4'
#///日终清理
OrganStatus_DayEndClean = '5'
#///注销
OrganStatus_Invalid = '9'
#///按金额扣收
CCBFeeMode_ByAmount = '1'
#///按月扣收
CCBFeeMode_ByMonth = '2'
#///客户端
CommApiType_Client = '1'
#///服务端
CommApiType_Server = '2'
#///交易系统的UserApi
CommApiType_UserApi = '3'
#///已经连接
LinkStatus_Connected = '1'
#///没有连接
LinkStatus_Disconnected = '2'
#///不核对
PwdFlag_NoCheck = '0'
#///明文核对
PwdFlag_BlankCheck = '1'
#///密文核对
PwdFlag_EncryptCheck = '2'
#///资金帐号
SecuAccType_AccountID = '1'
#///资金卡号
SecuAccType_CardID = '2'
#///上海股东帐号
SecuAccType_SHStockholderID = '3'
#///深圳股东帐号
SecuAccType_SZStockholderID = '4'
#///正常
TransferStatus_Normal = '0'
#///被冲正
TransferStatus_Repealed = '1'
#///期商
SponsorType_Broker = '0'
#///银行
SponsorType_Bank = '1'
#///请求
ReqRspType_Request = '0'
#///响应
ReqRspType_Response = '1'
#///签到
FBTUserEventType_SignIn = '0'
#///银行转期货
FBTUserEventType_FromBankToFuture = '1'
#///期货转银行
FBTUserEventType_FromFutureToBank = '2'
#///开户
FBTUserEventType_OpenAccount = '3'
#///销户
FBTUserEventType_CancelAccount = '4'
#///变更银行账户
FBTUserEventType_ChangeAccount = '5'
#///冲正银行转期货
FBTUserEventType_RepealFromBankToFuture = '6'
#///冲正期货转银行
FBTUserEventType_RepealFromFutureToBank = '7'
#///查询银行账户
FBTUserEventType_QueryBankAccount = '8'
#///查询期货账户
FBTUserEventType_QueryFutureAccount = '9'
#///签退
FBTUserEventType_SignOut = 'A'
#///密钥同步
FBTUserEventType_SyncKey = 'B'
#///预约开户
FBTUserEventType_ReserveOpenAccount = 'C'
#///撤销预约开户
FBTUserEventType_CancelReserveOpenAccount = 'D'
#///预约开户确认
FBTUserEventType_ReserveOpenAccountConfirm = 'E'
#///其他
FBTUserEventType_Other = 'Z'
#///插入
DBOperation_Insert = '0'
#///更新
DBOperation_Update = '1'
#///删除
DBOperation_Delete = '2'
#///已同步
SyncFlag_Yes = '0'
#///未同步
SyncFlag_No = '1'
#///一次同步
SyncType_OneOffSync = '0'
#///定时同步
SyncType_TimerSync = '1'
#///定时完全同步
SyncType_TimerFullSync = '2'
#///结汇
ExDirection_Settlement = '0'
#///售汇
ExDirection_Sale = '1'
#///成功
FBEResultFlag_Success = '0'
#///账户余额不足
FBEResultFlag_InsufficientBalance = '1'
#///交易结果未知
FBEResultFlag_UnknownTrading = '8'
#///失败
FBEResultFlag_Fail = 'x'
#///正常
FBEExchStatus_Normal = '0'
#///交易重发
FBEExchStatus_ReExchange = '1'
#///数据包
FBEFileFlag_DataPackage = '0'
#///文件
FBEFileFlag_File = '1'
#///未交易
FBEAlreadyTrade_NotTrade = '0'
#///已交易
FBEAlreadyTrade_Trade = '1'
#///签到
FBEUserEventType_SignIn = '0'
#///换汇
FBEUserEventType_Exchange = '1'
#///换汇重发
FBEUserEventType_ReExchange = '2'
#///银行账户查询
FBEUserEventType_QueryBankAccount = '3'
#///换汇明细查询
FBEUserEventType_QueryExchDetial = '4'
#///换汇汇总查询
FBEUserEventType_QueryExchSummary = '5'
#///换汇汇率查询
FBEUserEventType_QueryExchRate = '6'
#///对账文件通知
FBEUserEventType_CheckBankAccount = '7'
#///签退
FBEUserEventType_SignOut = '8'
#///其他
FBEUserEventType_Other = 'Z'
#///未处理
FBEReqFlag_UnProcessed = '0'
#///等待发送
FBEReqFlag_WaitSend = '1'
#///发送成功
FBEReqFlag_SendSuccess = '2'
#///发送失败
FBEReqFlag_SendFailed = '3'
#///等待重发
FBEReqFlag_WaitReSend = '4'
#///正常
NotifyClass_NOERROR = '0'
#///警示
NotifyClass_Warn = '1'
#///追保
NotifyClass_Call = '2'
#///强平
NotifyClass_Force = '3'
#///穿仓
NotifyClass_CHUANCANG = '4'
#///异常
NotifyClass_Exception = '5'
#///手工强平
ForceCloseType_Manual = '0'
#///单一投资者辅助强平
ForceCloseType_Single = '1'
#///批量投资者辅助强平
ForceCloseType_Group = '2'
#///系统通知
RiskNotifyMethod_System = '0'
#///短信通知
RiskNotifyMethod_SMS = '1'
#///邮件通知
RiskNotifyMethod_EMail = '2'
#///人工通知
RiskNotifyMethod_Manual = '3'
#///未生成
RiskNotifyStatus_NotGen = '0'
#///已生成未发送
RiskNotifyStatus_Generated = '1'
#///发送失败
RiskNotifyStatus_SendError = '2'
#///已发送未接收
RiskNotifyStatus_SendOk = '3'
#///已接收未确认
RiskNotifyStatus_Received = '4'
#///已确认
RiskNotifyStatus_Confirmed = '5'
#///导出数据
RiskUserEvent_ExportData = '0'
#///使用最新价升序
ConditionalOrderSortType_LastPriceAsc = '0'
#///使用最新价降序
ConditionalOrderSortType_LastPriceDesc = '1'
#///使用卖价升序
ConditionalOrderSortType_AskPriceAsc = '2'
#///使用卖价降序
ConditionalOrderSortType_AskPriceDesc = '3'
#///使用买价升序
ConditionalOrderSortType_BidPriceAsc = '4'
#///使用买价降序
ConditionalOrderSortType_BidPriceDesc = '5'
#///未发送
SendType_NoSend = '0'
#///已发送
SendType_Sended = '1'
#///已生成
SendType_Generated = '2'
#///报送失败
SendType_SendFail = '3'
#///接收成功
SendType_Success = '4'
#///接收失败
SendType_Fail = '5'
#///取消报送
SendType_Cancel = '6'
#///未申请
ClientIDStatus_NoApply = '1'
#///已提交申请
ClientIDStatus_Submited = '2'
#///已发送申请
ClientIDStatus_Sended = '3'
#///完成
ClientIDStatus_Success = '4'
#///拒绝
ClientIDStatus_Refuse = '5'
#///已撤销编码
ClientIDStatus_Cancel = '6'
#///单选
QuestionType_Radio = '1'
#///多选
QuestionType_Option = '2'
#///填空
QuestionType_Blank = '3'
#///请求
BusinessType_Request = '1'
#///应答
BusinessType_Response = '2'
#///通知
BusinessType_Notice = '3'
#///成功
CfmmcReturnCode_Success = '0'
#///该客户已经有流程在处理中
CfmmcReturnCode_Working = '1'
#///监控中客户资料检查失败
CfmmcReturnCode_InfoFail = '2'
#///监控中实名制检查失败
CfmmcReturnCode_IDCardFail = '3'
#///其他错误
CfmmcReturnCode_OtherFail = '4'
#///所有
ClientType_All = '0'
#///个人
ClientType_Person = '1'
#///单位
ClientType_Company = '2'
#///其他
ClientType_Other = '3'
#///特殊法人
ClientType_SpecialOrgan = '4'
#///资管户
ClientType_Asset = '5'
#///上海期货交易所
ExchangeIDType_SHFE = 'S'
#///郑州商品交易所
ExchangeIDType_CZCE = 'Z'
#///大连商品交易所
ExchangeIDType_DCE = 'D'
#///中国金融期货交易所
ExchangeIDType_CFFEX = 'J'
#///上海国际能源交易中心股份有限公司
ExchangeIDType_INE = 'N'
#///套保
ExClientIDType_Hedge = '1'
#///套利
ExClientIDType_Arbitrage = '2'
#///投机
ExClientIDType_Speculation = '3'
#///未更新
UpdateFlag_NoUpdate = '0'
#///更新全部信息成功
UpdateFlag_Success = '1'
#///更新全部信息失败
UpdateFlag_Fail = '2'
#///更新交易编码成功
UpdateFlag_TCSuccess = '3'
#///更新交易编码失败
UpdateFlag_TCFail = '4'
#///已丢弃
UpdateFlag_Cancel = '5'
#///开户
ApplyOperateID_OpenInvestor = '1'
#///修改身份信息
ApplyOperateID_ModifyIDCard = '2'
#///修改一般信息
ApplyOperateID_ModifyNoIDCard = '3'
#///申请交易编码
ApplyOperateID_ApplyTradingCode = '4'
#///撤销交易编码
ApplyOperateID_CancelTradingCode = '5'
#///销户
ApplyOperateID_CancelInvestor = '6'
#///账户休眠
ApplyOperateID_FreezeAccount = '8'
#///激活休眠账户
ApplyOperateID_ActiveFreezeAccount = '9'
#///未补全
ApplyStatusID_NoComplete = '1'
#///已提交
ApplyStatusID_Submited = '2'
#///已审核
ApplyStatusID_Checked = '3'
#///已拒绝
ApplyStatusID_Refused = '4'
#///已删除
ApplyStatusID_Deleted = '5'
#///文件发送
SendMethod_ByAPI = '1'
#///电子发送
SendMethod_ByFile = '2'
#///增加
EventMode_ADD = '1'
#///修改
EventMode_UPDATE = '2'
#///删除
EventMode_DELETE = '3'
#///复核
EventMode_CHECK = '4'
#///复制
EventMode_COPY = '5'
#///注销
EventMode_CANCEL = '6'
#///冲销
EventMode_Reverse = '7'
#///自动发送并接收
UOAAutoSend_ASR = '1'
#///自动发送，不自动接收
UOAAutoSend_ASNR = '2'
#///不自动发送，自动接收
UOAAutoSend_NSAR = '3'
#///不自动发送，也不自动接收
UOAAutoSend_NSR = '4'
#///投资者对应投资者组设置
FlowID_InvestorGroupFlow = '1'
#///投资者手续费率设置
FlowID_InvestorRate = '2'
#///投资者手续费率模板关系设置
FlowID_InvestorCommRateModel = '3'
#///零级复核
CheckLevel_Zero = '0'
#///一级复核
CheckLevel_One = '1'
#///二级复核
CheckLevel_Two = '2'
#///未复核
CheckStatus_Init = '0'
#///复核中
CheckStatus_Checking = '1'
#///已复核
CheckStatus_Checked = '2'
#///拒绝
CheckStatus_Refuse = '3'
#///作废
CheckStatus_Cancel = '4'
#///未生效
UsedStatus_Unused = '0'
#///已生效
UsedStatus_Used = '1'
#///生效失败
UsedStatus_Fail = '2'
#///手工录入
BankAcountOrigin_ByAccProperty = '0'
#///银期转账
BankAcountOrigin_ByFBTransfer = '1'
#///同日同合约
MonthBillTradeSum_ByInstrument = '0'
#///同日同合约同价格
MonthBillTradeSum_ByDayInsPrc = '1'
#///同合约
MonthBillTradeSum_ByDayIns = '2'
#///银行发起银行转期货
FBTTradeCodeEnum_BankLaunchBankToBroker = '102001'
#///期货发起银行转期货
FBTTradeCodeEnum_BrokerLaunchBankToBroker = '202001'
#///银行发起期货转银行
FBTTradeCodeEnum_BankLaunchBrokerToBank = '102002'
#///期货发起期货转银行
FBTTradeCodeEnum_BrokerLaunchBrokerToBank = '202002'
#///无动态令牌
OTPType_NONE = '0'
#///时间令牌
OTPType_TOTP = '1'
#///未使用
OTPStatus_Unused = '0'
#///已使用
OTPStatus_Used = '1'
#///注销
OTPStatus_Disuse = '2'
#///投资者
BrokerUserType_Investor = '1'
#///操作员
BrokerUserType_BrokerUser = '2'
#///商品期货
FutureType_Commodity = '1'
#///金融期货
FutureType_Financial = '2'
#///转账限额
FundEventType_Restriction = '0'
#///当日转账限额
FundEventType_TodayRestriction = '1'
#///期商流水
FundEventType_Transfer = '2'
#///资金冻结
FundEventType_Credit = '3'
#///投资者可提资金比例
FundEventType_InvestorWithdrawAlm = '4'
#///单个银行帐户转账限额
FundEventType_BankRestriction = '5'
#///银期签约账户
FundEventType_Accountregister = '6'
#///交易所出入金
FundEventType_ExchangeFundIO = '7'
#///投资者出入金
FundEventType_InvestorFundIO = '8'
#///银期同步
AccountSourceType_FBTransfer = '0'
#///手工录入
AccountSourceType_ManualEntry = '1'
#///统一开户(已规范)
CodeSourceType_UnifyAccount = '0'
#///手工录入(未规范)
CodeSourceType_ManualEntry = '1'
#///所有
UserRange_All = '0'
#///单一操作员
UserRange_Single = '1'
#///按投资者统计
ByGroup_Investor = '2'
#///按类统计
ByGroup_Group = '1'
#///按合约统计
TradeSumStatMode_Instrument = '1'
#///按产品统计
TradeSumStatMode_Product = '2'
#///按交易所统计
TradeSumStatMode_Exchange = '3'
#///相对已有规则设置
ExprSetMode_Relative = '1'
#///典型设置
ExprSetMode_Typical = '2'
#///公司标准
RateInvestorRange_All = '1'
#///模板
RateInvestorRange_Model = '2'
#///单一投资者
RateInvestorRange_Single = '3'
#///未同步
SyncDataStatus_Initialize = '0'
#///同步中
SyncDataStatus_Settlementing = '1'
#///已同步
SyncDataStatus_Settlemented = '2'
#///来自交易所普通回报
TradeSource_NORMAL = '0'
#///来自查询
TradeSource_QUERY = '1'
#///产品统计
FlexStatMode_Product = '1'
#///交易所统计
FlexStatMode_Exchange = '2'
#///统计所有
FlexStatMode_All = '3'
#///属性统计
ByInvestorRange_Property = '1'
#///统计所有
ByInvestorRange_All = '2'
#///所有
PropertyInvestorRange_All = '1'
#///投资者属性
PropertyInvestorRange_Property = '2'
#///单一投资者
PropertyInvestorRange_Single = '3'
#///未生成
FileStatus_NoCreate = '0'
#///已生成
FileStatus_Created = '1'
#///生成失败
FileStatus_Failed = '2'
#///下发
FileGenStyle_FileTransmit = '0'
#///生成
FileGenStyle_FileGen = '1'
#///增加
SysOperMode_Add = '1'
#///修改
SysOperMode_Update = '2'
#///删除
SysOperMode_Delete = '3'
#///复制
SysOperMode_Copy = '4'
#///激活
SysOperMode_AcTive = '5'
#///注销
SysOperMode_CanCel = '6'
#///重置
SysOperMode_ReSet = '7'
#///修改操作员密码
SysOperType_UpdatePassword = '0'
#///操作员组织架构关系
SysOperType_UserDepartment = '1'
#///角色管理
SysOperType_RoleManager = '2'
#///角色功能设置
SysOperType_RoleFunction = '3'
#///基础参数设置
SysOperType_BaseParam = '4'
#///设置操作员
SysOperType_SetUserID = '5'
#///用户角色设置
SysOperType_SetUserRole = '6'
#///用户IP限制
SysOperType_UserIpRestriction = '7'
#///组织架构管理
SysOperType_DepartmentManager = '8'
#///组织架构向查询分类复制
SysOperType_DepartmentCopy = '9'
#///交易编码管理
SysOperType_Tradingcode = 'A'
#///投资者状态维护
SysOperType_InvestorStatus = 'B'
#///投资者权限管理
SysOperType_InvestorAuthority = 'C'
#///属性设置
SysOperType_PropertySet = 'D'
#///重置投资者密码
SysOperType_ReSetInvestorPasswd = 'E'
#///投资者个性信息维护
SysOperType_InvestorPersonalityInfo = 'F'
#///查询当前交易日报送的数据
CSRCDataQueyType_Current = '0'
#///查询历史报送的代理经纪公司的数据
CSRCDataQueyType_History = '1'
#///活跃
FreezeStatus_Normal = '1'
#///休眠
FreezeStatus_Freeze = '0'
#///已规范
StandardStatus_Standard = '0'
#///未规范
StandardStatus_NonStandard = '1'
#///休眠户
RightParamType_Freeze = '1'
#///激活休眠户
RightParamType_FreezeActive = '2'
#///开仓权限限制
RightParamType_OpenLimit = '3'
#///解除开仓权限限制
RightParamType_RelieveOpenLimit = '4'
#///正常
DataStatus_Normal = '0'
#///已删除
DataStatus_Deleted = '1'
#///未复核
AMLCheckStatus_Init = '0'
#///复核中
AMLCheckStatus_Checking = '1'
#///已复核
AMLCheckStatus_Checked = '2'
#///拒绝上报
AMLCheckStatus_RefuseReport = '3'
#///检查日期
AmlDateType_DrawDay = '0'
#///发生日期
AmlDateType_TouchDay = '1'
#///零级审核
AmlCheckLevel_CheckLevel0 = '0'
#///一级审核
AmlCheckLevel_CheckLevel1 = '1'
#///二级审核
AmlCheckLevel_CheckLevel2 = '2'
#///三级审核
AmlCheckLevel_CheckLevel3 = '3'
#///CSV
ExportFileType_CSV = '0'
#///Excel
ExportFileType_EXCEL = '1'
#///DBF
ExportFileType_DBF = '2'
#///结算前准备
SettleManagerType_Before = '1'
#///结算
SettleManagerType_Settlement = '2'
#///结算后核对
SettleManagerType_After = '3'
#///结算后处理
SettleManagerType_Settlemented = '4'
#///必要
SettleManagerLevel_Must = '1'
#///警告
SettleManagerLevel_Alarm = '2'
#///提示
SettleManagerLevel_Prompt = '3'
#///不检查
SettleManagerLevel_Ignore = '4'
#///交易所核对
SettleManagerGroup_Exhcange = '1'
#///内部核对
SettleManagerGroup_ASP = '2'
#///上报数据核对
SettleManagerGroup_CSRC = '3'
#///可重复使用
LimitUseType_Repeatable = '1'
#///不可重复使用
LimitUseType_Unrepeatable = '2'
#///本系统
DataResource_Settle = '1'
#///交易所
DataResource_Exchange = '2'
#///报送数据
DataResource_CSRC = '3'
#///交易所保证金率
MarginType_ExchMarginRate = '0'
#///投资者保证金率
MarginType_InstrMarginRate = '1'
#///投资者交易保证金率
MarginType_InstrMarginRateTrade = '2'
#///仅当日生效
ActiveType_Intraday = '1'
#///长期生效
ActiveType_Long = '2'
#///交易所保证金率
MarginRateType_Exchange = '1'
#///投资者保证金率
MarginRateType_Investor = '2'
#///投资者交易保证金率
MarginRateType_InvestorTrade = '3'
#///未生成备份数据
BackUpStatus_UnBak = '0'
#///备份数据生成中
BackUpStatus_BakUp = '1'
#///已生成备份数据
BackUpStatus_BakUped = '2'
#///备份数据失败
BackUpStatus_BakFail = '3'
#///结算初始化未开始
InitSettlement_UnInitialize = '0'
#///结算初始化中
InitSettlement_Initialize = '1'
#///结算初始化完成
InitSettlement_Initialized = '2'
#///未生成报表数据
ReportStatus_NoCreate = '0'
#///报表数据生成中
ReportStatus_Create = '1'
#///已生成报表数据
ReportStatus_Created = '2'
#///生成报表数据失败
ReportStatus_CreateFail = '3'
#///归档未完成
SaveStatus_UnSaveData = '0'
#///归档完成
SaveStatus_SaveDatad = '1'
#///未归档数据
SettArchiveStatus_UnArchived = '0'
#///数据归档中
SettArchiveStatus_Archiving = '1'
#///已归档数据
SettArchiveStatus_Archived = '2'
#///归档数据失败
SettArchiveStatus_ArchiveFail = '3'
#///未知类型
CTPType_Unkown = '0'
#///主中心
CTPType_MainCenter = '1'
#///备中心
CTPType_BackUp = '2'
#///正常
CloseDealType_Normal = '0'
#///投机平仓优先
CloseDealType_SpecFirst = '1'
#///不能使用
MortgageFundUseRange_None = '0'
#///用于保证金
MortgageFundUseRange_Margin = '1'
#///用于手续费、盈亏、保证金
MortgageFundUseRange_All = '2'
#///人民币方案3
MortgageFundUseRange_CNY3 = '3'
#///郑商所套保产品
SpecProductType_CzceHedge = '1'
#///货币质押产品
SpecProductType_IneForeignCurrency = '2'
#///大连短线开平仓产品
SpecProductType_DceOpenClose = '3'
#///质押
FundMortgageType_Mortgage = '1'
#///解质
FundMortgageType_Redemption = '2'
#///基础保证金
AccountSettlementParamID_BaseMargin = '1'
#///最低权益标准
AccountSettlementParamID_LowestInterest = '2'
#///货币质入
FundMortDirection_In = '1'
#///货币质出
FundMortDirection_Out = '2'
#///盈利
BusinessClass_Profit = '0'
#///亏损
BusinessClass_Loss = '1'
#///其他
BusinessClass_Other = 'Z'
#///手工
SwapSourceType_Manual = '0'
#///自动生成
SwapSourceType_Automatic = '1'
#///结汇
CurrExDirection_Settlement = '0'
#///售汇
CurrExDirection_Sale = '1'
#///已录入
CurrencySwapStatus_Entry = '1'
#///已审核
CurrencySwapStatus_Approve = '2'
#///已拒绝
CurrencySwapStatus_Refuse = '3'
#///已撤销
CurrencySwapStatus_Revoke = '4'
#///已发送
CurrencySwapStatus_Send = '5'
#///换汇成功
CurrencySwapStatus_Success = '6'
#///换汇失败
CurrencySwapStatus_Failure = '7'
#///未发送
ReqFlag_NoSend = '0'
#///发送成功
ReqFlag_SendSuccess = '1'
#///发送失败
ReqFlag_SendFailed = '2'
#///等待重发
ReqFlag_WaitReSend = '3'
#///成功
ResFlag_Success = '0'
#///账户余额不足
ResFlag_InsuffiCient = '1'
#///交易结果未知
ResFlag_UnKnown = '8'
#///修改前
ExStatus_Before = '0'
#///修改后
ExStatus_After = '1'
#///国内客户
ClientRegion_Domestic = '1'
#///港澳台客户
ClientRegion_GMT = '2'
#///国外客户
ClientRegion_Foreign = '3'
#///没有
HasBoard_No = '0'
#///有
HasBoard_Yes = '1'
#///正常
StartMode_Normal = '1'
#///应急
StartMode_Emerge = '2'
#///恢复
StartMode_Restore = '3'
#///全量
TemplateType_Full = '1'
#///增量
TemplateType_Increment = '2'
#///备份
TemplateType_BackUp = '3'
#///交易
LoginMode_Trade = '0'
#///转账
LoginMode_Transfer = '1'
#///合约上下市
PromptType_Instrument = '1'
#///保证金分段生效
PromptType_Margin = '2'
#///有
HasTrustee_Yes = '1'
#///没有
HasTrustee_No = '0'
#///银行
AmType_Bank = '1'
#///证券公司
AmType_Securities = '2'
#///基金公司
AmType_Fund = '3'
#///保险公司
AmType_Insurance = '4'
#///信托公司
AmType_Trust = '5'
#///其他
AmType_Other = '9'
#///出入金
CSRCFundIOType_FundIO = '0'
#///银期换汇
CSRCFundIOType_SwapCurrency = '1'
#///期货结算账户
CusAccountType_Futures = '1'
#///纯期货资管业务下的资管结算账户
CusAccountType_AssetmgrFuture = '2'
#///综合类资管业务下的期货资管托管账户
CusAccountType_AssetmgrTrustee = '3'
#///综合类资管业务下的资金中转账户
CusAccountType_AssetmgrTransfer = '4'
#///中文
LanguageType_Chinese = '1'
#///英文
LanguageType_English = '2'
#///个人资管客户
AssetmgrClientType_Person = '1'
#///单位资管客户
AssetmgrClientType_Organ = '2'
#///特殊单位资管客户
AssetmgrClientType_SpecialOrgan = '4'
#///期货类
AssetmgrType_Futures = '3'
#///综合类
AssetmgrType_SpecialOrgan = '4'
#///合约交易所不存在
CheckInstrType_HasExch = '0'
#///合约本系统不存在
CheckInstrType_HasATP = '1'
#///合约比较不一致
CheckInstrType_HasDiff = '2'
#///手工交割
DeliveryType_HandDeliv = '1'
#///到期交割
DeliveryType_PersonDeliv = '2'
#///不使用大额单边保证金算法
MaxMarginSideAlgorithm_NO = '0'
#///使用大额单边保证金算法
MaxMarginSideAlgorithm_YES = '1'
#///自然人
DAClientType_Person = '0'
#///法人
DAClientType_Company = '1'
#///其他
DAClientType_Other = '2'
#///期货类
UOAAssetmgrType_Futures = '1'
#///综合类
UOAAssetmgrType_SpecialOrgan = '2'
#///Buy
DirectionEn_Buy = '0'
#///Sell
DirectionEn_Sell = '1'
#///Position Opening
OffsetFlagEn_Open = '0'
#///Position Close
OffsetFlagEn_Close = '1'
#///Forced Liquidation
OffsetFlagEn_ForceClose = '2'
#///Close Today
OffsetFlagEn_CloseToday = '3'
#///Close Prev.
OffsetFlagEn_CloseYesterday = '4'
#///Forced Reduction
OffsetFlagEn_ForceOff = '5'
#///Local Forced Liquidation
OffsetFlagEn_LocalForceClose = '6'
#///Speculation
HedgeFlagEn_Speculation = '1'
#///Arbitrage
HedgeFlagEn_Arbitrage = '2'
#///Hedge
HedgeFlagEn_Hedge = '3'
#///Deposit/Withdrawal
FundIOTypeEn_FundIO = '1'
#///Bank-Futures Transfer
FundIOTypeEn_Transfer = '2'
#///Bank-Futures FX Exchange
FundIOTypeEn_SwapCurrency = '3'
#///Bank Deposit
FundTypeEn_Deposite = '1'
#///Payment/Fee
FundTypeEn_ItemFund = '2'
#///Brokerage Adj
FundTypeEn_Company = '3'
#///Internal Transfer
FundTypeEn_InnerTransfer = '4'
#///Deposit
FundDirectionEn_In = '1'
#///Withdrawal
FundDirectionEn_Out = '2'
#///Pledge
FundMortDirectionEn_In = '1'
#///Redemption
FundMortDirectionEn_Out = '2'
#///看涨
OptionsType_CallOptions = '1'
#///看跌
OptionsType_PutOptions = '2'
#///欧式
StrikeMode_Continental = '0'
#///美式
StrikeMode_American = '1'
#///百慕大
StrikeMode_Bermuda = '2'
#///自身对冲
StrikeType_Hedge = '0'
#///匹配执行
StrikeType_Match = '1'
#///不执行数量
ApplyType_NotStrikeNum = '4'
#///系统生成
GiveUpDataSource_Gen = '0'
#///手工添加
GiveUpDataSource_Hand = '1'
#///没有执行
ExecResult_NoExec = 'n'
#///已经取消
ExecResult_Canceled = 'c'
#///执行成功
ExecResult_OK = '0'
#///期权持仓不够
ExecResult_NoPosition = '1'
#///资金不够
ExecResult_NoDeposit = '2'
#///会员不存在
ExecResult_NoParticipant = '3'
#///客户不存在
ExecResult_NoClient = '4'
#///合约不存在
ExecResult_NoInstrument = '6'
#///没有执行权限
ExecResult_NoRight = '7'
#///不合理的数量
ExecResult_InvalidVolume = '8'
#///没有足够的历史成交
ExecResult_NoEnoughHistoryTrade = '9'
#///未知
ExecResult_Unknown = 'a'
#///期货组合
CombinationType_Future = '0'
#///垂直价差BUL
CombinationType_BUL = '1'
#///垂直价差BER
CombinationType_BER = '2'
#///跨式组合
CombinationType_STD = '3'
#///宽跨式组合
CombinationType_STG = '4'
#///备兑组合
CombinationType_PRT = '5'
#///时间价差组合
CombinationType_CLD = '6'
#///期货对锁组合
DceCombinationType_SPL = '0'
#///期权对锁组合
DceCombinationType_OPL = '1'
#///期货跨期组合
DceCombinationType_SP = '2'
#///期货跨品种组合
DceCombinationType_SPC = '3'
#///买入期权垂直价差组合
DceCombinationType_BLS = '4'
#///卖出期权垂直价差组合
DceCombinationType_BES = '5'
#///期权日历价差组合
DceCombinationType_CAS = '6'
#///期权跨式组合
DceCombinationType_STD = '7'
#///期权宽跨式组合
DceCombinationType_STG = '8'
#///买入期货期权组合
DceCombinationType_BFO = '9'
#///卖出期货期权组合
DceCombinationType_SFO = 'a'
#///昨结算价
OptionRoyaltyPriceType_PreSettlementPrice = '1'
#///开仓价
OptionRoyaltyPriceType_OpenPrice = '4'
#///最新价与昨结算价较大值
OptionRoyaltyPriceType_MaxPreSettlementPrice = '5'
#///不计算期权市值盈亏
BalanceAlgorithm_Default = '1'
#///计算期权市值亏损
BalanceAlgorithm_IncludeOptValLost = '2'
#///执行
ActionType_Exec = '1'
#///放弃
ActionType_Abandon = '2'
#///已经提交
ForQuoteStatus_Submitted = 'a'
#///已经接受
ForQuoteStatus_Accepted = 'b'
#///已经被拒绝
ForQuoteStatus_Rejected = 'c'
#///按绝对值
ValueMethod_Absolute = '0'
#///按比率
ValueMethod_Ratio = '1'
#///保留
ExecOrderPositionFlag_Reserve = '0'
#///不保留
ExecOrderPositionFlag_UnReserve = '1'
#///自动平仓
ExecOrderCloseFlag_AutoClose = '0'
#///免于自动平仓
ExecOrderCloseFlag_NotToClose = '1'
#///期货
ProductType_Futures = '1'
#///期权
ProductType_Options = '2'
#///^\d{8}_zz_\d{4}
CZCEUploadFileName_CUFN_O = 'O'
#///^\d{8}成交表
CZCEUploadFileName_CUFN_T = 'T'
#///^\d{8}单腿持仓表new
CZCEUploadFileName_CUFN_P = 'P'
#///^\d{8}非平仓了结表
CZCEUploadFileName_CUFN_N = 'N'
#///^\d{8}平仓表
CZCEUploadFileName_CUFN_L = 'L'
#///^\d{8}资金表
CZCEUploadFileName_CUFN_F = 'F'
#///^\d{8}组合持仓表
CZCEUploadFileName_CUFN_C = 'C'
#///^\d{8}保证金参数表
CZCEUploadFileName_CUFN_M = 'M'
#///^\d{8}_dl_\d{3}
DCEUploadFileName_DUFN_O = 'O'
#///^\d{8}_成交表
DCEUploadFileName_DUFN_T = 'T'
#///^\d{8}_持仓表
DCEUploadFileName_DUFN_P = 'P'
#///^\d{8}_资金结算表
DCEUploadFileName_DUFN_F = 'F'
#///^\d{8}_优惠组合持仓明细表
DCEUploadFileName_DUFN_C = 'C'
#///^\d{8}_持仓明细表
DCEUploadFileName_DUFN_D = 'D'
#///^\d{8}_保证金参数表
DCEUploadFileName_DUFN_M = 'M'
#///^\d{8}_期权执行表
DCEUploadFileName_DUFN_S = 'S'
#///^\d{4}_\d{8}_\d{8}_DailyFundChg
SHFEUploadFileName_SUFN_O = 'O'
#///^\d{4}_\d{8}_\d{8}_Trade
SHFEUploadFileName_SUFN_T = 'T'
#///^\d{4}_\d{8}_\d{8}_SettlementDetail
SHFEUploadFileName_SUFN_P = 'P'
#///^\d{4}_\d{8}_\d{8}_Capital
SHFEUploadFileName_SUFN_F = 'F'
#///^\d{4}_SG\d{1}_\d{8}_\d{1}_Trade
CFFEXUploadFileName_SUFN_T = 'T'
#///^\d{4}_SG\d{1}_\d{8}_\d{1}_SettlementDetail
CFFEXUploadFileName_SUFN_P = 'P'
#///^\d{4}_SG\d{1}_\d{8}_\d{1}_Capital
CFFEXUploadFileName_SUFN_F = 'F'
#///^\d{4}_SG\d{1}_\d{8}_\d{1}_OptionExec
CFFEXUploadFileName_SUFN_S = 'S'
#///申请组合
CombDirection_Comb = '0'
#///申请拆分
CombDirection_UnComb = '1'
#///实值额
StrikeOffsetType_RealValue = '1'
#///盈利额
StrikeOffsetType_ProfitValue = '2'
#///实值比例
StrikeOffsetType_RealRatio = '3'
#///盈利比例
StrikeOffsetType_ProfitRatio = '4'
#///等待处理中
ReserveOpenAccStas_Processing = '0'
#///已撤销
ReserveOpenAccStas_Cancelled = '1'
#///已开户
ReserveOpenAccStas_Opened = '2'
#///无效请求
ReserveOpenAccStas_Invalid = '3'
#///弱密码库
WeakPasswordSource_Lib = '1'
#///手工录入
WeakPasswordSource_Manual = '2'
#///自对冲期权仓位
OptSelfCloseFlag_CloseSelfOptionPosition = '1'
#///保留期权仓位
OptSelfCloseFlag_ReserveOptionPosition = '2'
#///自对冲卖方履约后的期货仓位
OptSelfCloseFlag_SellCloseSelfFuturePosition = '3'
#///保留卖方履约后的期货仓位
OptSelfCloseFlag_ReserveFuturePosition = '4'
#///期货
BizType_Future = '1'
#///证券
BizType_Stock = '2'
#///直连的投资者
AppType_TYPE_Investor = '1'
#///为每个投资者都创建连接的中继
AppType_TYPE_InvestorRelay = '2'
#///所有投资者共享一个操作员连接的中继
AppType_TYPE_OperatorRelay = '3'
#///未知
AppType_TYPE_UnKnown = '4'
#///检查成功
ResponseValue_Right = '0'
#///检查失败
ResponseValue_Refuse = '1'
#///大宗交易
OTCTradeType_TRDT_Block = '0'
#///期转现
OTCTradeType_TRDT_EFP = '1'
#///基点价值
MatchType_MT_DV01 = '1'
#///面值
MatchType_MT_ParValue = '2'
