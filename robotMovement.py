#!/usr/bin/env python3
#Modified Given Code
import rospy
import socket
from std_msgs.msg import String 
from gazebo_msgs.srv import ApplyJointEffort
from gazebo_msgs.srv import GetJointProperties
from std_msgs.msg import Header

lastInput = None

def setRot(pub, val, direction):
    buff = ApplyJointEffort()
    buff.effort = val

    start_time = rospy.Time(0,0)
    end_time = rospy.Time(0.01,0)
    if direction == "l":
        buff.joint_name = "dd_robot::left_wheel_hinge"
        pub(buff.joint_name,  buff.effort, start_time, end_time)
    if direction == "l2":
        buff.joint_name = "dd_robot::left_wheel_hinge_2"
        pub(buff.joint_name,  buff.effort, start_time, end_time)
    if direction == "r":
        buff.joint_name = "dd_robot::right_wheel_hinge"
        pub(buff.joint_name, -buff.effort, start_time, end_time)
    if direction == "r2":
        buff.joint_name = "dd_robot::right_wheel_hinge_2"
        pub(buff.joint_name, -buff.effort, start_time, end_time)

def callback(msg): 

    global lastInput


    pub = rospy.ServiceProxy('/gazebo/apply_joint_effort',ApplyJointEffort)


    d = msg.data
    print(lastInput)

    
    lastInput = d

    if (d == "s"):
        #setRot(pub, 200, "r")
        #setRot(pub, -200, "l")
        setRot(pub, 300, "r2")
        setRot(pub, -300, "l2")
    elif (d == "w"):
        #setRot(pub, -200, "r")
        #setRot(pub, 200, "l")
        setRot(pub, -300, "r2")
        setRot(pub, 300, "l2")
        pass
    elif (d == "a"):
        setRot(pub, -550, "r")
        setRot(pub, -550, "l")
        #setRot(pub, -200, "r2")
        #setRot(pub, -200, "l2")
    elif (d == "d"):
        setRot(pub, 550, "r")
        setRot(pub, 550, "l")
        #setRot(pub, 200, "r2")
        #setRot(pub, 200, "l2")
    else:
        pass

    rate = rospy.Rate(10)
    rate.sleep()


rospy.init_node('dd_ctrl', anonymous=True)
sub = rospy.Subscriber('/key_press', String, callback)
rospy.spin()           