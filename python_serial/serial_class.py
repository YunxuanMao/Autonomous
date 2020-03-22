'================= Serial Class ================='
' Version: 1 '
' Author: Amo '
'================================================'

''' 
# bytes object
b = b"example"
 
# str object
s = "example"
# str to bytes
bytes(s, encoding = "utf8")
# bytes to str
str(b, encoding = "utf-8")
# an alternative method
# str to bytes
str.encode(s)
# bytes to str'
bytes.decode(b)
'''

# coding:utf-8
import serial

class Ser(object):
    def __init__(self, port_ = 'COM10', baudrate_ = 115200, timeout_ = 0):
        # 打开端口
        self.port = serial.Serial(port=port_, baudrate=baudrate_, bytesize=8, parity=serial.PARITY_NONE, stopbits=1, timeout=timeout_)

    # 发送指令的完整流程
    def send_cmd(self, cmd):
        self.port.write(cmd)

    def read_cmd(self, size_= 1):
        response = self.port.read(size = size_)
        return response