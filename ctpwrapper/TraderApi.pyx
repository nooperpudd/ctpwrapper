from cpython.mem cimport PyMem_Malloc, PyMem_Realloc, PyMem_Free
from libc cimport stdlib

from headers.cTraderApi cimport CTraderSpi,CTraderApi

class TraderApiWrapper:
    def __cinit__(self):
        pass

    def __dealloc__(self):
        pass

  