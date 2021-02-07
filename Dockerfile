From ros:melodic
#RUN apt-get update && apt-get install -y \
#    vim \
#    mc

RUN /bin/bash -c "source /ros_entrypoint.sh" \
    && mkdir -p ~/catkin_ws/src \
#
RUN cd ~/catkin_ws/src \
    && /bin/bash -c '. /opt/ros/melodic/setup.bash; catkin_init_workspace ~/catkin_ws/src'
#
RUN cd ~/catkin_ws \
    && /bin/bash -c '. /opt/ros/melodic/setup.bash; cd ~/catkin_ws; catkin_make' \
    && /bin/bash -c "source ~/catkin_ws/devel/setup.bash"
    