import os
import sys
import numpy as np
from robel_dclaw_kinematics import ForwardKinematics, InverseKinematics
from robel_dclaw_ros import ROSHandler
from robel_dclaw_ros.utils import ParameterObject
from dynamixel_ros_service import Control
from .utils import State


class RobelDClawValveRealEnvironment:
    def __init__(self, *areg):
        self.num_joint = 9
        # ---
        self.forward_kinematics = ForwardKinematics()
        self.inverse_kinematics = InverseKinematics()
        # ---
        self.params = ParameterObject()
        self.ros    = ROSHandler(self.params)


    def reset(self, ctrl_init: np.ndarray):
        assert ctrl_init.shape == (self.num_joint,)
        ctrl = Control.from_radvec(radvec=ctrl_init)
        self.ros.publisher.publish_initialize_ctrl(ctrl=ctrl)
        self.ros.wait_initialization()

    def set_ctrl_task_sapce(self, task_space_ctrl):
        radvec = task_space_ctrl
        ctrl   = Control.from_radvec(radvec)
        self.ros.publisher.publish_joint_ctrl(ctrl)

    def get_state(self):
        return State(
            robot_position        = self.ros.subscriber.joint_positions.data,
            object_position       = self.ros.subscriber.valve_position.data,
            robot_velocity        = self.ros.subscriber.joint_velocities.data,
            object_velocity       = None,
            end_effector_position = None, # to be implemented
            task_space_positioin  = None, # to be implemented
        )

    def render(self):
        pass

    def view(self):
        pass

    def step(self):
        pass
