# building image
sudo docker build -t turtle-app .
# give permissions to X server host
xhost local:root
# run docker compose un background - detach
sudo docker-compose up -d
echo "Waiting for the container to launch properly"
# python application with roslibpy
./wait-for-it.sh 10.1.10.10:9090 -- python simple_app.py
# kill container
docker kill turtle_app_container
# remove container
docker rm turtle_app_container
# clear console
clear