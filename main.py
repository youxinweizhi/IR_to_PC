#by:youxinweizhi
#precondition
#    usb to ttl module
#    IR decoding module
#wiring
#    ttl    IR
#    5V     5V
#    gnd    gnd
#   Tx      Rx
#   Rx      Tx
#
#
#main.py      后台程序
#config.conf  定义pc程序路径

import serial,os
import configparser

class IR_to_PC(object):
    def __init__(self,com,baudrate=9600):
        self.com=com
        self.baudrate=baudrate
        self.ser = serial.Serial(port=self.com,baudrate=self.baudrate)
        self.cf=configparser.ConfigParser()
        self.cf.read('./config.conf',encoding='utf-8')
        self.map={}
        self.map['69']='aj_1'
        self.map['70']='aj_2'
        self.map['71']='aj_3'
        self.map['68']='aj_4'
        self.map['64']='aj_5'
        self.map['67']='aj_6'
        self.map['7']='aj_7'
        self.map['21']='aj_8'
        self.map['9']='aj_9'
    def control(self):
        while 1:
            try:
                data=self.ser.read_all()
                if len(data)>0:
                    if data[0]==0 and data[1]==255:
                        key=self.map[str(data[2])]
                        program_path=r'"%s"'%self.cf.get('config',key)
                        os.system(program_path)
                        print('开始运行：%s'%program_path)
            except KeyError:
                pass

test=IR_to_PC('com3')
test.control()