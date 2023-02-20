# encoding:utf-8
# distutils: language=c++

from libc.string cimport const_char
from ctpwrapper.headers.DataCollect cimport CTP_GetSystemInfo, CTP_GetDataCollectApiVersion

def GetSystemInfo(char *pSystemInfo,int nLen):
    """
    :return:
    """
    cdef int result = CTP_GetSystemInfo(pSystemInfo, nLen)
    return result

def GetDataCollectApiVersion():
    cdef const_char *result
    with nogil:
        result = CTP_GetDataCollectApiVersion()
    return result


