import numpy as np
from .. import RobelDClawValveRealEnvironment


def run_tests():

    num_joint = 9
    ctrl_init = np.zeros(num_joint)
    # ----
    env = RobelDClawValveRealEnvironment()
    env.reset(ctrl_init)
    # ----


if __name__ == "__main__":
    run_tests()
