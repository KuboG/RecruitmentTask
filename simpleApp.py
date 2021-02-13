from __future__ import print_function
import roslibpy
import docker
import time
from roslibpy import Topic, Message, Ros

from pynput.keyboard import Key, Listener
import os

class keyListener:
    count = None
    presedFlag = None

    def __init__(self):
        self.count = 0
        self.presedFlag = 0

        self.docClient = docker.DockerClient()
        self.container = self.docClient.containers.get("ferko")
        self.ip_add = self.container.attrs['NetworkSettings']['IPAddress']
        print(self.ip_add)
        print("wainting for container")

        self.client = roslibpy.Ros(host=self.ip_add, port=9090)
        self.velocity_publisher = roslibpy.Topic(self.client, '/turtle1/cmd_vel', 'geometry_msgs/Twist', queue_size=10)
        self.client.run()
        self.client.on_ready(lambda: print('Is ROS connected?', self.client.is_connected))

        with Listener(
                on_press=self.on_press,
                on_release=self.on_release) as self.listener:
            self.listener.join()
           

    def moveXpositive(self):
        print("publishing")
        self.velocity_publisher.publish(Message({ 'linear': { 'x': 1.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}  }))
        self.client.run()
        #time.sleep(1)

    def moveXnegative(self):
        print("publishing")
        self.velocity_publisher.publish(Message({ 'linear': { 'x': -1.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}  }))
        self.client.run()
        #time.sleep(1)
    
    def rotateZclockwise(self):
        print("publishing")
        self.velocity_publisher.publish(Message({ 'linear': { 'x': 0.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': -2.0}  }))
        self.client.run()
        #time.sleep(1)
    
    def rotateZcounterclockwise(self):
        print("publishing")
        self.velocity_publisher.publish(Message({ 'linear': { 'x': 0.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': 2.0}  }))
        self.client.run()

    def on_press(self, key):
        #clear = lambda: os.system('clear')
        #clear()
        if key == Key.up: # and self.presedFlag == 0:
            self.presedFlag = 1
            self.client.on_ready(self.moveXpositive, run_in_thread=True)

        if key == Key.down: # and self.presedFlag == 0:
            self.presedFlag = 1
            self.client.on_ready(self.moveXnegative, run_in_thread=True)

        if key == Key.right: # and self.presedFlag == 0:
            self.presedFlag = 1
            self.client.on_ready(self.rotateZclockwise, run_in_thread=True)

        if key == Key.left: # and self.presedFlag == 0:
            self.presedFlag = 1
            self.client.on_ready(self.rotateZcounterclockwise, run_in_thread=True)

    def on_release(self, key):
        self.presedFlag = 0
        if key == Key.esc:
            # stop listening and close rosbidge connection
            print(self.count)
            self.client.terminate()
            return False

keyListener()