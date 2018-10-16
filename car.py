#-*-coding:utf-8-*-
class Car():
    def __init__(self,carID,car_type,car_color,carID_color,car_logo):
        #carID车牌号，car_type车类型，car_color车颜色，carID_color车牌颜色，car_logo车品牌
        self.carID = carID
        self.car_type = car_type
        self.car_color = car_color
        self.carID_color = carID_color
        self.car_logo = car_logo
    def car_message(self):
        print(self.carID,self.car_type,self.car_color,self.carID_color,self.car_logo)