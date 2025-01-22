import numpy as np


def make_position_p_gain(position_p_gain: np.ndarray):
    if position_p_gain is None:
        position_p_gain = np.hstack([180, 120, 60]*3).astype(int)
    assert position_p_gain.shape == (9,)
    return position_p_gain
