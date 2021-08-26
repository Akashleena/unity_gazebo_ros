#include "ros/ros.h"
#include "unity_robotics_demo_msgs/PosRot.h"
#include<gazebo_msgs/ModelState.h>


//std::vector<geometry_msgs::PoseStamped::ConstPtr> pose;
class RoboSimulation
{
    public:
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
    
   RoboSimulation()
   {
   endPose_sub = nh.subscribe("/new_pos_rot", 50, &RoboSimulation::poseCallback,this);
   pose_pub = nh.advertise<gazebo_msgs::ModelState>("/gazebo/set_model_state", 50);
   ROS_INFO_STREAM("inside constructor \n");
   }

    private:

    ros::NodeHandle nh;
    ros::Publisher  pose_pub;
    ros::Subscriber endPose_sub;

    void poseCallback(const unity_robotics_demo_msgs::PosRot::ConstPtr & msg)
  {
    //unity_robotics_demo_msgs::PosRot msg;
    ROS_INFO_STREAM("Received pose: " << msg);
    x_current = msg->pos_x;
    y_current = msg->pos_y;
    z_current = msg->pos_z;
    x_quat = msg->rot_x;
    y_quat = msg->rot_y;
    z_quat = msg->rot_z;
    w_quat = msg->rot_w;

    ROS_INFO_STREAM("Pose received \n");
        ROS_INFO_STREAM(x_current);
        ROS_INFO_STREAM(y_current);
        ROS_INFO_STREAM(z_current);
        ROS_INFO_STREAM(x_quat);
        ROS_INFO_STREAM(y_quat);
        ROS_INFO_STREAM(z_quat);
        ROS_INFO_STREAM(w_quat);
  
      
      gazebo_msgs::ModelState ms;
      ms.model_name="robot";
      ms.reference_frame="world";
      ms.pose.position.x=x_current;
      ms.pose.position.y=y_current;
      ms.pose.position.z=z_current;
      ms.pose.orientation.x=x_quat;
      ms.pose.orientation.y=y_quat;
      ms.pose.orientation.z=z_quat;
      ms.pose.orientation.w=w_quat;
      ROS_INFO_STREAM("Publishing to gazebo \n");
      pose_pub.publish(ms);

  }
};

int main(int argc, char **argv)
{
 
  ros::init(argc, argv, "robo_simulation"); //node name
  
  ROS_INFO_STREAM("inside main \n");
  RoboSimulation rs;
  ros::Rate rate(10.0);
  ros::spin();
  rate.sleep();
  return 0;
}
