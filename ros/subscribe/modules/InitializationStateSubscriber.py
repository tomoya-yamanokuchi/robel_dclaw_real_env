import rospy
from std_msgs.msg import Bool
# from .BaseSubscriber import BaseSubscriber
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..SubscriberManager import SubscriberManager


class InitializationStateSubscriber:
    def __init__(self):
        rospy.Subscriber("/dclaw/is_initialize_finished", Bool, self.callback)

    def callback(self, data: Bool):
        self.is_initialize_finished = data.data
        # print("is_initialize_finished = ",  data.data)
        # self.update_flag()
