import rospy
from std_msgs.msg import Int32MultiArray
from .BaseSubscriber import BaseSubscriber
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..SubscriberManager import SubscriberManager


class JointCurrentsSubscriber(BaseSubscriber):
    def __init__(self, id: int, manager: 'SubscriberManager') :
        super().__init__(id, manager)
        rospy.Subscriber("/dclaw/joint_currents", Int32MultiArray, self.callback)

    def callback(self, data: Int32MultiArray):
        self.joint_currents = data
        self.update_flag()
