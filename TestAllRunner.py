# -*- coding:utf-8 -*-
import threading # 导入多线程库
from TestAllCase import *



def hthreads():
    threads = [] # 创建线程数组
    # 定义线程
    threads.append(threading.Thread(target=TestCase_Poll()))
    threads.append(threading.Thread(target=TestCase_API()))
    for h in threads:
        # 读取数组里的所有线程，并同时执行
        h.start() # 开始线程活动
    h.join() # 把主线程挂起，等待上面的线程跑完了再运行



