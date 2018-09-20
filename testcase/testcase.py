# -*- coding:utf-8 -*-
import xlrd
from TestRequest import TestPostRequest,TestGetRequest,TestDeleteRequest
from testdata.getpath import GetTestDataPath

testurl="http://127.0.0.1:8000"
def post_vote():
    Testdata = xlrd.open_workbook(GetTestDataPath())
    table = Testdata.sheets()[1]
    for i in range(3,5):
        choice = table.cell(i,0).value
        status = table.cell(i,1).value
        qiwang = table.cell(i,2).value
        try:
            hdata={
                "choice":choice
            }
            header = {
                "content-type":"application/x-www-form-urlencoded"
            }
            testcaseid="1-1"
            testname="testvote:"+testcaseid
            testhope=status
            fanhuitesthope=qiwang
            r=TestPostRequest(testurl+"/polls/1/vote/",hdata,header,testcaseid,testname,testhope,fanhuitesthope)

        except Exception as e:
            print(e)

# post_vote()


def get_polls():
    Testdata = xlrd.open_workbook(GetTestDataPath())
    table = Testdata.sheets()[1]
    for i in range(13,15):
        status = table.cell(i, 0).value
        qiwang = table.cell(i, 1).value
        try:
            hdata=""
            header = {
                "content-type":"application/x-www-form-urlencoded"
            }
            testcaseid="1-2"
            testname="test_getPolls:"+testcaseid
            testhope=status
            fanhuitesthope=qiwang
            r=TestGetRequest(testurl+"/polls/1/",hdata,header,testcaseid,testname,testhope,fanhuitesthope,'status')

        except Exception as e:
            print(e)

# get_polls()

def get_questions():
    try:
        hdata=""
        header = {
            "content-type":"application/x-www-form-urlencoded"
        }
        testcaseid="1-3"
        testname="testquestions:"+testcaseid
        testhope="200"
        fanhuitesthope="success"
        r=TestGetRequest(testurl+"/polls/",hdata,header,testcaseid,testname,testhope,fanhuitesthope,'status')

    except Exception as e:
        print(e)

# get_questions()

'''
用户登录接口
https://www.apiopen.top/login?key=00d91e8e0cca2b76f515926a36db68f5&phone=13594347817&passwd=123456
'''
def get_login():
    Testdata = xlrd.open_workbook(GetTestDataPath())
    table = Testdata.sheets()[2]      #sheet页从0开始
    for i in range(3,5):
        key = table.cell(i, 0).value
        phone = table.cell(i, 1).value
        pwd = table.cell(i, 2).value
        status = table.cell(i, 3).value
        qiwang = table.cell(i, 4).value
        try:
            hdata = {"key": key,
                     "phone": phone,
                     "passwd": pwd}
            header = {
                "content-type": "application/json;charset=utf-8"
            }
            testcaseid = "1-4"
            testname = "testvote" + testcaseid
            testhope = status
            fanhuitesthope = qiwang
            r = TestGetRequest("https://www.apiopen.top/login", hdata, header, testcaseid, testname, testhope,
                               fanhuitesthope, 'code')

        except Exception as e:
            print(e)

# get_login()


'''
自己开发的登录接口：
http://127.0.0.1:8000/polls/login/
POST
username,password
'''
def post_login():
    Testdata = xlrd.open_workbook(GetTestDataPath())
    table = Testdata.sheets()[3]
    for i in range(3,5):
        try:
            username = table.cell(i,0).value
            password = table.cell(i,1).value
            status = table.cell(i,2).value
            qiwang = table.cell(i,3).value
            hdata={
                "username":username,
                "password":password
            }
            header = {
                "content-type":"application/x-www-form-urlencoded"
            }
            testcaseid="1-5"
            testname="testvote:"+testcaseid
            testhope=status
            fanhuitesthope=qiwang
            r=TestPostRequest(testurl+"/polls/login/",hdata,header,testcaseid,testname,testhope,fanhuitesthope)

        except Exception as e:
            print(e)

# post_login()


'''
免费接口1：
小说搜索接口
https://www.apiopen.top/novelSearchApi?name=%E7%9B%97%E5%A2%93%E7%AC%94%E8%AE%B0
'''

def get_novelSearchAPI():
    Testdata = xlrd.open_workbook(GetTestDataPath())
    table = Testdata.sheets()[2]      #sheet页从0开始
    for i in range(13,15):
        name = table.cell(i, 0).value
        status = table.cell(i, 1).value
        qiwang = table.cell(i, 2).value
        try:
            hdata = {"name": name}
            header = {
                "content-type": "application/json;charset=utf-8"
            }
            testcaseid = "1-6"
            testname = "test_get_novelSearchAPI" + testcaseid
            testhope = status
            fanhuitesthope = qiwang
            r = TestGetRequest("https://www.apiopen.top/novelSearchApi", hdata, header, testcaseid, testname, testhope,
                               fanhuitesthope, 'code')

        except Exception as e:
            print(e)


# get_novelSearchAPI()


'''
免费接口2：
增加统计信息接口
https://www.apiopen.top/addStatistics?appKey=00d91e8e0cca2b76f515926a36db68f5&type=点击统计&typeId=1&count=2
'''

def get_addStatisticsAPI():
    Testdata = xlrd.open_workbook(GetTestDataPath())
    table = Testdata.sheets()[2]      #sheet页从0开始
    for i in range(21,24):
        appKey = table.cell(i, 0).value
        type = table.cell(i, 1).value
        typeID = table.cell(i, 2).value
        count = table.cell(i, 3).value
        status = table.cell(i, 4).value
        qiwang = table.cell(i, 5).value
        try:
            hdata = {"appKey": appKey,  "type":type, "typeId":typeID, "count":count}
            header = {
                "content-type": "application/json;charset=utf-8"
            }
            testcaseid = "1-7"
            testname = "test_get_addStatisticsAPI" + testcaseid
            testhope = status
            fanhuitesthope = qiwang
            r = TestGetRequest("https://www.apiopen.top/addStatistics", hdata, header, testcaseid, testname, testhope,
                               fanhuitesthope, 'code')

        except Exception as e:
            print(e)


# get_addStatisticsAPI()


'''
免费接口3：
创建应用接口
https://www.apiopen.top/createUserKey?appId=com.chat.peakchao&passwd=123456
'''


def get_createUserKeyAPI():
    Testdata = xlrd.open_workbook(GetTestDataPath())
    table = Testdata.sheets()[2]      #sheet页从0开始
    for i in range(31,33):
        appId = table.cell(i, 0).value
        passwd = table.cell(i, 1).value
        status = table.cell(i, 2).value
        qiwang = table.cell(i, 3).value
        try:
            hdata = {"appId": appId,  "passwd":passwd}
            header = {
                "content-type": "application/json;charset=utf-8"
            }
            testcaseid = "1-8"
            testname = "test_get_createUserKeyAPI" + testcaseid
            testhope = status
            fanhuitesthope = qiwang
            r = TestGetRequest("https://www.apiopen.top/createUserKey", hdata, header, testcaseid, testname, testhope,
                               fanhuitesthope, 'code')

        except Exception as e:
            print(e)

# get_createUserKeyAPI()




