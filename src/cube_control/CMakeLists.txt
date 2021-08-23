cmake_minimum_required(VERSION 3.0.2)
project(cube_control)

## Compile as C++11, supported in ROS Kinetic and newer
# add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages

find_package(catkin REQUIRED COMPONENTS
  controller_manager
  effort_controllers
  joint_state_controller
  robot_state_publisher
)
catkin_package()



