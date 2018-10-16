#-*-coding:utf-8-*-
from  car import Car
from stop import Stop
from parking_record import ParkingRecord
from order import Order
class Driver():
    def __init__(self,id,name,phone_number,use_car):
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.use_car = use_car
    def driver_message(self):
        print(self.id,self.name,self.phone_number,self.use_car)
    def driver_car(self):
        print(self.name+'开着'+self.use_car+'车')
    def driver_shopping(self):
        print('购物中')
    def driver_shopped(self):
        print('购物完毕')