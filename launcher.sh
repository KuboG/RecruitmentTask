# building image
docker build -t turtle-app .
# give permissions to X server host
xhost local:root
# run image turttle-app in docker with name 'turtle_app_container'
# eviroment variable: "DISPLAY", "QT_X11_NO_MITSHM=1"
# shared volume: "/tmp/.X11-unix:/tmp/.X11-unix:rw"
docker run -id --name turtle_app_container --env="DISPLAY" --env="QT_X11_NO_MITSHM=1" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" turtle-app
echo "Waiting for the container to launch properly"
# wait for all process to run in cointainer (roscore, turtle_sim node, rosbridge_server, tf2_web_republisher and turtle_line_cleaner)
sleep 20
# python application with roslibpy
python simpleApp.py
# kill container
docker kill turtle_app_container
# remove container
docker rm turtle_app_container
# clear console
clear
