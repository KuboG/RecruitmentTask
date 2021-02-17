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
    moveX = None
    rotateZ = None

    # constructor
    def __init__(self):        
        self.moveX = 0.0
        self.rotateZ = 0.0

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

    # publishing on topic
    def publishingMovement(self):
        self.velocity_publisher.publish(Message({ 'linear': { 'x': self.moveX, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': self.rotateZ}  }))
        self.client.run()

    # determine which key is pressed
    # sefl - object in class
    # key - store pressed kye
    def on_press(self, key):
        # clear console
        clear = lambda: os.system('clear')
        clear()
        if key == Key.up:
            self.moveX = 1.0
            self.rotateZ = 0.0
            print("moving in X axis positive direction")    
        elif key == Key.down:
            self.moveX = -1.0
            self.rotateZ = 0.0
            print("moving in X axis negative direction")
        elif key == Key.right:
            self.moveX = 0.0
            self.rotateZ = -2.0
            print("rotate in Z axis clockwise direction")
        elif key == Key.left:
            self.moveX = 0.0
            self.rotateZ = 2.0
            print("rotate in Z axis counterclockwise direction")
        elif key == Key.esc:
            print("closing")
        else:
            self.moveX = 0.0
            self.rotateZ = 0.0
            print("wrong key")
        self.client.on_ready(self.publishingMovement, run_in_thread=True)

    # determine which key is released
    # sefl - object in class
    # key - store pressed kye
    def on_release(self, key):
        if key == Key.esc:
            # stop listening and close rosbidge connection
            self.client.terminate()
            return False

# call keyListener class
KeyListener()