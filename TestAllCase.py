# -*- coding:utf-8 -*-
# 导入测试用例
from testcase.testcase import *
def TestCase_Poll():
    post_vote()
    get_polls()
    get_questions()
    post_login()

def TestCase_API():
    get_login()
    get_novelSearchAPI()
    get_addStatisticsAPI()
    get_createUserKeyAPI()