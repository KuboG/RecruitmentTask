From ros:melodic
#
# update packages and install vim and mc
# install ros-melodic-turtlesim
# instal rosbridge server and tf2 web republisher -> necessary for roslibpy
# clean up apt cache with last command - reduce image size
RUN apt-get update && apt-get install -y \
    vim \
    mc \
    ros-melodic-turtlesim \
    ros-melodic-rosbridge-server \
    ros-melodic-tf2-web-republisher \
    && rm -rf /var/lib/apt/lists/* 

# sourcing entrypoint to use ros commands and making directory for workspace
RUN /bin/bash -c "source /ros_entrypoint.sh" \
    && mkdir -p /home/catkin_ws/src \ 
#
# init workspace
RUN cd /home/catkin_ws/src \
    && /bin/bash -c '. /opt/ros/melodic/setup.bash; catkin_init_workspace /home/catkin_ws/src'
#
# building workspace
RUN cd /home/catkin_ws \
    && /bin/bash -c '. /opt/ros/melodic/setup.bash; cd /home/catkin_ws; catkin_make' \
    && /bin/bash -c "source /home/catkin_ws/devel/setup.bash"
#
# creating and building package in created workspace, making new folder 'scripts'
RUN cd /home/catkin_ws/src \
    && catkin_create_pkg turtle_line_cleaner geometry_msgs std_msgs std_srvs rospy \
    && cd /home/catkin_ws \
    && /bin/bash -c '. /opt/ros/melodic/setup.bash; catkin_make' \
    && mkdir -p /home/catkin_ws/src/turtle_line_cleaner/scripts
#
# copy python script clear_service.py to container and make it executable
COPY /clear_service.py /home/catkin_ws/src/turtle_line_cleaner/scripts/clear_service.py
RUN chmod +x /home/catkin_ws/src/turtle_line_cleaner/scripts/clear_service.py
#
# copy scripts wait-for-it.sh and make it executable
COPY /wait-for-it.sh /home
RUN chmod +x /home/wait-for-it.sh
#
# copy roslauch file and make in executable
COPY /ros_app.launch /home/catkin_ws/src/turtle_line_cleaner/ros_app.launch
RUN chmod +x /home/catkin_ws/src/turtle_line_cleaner/ros_app.launch
#
# appending these lines to CMakeList.txt to instal and use scripts properly
RUN echo "catkin_install_python(PROGRAMS scripts/clear_service.py\n\
  DESTINATION \${CATKIN_PACKAGE_BIN_DESTINATION}\n\
)" >> /home/catkin_ws/src/turtle_line_cleaner/CMakeLists.txt
#
# building node
RUN cd /home/catkin_ws \
    && /bin/bash -c '. /opt/ros/melodic/setup.bash; catkin_make'
#
# copy container_entrypoint to container and make it executable
COPY /container_entrypoint.sh /
RUN chmod +x /container_entrypoint.sh
#
# set container_entrypoint as entrypoint
ENTRYPOINT ["/container_entrypoint.sh"]
