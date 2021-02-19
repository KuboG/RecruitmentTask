#!/bin/bash
# source to use ros commands
source /ros_entrypoint.sh
# source new package
source /home/catkin_ws/devel/setup.bash
# start roscore
roscore &
#start turtlesim node
./home/wait-for-it.sh localhost:11311 -- rosrun turtlesim turtlesim_node &
# start rosbridge_server
./home/wait-for-it.sh localhost:11311 -- roslaunch rosbridge_server rosbridge_websocket.launch &
# start tf2_web_republisher
./home/wait-for-it.sh localhost:11311 -- rosrun tf2_web_republisher tf2_web_republisher &
# start turtle_line_cleaner node
./home/wait-for-it.sh localhost:11311 -- rosrun turtle_line_cleaner clear_service.py &
/bin/bash
