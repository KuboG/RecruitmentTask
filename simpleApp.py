from __future__ import print_function
import roslibpy
import docker
import time
from roslibpy import Topic, Message, Ros

docClient = docker.DockerClient()
container = docClient.containers.get("ferko")
ip_add = container.attrs['NetworkSettings']['IPAddress']
print(ip_add)
print("wainting for container")


def move():
    client = roslibpy.Ros(host=ip_add, port=9090)
    #client.run()
    velocity_publisher = roslibpy.Topic(client, '/turtle1/cmd_vel', 'geometry_msgs/Twist', queue_size=10)

    def pub():
        velocity_publisher.publish(Message({ 'linear': { 'x': 2.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': 1.0}  }))
        time.sleep(1)
 
    client.on_ready(lambda: print('Is ROS connected?', client.is_connected))
    #client.get_message_details('geometry_msgs/Twist', print)
    #client.get_topics(print)
    client.on_ready(pub, run_in_thread=True)

    velocity_publisher.unadvertise()
    #client.terminate()
    client.run_forever()

move()

'''

client = roslibpy.Ros(host=ip_add, port=9090)
client.run()

#velocity_publisher = roslibpy.Topic(client, '/turtle1/cmd_vel', 'geometry_msgs/Twist', queue_size=10)
listener = roslibpy.Topic(client, '/turtle1/pose', 'turtlesim/Pose')

#while client.is_connected:
#    velocity_publisher.publish(Message({'linear': [1.0, 0.0, 0.0], 'anglular': [1.0, 0.0, 0.0] }))
#    time.sleep(1)

#listener.subscribe(lambda message: print('toto:' + message['data'])) 
listener.subscribe(lambda message: print()) 
try:
    while True:
        pass
except KeyboardInterrupt:
    client.terminate()    
#client.get_message_details('geometry_msgs/Twist', print)
#velocity_publisher.unadvertise()
#client.terminate() 
'''