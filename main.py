#-*-coding:utf-8-*-
from driver import Driver
from car import Car
from stop import Stop
from parking_record import ParkingRecord
from order import Order
from stop_place import StopPlace
import datetime
import time

car1 = Car('辽A666','小型轿车','白色','车牌为蓝色','福特—福睿斯')
driver1 =  Driver('9527','鸡小萌','1381111111',car1.car_logo)
parkingrecord1 = ParkingRecord('9527','辽A666')
stopplace1 = StopPlace('9527','辽A666')
order = Order('1','50','支付宝','未支付','鸡小萌','福特—福睿斯','',"未完成")

car1.car_message()
driver1.driver_car()
parkingrecord1.start()
stopplace1.place_stop_time()
driver1.driver_shopping()
time.sleep(5)
driver1.driver_shopped()
stopplace1.place_go_time()
parkingrecord1.end()
order.pay()
