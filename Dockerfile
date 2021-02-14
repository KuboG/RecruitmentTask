From ros:melodic
#
# update packages and install vim and mc
RUN apt-get update && apt-get install -y \
    vim \
    mc
#
# update packages and install turtlesim 
RUN apt-get install ros-melodic-turtlesim -y
#
# instal rosbridge server and tf2 web republisher -> necessary for roslibpy
RUN apt-get install -y ros-melodic-rosbridge-server \
    && apt-get install -y ros-melodic-tf2-web-republisher
#
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
# copy python script clearService.py to container and make it executable
COPY /clearService.py /home/catkin_ws/src/turtle_line_cleaner/scripts/clearService.py
RUN chmod +x /home/catkin_ws/src/turtle_line_cleaner/scripts/clearService.py
#
# appending these lines to CMakeList.txt to instal and use it properly
RUN echo "catkin_install_python(PROGRAMS scripts/clearService.py\n\
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