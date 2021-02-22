#!/bin/bash
# source to use ros commands
source /ros_entrypoint.sh
# source new package
source /home/catkin_ws/devel/setup.bash
# lauch all nodes in ros launch file
roslaunch turtle_line_cleaner ros_app.launch

