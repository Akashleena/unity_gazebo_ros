#!/bin/bash 
rosparam set ROS_IP 127.0.0.1
rosparam set ROS_TCP_PORT 55000
rosrun ros_tcp_endpoint default_server_endpoint.py


