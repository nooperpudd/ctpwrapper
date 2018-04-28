# encoding:utf-8
# distutils: language=c++

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
from cpython cimport PyObject
from libc.stdlib cimport malloc, free
from libc.string cimport const_char
from libcpp cimport bool as cbool

# from libcpp.memory cimport shared_ptr,make_shared

from .headers.cMdAPI cimport CMdSpi, CMdApi, CreateFtdcMdApi
from .headers.ThostFtdcUserApiStruct cimport (
CThostFtdcRspUserLoginField,
CThostFtdcRspInfoField,
CThostFtdcUserLogoutField,
CThostFtdcSpecificInstrumentField,
CThostFtdcDepthMarketDataField,
CThostFtdcFensUserInfoField,
CThostFtdcReqUserLoginField,
CThostFtdcForQuoteRspField
)

import ctypes

from . import ApiStructure


cdef class MdApiWrapper:
    cdef CMdApi *_api
    cdef CMdSpi *_spi

    def __cinit__(self):

        self._api = NULL
        self._spi = NULL

    def __dealloc__(self):
        self.Release()

    def Release(self):

        if self._api is not NULL:
            self._api.RegisterSpi(NULL)
            self._api.Release()
            self._api = NULL
            self._spi = NULL

    def Create(self, const_char *pszFlowPath, cbool bIsUsingUdp, cbool bIsMulticast):

        self._api = CreateFtdcMdApi(pszFlowPath, bIsUsingUdp, bIsMulticast)
        if not self._api:
            raise MemoryError()

    @staticmethod
    def GetApiVersion():
        return CMdApi.GetApiVersion()

    def Init(self):

        if self._api is not NULL:
            self._spi = new CMdSpi(<PyObject *> self)
            with nogil:
                self._api.RegisterSpi(self._spi)
                self._api.Init()

    def Join(self):

        cdef int result
        if self._spi is not NULL:
            with nogil:
                result = self._api.Join()
            return result

    def ReqUserLogin(self, pReqUserLoginField, nRequestID):
        """
        用户登录请求
        :return:
        """

        cdef int result
        if self._spi is not NULL:
            result = self._api.ReqUserLogin(<CThostFtdcReqUserLoginField *> <size_t> ctypes.addressof(pReqUserLoginField), nRequestID)
            return result

    def ReqUserLogout(self, pUserLogout, nRequestID):
        """
        登出请求
        :return:
        """
        cdef int result

        if self._spi is not NULL:
            result = self._api.ReqUserLogout(<CThostFtdcUserLogoutField *> <size_t> ctypes.addressof(pUserLogout), nRequestID)

            return result

    def GetTradingDay(self):
        """
        获取当前交易日
        @retrun 获取到的交易日
        @remark 只有登录成功后,才能得到正确的交易日
        :return:
        """
        cdef const_char *result

        if self._spi is not NULL:
            with nogil:
                result = self._api.GetTradingDay()
            return result

    def RegisterFront(self, char *pszFrontAddress):
        """
        注册前置机网络地址
        @param pszFrontAddress：前置机网络地址。
        @remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。
        @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
        :return:
        """
        if self._api is not NULL:
            with nogil:
                self._api.RegisterFront(pszFrontAddress)

    def RegisterNameServer(self, char *pszNsAddress):
        """
        注册名字服务器网络地址
        @param pszNsAddress：名字服务器网络地址。
        @remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:12001”。
        @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”12001”代表服务器端口号。
        @remark RegisterNameServer优先于RegisterFront
        :return:
        """
        if self._api is not NULL:
            with nogil:
                self._api.RegisterNameServer(pszNsAddress)

    def RegisterFensUserInfo(self, pFensUserInfo):
        """
        注册名字服务器用户信息
        @param pFensUserInfo：用户信息。
        :return:
        """
        if self._api is not NULL:
            self._api.RegisterFensUserInfo(<CThostFtdcFensUserInfoField *> <size_t> ctypes.addressof(pFensUserInfo))


    def SubscribeMarketData(self, pInstrumentID):
        """
         订阅行情。
        @param ppInstrumentID 合约ID
        @param nCount 要订阅/退订行情的合约个数

        #  https://www.quora.com/How-do-char-array-pointers-work-in-C++
        # http://docs.cython.org/en/latest/src/userguide/language_basics.html#integer-for-loops
        # https://stackoverflow.com/questions/15686890/how-to-allocate-array-of-pointers-for-strings-by-malloc-in-c

        :return:
        """
        cdef Py_ssize_t count
        cdef int result
        cdef char **InstrumentIDs

        if self._spi is not NULL:

            count = len(pInstrumentID)
            InstrumentIDs = <char **> malloc(sizeof(char*) * count)

            try:
                for i from 0 <= i < count:
                    InstrumentIDs[i] = pInstrumentID[i]
                with nogil:
                    result = self._api.SubscribeMarketData(InstrumentIDs, <int>count)
            finally:
                free(InstrumentIDs)
            return result

    def UnSubscribeMarketData(self, pInstrumentID):
        """
        退订行情。
        @param ppInstrumentID 合约ID
        @param nCount 要订阅/退订行情的合约个数
        :return:
        """
        cdef Py_ssize_t count
        cdef int result
        cdef char **InstrumentIDs

        if self._spi is not NULL:
            count = len(pInstrumentID)
            InstrumentIDs = <char **> malloc(sizeof(char*) * count)

            try:
                for i from 0 <= i < count:
                    InstrumentIDs[i] = pInstrumentID[i]
                with nogil:
                    result = self._api.UnSubscribeMarketData(InstrumentIDs, <int>count)
            finally:
                free(InstrumentIDs)
            return result

    def SubscribeForQuoteRsp(self, pInstrumentID):
        """
        订阅询价。
        :param pInstrumentID: 合约ID list
        :return:
        """
        cdef Py_ssize_t count
        cdef int result
        cdef char **InstrumentIDs

        if self._spi is not NULL:

            count = len(pInstrumentID)
            InstrumentIDs = <char **> malloc(sizeof(char*) * count)

            try:
                for i from 0 <= i < count:
                    InstrumentIDs[i] = pInstrumentID[i]
                with nogil:
                    result = self._api.SubscribeForQuoteRsp(InstrumentIDs, <int>count)
            finally:
                free(InstrumentIDs)
            return result

    def UnSubscribeForQuoteRsp(self, pInstrumentID):
        """
        退订询价。
        :param pInstrumentID: 合约ID list
        :return:
        """
        cdef Py_ssize_t count
        cdef int result
        cdef char **InstrumentIDs

        if self._spi is not NULL:

            count = len(pInstrumentID)
            InstrumentIDs = <char **> malloc(sizeof(char*) * count)
            try:
                for i from 0 <= i < count:
                    InstrumentIDs[i] = pInstrumentID[i]
                with nogil:
                    result = self._api.UnSubscribeForQuoteRsp(InstrumentIDs, <int>count)
            finally:
                free(InstrumentIDs)
            return result

