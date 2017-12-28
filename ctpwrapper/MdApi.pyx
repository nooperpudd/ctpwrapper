# encoding:utf-8
# cython: nonecheck=True
# cython: profile=False

from cpython cimport PyObject_GetBuffer, PyBuffer_Release, PyBUF_SIMPLE, PyBytes_AsString
from cpython.mem cimport PyMem_Malloc, PyMem_Realloc, PyMem_Free
from libc.stdlib cimport malloc, free
from libc.string cimport const_char
from libcpp cimport bool

from headers.cMdAPI cimport CMdSpi,CMdApi,GetApiVersion,CreateFtdcMdApi

from headers.ThostFtdcUserApiStruct cimport (
CThostFtdcRspUserLoginField,
CThostFtdcRspInfoField,
CThostFtdcUserLogoutField,
CThostFtdcSpecificInstrumentField,
CThostFtdcDepthMarketDataField,
CThostFtdcFensUserInfoField,
CThostFtdcReqUserLoginField)

import ctypes

cdef class MdApiWrapper:
    cdef CMdApi *_api

    def __cinit__(self, const_char *pszFlowPath,
                  bool bIsUsingUdp,
                  bool bIsMulticast):

        self._api= CreateFtdcMdApi(pszFlowPath,bIsUsingUdp,bIsMulticast)
        if not self._api:
            raise MemoryError()

    def __dealloc__(self):

        if self._api is not NULL:
            self._api.Release()
            self._api= NULL

    def __init__(self,pszFlowPath, bIsUsingUdp, bIsMulticast):
        pass

    @classmethod
    def GetApiVersion(cls):
        return GetApiVersion()

    def ReqUserLogin(self, pReqUserLoginField, nRequestID):
        """
        用户登录请求
        :return:
        """
        self._api.ReqUserLogin(<CThostFtdcReqUserLoginField *><size_t>(ctypes.addressof(pReqUserLoginField)),nRequestID)


    def ReqUserLogout(self, pUserLogout, nRequestID):
        """
        登出请求
        :return:
        """
        self._api.ReqUserLogout(<CThostFtdcUserLogoutField *><size_t>(ctypes.addressof(pUserLogout)),nRequestID)


    def GetTradingDay(self):
        """
        获取当前交易日
        @retrun 获取到的交易日
        @remark 只有登录成功后,才能得到正确的交易日
        :return:
        """
        cdef const_char *result
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
        self._api.RegisterNameServer(pszFrontAddress)

    def RegisterNameServer(self,char *pszNsAddress):
        """
        注册名字服务器网络地址
        @param pszNsAddress：名字服务器网络地址。
        @remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:12001”。
        @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”12001”代表服务器端口号。
        @remark RegisterNameServer优先于RegisterFront
        :return:
        """
        self._api.RegisterNameServer(pszNsAddress)


    def RegisterFensUserInfo(self, pFensUserInfo):
        """
        注册名字服务器用户信息
        @param pFensUserInfo：用户信息。
        :return:
        """
        self._api.RegisterFensUserInfo(<CThostFtdcFensUserInfoField *><size_t>(ctypes.addressof(pFensUserInfo)))


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
        cdef int count
        cdef int result
        cdef char **InstrumentIDs

        count = len(pInstrumentID)
        InstrumentIDs = <char **>malloc(sizeof(char*) *count)

        try:
            for i from 0<= i <count:
                InstrumentIDs[i] = pInstrumentID[i]
            result = self._api.SubscribeMarketData(InstrumentIDs,count)
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
        cdef int count
        cdef int result
        cdef char **InstrumentIDs

        count = len(pInstrumentID)
        InstrumentIDs = <char **>malloc(sizeof(char*) *count)

        try:
            for i from 0<= i <count:
                InstrumentIDs[i] = pInstrumentID[i]
            result = self._api.UnSubscribeMarketData(InstrumentIDs,count)
        finally:
            free(InstrumentIDs)
        return result

    def SubscribeForQuoteRsp(self, pInstrumentID):
        """
        订阅询价。
        :param pInstrumentID: 合约ID list

        :return:
        """
        cdef int count
        cdef int result
        cdef char **InstrumentIDs
        count = len(pInstrumentID)
        InstrumentIDs = <char **>malloc(sizeof(char*) *count)

        try:
            for i from 0<= i <count:
                InstrumentIDs[i] = pInstrumentID[i]
            result = self._api.SubscribeForQuoteRsp(InstrumentIDs,count)
        finally:
            free(InstrumentIDs)
        return result

    def UnSubscribeForQuoteRsp(self, pInstrumentID):
        """
        退订询价。
        :param pInstrumentID: 合约ID list
        :return:
        """
        cdef int count
        cdef int result
        cdef char **InstrumentIDs

        count = len(pInstrumentID)
        InstrumentIDs = <char **>malloc(sizeof(char*) *count)
        try:
            for i from 0<= i <count:
                InstrumentIDs[i] = pInstrumentID[i]

            result = self._api.UnSubscribeForQuoteRsp(InstrumentIDs,count)
        finally:
            free(InstrumentIDs)
        return result





# cdef class CThostFtdcMdSpi:
#     cdef CMdSpi*  _this_Ftdc_Md_Spi
#
#     def __cinit__(self):
#         pass
#
#     def __dealloc__(self):
#         pass
#
#     def



    # cpdef on_front_connected(self, ) except? -1:
    #     pass
    #
    # cpdef on_front_disconnected(self, def reason) except? -1:
    #     pass
    #
    # cpdef on_heart_beat_warning(self, def time_lapse) except? -1:
    #     pass
    #
    # cpdef on_user_login(self,):
    #     pass

# cdef class CThostFtdcMdApi:
#     def __cinit__(self):
#         pass
#
#     def __dealloc__(self):
#         pass


