# encoding:utf-8
# cython: nonecheck=True
# cython: profile=False

from Cpython.mem cimport PyMem_Malloc, PyMem_Realloc, PyMem_Free
from libc.stdlib cimport atoi

from cMdAPI cimport CMdSpi

cdef class CThostFtdcMdSpi:
    cdef CMdSpi*  _this_Ftdc_Md_Spi

    def __cinit__(self):
        pass

    def __dealloc__(self):
        pass

    # cpdef on_front_connected(self, ) except? -1:
    #     pass
    #
    # cpdef on_front_disconnected(self, int reason) except? -1:
    #     pass
    #
    # cpdef on_heart_beat_warning(self, int time_lapse) except? -1:
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

