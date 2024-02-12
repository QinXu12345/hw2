from __future__ import annotations
from scipy import stats
from numpy.typing import NDArray
import numpy as np

def ks_distance(rvs: NDArray, cdf: NDArray):
    assert rvs.shape == cdf.shape
    sorted_rvs = np.sort(rvs)
    diff = np.abs(sorted_rvs - cdf)
    max_diff = np.max(diff)
    return np.sqrt(len(rvs)) * max_diff
    