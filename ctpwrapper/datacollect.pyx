from .headers.DataCollect cimport CTP_GetSystemInfo

def GetSystemInfo(char *pSystemInfo,int nLen):
    """
    :return:
    """
    cdef int result = CTP_GetSystemInfo(pSystemInfo, nLen)
    return result
