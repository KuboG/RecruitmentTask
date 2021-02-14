#!/bin/bash
# source to use ros commands
source /ros_entrypoint.sh
# source new package
source /home/catkin_ws/devel/setup.bash
# start roscore
roscore &
sleep 5
# start turtlesim node
rosrun turtlesim turtlesim_node &
sleep 5
# start rosbridge_server
roslaunch rosbridge_server rosbridge_websocket.launch &
sleep 5
# start tf2_web_republisher
rosrun tf2_web_republisher tf2_web_republisher &
sleep 3
# start turtle_line_cleaner node
rosrun turtle_line_cleaner clearService.py
/bin/bash
