#!/usr/bin/env python3

import math
from spatialmath.base import *
from spatialmath import SE3
import spatialmath.base.symbolic as sym
import numpy as np
import roboticstoolbox as rtb
import rospy
from std_msgs.msg import Float32MultiArray


class inversepose:

    def __init__(self):
        rospy.init_node('inversepose', anonymous=True)

        #Publishing data of joint rotations and positions

        self.inverse_joint_pub = rospy.Publisher('arm_joint_position', Float32MultiArray, queue_size=10)

        # Subscribing the x, y, z values from the image vectors

        rospy.Subscriber("/robotic_arm_goal", Float32MultiArray, self.vector_callback)

        ## Creating Robotic arm through defining links and Serial Linkage
        Link_1=rtb.DHLink(1.24, -math.pi/2, 0, 0)
        Link_2=rtb.DHLink(0,    0,   0, 2.7)
        Link_3=rtb.DHLink(0,    -math.pi/2,   0, 0.7)
        Link_4=rtb.DHLink(3.02, -math.pi/2, 0, 0)
        Link_5=rtb.DHLink(0, math.pi/2, 0, 0)
        Link_6=rtb.DHLink(0.72, 0, 0, 0)
        # initialising and setting irb_robot
        self.irb_robot= rtb.DHRobot([Link_1, Link_2, Link_3, Link_4, Link_5, Link_6])
        self.irb_robot


    def inverse_kinematics_solver(self, data):
        
        #getting x,y,z data from the image
        point = SE3(data.data)

        #calculating inverse kinematics points of each joints
        point_sol = self.irb_robot.ikine_LM(point)
        print(point_sol.q)
        return point_sol.q


    def joint_publisher(self, inverse_slove_point):
        msg.layout.dim = []
        msg = Float32MultiArray()
        msg.data= inverse_slove_point.q.tolist()

        self.inverse_joint_pub.publish(msg)

    def vector_callback(self, data):
        
        rospy.loginfo(f"recieved image vector {data.data}")

        try:
            # calculate point_solution irb_robot
            point_sol = self.inverse_kinematics_solver(data)
            #publishing point_solution
            self.joint_publisher(point_sol)
        except Exception as e:
            print(e)
            pass



def main():
    node = inversepose()

    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        # node.publish_message("Hello")
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass        
        
