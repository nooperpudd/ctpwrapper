# encoding:utf-8

from cpython cimport PyObject
from libc.string cimport const_char
from libcpp cimport bool as cbool
# from libcpp.memory cimport shared_ptr,make_shared

from ThostFtdcUserApiStruct cimport (CThostFtdcReqUserLoginField,
CThostFtdcUserLogoutField,
CThostFtdcFensUserInfoField)



cdef extern from 'ThostFtdcMdApi.h':

    # cdef cppclass CMdSpi "CThostFtdcMdSpi":
    #     # 当客户端与交易后台建立起通信连接时（还未登易后台通信连接断开时，该方法被调用。当发生这个情况后，API会自动重新连接，客户端可不做处理。
    #     # @param nReason 错误原因
    #     #  0x1001 网络读失败
    #     #  0x1002 网络写失败
    #     #  0x2001 接收心跳超时
    #     #  0x2002 发送心跳失败
    #     #  0x2003 收到错误报文
    #     void OnFrontDisconnected(int nReason) except +
    #
    #     # 心跳超时警告。当长时间未收到报文时，该方法被调用。
    #     # @param nTimeLapse 距离上次接收报文的时间
    #     void OnHeartBeatWarning(int nTimeLapse) except +
    #
    #     # 登录请求响应
    #     void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin,
    #                         CThostFtdcRspInfoField *pRspInfo,
    #                         int nRequestID,
    #                         cbool bIsLast) except +
    #
    #     # 登出请求响应
    #     void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout,
    #                          CThostFtdcRspInfoField *pRspInfo,
    #                          int nRequestID,
    #                          cbool bIsLast) except +
    #
    #     # 错误应答
    #     void OnRspError(CThostFtdcRspInfoField *pRspInfo,
    #                     int nRequestID,
    #                     cbool bIsLast) except +
    #
    #     # 订阅行情应答
    #     void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument,
    #                             CThostFtdcRspInfoField *pRspInfo,
    #                             int nRequestID,
    #                             cbool bIsLast) except +
    #
    #     # 取消订阅行情应答
    #     void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument,
    #                               CThostFtdcRspInfoField *pRspInfo,
    #                               int nRequestID,
    #                               cbool bIsLast) except +
    #
    #     # 深度行情通知
    #     void OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData) except +


    cdef cppclass CMdApi "CThostFtdcMdApi":

        @staticmethod
        const_char *GetApiVersion() nogil

        #  删除接口对象本身
        #  @remark 不再使用本接口对象时,调用该函数删除接口对象
        void Release() nogil

        #  初始化
        #  @remark 初始化运行环境,只有调用后,接口才开始工作
        void Init() nogil

        #  等待接口线程结束运行
        #  @return 线程退出代码
        int Join() nogil

        #  获取当前交易日
        #  @retrun 获取到的交易日
        #  @remark 只有登录成功后,才能得到正确的交易日
        const_char *GetTradingDay() nogil except +

        #  注册前置机网络地址
        #  @param pszFrontAddress：前置机网络地址。
        #  @remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:17001”。
        #  @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”17001”代表服务器端口号。
        void RegisterFront(char *pszFrontAddress) nogil except +

        #  注册名字服务器网络地址
        #  @param pszNsAddress：名字服务器网络地址。
        #  @remark 网络地址的格式为：“protocol://ipaddress:port”，如：”tcp://127.0.0.1:12001”。
        #  @remark “tcp”代表传输协议，“127.0.0.1”代表服务器地址。”12001”代表服务器端口号。
        #  @remark RegisterNameServer优先于RegisterFront
        void RegisterNameServer(char *pszNsAddress) nogil except +

        #  注册名字服务器用户信息
        #  @param pFensUserInfo：用户信息。
        void RegisterFensUserInfo(CThostFtdcFensUserInfoField *pFensUserInfo) nogil except +

        #  注册回调接口
        #  @param pSpi 派生自回调接口类的实例
        void RegisterSpi(CMdSpi *pSpi) nogil except +

        #  订阅行情。
        #  @param ppInstrumentID 合约ID
        #  @param nCount 要订阅/退订行情的合约个数
        int SubscribeMarketData(char *ppInstrumentID[],int nCount) nogil except +

        #  退订行情。
        #  @param ppInstrumentID 合约ID
        #  @param nCount 要订阅/退订行情的合约个数
        int UnSubscribeMarketData(char *ppInstrumentID[],int nCount) nogil except +
        
        #订阅询价。
        #@param ppInstrumentID 合约ID
        #@param nCount 要订阅/退订行情的合约个数
        int SubscribeForQuoteRsp(char *ppInstrumentID[],int nCount) nogil except +

        #退订询价。
        #@param ppInstrumentID 合约ID
        #@param nCount 要订阅/退订行情的合约个数
        int UnSubscribeForQuoteRsp(char *ppInstrumentID[],int nCount) nogil except +

        #  用户登录请求
        int ReqUserLogin(CThostFtdcReqUserLoginField *pReqUserLoginField,int nRequestID) nogil except +

        #  登出请求
        int ReqUserLogout(CThostFtdcUserLogoutField *pUserLogout,int nRequestID) nogil except +

cdef extern from 'ThostFtdcMdApi.h' namespace "CThostFtdcMdApi":
    #获取API的版本信息
    #@retrun 获取到的版本号
    CMdApi  *CreateFtdcMdApi(const_char *pszFlowPath, cbool bIsUsingUdp, cbool bIsMulticast) nogil except +


cdef extern from 'CMdAPI.h':

    cdef cppclass CMdSpi:
         CMdSpi(PyObject *obj)


