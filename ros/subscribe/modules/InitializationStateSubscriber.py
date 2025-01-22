import rospy
from std_msgs.msg import Bool


class InitializationStateSubscriber:
    def __init__(self):
        rospy.Subscriber("/dclaw/is_initialize_finished", Bool, self.callback)

    def callback(self, data: Bool):
        self.data = data.data

