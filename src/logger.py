#!/usr/bin/env python3

import rospy
#from rosplane_msgs.msg import State
#from rosplane_msgs.msg import Controller_Commands
#from rosflight_msgs.msg import Command
#from sensor_msgs.msg import Imu
#from rosflight_msgs.msg import OutputRaw
from unity_robotics_demo_msgs import PosRot.msg
from gazebo_msgs import ModelStates.msg
from csv import writer
import os
import numpy as np
import argparse

log_list = []
flag = 0  # to collect the data in order
file_name = "./src/system_id_python/log_data/state_data_log.csv"


def logger():
    
    rospy.init_node('listener', anonymous=True)
    r = rospy.Rate(10) 
    rospy.loginfo('subscribing to /fixedwing/imu/data')
    rospy.loginfo('subscribing to /fixedwing/truth')
    rospy.loginfo('subscribing to /fixedwing/output_raw')
    # rospy.Subscriber('/fixedwing/imu/data', Imu, callback_imu)
    # rospy.Subscriber('/fixedwing/truth', State, callback_state) 
    # rospy.Subscriber('/fixedwing/output_raw', OutputRaw, callback_servo) 

    rospy.Subscriber('/pos_rot', State, callback_unity_state)
    rospy.Subscriber('/new_pos_rot', State, callback_unity_state)
    #rospy.Subscriber('/new_pos_rot', Controller_Commands, callback_ctrl_cmd)
    #rospy.Subscriber('/fixedwing/mavros_commands', Command, callback_px4_ctrl_cmd)
    #rospy.Subscriber('/fixedwing/mavros_truth', State, callback_px4_state)
    
    r.sleep()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

def callback_imu(data):
    global log_list
    global flag
    if flag == 0:
        # log_list.append([data.header.stamp.secs, data.header.stamp.nsecs, data.quat[0], data.quat[1], data.q, data.theta, 'Flag']) 
        log_list.append([data.header.stamp.secs, data.header.stamp.nsecs, data.linear_acceleration.x, data.linear_acceleration.z])
        flag = 1
           
      
def callback_state(data):
    global log_list
    global flag
    if log_list and flag == 1:
        log_list[-1] = log_list[-1] + [data.header.stamp.secs, data.header.stamp.nsecs, data.quat[0], data.quat[2], data.q, data.theta]
        flag = 2
 

def callback_servo(data):
    global log_list
    global flag

    if log_list and flag == 2:
        with open(file_name, 'a+', newline='') as f:
            writer_object = writer(f)
            
            log_list[-1] = log_list[-1] + [rospy.Time.now().secs, rospy.Time.now().nsecs, data.values[1], data.values[2]]

            writer_object.writerow(log_list[-1])
            log_list = []
            flag = 0

def callback_unity_state(data):
    global log_list
    global flag

    if flag == 0:
        log_list.append([data.header.stamp.secs, data.header.stamp.nsecs, data.position[0],
                                                                                        data.position[1],
                                                                                        data.position[2],
                                                                                        data.Va,
                                                                                        data.alpha,
                                                                                        data.beta,
                                                                                        data.phi,
                                                                                        data.theta,
                                                                                        data.psi,
                                                                                        data.chi,
                                                                                        data.p,
                                                                                        data.q,
                                                                                        data.r,
                                                                                        data.Vg,
                                                                                        data.wn,
                                                                                        data.we,
                                                                                        data.quat[0],
                                                                                        data.quat[1],
                                                                                        data.quat[2],
                                                                                        data.quat[3],
                                                                                        data.quat_valid,
                                                                                        data.chi_deg,
                                                                                        data.psi_deg,
                                                                                        data.initial_lat,
                                                                                        data.initial_lon,
                                                                                        data.initial_alt])
        flag = 1

def callback_ctrl_cmd(data):
    global log_list
    global flag
    

    if log_list and flag == 1:
        
            
        log_list[-1] = log_list[-1] + [rospy.Time.now().secs, rospy.Time.now().nsecs, data.Va_c,
                                                                                    data.h_c,
                                                                                    data.chi_c,
                                                                                    data.phi_ff,
                                                                                    data.aux[0],
                                                                                    data.aux[1],
                                                                                    data.aux[2],
                                                                                    data.aux[3],
                                                                                    data.aux_valid]

        flag = 2

def callback_px4_ctrl_cmd(data):
    global log_list
    global flag
    

    if log_list and flag == 2:
       
            
        log_list[-1] = log_list[-1]+[rospy.Time.now().secs, rospy.Time.now().nsecs, data.x*180/np.pi,
                                                                                    data.y*180/np.pi,
                                                                                    data.z*180/np.pi,
                                                                                    data.F]
        flag = 3


        

def callback_px4_state(data):
    global log_list
    global flag

    if log_list and flag == 3:
        # print('2')
        with open(file_name, 'a+', newline='') as f:
            writer_object = writer(f)
            
            log_list[-1] = log_list[-1] + [rospy.Time.now().secs, rospy.Time.now().nsecs,data.position[0],
                                                                                        data.position[1],
                                                                                        data.position[2],
                                                                                        data.Va,
                                                                                        data.alpha,
                                                                                        data.beta,
                                                                                        data.phi*180/np.pi,
                                                                                        data.theta*180/np.pi,
                                                                                        data.psi*180/np.pi,
                                                                                        data.chi*180/np.pi,
                                                                                        data.p,
                                                                                        data.q,
                                                                                        data.r,
                                                                                        data.Vg,
                                                                                        data.wn,
                                                                                        data.we,
                                                                                        data.quat[0],
                                                                                        data.quat[1],
                                                                                        data.quat[2],
                                                                                        data.quat[3],
                                                                                        data.quat_valid,
                                                                                        data.chi_deg,
                                                                                        data.psi_deg,
                                                                                        data.initial_lat,
                                                                                        data.initial_lon,
                                                                                        data.initial_alt]

            writer_object.writerow(log_list[-1])
            log_list = []
            flag = 0

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description='Process some integers.')
        parser.add_argument('-csv_output', type=str, help='path of csv for input for simulation',
                             default='./src/system_id_python/log_data/state_data_log.csv')
        args = parser.parse_args()

        file_name = args.csv_output
        if os.path.exists(file_name):
            os.remove(file_name)
        logger()
    except rospy.ROSInterruptException:
        pass

