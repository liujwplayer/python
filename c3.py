import time
import datetime
#创建停车场对象
class Park(object):
    pass
    
    def printo(self):
        self.start()
        print('开始计时')
        #当前线程休眠
        time.sleep(2)
        print('购物中')
        self.end()
        print('结束计时')
        print('输出计费单')
        self.money()
    #费用计算
    def money(self):
        time_difference = (self.end - self.start).seconds/60
        print('费用计算为：'+str(time_difference * 0.1))

    #开始的时间纳入
    def start(self):
        now_time = datetime.datetime.now()
        self.start = now_time
    #结束的时间纳入
    def end(self):
        now_time = datetime.datetime.now()
        self.end = now_time


park = Park()
park.printo()
   
