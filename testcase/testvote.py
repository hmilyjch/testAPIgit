# -*- coding:utf-8 -*-

from TestRequest import TestPostRequest,TestGetRequest,TestDeleteRequest


testurl="http://127.0.0.1:8000"
def post_vote():
    try:
        hdata={
            "choice":"1"
        }
        header = {
            "content-type":"application/x-www-form-urlencoded"
        }
        print(header)
        testcaseid="1-1"
        testname="testvote"+testcaseid
        testhope="200"
        fanhuitesthope="success"
        r=TestPostRequest(testurl+"/polls/1/vote/",hdata,header,testcaseid,testname,testhope,fanhuitesthope)

    except Exception as e:
        print(e)
post_vote()

def get_polls():
    try:
        hdata=""
        header = {
            "content-type":"application/x-www-form-urlencoded"
        }
        testcaseid="1-2"
        testname="testvote"+testcaseid
        testhope="200"
        fanhuitesthope="success"
        r=TestGetRequest(testurl+"/polls/1/",hdata,header,testcaseid,testname,testhope,fanhuitesthope,'status')

    except Exception as e:
        print(e)


# get_polls()


def get_login():
    try:
        hdata={"key":"00d91e8e0cca2b76f515926a36db68f5",
               "phone":"13594347817",
                "passwd":"123654"}
        header = {
            "content-type":"application/json;charset=utf-8"
        }
        testcaseid="1-3"
        testname="testvote"+testcaseid
        testhope="202"
        fanhuitesthope="用户已注册"
        r=TestGetRequest("https://www.apiopen.top/createUser",hdata,header,testcaseid,testname,testhope,fanhuitesthope,'code')

    except Exception as e:
        print(e)

# get_login()


def delete_vote():
    try:
        hdata={
            "choice":"1"
        }
        header = {
            "content-type":"application/x-www-form-urlencoded"
        }
        testcaseid="1-1"
        testname="testvote"+testcaseid
        testhope="200"
        fanhuitesthope="success"
        r=TestDeleteRequest(testurl+"/polls/1/vote/",hdata,header,testcaseid,testname,testhope,fanhuitesthope)

    except Exception as e:
        print(e)
# delete_vote()