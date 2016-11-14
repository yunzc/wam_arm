#!/usr/bin/env python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import geom_subscriber

def plan_generator(orientation, pose):
	#orientation and pose are two tuples
	print "=== Generating plan 1 ==="
	pose_target = geometry_msgs.msg.Pose()
	pose_target.orientation.x = orientation[0]
	pose_target.orientation.y = orientation[1]
	pose_target.orientation.z = orientation[2]
	pose_target.orientation.w = orientation[3]
	pose_target.position.x = pose[0]
	pose_target.position.y = pose[1]
	pose_target.position.z = pose[2]
	group.set_pose_target(pose_target)
	return True


moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('arm_control', anonymous=True)

robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander("arm")
display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path', moveit_msgs.msg.DisplayTrajectory)

print "============ Reference frame: %s" % group.get_planning_frame()
print "============ Reference frame: %s" % group.get_end_effector_link()

print "============ Robot Groups:"
print robot.get_group_names()

print "============ Printing robot state"
print robot.get_current_state()

des_pose = geom_subscriber.listener()
pos = des_pose['position']
ori = des_pose['orientation']

generate_plan = plan_generator(ori, pos)

plan1 = group.plan()

group.go(wait=True)

pose_now = geometry_msgs.msg.Pose()
print "current pose", pose_now

rospy.sleep(5)
