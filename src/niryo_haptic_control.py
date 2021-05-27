#!/usr/bin/env python

import rospy,sys
import time
# Lib
import actionlib
# Action
from niryo_one_msgs.msg import RobotMoveAction
from niryo_one_msgs.msg import RobotMoveActionGoal
from niryo_one_msgs.msg import RobotMoveActionResult
from niryo_one_msgs.msg import RobotMoveCommand
from niryo_one_msgs.msg import ToolCommand
from geomagic_control.msg import PhantomButtonEvent
# Messages
from geometry_msgs.msg import Point
from niryo_one_msgs.msg import RPY
from niryo_one_msgs.msg import TrajectoryPlan
# Services
from niryo_one_msgs.srv import SetInt
from niryo_one_api import *
n = NiryoOne()
#n.calibrate_auto()
n.activate_learning_mode(False)
n.change_tool(TOOL_GRIPPER_2_ID)
#n.open_gripper(TOOL_GRIPPER_2_ID,500)
#n.close_gripper(TOOL_GRIPPER_2_ID,500)

def Call():    
    rospy.init_node('Joint_controller', anonymous=True)
    rospy.Subscriber('/Geomagic1/joint_states', JointState, Phantom, queue_size=1)
    rospy.Subscriber("/joint_states",JointState, main, queue_size=1)		
    rospy.Subscriber('/Geomagic1/button', PhantomButtonEvent, omni_white_cb, queue_size=1)
    rospy.spin()

#Phantom state
def Phantom (state):
    global sub
    sub = state.position
    #print (sub)
    
#Gripper control
def omni_white_cb (omni_msg):
    global whitebutton, greybutton
    whitebutton = omni_msg.white_button
    greybutton = omni_msg.grey_button  

#Niryo arm Control
def main(data):
    niryo_status = data
    pose_current = niryo_status.position
    traj=n.get_joints()
    rate = rospy.Rate(100)
    
    while not rospy.is_shutdown():
        Q0 = [sub[0]*2.5, sub[1]/2, sub[2]+0.36,-sub[3]+1.9, -sub[4]-2, -sub[5]/3]
        n.move_joints(Q0)
        if greybutton:
            n.open_gripper(TOOL_GRIPPER_2_ID,500)
        elif whitebutton:
            n.close_gripper(TOOL_GRIPPER_2_ID,500)
    #rospy.loginfo(traj)
    #rospy.loginfo(data)
        rate.sleep()


if __name__ == '__main__':
    try:
        Call()
        #Phantom
    except rospy.ROSInterruptException:
        print ("Program interrupted before completion")