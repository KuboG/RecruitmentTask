From ros:melodic
#RUN apt-get update && apt-get install -y \
#    vim \
#    mc
#
RUN apt-get update \
    && apt-get install ros-melodic-turtlesim -y
#
RUN apt-get install -y ros-melodic-rosbridge-server \
    && apt-get install -y ros-melodic-tf2-web-republisher
#
RUN /bin/bash -c "source /ros_entrypoint.sh" \
    && mkdir -p /home/catkin_ws/src \ 
#
RUN cd /home/catkin_ws/src \
    && /bin/bash -c '. /opt/ros/melodic/setup.bash; catkin_init_workspace /home/catkin_ws/src'
#
RUN cd /home/catkin_ws \
    && /bin/bash -c '. /opt/ros/melodic/setup.bash; cd /home/catkin_ws; catkin_make' \
    && /bin/bash -c "source /home/catkin_ws/devel/setup.bash"
#
RUN cd /home/catkin_ws/src \
    && catkin_create_pkg turtle_line_cleaner geometry_msgs std_msgs std_srvs rospy \
    && cd /home/catkin_ws \
    && /bin/bash -c '. /opt/ros/melodic/setup.bash; catkin_make' \
    && mkdir -p /home/catkin_ws/src/turtle_line_cleaner/scripts
#
COPY /clearService.py /home/catkin_ws/src/turtle_line_cleaner/scripts/clearService.py
RUN chmod +x /home/catkin_ws/src/turtle_line_cleaner/scripts/clearService.py
#
RUN echo "catkin_install_python(PROGRAMS scripts/clearService.py\n\
  DESTINATION \${CATKIN_PACKAGE_BIN_DESTINATION}\n\
)" >> /home/catkin_ws/src/turtle_line_cleaner/CMakeLists.txt
#
RUN cd /home/catkin_ws \
    && /bin/bash -c '. /opt/ros/melodic/setup.bash; catkin_make'
#
COPY /container_entrypoint.sh /
RUN chmod +x /container_entrypoint.sh
#
ENTRYPOINT ["/container_entrypoint.sh"]