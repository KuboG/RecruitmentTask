from __future__ import print_function
import roslibpy
import docker
import time
from roslibpy import Topic, Message, Ros

from pynput.keyboard import Key, Listener
import os

# class keyListener
# providing connection to ros in container via roslibpy
# publishing on topic '/turtle1/cmd_vel' acording to arrows keys
# listening on press arrows key 
# listnening on release esc key
class KeyListener:
    count = None
    presedFlag = None

    def __init__(self):
        self.count = 0
        self.presedFlag = 0

        # get ip addres of container 'turtle_app_container'
        self.docClient = docker.DockerClient()
        self.container = self.docClient.containers.get("turtle_app_container")
        self.ip_add = self.container.attrs['NetworkSettings']['IPAddress']

        # connesct to container via ip address
        self.client = roslibpy.Ros(host=self.ip_add, port=9090)
        # create publisher 
        self.velocity_publisher = roslibpy.Topic(self.client, '/turtle1/cmd_vel', 'geometry_msgs/Twist', queue_size=10)
        # connect to the container 
        self.client.run()
        
        #basic intructions
        if self.client.is_connected:
            clear = lambda: os.system('clear')
            clear()
            print("You are connected")
            print("use arrows keys to move with turtle\nTo close application use ESC key")
            print("-------ready to go----------")
        
        # create Listener on events --- on_press, on_release
        with Listener(
                on_press=self.on_press,
                on_release=self.on_release) as self.listener:
            self.listener.join()     

    # moving with turtle in X axis in positive direction
    def moveXpositive(self):
        #if self.presedFlag == 0:
        print("moving in X axis positive direction")
        self.velocity_publisher.publish(Message({ 'linear': { 'x': 1.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}  }))
        self.client.run()
    
    # moving with turtle in X axis in negative direction
    def moveXnegative(self):
        print("moving in X axis negative direction")
        self.velocity_publisher.publish(Message({ 'linear': { 'x': -1.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': 0.0}  }))
        self.client.run()
    
    # rotate with turtle in Z axis in clockwise direction
    def rotateZclockwise(self):
        print("rotate in Z axis clockwise direction")
        self.velocity_publisher.publish(Message({ 'linear': { 'x': 0.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': -2.0}  }))
        self.client.run()

    # rotate with turtle in Z axis in counterclockwise direction    
    def rotateZcounterclockwise(self):
        print("rotate in Z axis counterclockwise direction")
        self.velocity_publisher.publish(Message({ 'linear': { 'x': 0.0, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': 2.0}  }))
        self.client.run()

    # determine which key is pressed
    def on_press(self, key):
        # clear console
        clear = lambda: os.system('clear')
        clear()
        if key == Key.up:
            self.presedFlag = 1
            # call moveXpositive in a thread
            self.client.on_ready(self.moveXpositive, run_in_thread=True)

        if key == Key.down:
            self.presedFlag = 1
            # call moveXnegative in a thread
            self.client.on_ready(self.moveXnegative, run_in_thread=True)

        if key == Key.right:
            self.presedFlag = 1
            # call rotateZclockwise in a thread
            self.client.on_ready(self.rotateZclockwise, run_in_thread=True)

        if key == Key.left:
            self.presedFlag = 1
            # call rotateZcounterclockwise in a thread
            self.client.on_ready(self.rotateZcounterclockwise, run_in_thread=True)

    def on_release(self, key):
        self.presedFlag = 0
        if key == Key.esc:
            # stop listening and close rosbidge connection
            self.client.terminate()
            return False

# call keyListener class
KeyListener()