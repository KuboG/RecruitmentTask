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
    && catkin_create_pkg turtle_sim_move geometry_msgs rospy \
    && cd /home/catkin_ws \
    && /bin/bash -c '. /opt/ros/melodic/setup.bash; catkin_make'
    #&& cd ~/catkin_ws/src/turtle_sim_move \
    #&& mkdir src \
    #&& cd ~/catkin_ws \
    #&& /bin/bash -c '. /opt/ros/melodic/setup.bash; catkin_make'
#
COPY /moveWithTurtle.py /home/catkin_ws/src/turtle_sim_move/src
RUN chmod +x /home/catkin_ws/src/turtle_sim_move/src/moveWithTurtle.py
#
COPY /container_entrypoint.sh /
RUN chmod +x /container_entrypoint.sh
#
ENTRYPOINT ["/container_entrypoint.sh"]