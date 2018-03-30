# CTP期货 API Python Wrapper 

[![Build Status](https://travis-ci.org/nooperpudd/ctpwrapper.svg)](https://travis-ci.org/nooperpudd/ctpwrapper)
[![Build status](https://ci.appveyor.com/api/projects/status/gvvtcqsjo9nsw0ct?svg=true)](https://ci.appveyor.com/project/nooperpudd/ctpwrapper)

[![pypi](https://img.shields.io/pypi/v/ctpwrapper.svg)](https://pypi.python.org/pypi/ctpwrapper)
[![status](https://img.shields.io/pypi/status/ctpwrapper.svg)](https://pypi.python.org/pypi/ctpwrapper)
[![pyversion](https://img.shields.io/pypi/pyversions/ctpwrapper.svg)](https://pypi.python.org/pypi/ctpwrapper)


[CTP Website](http://www.sfit.com.cn/5_2_DocumentDown.htm)

Version: v6.3.6_20160606

Platform: Linux 64bit, Windows 64bit

Python Requirement: x86-64

Inspire By lovelylain 

# Install
   pip install ctpwrapper 

# Init Package

 MdApi Class Wrapper
 
    class Md(MdApiPy):
    """
    """
    def __init__(self, broker_id, investor_id, password, request_id=1):
        
        self.broker_id = broker_id
        self.investor_id = investor_id
        self.password = password
        self.request_id = request_id

    def OnRspError(self, pRspInfo, nRequestID, bIsLast):

        self.ErrorRspInfo(pRspInfo, nRequestID)

    def ErrorRspInfo(self, info, request_id):
        """
        :param info:
        :return:
        """
        if info.ErrorID != 0:
            print('request_id=%s ErrorID=%d, ErrorMsg=%s',
                  request_id, info.ErrorID, info.ErrorMsg.decode('gbk'))
        return info.ErrorID != 0

    def OnFrontConnected(self):
        """
        :return:
        """

        user_login = ApiStructure.ReqUserLoginField(BrokerID=self.broker_id,
                                                    UserID=self.investor_id,
                                                    Password=self.password)
        self.ReqUserLogin(user_login, self.request_id)

    def OnFrontDisconnected(self, nReason):
        
        print("Md OnFrontDisconnected %s", nReason)
        sys.exit()

    def OnHeartBeatWarning(self, nTimeLapse):
        """心跳超时警告。当长时间未收到报文时，该方法被调用。
        @param nTimeLapse 距离上次接收报文的时间
        """
        print('Md OnHeartBeatWarning, time = %s', nTimeLapse)

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):
        """
        用户登录应答
        :param pRspUserLogin:
        :param pRspInfo:
        :param nRequestID:
        :param bIsLast:
        :return:
        """
        if pRspInfo.ErrorID != 0:
            print("Md OnRspUserLogin failed error_id=%s msg:%s",
                  pRspInfo.ErrorID, pRspInfo.ErrorMsg.decode('gbk'))
        else:
            print("Md user login successfully")
            print(pRspUserLogin)
            print(pRspInfo)
    
    broker_id=""
    investor_id=""
    password=""
    server=""
    
    md = Md(broker_id,investor_id,password)
    md.Create()
    md.RegisterFront(server)
    md.Init()
    day = md.GetTradingDay()
    
    print(day)
    print("api worker!")
    

 
