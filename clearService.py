#!/usr/bin/env python
import rospy
import std_srvs 
from std_srvs.srv import Empty

clearLine = rospy.ServiceProxy('clear', std_srvs.srv.Empty)

while not rospy.is_shutdown():
    try:
        resp = clearLine()
        rate = rospy.Rate(10)
    except:
        print("unsuccessful line cleaning")
