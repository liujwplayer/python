#-*-coding:utf-8-*-
import sys
import datetime
class ParkingRecord():
    def __init__(self,id,car_id):
        self.id = id
        self.car_id = car_id

    def start(self):
        self.start = datetime.datetime.now()
        print("进入停车场，当前时间: " + str(self.start))
       
    def end(self):
        self.end = datetime.datetime.now()
        print("离开停车场，当前时间: " + str(self.end))

    def stop(self):
        time_difference = (self.end - self.start).seconds/60
        print("离开停车场，共用时: " + str(time_difference) + " 分钟")    