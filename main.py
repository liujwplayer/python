#coding:utf-8
import park
import sys
import time

class Main(object):

    def main():
        parking = park.Park()
        while True:
            index = input("欢迎来到使用停车场系统：\n"
            + "-----------------------\n"
            + "键入对应数字执行操作：\n"
            + "【1】: 驶入停车场\n"
            + "【2】: 开始购物(目前设定购物5秒)\n"
            + "【3】: 驶入停车场，并缴费\n"
            + "【0】: 退出程序\n"
            + "-----------------------\n")
            if int(index) == 1:
                parking.start()
            elif int(index) == 2:
                parking.shopping()
                time.sleep(5)
            elif int(index) == 3:
                parking.end()
                parking.money()
            elif int(index) == 0:
                sys.exit(0)
            else:
                print("键入正确的功能数字！")
        
        
    if __name__ == '__main__':
        main()