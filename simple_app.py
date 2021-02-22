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
    move_x = None
    rotate_z = None

    # constructor
    def __init__(self):        
        self.move_x = 0.0
        self.rotate_z = 0.0

        # connesct to container via ip address
        self.client = roslibpy.Ros(host="10.1.10.10", port=9090)
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
    def publishing_movement(self):
        self.velocity_publisher.publish(Message({ 'linear': { 'x': self.move_x, 'y': 0.0, 'z': 0.0}, 'angular': {'x': 0.0, 'y': 0.0, 'z': self.rotate_z}  }))
        self.client.run()

    # determine which key is pressed
    # sefl - object in class
    # key - store pressed kye
    def on_press(self, key):
        # clear console
        clear = lambda: os.system('clear')
        clear()
        if key == Key.up:
            self.move_x = 1.0
            self.rotate_z = 0.0
            print("moving in X axis positive direction")    
        elif key == Key.down:
            self.move_x = -1.0
            self.rotate_z = 0.0
            print("moving in X axis negative direction")
        elif key == Key.right:
            self.move_x= 0.0
            self.rotate_z = -2.0
            print("rotate in Z axis clockwise direction")
        elif key == Key.left:
            self.move_x = 0.0
            self.rotate_z = 2.0
            print("rotate in Z axis counterclockwise direction")
        elif key == Key.esc:
            print("closing")
        else:
            self.move_x = 0.0
            self.rotate_z = 0.0
            print("wrong key")
        self.client.on_ready(self.publishing_movement, run_in_thread=True)

    # determine which key is released
    # sefl - object in class
    # key - store pressed kye
    def on_release(self, key):
        if key == Key.esc:
            # stop listening and close rosbidge connection
            self.client.terminate()
            return False

# main function
def main():
    # call keyListener class
    KeyListener()

# call main function
if __name__ == "__main__":
    main()