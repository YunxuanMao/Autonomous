#!/usr/bin/env python
'============== Subscriber for serial communication =================='
' Function: Get data from topic and send the data through serial port '
' Version: 1.0 '
' Author: Yunxuan '
' Date: 2020.3.21 ' 
'====================================================================='

import rospy
from std_msgs.msg import String
from serial_class import Ser
import time

xiaoxin = Ser(port_='/dev/ttyUSB0', timeout_=0)  # name of serial port

class Car:
    def __init__(self, sub_name, topic_name):
        self.data = ''
        self.sub_name = sub_name      # Name of the subscriber node
        self.topic_name = topic_name  # Name of the topic

    def callback(self, data):
        rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data) # Print the data
        self.data = data.data
        s = self.data
        xiaoxin.send_cmd(s.encode('utf-8'))  # Send message through serial port

    def listener(self):

        rospy.init_node(self.sub_name, anonymous=True)

        rospy.Subscriber(self.topic_name, String, callback)

        rospy.spin()


if __name__ == '__main__':
    a = Car('listener', '123')
    a.listener()
