#ifndef CMDAPI_H
#define CMDAPI_H

#include "Python.h"
#include "pythread.h"
#include "ThostFtdcMdApi.h"


static inline void MdSpi_OnFrontConnected(PyObject *);
static inline void MdSpi_OnFrontDisconnected(PyObject *, int);
static inline void MdSpi_OnHeartBeatWarning(PyObject *, int);
static inline void MdSpi_OnRspUserLogin(PyObject *, CThostFtdcRspUserLoginField *, CThostFtdcRspInfoField *, int, bool);
static inline void MdSpi_OnRspUserLogout(PyObject *, CThostFtdcUserLogoutField *, CThostFtdcRspInfoField *, int, bool);
static inline void MdSpi_OnRspError(PyObject *, CThostFtdcRspInfoField *, int, bool);
static inline void MdSpi_OnRspSubMarketData(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline void MdSpi_OnRspUnSubMarketData(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline void MdSpi_OnRspSubForQuoteRsp(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline void MdSpi_OnRspUnSubForQuoteRsp(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline void MdSpi_OnRtnDepthMarketData(PyObject *, CThostFtdcDepthMarketDataField *);
static inline void MdSpi_OnRtnForQuoteRsp(PyObject *, CThostFtdcForQuoteRspField *);


#define Python_GIL(func) \
	do { \
		PyGILState_STATE g_state = PyGILState_Ensure(); \
		if ((func) == -1) PyErr_Print(); \
		PyGILState_Release(g_state); \
	} while (false)


class CMdSpi : public CThostFtdcMdSpi {
public:

    CMdSpi(PyObject *obj):self(obj) {}

	virtual ~CMdSpi() {}

	virtual void OnFrontConnected() {
		Python_GIL(MdSpi_OnFrontConnected(self));
	}

	virtual void OnFrontDisconnected(int nReason) {
		Python_GIL(MdSpi_OnFrontDisconnected(self, nReason));
	}

	virtual void OnHeartBeatWarning(int nTimeLapse) {
		Python_GIL(MdSpi_OnHeartBeatWarning(self, nTimeLapse));
	}

	virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		Python_GIL(MdSpi_OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		Python_GIL(MdSpi_OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		Python_GIL(MdSpi_OnRspError(self, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		Python_GIL(MdSpi_OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		Python_GIL(MdSpi_OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		Python_GIL(MdSpi_OnRspSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRspUnSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		Python_GIL(MdSpi_OnRspUnSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast));
	}

	virtual void OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData) {
		Python_GIL(MdSpi_OnRtnDepthMarketData(self, pDepthMarketData));
	}

	virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {
		Python_GIL(MdSpi_OnRtnForQuoteRsp(self, pForQuoteRsp));
	}

private:
	PyObject *self;
};

#endif /* CMDAPI_H */