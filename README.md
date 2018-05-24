# CTP期货 API Python Wrapper 

[![Build Status](https://travis-ci.org/nooperpudd/ctpwrapper.svg?branch=master)](https://travis-ci.org/nooperpudd/ctpwrapper)
[![Build status](https://ci.appveyor.com/api/projects/status/gvvtcqsjo9nsw0ct/branch/master?svg=true)](https://ci.appveyor.com/project/nooperpudd/ctpwrapper)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9ed5d0e55ed84dfeba30a7630ab5c160)](https://www.codacy.com/app/nooperpudd/ctpwrapper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=nooperpudd/ctpwrapper&amp;utm_campaign=Badge_Grade)
[![pypi](https://img.shields.io/pypi/v/ctpwrapper.svg)](https://pypi.python.org/pypi/ctpwrapper)
[![status](https://img.shields.io/pypi/status/ctpwrapper.svg)](https://pypi.python.org/pypi/ctpwrapper)
[![pyversion](https://img.shields.io/pypi/pyversions/ctpwrapper.svg)](https://pypi.python.org/pypi/ctpwrapper)
[![implementation](https://img.shields.io/pypi/implementation/ctpwrapper.svg)](https://pypi.python.org/pypi/ctpwrapper)

[CTP Website](http://www.sfit.com.cn/5_2_DocumentDown.htm)

Version: v6.3.11_20180109

Platform: Linux 64bit, Windows 64bit

Python Requirement: x86-64

**Especially Support PyPy3-v5.10.1-3.5.3 Linux 64bit**

Inspire By lovelylain 

# Install

Before you install ctpwrapper package, you need to make sure you have 
already install cython package.

    >>>pip install cython --upgrade
    >>>pip install ctpwrapper --upgrade


# Donate [捐助]

  <img src="images/alipay.jpg" width="250" height="250"><img src="images/wechat.jpg" width="250" height="250">


# Usage

 MdApi Class Wrapper
    
```python
import sys

from ctpwrapper import ApiStructure
from ctpwrapper import MdApiPy


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


BORDKER_ID = ""
INVESTOR_ID = ""
PASSWORD = ""
SERVER = ""

md = Md(BORDKER_ID, INVESTOR_ID, PASSWORD)
md.Create()
md.RegisterFront(SERVER)
md.Init()
day = md.GetTradingDay()

print(day)
print("api worker!")
```

Trader Class Wrapper

```python

from ctpwrapper import ApiStructure
from ctpwrapper import TraderApiPy

class Trader(TraderApiPy):

    def __init__(self, broker_id, investor_id, password, request_id=1):
        self.request_id = request_id
        self.broker_id = broker_id.encode()
        self.investor_id = investor_id.encode()
        self.password = password.encode()

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

    def OnHeartBeatWarning(self, nTimeLapse):
        """心跳超时警告。当长时间未收到报文时，该方法被调用。
        @param nTimeLapse 距离上次接收报文的时间
        """
        print("on OnHeartBeatWarning time: ", nTimeLapse)

    def OnFrontDisconnected(self, nReason):
        print("on FrontDisConnected disconnected", nReason)

    def OnFrontConnected(self):

        req = ApiStructure.ReqUserLoginField(BrokerID=self.broker_id,
                                             UserID=self.investor_id,
                                             Password=self.password)
        self.ReqUserLogin(req, self.request_id)
        print("trader on front connection")

    def OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast):

        if pRspInfo.ErrorID != 0:
            print("Md OnRspUserLogin failed error_id=%s msg:%s",
                  pRspInfo.ErrorID, pRspInfo.ErrorMsg.decode('gbk'))
        else:
            print("Md user login successfully")

            inv = ApiStructure.QryInvestorField(BrokerID=self.broker_id, InvestorID=self.investor_id)

            self.ReqQryInvestor(inv, self.inc_request_id())
            req = ApiStructure.SettlementInfoConfirmField.from_dict({"BrokerID": self.broker_id,
                                                                     "InvestorID": self.investor_id})

            self.ReqSettlementInfoConfirm(req, self.inc_request_id())

    def OnRspSettlementInfoConfirm(self, pSettlementInfoConfirm, pRspInfo, nRequestID, bIsLast):
        print(pSettlementInfoConfirm, pRspInfo)
        print(pRspInfo.ErrorMsg.decode("GBK"))

    def inc_request_id(self):
        self.request_id += 1
        return self.request_id

    def OnRspQryInvestor(self, pInvestor, pRspInfo, nRequestID, bIsLast):
        print(pInvestor, pRspInfo)

if __name__ == "__main__":
    investor_id = ""
    broker_id = ""
    password = ""
    server = ""

    user_trader = Trader(broker_id=broker_id, investor_id=investor_id, password=password)

    user_trader.Create()
    user_trader.RegisterFront(server)
    user_trader.SubscribePrivateTopic(2) # 只传送登录后的流内容
    user_trader.SubscribePrivateTopic(2) # 只传送登录后的流内容

    user_trader.Init()

    print("trader started")
    print(user_trader.GetTradingDay())

    user_trader.Join()

```

# Documentation
  CTP's documentation can be found in the [docs](doc/ctp/)



# Contact

If you have any question about the ctpwrapper API, contact 365504029@qq.com



 
