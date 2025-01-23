from sqlite3 import paramstyle
import numpy as np
from .. import RobelDClawValveRealEnvironment
from robel_dclaw_task_space.value_object import Manifold1D
from robel_dclaw_ros.utils import ParameterObject


def run_tests():
    # ----
    task_space_position_init = np.array([0.65, 0.18, 0.65])
    task_space_ctrl_init     = Manifold1D(value=task_space_position_init.reshape(1,1,3))
    # ----
    params = ParameterObject()
    params.sleep_time_sec = 0.1
    env = RobelDClawValveRealEnvironment(params)
    env.reset(task_space_ctrl_init)
    # ----
    num_step = 100
    task_space_ctrl = task_space_ctrl_init
    for i in range(num_step):
        task_space_ctrl.value += 0.01
        env.set_ctrl_task_sapce(task_space_ctrl)
        env.step()

if __name__ == "__main__":
    run_tests()
