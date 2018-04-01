/*
(Copyright) 2018, Winton Wang <365504029@qq.com>

ctpwrapper is free software: you can redistribute it and/or modify
it under the terms of the GNU LGPLv3 as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with ctpwrapper.  If not, see <http://www.gnu.org/licenses/>.

*/

#ifndef CMDAPI_H
#define CMDAPI_H

#include "Python.h"
#include "pythread.h"
#include "ThostFtdcMdApi.h"


static inline int MdSpi_OnFrontConnected(PyObject *);
static inline int MdSpi_OnFrontDisconnected(PyObject *, int);
static inline int MdSpi_OnHeartBeatWarning(PyObject *, int);
static inline int MdSpi_OnRspUserLogin(PyObject *, CThostFtdcRspUserLoginField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRspUserLogout(PyObject *, CThostFtdcUserLogoutField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRspError(PyObject *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRspSubMarketData(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRspUnSubMarketData(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRspSubForQuoteRsp(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRspUnSubForQuoteRsp(PyObject *, CThostFtdcSpecificInstrumentField *, CThostFtdcRspInfoField *, int, bool);
static inline int MdSpi_OnRtnDepthMarketData(PyObject *, CThostFtdcDepthMarketDataField *);
static inline int MdSpi_OnRtnForQuoteRsp(PyObject *, CThostFtdcForQuoteRspField *);


#define Python_GIL(func) \
	do { \
		PyGILState_STATE gil_state = PyGILState_Ensure(); \
		if ((func) == -1) PyErr_Print();  \
		PyGILState_Release(gil_state); \
	} while (false)


class CMdSpi : public CThostFtdcMdSpi {
public:

    CMdSpi(PyObject *obj):self(obj) {};

	virtual ~CMdSpi() {};

	virtual void OnFrontConnected() {
		Python_GIL(MdSpi_OnFrontConnected(self));
	};

	virtual void OnFrontDisconnected(int nReason) {
		Python_GIL(MdSpi_OnFrontDisconnected(self, nReason));
	};

	virtual void OnHeartBeatWarning(int nTimeLapse) {
		Python_GIL(MdSpi_OnHeartBeatWarning(self, nTimeLapse));
	};

	virtual void OnRspUserLogin(CThostFtdcRspUserLoginField *pRspUserLogin, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		Python_GIL(MdSpi_OnRspUserLogin(self, pRspUserLogin, pRspInfo, nRequestID, bIsLast));
	};

	virtual void OnRspUserLogout(CThostFtdcUserLogoutField *pUserLogout, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		Python_GIL(MdSpi_OnRspUserLogout(self, pUserLogout, pRspInfo, nRequestID, bIsLast));
	};

	virtual void OnRspError(CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		Python_GIL(MdSpi_OnRspError(self, pRspInfo, nRequestID, bIsLast));
	};

	virtual void OnRspSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		Python_GIL(MdSpi_OnRspSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast));
	};

	virtual void OnRspUnSubMarketData(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		Python_GIL(MdSpi_OnRspUnSubMarketData(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast));
	};

	virtual void OnRspSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		Python_GIL(MdSpi_OnRspSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast));
	};

	virtual void OnRspUnSubForQuoteRsp(CThostFtdcSpecificInstrumentField *pSpecificInstrument, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {
		Python_GIL(MdSpi_OnRspUnSubForQuoteRsp(self, pSpecificInstrument, pRspInfo, nRequestID, bIsLast));
	};

	virtual void OnRtnDepthMarketData(CThostFtdcDepthMarketDataField *pDepthMarketData) {
		Python_GIL(MdSpi_OnRtnDepthMarketData(self, pDepthMarketData));
	};

	virtual void OnRtnForQuoteRsp(CThostFtdcForQuoteRspField *pForQuoteRsp) {
		Python_GIL(MdSpi_OnRtnForQuoteRsp(self, pForQuoteRsp));
	};

private:
	PyObject *self;
};

#endif /* CMDAPI_H */