import numpy as np
from .make_current_limit import make_current_limit
from .make_position_p_gain import make_position_p_gain


class ParameterObject:
    def __init__(self):
        self.node_name      : str        = "dclaw_node"
        self.queue_size     : int        = 10
        self.sleep_time_sec : float      = 0.2 # 1.0
        self.current_limit  : float      = make_current_limit(None)
        self.position_p_gain: np.ndarray = make_position_p_gain(None)
