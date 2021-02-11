from __future__ import print_function
import roslibpy
import docker

docClient = docker.DockerClient()
container = docClient.containers.get("ferko")
ip_add = container.attrs['NetworkSettings']['IPAddress']
print(ip_add)
print("wainting for container")

client = roslibpy.Ros(host=ip_add, port=9090)
client.on_ready(lambda: print('Is ROS connected?', client.is_connected))
client.run_forever()
print(get_topic_type(topic, callback=None, errback=None))