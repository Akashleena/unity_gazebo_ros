cmake_minimum_required(VERSION 3.0.2)
project(robo_simulation)
find_package(gazebo REQUIRED)
include_directories(${GAZEBO_INCLUDE_DIRS})
link_directories(${GAZEBO_LIBRARY_DIRS})

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  unity_robotics_demo_msgs
  message_generation
  gazebo_msgs
  std_msgs
  
)
## System dependencies are found with CMake's conventions
find_package(Boost REQUIRED COMPONENTS system)

  #add_message_files(
   #FILES
   #PosRot.msg
   #UnityColor.msg
 #)


catkin_package(
  CATKIN_DEPENDS roscpp rospy message_runtime std_msgs
)
include_directories(
  include
  ${catkin_INCLUDE_DIRS}
  ${Boost_INCLUDE_DIRS}
)
add_library(GazeboPlugin SHARED ./src/GazeboPlugin.cpp)
target_link_libraries(GazeboPlugin ${GAZEBO_LIBRARIES})
list(APPEND CMAKE_CXX_FLAGS "${GAZEBO_CXX_FLAGS}")

#add_executable(unity_subscribe src/unity_subscribe.cpp)
#add_dependencies(unity_subscribe robo_simulation_generate_messages_cpp)
#target_link_libraries(unity_subscribe ${catkin_LIBRARIES})

add_executable(unity_subscribe src/unity_subscribe.cpp)
add_dependencies(unity_subscribe ${unity_subscribe_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
target_link_libraries(unity_subscribe
  ${catkin_LIBRARIES}
)

