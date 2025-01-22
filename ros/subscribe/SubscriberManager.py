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
        self.initialization_state  = InitializationStateSubscriber() # これだけ登録しない
        self.joint_positions       = JointPositionsSubscriber (id=1, manager=self)
        self.joint_currents        = JointCurrentsSubscriber  (id=2, manager=self)
        self.joint_velocities      = JointVelocitiesSubscriber(id=3, manager=self)
        self.valve_moving          = ValveMovingSubscriber    (id=4, manager=self)
        self.valve_position        = ValvePositionSubscriber  (id=0, manager=self)

    '''
        initialization related function
    '''
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


    '''
        subscribe related function
    '''
    def get_joint_positions(self):
        return self.joint_positions.data

    def get_valve_position(self):
        return self.valve_position.data
