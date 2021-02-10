import roslibpy
import docker

docClient = docker.DockerClient()
container = docClient.containers.get("ferko")
ip_add = container.attrs['NetworkSettings']['IPAddress']
print(ip_add)

ferko = roslibpy.Ros(host=ip_add, port=9090)
ferko.run()
print('Is ROS connected?', ferko.is_connected)
ferko.terminate()