import numpy as np
from .. import RobelDClawValveRealEnvironment
from robel_dclaw_task_space import TaskSpaceValueObjectFactory


def run_tests():
    Manifold1D = TaskSpaceValueObjectFactory.create(task_space_name="manifold_1d")
    # ----
    task_space_position_init = np.array([0, 0, 0])
    task_space_ctrl_init     = Manifold1D(value=task_space_position_init.reshape(1,1,3))
    # ----
    env = RobelDClawValveRealEnvironment()
    env.reset(task_space_ctrl_init)
    # ----

if __name__ == "__main__":
    run_tests()
