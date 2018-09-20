# -*- coding:utf-8 -*-

import time
import xlsxwriter
import TestRequest
from testcase.testcase import *
from testdata.getpath import *
from TestAllRunner import hthreads
from initdata import init_data
from sendmail import MyMail
from log import *


init_data()

hthreads()

# post_vote()
# get_polls()
# get_questions()
# get_login()
# post_login()
# get_novelSearchAPI()
# get_addStatisticsAPI()
# get_createUserKeyAPI()


TestReport = TestRequest.hlist

hpassnum = 0

def get_format(wd,option={}):
    return wd.add_format(option)


def get_format_center(wd,num=1):
    return wd.add_format({'align':'center','valign':'vcenter','border':num})

def get_format_left(wd,num=1):
    return wd.add_format({'align':'left','valign':'vcenter','border':num})

def get_format_error(wd,num=1):
    return wd.add_format({'align':'left','valign':'vcenter','border':num,'fg_color':'red'})

def set_border_(wd,num=1):
    return wd.add_format({}).set_border(num)

def _write_center(worksheet,cl,data,wd):
    return worksheet.write(cl,data,get_format_left(wd))


def _write_left_error(worksheet,cl,data,wd):
    return worksheet.write(cl,data,get_format_error(wd))


now = time.strftime("%Y-%m-%d-%H-%M-%S-",time.localtime(time.time()))
timenow = time.strftime("%Y/%m/%d %H:%M",time.localtime(time.time()))
ReportPath = GetTestReport()
workbook = xlsxwriter.Workbook(ReportPath)
worksheet = workbook.add_worksheet("测试总结")
worksheet2 = workbook.add_worksheet("用例详情")

def pie(workbook,worksheet):
    chart1 = workbook.add_chart({'type':'pie'})
    chart1.add_series({
        'name':'接口测试统计',
        'categories':'=测试总结!$D$4:$D$5',
        'values':'=测试总结!$E$4:$E$5'
    })
    chart1.set_title({'name':'接口测试统计'})
    chart1.set_style(10)
    worksheet.insert_chart('A9',chart1,{'x_offset':25,'y_offset':10})


def init(worksheet):
    worksheet.set_column("A:A", 15)
    worksheet.set_column("B:B", 20)
    worksheet.set_column("C:C", 20)
    worksheet.set_column("D:D", 20)
    worksheet.set_column("E:E", 20)
    worksheet.set_column("F:F", 20)

    worksheet.set_row(1, 30)
    worksheet.set_row(2, 30)
    worksheet.set_row(3, 30)
    worksheet.set_row(4, 30)
    worksheet.set_row(5, 30)

    define_format_H1 = get_format(workbook, {'bold': True, 'font_size': 18})
    define_format_H2 = get_format(workbook, {'bold': True, 'font_size': 14})
    define_format_H1.set_border(1)

    define_format_H2.set_border(1)
    define_format_H1.set_align("center")
    define_format_H2.set_align("center")
    define_format_H2.set_bg_color("yellow")
    define_format_H2.set_color("red")

    worksheet.merge_range('A1:F1','接口自动化测试报告',define_format_H1)
    worksheet.merge_range('A2:F2','测试概括',define_format_H2)
    worksheet.merge_range('A3:A6','炼数成金',get_format_left(workbook))

    _write_center(worksheet, "B3", '项目名称', workbook)
    _write_center(worksheet, "B4", '接口版本', workbook)
    _write_center(worksheet, "B5", '脚本语言', workbook)
    _write_center(worksheet, "B6", '测试地址', workbook)

    data = {"test_name":"炼数成金项目接口","test_version":"v1.0.0",
            "test_pl":"Python3","test_net":testurl}

    _write_center(worksheet, "C3", data['test_name'], workbook)
    _write_center(worksheet, "C4", data['test_version'], workbook)
    _write_center(worksheet, "C5", data['test_pl'], workbook)
    _write_center(worksheet, "C6", data['test_net'], workbook)

    _write_center(worksheet, "D3", "测试用例总数", workbook)
    _write_center(worksheet, "D4", "测试用例通过数", workbook)
    _write_center(worksheet, "D5", "测试用例失败数", workbook)
    _write_center(worksheet, "D6", "测试日期", workbook)

    data1 = {"test_sum":len(TestReport),
             "test_success":hpassnum,
             "test_failed":len(TestReport)-hpassnum,
             "test_date":timenow}
    _write_center(worksheet, "E3", data1['test_sum'], workbook)
    _write_center(worksheet, "E4", data1['test_success'], workbook)
    _write_center(worksheet, "E5", data1['test_failed'], workbook)
    _write_center(worksheet, "E6", data1['test_date'], workbook)

    _write_center(worksheet, "F3", "测试用例通过率", workbook)

    worksheet.merge_range('F4:F6',str((round(hpassnum/len(TestReport),4))*100)+'%',get_format_left(workbook))

    pie(workbook,worksheet)




