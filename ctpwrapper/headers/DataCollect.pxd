# encoding:utf-8
# distutils: language=c++

from libc.string cimport const_char

cdef extern from "DataCollect.h":
    int CTP_GetSystemInfo(char *pSystemInfo, int &nLen) nogil except +
    const_char *CTP_GetDataCollectApiVersion(void) nogil except +
