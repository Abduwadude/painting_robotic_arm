#!/usr/bin/env python3
import rospy
import sys
from std_msgs.msg import Float32MultiArray
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint

# Initialize global variable for goal_positions
goal_positions = None

def joint_position_callback(data):
    global goal_positions
    goal_positions = data.data

def perform_trajectory():
    global goal_positions  # Add this line to declare goal_positions as global
    rospy.init_node('arm_trajectory_publisher')
    controller_name = '/irb_controller/command'
    trajectory_publisher = rospy.Publisher(controller_name, JointTrajectory, queue_size=10)
    rospy.Subscriber('arm_joint_position', Float32MultiArray, joint_position_callback)

    arm_joints = ['joint_1', 'joint_2', 'joint_3', 'joint_4', 'joint_5', 'joint_6']

    rospy.loginfo("Waiting for arm_joint_position data...")
    rospy.wait_for_message('arm_joint_position', Float32MultiArray)
    rospy.loginfo("Received arm_joint_position data. Let's go!")

    rate = rospy.Rate(12)  # Adjust the rate as needed

    while not rospy.is_shutdown():
        if goal_positions is not None:
            trajectory_msg = JointTrajectory()
            trajectory_msg.joint_names = arm_joints
            trajectory_msg.points.append(JointTrajectoryPoint())
            trajectory_msg.points[0].positions = goal_positions
            trajectory_msg.points[0].velocities = [0.0 for _ in arm_joints]
            trajectory_msg.points[0].accelerations = [0.0 for _ in arm_joints]
            trajectory_msg.points[0].time_from_start = rospy.Duration(3)

            trajectory_publisher.publish(trajectory_msg)

            # Reset goal_positions to avoid republishing the same trajectory
            goal_positions = None

        rate.sleep()

    # Ensure a clean shutdown
    rospy.signal_shutdown("Shutdown requested")


if __name__ == '__main__':
    try:
        perform_trajectory()
    except rospy.ROSInterruptException:
        pass