def test_detail(worksheet):
    worksheet.set_column("A:A", 8)
    worksheet.set_column("B:B", 30)
    worksheet.set_column("C:C", 10)
    worksheet.set_column("D:D", 30)
    worksheet.set_column("E:E", 30)
    worksheet.set_column("F:F", 30)
    worksheet.set_column("G:G", 30)
    worksheet.set_column("H:H", 10)


    for hrow in range(len(TestReport)+2):
        worksheet.set_row(hrow,25)

    worksheet.merge_range('A1:H1','测试详情',get_format(workbook,{'bold':True,
                                                              'font_size':18,
                                                              'align':'center',
                                                              'valign':'vcenter',
                                                              'bg_color':'yellow',
                                                              'font_color':'red'}))
    _write_center(worksheet, "A2", '用例ID', workbook)
    _write_center(worksheet, "B2", '接口名称', workbook)
    _write_center(worksheet, "C2", '接口协议', workbook)
    _write_center(worksheet, "D2", 'URL', workbook)
    _write_center(worksheet, "E2", '参数', workbook)
    _write_center(worksheet, "F2", '预期值', workbook)
    _write_center(worksheet, "G2", '实际值', workbook)
    _write_center(worksheet, "H2", '测试结果', workbook)

    data = {"info":TestReport}

    temp = len(TestReport)+ 2
    global hpassnum
    for item in data["info"]:
        if item["t_result"]=="通过":
            hpassnum+=1
            _write_center(worksheet, "H" + str(temp), item["t_result"], workbook)
        else:
            #能否把这里失败的背景修改为红色  get_format_error
            _write_left_error(worksheet, "H" + str(temp), item["t_result"], workbook)
            pass
        _write_center(worksheet, "A" + str(temp), item["t_id"], workbook)
        _write_center(worksheet, "B" + str(temp), item["t_name"], workbook)
        _write_center(worksheet, "C" + str(temp), item["t_method"], workbook)
        _write_center(worksheet, "D" + str(temp), item["t_url"], workbook)
        _write_center(worksheet, "E" + str(temp), item["t_param"], workbook)
        _write_center(worksheet, "F" + str(temp), item["t_hope"], workbook)
        _write_center(worksheet, "G" + str(temp), item["t_actual"], workbook)

        temp = temp - 1








        # _write_center(worksheet, "A" + str(temp), item["t_id"], workbook)
        # _write_center(worksheet, "B" + str(temp), item["t_name"], workbook)
        # _write_center(worksheet, "C" + str(temp), item["t_method"], workbook)
        # _write_center(worksheet, "D" + str(temp), item["t_url"], workbook)
        # _write_center(worksheet, "E" + str(temp), item["t_param"], workbook)
        # _write_center(worksheet, "F" + str(temp), item["t_hope"], workbook)
        # _write_center(worksheet, "G" + str(temp), item["t_actual"], workbook)
        # _write_center(worksheet, "H" + str(temp), item["t_result"], workbook)
        # temp = temp - 1


test_detail(worksheet2)
init(worksheet)
workbook.close()


msg = """
<table width = "800" border="0" cellspacing="0" cellpadding="4">
    <tr>
        <td  height="20" style="font-size:24px">接口自动化测试报告</td>
    </tr>
"""



try:
    logger.info ('生成测试报告成功')
    mymail = MyMail(GetTestConfig('mail.conf'))
    mymail.connect()
    mymail.login()
    mail_content = msg.format(len(TestReport), hpassnum, len(TestReport)-hpassnum, round(hpassnum/len(TestReport),2)*100, now)
    mail_title = '【接口自动化测试报告】'
    attachments = set([ReportPath])

    logger.info("发送测试报告....")
    mymail.send_mail(mail_title, mail_content, attachments)
except Exception as e:
    logger.error("邮件发送失败"+ str(e))
    mymail.quit()
else:
    mymail.quit()
