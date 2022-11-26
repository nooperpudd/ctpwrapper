# CTP期货 API Python Wrapper 

[![Build Status](https://app.travis-ci.com/nooperpudd/ctpwrapper.svg?branch=master)](https://app.travis-ci.com/nooperpudd/ctpwrapper)
[![Build status](https://ci.appveyor.com/api/projects/status/gvvtcqsjo9nsw0ct/branch/master?svg=true)](https://ci.appveyor.com/project/nooperpudd/ctpwrapper)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9ed5d0e55ed84dfeba30a7630ab5c160)](https://www.codacy.com/app/nooperpudd/ctpwrapper?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=nooperpudd/ctpwrapper&amp;utm_campaign=Badge_Grade)
[![pypi](https://img.shields.io/pypi/v/ctpwrapper.svg)](https://pypi.python.org/pypi/ctpwrapper)
[![status](https://img.shields.io/pypi/status/ctpwrapper.svg)](https://pypi.python.org/pypi/ctpwrapper)
[![pyversion](https://img.shields.io/pypi/pyversions/ctpwrapper.svg)](https://pypi.python.org/pypi/ctpwrapper)
[![implementation](https://img.shields.io/pypi/implementation/ctpwrapper.svg)](https://pypi.python.org/pypi/ctpwrapper)
[![Downloads](https://pepy.tech/badge/ctpwrapper)](https://pepy.tech/project/ctpwrapper)

[CTP Website](http://www.sfit.com.cn/5_2_DocumentDown_1.htm)

Version: v6.6.9

Platform: Linux 64bit, Windows 64bit

Python Requirement: x86-64

**Especially Support PyPy3-3.6 Linux 64bit**

Inspire By lovelylain 

# Install

Before you install ctpwrapper package, you need to make sure you have 
already install cython package.

    >>>pip install cython --upgrade
    >>>pip install ctpwrapper --upgrade


# Donate [捐助]

  <img src="images/alipay.png" width="250" height="250"><img src="images/wechat.jpg" width="250" height="250">

## ⚠️⚠️ notice ⚠️⚠️
 sometimes quote the market futures data, but there is no trading data from the API stream,
 better just add `time.sleep(2)` func call after `Init()` method invoked, this could help to solve no data response issue.
 
## Demo
sample code  [samples](samples/)

## issues
 https://github.com/nooperpudd/ctpwrapper/issues/62
 this is a temporary solution for the UnicodeDecodeError issue.
 ```
  Traceback (most recent call last):
    File "ctpwrapper/TraderApi.pyx", line 1402, in ctpwrapper.TraderApi.TraderSpi_OnRspQrySettlementInfo
    File "/root/python/futures/trader_main.py", line 149, in OnRspQrySettlementInfo
      print(pSettlementInfo.Content)
    File "/root/python/futures/.venv/lib/python3.9/site-packages/ctpwrapper/base.py", line 28, in __getattribute__
      return value.decode("gbk")
  UnicodeDecodeError: 'gbk' codec can't decode byte 0xd2 in position 499: incomplete multibyte sequence
 ```
 ```python

error_message = ""

def OnRspQryTradingAccount(self, pTradingAccount, pRspInfo, nRequestID, bIsLast):
     print("OnRspQryTradingAccount")
     print("nRequestID:", nRequestID)
     print("bIsLast:", bIsLast)
     print("pRspInfo:", pRspInfo)
     print("pTradingAccount:", pTradingAccount)
     # need to check is last message from the server.
     global error_message
     if not bIsLast:
        error_message+=pRspInfo.ErrorMsg
     else:
        error_message+=pRspInfo.ErrorMsg
        if isinstance(error_message,bytes):
            error_message.decode("gbk")
 ```

# Documentation
  CTP documentation can be found in the [docs](doc/ctp/)

# Contact

If you have any question about the ctpwrapper API, contact 365504029@qq.com



 
