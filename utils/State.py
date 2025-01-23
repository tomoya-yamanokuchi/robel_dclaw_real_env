from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class State:
    robot_position       : np.ndarray
    object_position      : np.ndarray
    robot_velocity       : np.ndarray
    object_velocity      : np.ndarray
    end_effector_position: np.ndarray
    task_space_positioin : np.ndarray
