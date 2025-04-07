import os
import sys
import numpy as np
from robel_dclaw_kinematics import ForwardKinematics, InverseKinematics
from robel_dclaw_ros import ROSHandler
from robel_dclaw_ros.utils import ParameterObject
from dynamixel_ros_service import Orientation
from robel_dclaw_task_space.utils.AbstractTaskSpaceInterface import AbstractTaskSpaceInterface
from robel_dclaw_task_space.utils.AbstractTaskSpaceObject import AbstractTaskSpaceObject
from .utils import State


class RobelDClawValveRealEnvironment:
    def __init__(self, params: ParameterObject = None):
        self.params = params
        if params is None:
            self.params = ParameterObject()
        # ----
        self.ros    = ROSHandler(self.params)
        # ----
        self.forward_kinematics   = ForwardKinematics()
        self.inverse_kinematics   = InverseKinematics()
        # -----
        # self.task_space_interface = TaskSpaceInterface()

        from robel_dclaw_task_space import TaskSpaceInterfaceFactory
        self.task_space_interface = TaskSpaceInterfaceFactory.create(
            task_space_name = "manifold_1d",
        )

        # import ipdb; ipdb.set_trace()

    def reset(self, task_space_ctrl_init: AbstractTaskSpaceObject):
        task_space_position   = task_space_ctrl_init.value.squeeze()
        end_effector_position = self.task_space_interface.task2end(task_space_position)
        joint_space_position  = self.inverse_kinematics.calc(end_effector_position)
        joint_space_position  = np.squeeze(joint_space_position)
        # -------
        ctrl = Orientation.from_radvec(radvec=joint_space_position)
        self.ros.publisher.publish_initialize_ctrl(ctrl=ctrl)
        self.ros.wait_initialization()

    def set_ctrl_task_sapce(self, task_space_ctrl: AbstractTaskSpaceObject):
        task_space_position   = task_space_ctrl.value.squeeze()
        end_effector_position = self.task_space_interface.task2end(task_space_position)
        joint_space_position  = self.inverse_kinematics.calc(end_effector_position)
        joint_space_position  = np.squeeze(joint_space_position)
        # -------
        ctrl   = Orientation.from_radvec(radvec=joint_space_position)
        self.ros.publisher.publish_joint_ctrl(ctrl)

    def get_state(self):
        robot_position        = self.ros.subscriber.get_joint_positions()
        end_effector_position = self.forward_kinematics.calc(robot_position).squeeze()
        task_space_positioin  = self.task_space_interface.end2task(end_effector_position).squeeze()
        # ----
        return State(
            robot_position        = robot_position,
            object_position       = self.ros.subscriber.get_valve_position(),
            robot_velocity        = None,
            object_velocity       = None,
            end_effector_position = end_effector_position,
            task_space_positioin  = task_space_positioin,
        )

    def get_image(self):
        return self.ros.subscriber.get_image()

    def render(self):
        pass

    def view(self):
        pass

    def step(self):
        pass
