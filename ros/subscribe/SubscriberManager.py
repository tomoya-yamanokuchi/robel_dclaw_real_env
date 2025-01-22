import rospy
from .modules import BaseSubscriber
from .modules import InitializationStateSubscriber
from .modules import JointPositionsSubscriber
from .modules import JointCurrentsSubscriber
from .modules import JointVelocitiesSubscriber
from .modules import ValveMovingSubscriber
from .modules import ValvePositionSubscriber
from ..utils import ParameterObject


class SubscriberManager:
    def __init__(self, params: ParameterObject):
        # ----
        self.num_total_subscribers = 5
        self.subscribers           = {} # 各IDとその状態を保持
        self.all_initialized       = None
        # -----
        self.initialization_state = InitializationStateSubscriber() # これだけ登録しない
        # ------
        JointPositionsSubscriber     (id=1, manager=self)
        JointCurrentsSubscriber      (id=2, manager=self)
        JointVelocitiesSubscriber    (id=3, manager=self)
        ValveMovingSubscriber        (id=4, manager=self)
        ValvePositionSubscriber      (id=0, manager=self)

    def register(self, subscriber: BaseSubscriber):
        self.subscribers[subscriber.id] = False  # 初期状態は False

    def update_state(self, subscriber_id, state):
        self.subscribers[subscriber_id] = state
        self.check_all_initialized()

    def check_all_initialized(self):
        # print("all(self.subscribers.values()) = ", all(self.subscribers.values()))
        if all(self.subscribers.values()) and (self.all_initialized is None):
            self.all_initialized = True
            self.notify_all_initialized()

    def notify_all_initialized(self):
        rospy.loginfo("ROS connection is establised!")
