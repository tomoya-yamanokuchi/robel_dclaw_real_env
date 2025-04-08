from unicodedata import name
import numpy as np
from .. import RobelDClawValveRealEnvironment
from robel_dclaw_task_space import TaskSpaceValueObjectFactory


def run_tests():

    Manifold1D = TaskSpaceValueObjectFactory.create(task_space_name="manifold_1d")

    # ----
    task_space_position_init = np.array([0.65, 0.18, 0.65])
    task_space_ctrl_init     = Manifold1D(value=task_space_position_init.reshape(1,1,3))
    # ----
    env = RobelDClawValveRealEnvironment()
    env.reset(task_space_ctrl_init, valve_position_init=np.pi)
    # ----

if __name__ == "__main__":
    run_tests()
