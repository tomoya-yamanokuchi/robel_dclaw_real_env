import numpy as np
from .. import RobelDClawValveRealEnvironment
from robel_dclaw_task_space.value_object import Manifold1D


def run_tests():
    # ----
    task_space_position_init = np.array([0.65, 0.18, 0.65])
    task_space_ctrl_init     = Manifold1D(value=task_space_position_init.reshape(1,1,3))
    # ----
    env = RobelDClawValveRealEnvironment()
    env.reset(task_space_ctrl_init)
    # ----


if __name__ == "__main__":
    run_tests()
