import rospy
from std_msgs.msg import Int32
from .BaseSubscriber import BaseSubscriber
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..SubscriberManager import SubscriberManager


class ValveMovingSubscriber(BaseSubscriber):
    def __init__(self, id: int, manager: 'SubscriberManager'):
        super().__init__(id, manager)
        rospy.Subscriber("/dclaw/valve_moving", Int32, self.callback)

    def callback(self, data: Int32):
        self.valve_moving = data.data
        self.update_flag()
