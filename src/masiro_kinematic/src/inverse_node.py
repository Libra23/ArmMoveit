#!/usr/bin/env python

import sys
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg

from math import pi

def talker():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('inverse_node',
                    anonymous=True)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "arm"
    move_group = moveit_commander.MoveGroupCommander(group_name)
    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                               moveit_msgs.msg.DisplayTrajectory,
                                               queue_size=20)
    # set position & orientation
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.position.x = 0.089973697223
    pose_goal.position.y = 0.180020156677
    pose_goal.position.z = -0.335890154759
    pose_goal.orientation.x = 2.00719893294e-06
    pose_goal.orientation.y = -0.25878908403
    pose_goal.orientation.z = 6.86465394841e-05
    pose_goal.orientation.w = 0.965933851395

    move_group.set_pose_target(pose_goal)
    plan = move_group.go(wait=True)
    move_group.stop()
    move_group.clear_pose_targets()
    
    print move_group.get_current_joint_values()
    
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():

        r.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass