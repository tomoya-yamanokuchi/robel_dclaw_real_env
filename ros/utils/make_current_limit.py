import numpy as np


def make_current_limit(current_limit: np.ndarray):
    if current_limit is None:
        current_limit = np.hstack([180, 120, 60]*3).astype(int)
    assert current_limit.shape == (9,)
    return current_limit