cdef extern int MdSpi_OnFrontConnected(self) except -1:
    self.OnFrontConnected()
    return 0

cdef extern int MdSpi_OnFrontDisconnected(self, int nReason) except -1:
    self.OnFrontDisconnected(nReason)
    return 0

cdef extern int MdSpi_OnHeartBeatWarning(self, int nTimeLapse) except -1:
    self.OnHeartBeatWarning(nTimeLapse)
    return 0

cdef extern int MdSpi_OnRspUserLogin(self, CThostFtdcRspUserLoginField *pRspUserLogin,
                                     CThostFtdcRspInfoField *pRspInfo,
                                     int nRequestID,
                                     cbool bIsLast) except -1:
    if pRspUserLogin is NULL:
        user_login = None
    else:
        user_login = ApiStructure.RspUserLoginField.from_address(<size_t> pRspUserLogin)

    if pRspInfo is NULL:
        rsp_info = None
    else:
        rsp_info = ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)
    self.OnRspUserLogin(user_login, rsp_info, nRequestID, bIsLast)
    return 0

cdef extern int MdSpi_OnRspUserLogout(self, CThostFtdcUserLogoutField *pUserLogout,
                                      CThostFtdcRspInfoField *pRspInfo,
                                      int nRequestID,
                                      cbool bIsLast) except -1:
    if pUserLogout is NULL:
        user_logout = None
    else:
        user_logout = ApiStructure.UserLogoutField.from_address(<size_t> pUserLogout)
    if pRspInfo is NULL:
        rsp_info = None
    else:
        rsp_info = ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)

    self.OnRspUserLogout(user_logout, rsp_info, nRequestID, bIsLast)
    return 0

