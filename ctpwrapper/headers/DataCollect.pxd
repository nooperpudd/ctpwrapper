
cdef extern from "DataCollect.h":
    int CTP_GetSystemInfo(char *pSystemInfo, int &nLen) nogil except +