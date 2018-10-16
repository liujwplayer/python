#-*-coding:utf-8-*-
class Order():
    def __init__(self,order_id,order_money,pay_way,pay_status,pay_time,pay_people,parking_record_id,order_status):
        self.order_id = order_id
        self.order_money = order_money
        self.pay_way = pay_way
        self.pay_status = pay_status
        self.pay_time = pay_time
        self.pay_people = pay_people
        self.parking_record_id = parking_record_id
        self.order_status = order_status
    def pay(self):
        print(self.order_id,self.order_money,self.pay_way,self.pay_status,self.pay_time,self.pay_people,self.parking_record_id,self.order_status)