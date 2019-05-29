
cdef extern from "ThostFtdcTraderApi.h":
    int CTP_GetSystemInfo(char *pSystemInfo, int &nLen) nogil except +