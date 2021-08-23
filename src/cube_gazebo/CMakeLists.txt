cmake_minimum_required(VERSION 3.0.2)
project(cube_gazebo)

find_package(catkin REQUIRED COMPONENTS
  cube_description
  gazebo_msgs
  gazebo_plugins
  gazebo_ros
  gazebo_ros_control
)
catkin_package()
