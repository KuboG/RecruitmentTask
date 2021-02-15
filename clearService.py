#!/usr/bin/env python
import rospy
import std_srvs 
from std_srvs.srv import Empty

# connect to a service clear and type std_srvs.srv.Empty
clearLine = rospy.ServiceProxy('clear', std_srvs.srv.Empty)

# while rospy is not shutdown call service 'clear' 10 times per second
while not rospy.is_shutdown():
    try:
        resp = clearLine()
        rate = rospy.Rate(10)
    except:
        print("unsuccessful line cleaning")
