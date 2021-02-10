#!/bin/bash
source /ros_entrypoint.sh
source /opt/ros/melodic/setup.bash
roslaunch rosbridge_server rosbridge_websocket.launch &
rosrun tf2_web_republisher tf2_web_republisher &
roscore &
rosrun turtlesim turtlesim_node &
/bin/bash
