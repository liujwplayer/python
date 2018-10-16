#-*-coding:utf-8-*-
import sys
import datetime
class StopPlace():  
    def __init__(self,id,car_id):
        self.id = id
        self.car_id = car_id
    def place_stop_time(self):
        self.place_stop_time = datetime.datetime.now()
        print("进入停车位，当前时间: " + str(self.place_stop_time))

    def place_go_time(self):
        self.place_go_time = datetime.datetime.now()
        print("离开停车位，当前时间: " + str(self.place_go_time))