cdef extern int MdSpi_OnRspError(self, CThostFtdcRspInfoField *pRspInfo,
                                 int nRequestID,
                                 cbool bIsLast) except -1:
    if pRspInfo is NULL:
        rsp_info = None
    else:
        rsp_info = ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)
    self.OnRspError(rsp_info, nRequestID, bIsLast)
    return 0

cdef extern int MdSpi_OnRspSubMarketData(self, CThostFtdcSpecificInstrumentField *pSpecificInstrument,
                                         CThostFtdcRspInfoField *pRspInfo,
                                         int nRequestID,
                                         cbool bIsLast) except -1:
    if pSpecificInstrument is NULL:
        instrument = None
    else:
        instrument = ApiStructure.SpecificInstrumentField.from_address(<size_t> pSpecificInstrument)

    if pRspInfo is NULL:
        rsp_info = None
    else:
        rsp_info = ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)
    self.OnRspSubMarketData(instrument, rsp_info, nRequestID, bIsLast)
    return 0

cdef extern int MdSpi_OnRspUnSubMarketData(self, CThostFtdcSpecificInstrumentField *pSpecificInstrument,
                                           CThostFtdcRspInfoField *pRspInfo,
                                           int nRequestID,
                                           cbool bIsLast) except -1:
    if pSpecificInstrument is NULL:
        instrument = None
    else:
        instrument = ApiStructure.SpecificInstrumentField.from_address(<size_t> pSpecificInstrument)

    if pRspInfo is NULL:
        rsp_info = None
    else:
        rsp_info = ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)

    self.OnRspUnSubMarketData(instrument, rsp_info, nRequestID, bIsLast)
    return 0

cdef extern int MdSpi_OnRspSubForQuoteRsp(self,
                                          CThostFtdcSpecificInstrumentField *pSpecificInstrument,
                                          CThostFtdcRspInfoField *pRspInfo,
                                          int nRequestID,
                                          cbool bIsLast) except -1:
    if pSpecificInstrument is NULL:
        instrument = None
    else:
        instrument = ApiStructure.SpecificInstrumentField.from_address(<size_t> pSpecificInstrument)

    if pRspInfo is NULL:
        rsp_info = None
    else:
        rsp_info = ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)
    self.OnRspSubForQuoteRsp(instrument, rsp_info, nRequestID, bIsLast)
    return 0

cdef extern int MdSpi_OnRspUnSubForQuoteRsp(self, CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, cbool bIsLast) except -1:
    if pSpecificInstrument is NULL:
        instrument = None
    else:
        instrument = ApiStructure.SpecificInstrumentField.from_address(<size_t> pRspInfo)

    if pRspInfo is NULL:
        rsp_info = None
    else:
        rsp_info = ApiStructure.RspInfoField.from_address(<size_t> pRspInfo)
    self.OnRspUnSubForQuoteRsp(instrument, rsp_info, nRequestID, bIsLast)
    return 0

cdef extern int MdSpi_OnRtnDepthMarketData(self, CThostFtdcDepthMarketDataField *pDepthMarketData) except -1:
    if pDepthMarketData is NULL:
        depth_market = None
    else:
        depth_market = ApiStructure.DepthMarketDataField.from_address(<size_t> pDepthMarketData)
    self.OnRtnDepthMarketData(depth_market)
    return 0

cdef extern int MdSpi_OnRtnForQuoteRsp(self, CThostFtdcForQuoteRspField *pForQuoteRsp) except -1:
    if pForQuoteRsp is NULL:
        quote = None
    else:
        quote = ApiStructure.ForQuoteRspField.from_address(<size_t> pForQuoteRsp)

    self.OnRtnForQuoteRsp(quote)
    return 0
