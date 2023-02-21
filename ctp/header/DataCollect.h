#ifndef  DATA_COLLECT_H
#define  DATA_COLLECT_H

#define DLL_EXPORT   __declspec(dllexport)

#if defined(IS_WINCOLLECT_LIB) && defined(WIN32)
#ifdef LIB_DATA_COLLECT_API_EXPORT
#define DATA_COLLECT_API_EXPORT __declspec(dllexport)
#else
#define DATA_COLLECT_API_EXPORT __declspec(dllimport)
#endif
#else
#define DATA_COLLECT_API_EXPORT 
#endif



///获取AES加密和RSA加密的终端信息 pSystemInfo的空间需要调用者自己分配 至少270个字节
/// windows返回值定义
/* 返回的int值 不为0 表示采集信息有误 具体哪个采集项有问题需要做如下判断
从低位开始分别标示 终端信息 ->系统盘分区信息
返回值 & （0x01 << 0） 不为0 表示终端类型未采集到
返回值 & （0x01 << 1） 不为0 表示 信息采集时间获取异常
返回值 & （0x01 << 2） 不为0 表示ip 获取失败  （采集多个相同类型信息的场景有一个采集到 即表示采集成功）
返回值 & （0x01 << 3） 不为0 表示mac 获取失败
返回值 & （0x01 << 4） 不为0 表示 设备名 获取失败
返回值 & （0x01 << 5） 不为0 表示 操作系统版本 获取失败
返回值 & （0x01 << 6） 不为0 表示 硬盘序列号 获取失败
返回值 & （0x01 << 7） 不为0 表示 CPU序列号 获取失败
返回值 & （0x01 << 8） 不为0 表示 BIOS 获取失败
返回值 & （0x01 << 9） 不为0 表示 系统盘分区信息 获取失败
*/

/// linux返回值定义
/* 返回的int值 不为0 表示采集信息有误 具体哪个采集项有问题需要做如下判断
从低位开始分别标示 终端信息 -> BIOS信息
返回值 & （0x01 << 0） 不为0 表示终端类型未采集到
返回值 & （0x01 << 1） 不为0 表示 信息采集时间获取异常
返回值 & （0x01 << 2） 不为0 表示ip 获取失败  （采集多个相同类型信息的场景有一个采集到 即表示采集成功）
返回值 & （0x01 << 3） 不为0 表示mac 获取失败
返回值 & （0x01 << 4） 不为0 表示 设备名 获取失败
返回值 & （0x01 << 5） 不为0 表示 操作系统版本 获取失败
返回值 & （0x01 << 6） 不为0 表示 硬盘序列号 获取失败
返回值 & （0x01 << 7） 不为0 表示 CPU序列号 获取失败
返回值 & （0x01 << 8） 不为0 表示 BIOS 获取失败
*/

DATA_COLLECT_API_EXPORT int CTP_GetSystemInfo(char* pSystemInfo, int& nLen);


//版本号格式
//Sfit + 生产还是测试秘钥(pro/tst) + 秘钥版本 + 编译时间 + 版本(内部)

DATA_COLLECT_API_EXPORT const char * CTP_GetDataCollectApiVersion(void);


#endif
