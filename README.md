# Unity-ROS-GAZEBO communication

## ROS Environment Setup

Use ROS Melodic or Noetic or you can use a docker from here. Download and copy the [ROS-TCP-Endpoint](https://github.com/Unity-Technologies/ROS-TCP-Endpoint) package into the src folder in your Catkin workspace. Then navigate to your Catkin workspace and run catkin_make, then source devel/setup.bash. Ensure there are no errors.

Additionally to build the backages you need to have [unity_robotics_demo_msgs](https://github.com/Unity-Technologies/Unity-Robotics-Hub/tree/main/tutorials/ros_unity_integration/ros_packages) package inside your src


## To use the simulation

In the first terminal start the ROS Master

```
roscore
```
In the second terminal do

```
source devel/setup.bash
./setTCPserver.sh
```
This will create the TCP connection with the Unity3D cube simulation

In the third terminal spawn the cube in the gazebo world

```
source devel/setup.bash
roslaunch cube_description gazebo.launch
```
In the fourth terminal start the ROS service client and the robo_simulation node that subcribes to unity /new_pos_rot topic and sends the pose to Gazebo cube model

```
rosrun robo_simulation unity_subscribe
```

