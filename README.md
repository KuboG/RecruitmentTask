# ROS docker application with a simple python application 
The main goal of this application is to demonstrate knowledge of new technologies such as [`docker`](https://www.docker.com/), [`ROS`](https://www.ros.org/), [`Python`](https://www.python.org/), and some of its libraries. In docker container runs [`turtlesim node`](http://wiki.ros.org/turtlesim), own clear [`service`](https://github.com/KuboG/RecruitmentTask/blob/master/clear_service.py), and [`rosbrigde`](https://roslibpy.readthedocs.io/en/latest/reference/index.html). On the host computer there run a [`python application`](https://github.com/KuboG/RecruitmentTask/blob/master/simple_app.py) that uses library [`roslibpy`](https://roslibpy.readthedocs.io/en/latest/index.html) to communicate with ros in a docker container and publishing on its topics. Communication is shown on the GUI application with the turtle where the python application moves with the turtle via arrow keys.

# Main features
* own image base on image `ros:melodic` defined in [dockerfile](https://github.com/KuboG/RecruitmentTask/blob/master/Dockerfile)
* [`turtlesim node`](http://wiki.ros.org/turtlesim) and [`clear service`](https://github.com/KuboG/RecruitmentTask/blob/master/clear_service.py) run in a container 
* turtlesim GUI shows communications with the [`python application`](https://github.com/KuboG/RecruitmentTask/blob/master/simple_app.py) running on the host computer
* [`python application`](https://github.com/KuboG/RecruitmentTask/blob/master/simple_app.py) is publishing on turtlesim topic and move with turtle via arrows keys
* the python application uses [`roslibpy`](https://roslibpy.readthedocs.io/en/latest/index.html) to communicate with ros in a container
* publishing to docker container via `rosbridge_websocket` and `tf2_web_republisher`
* cleaning trajectory line behind the turtle with [`clear service`](https://github.com/KuboG/RecruitmentTask/blob/master/clear_service.py)

![alt text](https://github.com/KuboG/RecruitmentTask/blob/develop_JG/Documentation/schematicpng.png?raw=true)

# Technologies
Project is created with:
* [`Ubuntu 18.04`](https://releases.ubuntu.com/18.04/) as an operations system
* [`Docker`](https://www.docker.com/) version: 20.10.2
* [`Python`](https://www.python.org/)  version: 2.7.17
* [`ros:melodic docker`](https://hub.docker.com/_/ros) 
* [`wait-for-it.sh`](https://github.com/vishnubob/wait-for-it)

## Installation
Please run the following commands to install all dependencies:

To install docker use this  [link](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04)

install python
```bash 
sudo apt-get install python
```
install python pip
``` bash
sudo apt-get install python-pip
```
install python dependencies (`docker`, `pynput`, `roslibpy`) [install_python_dependencies.sh](https://github.com/KuboG/RecruitmentTask/blob/master/install_python_dependencies.sh)
``` bash
bash install_python_dependencies.sh
```

# For developers
To continue developing this application, the following software packages and dependencies have to be installed. Please follow the steps in the [Installation](https://github.com/KuboG/RecruitmentTask/tree/develop_JG#installation) chapter. There are also some additional commands to prepare your system.

## System preparation
Use this command if you want to run docker commands without sudo: [setup_user_groups.sh](https://github.com/KuboG/RecruitmentTask/blob/master/set_user_group.sh)
``` bash
bash setup_user_groups.sh # this adds the currently logged user to the docker group
```
## Launching application
To launch the application use [launcher.sh](https://github.com/KuboG/RecruitmentTask/blob/master/launcher.sh):
``` bash
bash launcher.sh
```
When you want to run the whole application after some modifications you can also use that command.

The necessary processes inside the container such as `roscore`, `turtlesim`, `rosbridge_server`, `tf2_web_republisher`, and `clear_service` run in the [container_entrypoint.sh](https://github.com/KuboG/RecruitmentTask/blob/master/container_entrypoint.sh).

#### Documentation
You can find more technical details including commands in [dockerfile](https://github.com/KuboG/RecruitmentTask/blob/master/Dockerfile) or methods in [python application](https://github.com/KuboG/RecruitmentTask/blob/master/simple_app.py) in [technical documentation](https://github.com/KuboG/RecruitmentTask/blob/master/Documentation/technical_documentation.pdfs). 

# User manual
Please follow the steps in the [Installation](https://github.com/KuboG/RecruitmentTask/tree/develop_JG#installation) chapter. There are also some commands which have to be run to ensure the usage of the application. These are also mentioned in this section.

### Before the first launch
Before the first launch, run this command (it will ask your sudo password from you):
``` bash
bash setup_user_groups.sh # this adds the currently logged user to the docker group
```
To launch the application use:
``` bash
bash launcher.sh
```
#### Documentation
More pieces of information of the application you can find in [user manual](https://github.com/KuboG/RecruitmentTask/blob/master/Documentation/user_manual.pdf)







