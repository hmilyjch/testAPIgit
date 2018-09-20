# -*- coding:utf-8 -*-
import json
import requests
from log import logger



# 添加一个数组，用来装测试结果
hlist = []
#公共的头文件设置
header = {
    "content-type": "application/json;charset=UTF-8"
}



def TestPostRequest(hurl, hdata, headers, htestcaseid, htestcasename, htesthope, fanhuitesthope):
    # hr = requests.post(hurl, data=json.dumps(hdata), headers=header)
    # hlist=[];
    hr = requests.post(hurl,data=hdata,headers=headers)
    hresult = json.loads(hr.text) # 获取并处理返回的json数据
    hstatus = str(hresult['status'])
    print(hstatus)
    if hstatus == htesthope and fanhuitesthope in str(hresult):
        hhhdata = {"t_id": htestcaseid,
                    "t_name": htestcasename,
                    "t_method": "POST",
                    "t_url": hurl,
                    "t_param": "测试数据:" + str(hdata),
                    "t_hope": "status:" + str(htesthope) + " 期望结果：" + fanhuitesthope,
                    "t_actual": "status:" + hstatus + ";实际返回结果:" + str(hresult),
                    "t_result": "通过"}
        hlist.append(hhhdata) # 把测试结果添加到数组里面
        logger.info("success")
        logger.info(htestcasename)
        logger.info(" 期望结果：" + fanhuitesthope)
    else:
        hhhdata = {"t_id": htestcaseid,
                    "t_name": htestcasename,
                    "t_method": "POST",
                    "t_url": hurl,
                    "t_param": "测试数据:" + str(hdata),
                    "t_hope": "status:" + str(htesthope) + " 期望结果：" + fanhuitesthope,
                    "t_actual": "status:" + hstatus + ";实际返回结果:" + str(hresult),
                    "t_result": "失败"}
        hlist.append(hhhdata)
        logger.error("success")
        logger.error(htestcasename)
        logger.error(" 期望结果：" + fanhuitesthope)
    # print(hlist)




def TestGetRequest(hurl, hdata, headers, htestcaseid, htestcasename, htesthope, fanhuitesthope,st):
    # hlist = [];
    if hdata=="":
        hr = requests.get(hurl,  headers=headers)
    else:
        hr = requests.get(hurl, params=hdata, headers=headers)

    hresult = json.loads(hr.text) # 获取并处理返回的json数据
    # hstatus = str(hresult['status'])
    hstatus = str(hresult[st])
    print("hstatus:"+hstatus)
    if hstatus == htesthope and fanhuitesthope in str(hresult):
        hhhdata = {"t_id": htestcaseid,
                    "t_name": htestcasename,
                    "t_method": "GET",
                    "t_url": hurl,
                    "t_param": "测试数据:" + str(hdata),
                    "t_hope": st+":" + str(htesthope) + " 期望结果：" + fanhuitesthope,
                    "t_actual": st+":" + hstatus + ";实际返回结果:" + str(hresult),
                    "t_result": "通过"}
        hlist.append(hhhdata) # 把测试结果添加到数组里面
        logger.info("success")
        logger.info(htestcasename)
        logger.info(" 期望结果：" + fanhuitesthope)
    else:
        hhhdata = {"t_id": htestcaseid,
                    "t_name": htestcasename,
                    "t_method": "GET",
                    "t_url": hurl,
                    "t_param": "测试数据:" + str(hdata),
                    "t_hope": st+":" + str(htesthope) + " 期望结果：" + fanhuitesthope,
                    "t_actual": st+":"  + hstatus + ";实际返回结果:" + str(hresult),
                    "t_result": "失败"}
        hlist.append(hhhdata)
        logger.error("success")
        logger.error(htestcasename)
        logger.error(" 期望结果：" + fanhuitesthope)
    # print(hlist)




def TestDeleteRequest(hurl, hdata, headers, htestcaseid, htestcasename, htesthope, fanhuitesthope):
    # hlist = [];
    # hr = requests.post(hurl, data=json.dumps(hdata), headers=header)
    hr = requests.delete(hurl, data=hdata, headers=headers)
    print(hr)
    hresult = json.loads(hr.text)  # 获取并处理返回的json数据
    print(hresult)
    hstatus = str(hresult['status'])
    print(hstatus)

    print(header)
    if hstatus == htesthope and fanhuitesthope in str(hresult):
        hhhdata = {"t_id": htestcaseid,
                   "t_name": htestcasename,
                   "t_method": "DELETE",
                   "t_url": hurl,
                   "t_param": "测试数据:" + str(hdata),
                   "t_hope": "status:" + str(htesthope) + " 期望结果：" + fanhuitesthope,
                   "t_actual": "status:" + hstatus + ";实际返回结果:" + str(hresult),
                   "t_result": "通过"}
        hlist.append(hhhdata)  # 把测试结果添加到数组里面
        logger.info("success")
        logger.info(htestcasename)
        logger.info(" 期望结果：" + fanhuitesthope)
    else:
        hhhdata = {"t_id": htestcaseid,
                   "t_name": htestcasename,
                   "t_method": "DELETE",
                   "t_url": hurl,
                   "t_param": "测试数据:" + str(hdata),
                   "t_hope": "status:" + str(htesthope) + " 期望结果：" + fanhuitesthope,
                   "t_actual": "status:" + hstatus + ";实际返回结果:" + str(hresult),
                   "t_result": "失败"}
        hlist.append(hhhdata)
        logger.error("success")
        logger.error(htestcasename)
        logger.error(" 期望结果：" + fanhuitesthope)
    # print(hlist)


