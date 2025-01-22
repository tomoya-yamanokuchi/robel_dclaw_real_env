import rospy
import numpy as np
from dynamixel_ros_service import Control
from .modules import InitializeCommandPublisher
from .modules import JointCtrlPublisher
from .modules import ValveCtrlPublisher
from ..utils import make_current_limit, make_position_p_gain


class Publisher(object):
    def __init__(self,
            sleep_time_sec : float      = 1.0,
            queue_size     : int        = 10,
            # ---
            current_limit  : np.ndarray = None,
            position_p_gain: np.ndarray = None
        ):
        # -----
        self.current_limit   = make_current_limit(current_limit)
        self.position_p_gain = make_position_p_gain(position_p_gain)
        # -----
        self.initialize_ctrl = InitializeCommandPublisher(sleep_time_sec, queue_size)
        self.joint_ctrl      = JointCtrlPublisher(sleep_time_sec, queue_size)
        self.valve_ctrl      = ValveCtrlPublisher(sleep_time_sec, queue_size)


    def publish_initialize_ctrl(self, ctrl: Control):
        assert isinstance(ctrl, Control)
        initialize_command = np.hstack([ctrl.as_resvec(), self.current_limit, self.position_p_gain])
        # ----
        # import ipdb; ipdb.set_trace()
        # self.__print_initialization_info(self.msg_initialize_ctrl)
        self.initialize_ctrl.publish(initialize_command)
        self.joint_ctrl.publish(ctrl.as_resvec()) # <--必要：無いと初期化前に残っている制御入力が入力され続けてしまう


    # def __print_initialization_info(self, msg_initialize_ctrl):
    #     print("\n\n")
    #     print("=====================================================================================")
    #     print("  initial joint_positions : ", msg_initialize_ctrl.data[:9])
    #     print("            Current_Limit : ", msg_initialize_ctrl.data[9:18])
    #     print("          Position_P_Gain : ", msg_initialize_ctrl.data[18:])
    #     print("=====================================================================================")
    #     print("\n\n")



    # def publish_joint_ctrl(self, ctrl):
    #     self.joint_ctrl.publish(ctrl)


    # def publish_valve_ctrl(self, ctrl):
    #     self.msg_valve_ctrl.data = tuple(ctrl)
    #     self.pub_valve_ctrl.publish(self.msg_valve_ctrl)
    #     rospy.sleep(self.sleep_time_sec)
