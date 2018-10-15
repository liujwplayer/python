#coding:utf-8
import sys
import datetime

class Park(object):
    pass

    def money(self):
        print(type(self.end))
        print(type(self.start))
        time_difference = (self.end - self.start).seconds/60
        print("离开停车场，共用时: " + str(time_difference) + " 分钟")
        print("缴纳停车费用 " + str(time_difference * 0.1) + " 元")

    def start(self):
        self.start = datetime.datetime.now()
        print("进入停车场，当前时间: " + str(self.start))
        
    def end(self):
        self.end = datetime.datetime.now()
        print("购物结束离开停车场，当前时间: " + str(self.end))
    
    def shopping(self):
        print("购物ing...")

