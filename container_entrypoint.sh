#!/bin/bash
source /ros_entrypoint.sh
source /opt/ros/melodic/setup.bash
source /home/catkin_ws/devel/setup.bash
roscore &
sleep 5
rosrun turtlesim turtlesim_node &
sleep 5
roslaunch rosbridge_server rosbridge_websocket.launch &
sleep 5
rosrun tf2_web_republisher tf2_web_republisher &
sleep 3
rosrun turtle_line_cleaner clearService.py &
/bin/bash
