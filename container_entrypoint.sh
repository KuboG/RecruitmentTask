#!/bin/bash
source /ros_entrypoint.sh
source /opt/ros/melodic/setup.bash
roscore &
sleep 5
rosrun turtlesim turtlesim_node &
sleep 5
roslaunch rosbridge_server rosbridge_websocket.launch &
sleep 5
rosrun tf2_web_republisher tf2_web_republisher &
sleep 3
#python /home/catkin_ws/src/turtle_sim_move/src/moveWithTurtle.py
/bin/bash
