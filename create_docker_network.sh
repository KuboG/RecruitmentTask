# create docker network with name ros_network - used in docker-compose.yml
docker network create ros_network --subnet=10.1.10.10/24 --gateway=10.1.10.1