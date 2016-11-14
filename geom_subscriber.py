import rospy
from geometry_msgs.msg import Pose

def callback(data):
    global geom_data
    geom_data = {}
    geom_data['position'] = [data.position.x,data.position.y,data.position.z]
    geom_data['orientation'] = [data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w]
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    # rospy.init_node('Oracle', anonymous=True)
    rospy.Subscriber("geom_messenger", Pose, callback)
    rospy.wait_for_message("geom_messenger", Pose, timeout = 20)
    # spin() simply keeps python from exiting until this node is stopped
    return geom_data

if __name__ == '__main__':
    print listener()
