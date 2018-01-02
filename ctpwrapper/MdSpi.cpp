#include <string.h>
#include "Python.h"

#include "wrapper_MdApi.h"
#include "MdApi.h"
using namespace std;

CMdSpi::CMdSpi(){
    Py_Initialize();
    PyInit_MdApi();
    //MdSpiWrapper *obj = buildMdSpiWrapper();
    // this->obj;//
    this->spi = buildMdSpiWrapper();
    std::cout << "spi init in cpp" << std::endl;

    /// https://github.com/shizhuolin/PyCTP/blob/master/src/MdApi.cpp#120
//    Py_Finalize();
}

CMdSpi::~CMdSpi(){
//this->spi->NULL;
Py_Finalize();
}

void CMdSpi::OnRspError(CThostFtdcRspInfoField *pRspInfo,
		int nRequestID, bool bIsLast)
{
    PyGILState_STATE gstate = PyGILState_Ensure();
    OnRspError(this->spi,&pRspInfo,nRequestID,bIsLast);
	cerr << "--->>> "<< __FUNCTION__ << endl;
	PyGILState_Release(gstate);
	//IsErrorRspInfo(pRspInfo);
}

void CMdSpi::OnFrontDisconnected(int nReason)
{
    PyGILState_STATE gstate = PyGILState_Ensure();
	cerr << "--->>> " << __FUNCTION__ << endl;
	cerr << "--->>> Reason = " << nReason << endl;
	OnFrontDisconnected(this->spi,nReason);
	PyGILState_Release(gstate);
}

void CMdSpi::OnHeartBeatWarning(int nTimeLapse)
{
    PyGILState_STATE gstate = PyGILState_Ensure();

	cerr << "--->>> " << __FUNCTION__ << endl;
	cerr << "--->>> nTimerLapse = " << nTimeLapse << endl;
	OnHeartBeatWarning(this->spi,nTimeLapse);
	PyGILState_Release(gstate);

}

void CMdSpi::OnFrontConnected()
{
    PyGILState_STATE gstate = PyGILState_Ensure();
    OnFrontConnected(this->spi);
	cerr << "--->>> " << __FUNCTION__ << endl;
	///用户登录请求
//	ReqUserLogin();
    PyGILState_Release(gstate);

}
