#include "ros/ros.h"
#include "unity_robotics_demo_msgs/PosRot.h"


//std::vector<geometry_msgs::PoseStamped::ConstPtr> pose;

double x_current = 0;
double y_current = 0;
double z_current = 0;
double x_quat = 0;
double y_quat = 0;
double z_quat = 0;
double w_quat = 0;
double pos_x=0;
double pos_y=0;
double pos_z=0;
double rot_x=0;
double rot_y=0;
double rot_z=0;
double rot_w=0;
unity_robotics_demo_msgs::PosRot msg;

void poseCallback(const unity_robotics_demo_msgs::PosRot::ConstPtr & msg)
{
    ROS_INFO_STREAM("Received pose: " << msg);
    x_current = msg.pos_x;
    y_current = msg.pos_y;
    z_current = msg.pos_z;
    x_quat = msg.rot_x;
    y_quat = msg.rot_y;
    z_quat = msg.rot_z;
    w_quat = msg.rot_w;

    ROS_INFO_STREAM("Pose received \n");
        ROS_INFO_STREAM(x_current);
        ROS_INFO_STREAM(y_current);
        ROS_INFO_STREAM(z_current);
        ROS_INFO_STREAM(x_quat);
        ROS_INFO_STREAM(y_quat);
        ROS_INFO_STREAM(z_quat);
        ROS_INFO_STREAM(w_quat);
}

int main(int argc, char **argv)
{
 
  ros::init(argc, argv, "robo_simulation"); //node name

  
  ros::NodeHandle nh;

  ros::Subscriber endPose_sub = nh.subscribe("/pos_rot", 1000, poseCallback);

 
  ros::spin();

  return 0;
}
