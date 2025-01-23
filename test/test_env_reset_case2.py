import numpy as np
from .. import RobelDClawValveRealEnvironment
from robel_dclaw_ros.utils import get_initial_positions
from dynamixel_ros_service import Control


def run_tests():
    # ----
    ctrl_res = get_initial_positions()
    ctrl     = Control.from_resvec(ctrl_res)
    ctrl_rad = ctrl.as_radvec()
    # ----
    env = RobelDClawValveRealEnvironment()
    env.reset(ctrl_init=ctrl_rad)
    # ----

if __name__ == "__main__":
    run_tests()
