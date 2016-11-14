#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Pose


def talker():
    pub = rospy.Publisher('geom_messenger', Pose, queue_size=10)
    rospy.init_node('Hermes', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        mesg = Pose()
        mesg.position.x = -0.5
        mesg.position.y = 0.2
        mesg.position.z = 0.18
        mesg.orientation.x = 0
        mesg.orientation.y = 0
        mesg.orientation.z = 0.5
        mesg.orientation.w = 0.87
        rospy.loginfo(mesg)
        pub.publish(mesg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
