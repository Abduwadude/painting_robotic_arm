#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float32MultiArray
import time

def move_robotic_arm(publisher, goal_position):
    msg = Float32MultiArray(data=goal_position)
    publisher.publish(msg)
    rospy.loginfo("Sending goal position: {}".format(goal_position))
    time.sleep(5)  # Adjust this delay based on your robot's response time

def robotic_arm_square_movement():
    rospy.init_node('robotic_arm_square_movement', anonymous=True)
    pub = rospy.Publisher('/robotic_arm_goal', Float32MultiArray, queue_size=10)
    rospy.sleep(1)  # Wait for the publisher to initialize

    # Define the square movement coordinates
    square_coordinates = [
        [1.0, 1.0, 0.0],
        [1.0, -1.0, 0.0],
        [-1.0, -1.0, 0.0],
        [-1.0, 1.0, 0.0],
    ]

    rate = rospy.Rate(0.2)  # Adjust the rate based on your desired movement speed

    while not rospy.is_shutdown():
        for goal_position in square_coordinates:
            move_robotic_arm(pub, goal_position)
            rate.sleep()

if __name__ == '__main__':
    try:
        robotic_arm_square_movement()
    except rospy.ROSInterruptException:
        pass

