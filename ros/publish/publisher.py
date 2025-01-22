import numpy as np
from dynamixel_ros_service import Control
from .modules import InitializeCommandPublisher
from .modules import JointCtrlPublisher
from .modules import ValveCtrlPublisher
from ..utils import ParameterObject


class Publisher:
    def __init__(self, params: ParameterObject):
        # -----
        self.current_limit   = params.current_limit
        self.position_p_gain = params.position_p_gain
        # -----
        self.initialize_ctrl = InitializeCommandPublisher(params)
        self.joint_ctrl      = JointCtrlPublisher(params)
        self.valve_ctrl      = ValveCtrlPublisher(params)


    def publish_initialize_ctrl(self, ctrl: Control):
        assert isinstance(ctrl, Control)
        initialize_command = np.hstack([ctrl.as_resvec(), self.current_limit, self.position_p_gain])
        self.initialize_ctrl.publish(initialize_command)
        self.joint_ctrl.publish(ctrl.as_resvec()) # <-- 必要：無いと初期化前の直前に使用された制御入力が入力され続けてしまう

    def publish_joint_ctrl(self, ctrl: Control):
        self.joint_ctrl.publish(ctrl.as_resvec())

    def publish_valve_ctrl(self, ctrl: Control):
        self.valve_ctrl.publish(ctrl.as_resvec())
