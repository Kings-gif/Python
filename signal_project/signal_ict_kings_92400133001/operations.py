"""
Module: operations
Purpose: Basic operations in signal processing - shifting, scaling, addition, and multiplication.
"""

import numpy as np
from scipy.interpolate import interp1d

def time_shift(signal: np.ndarray, k: int) -> np.ndarray:
    """Shifts a discrete signal for k samples.
    For positive k, we get a right shift, whereas with a negative k, left shift emerges.
    """
    shifted = np.roll(signal, k)
    if k > 0:
        shifted[:k] = 0
    elif k < 0:
        shifted[k:] = 0
    return shifted

def time_scale(signal: np.ndarray, k: float) -> np.ndarray:
    """
    Scaling the time axis by a factor k.
    k>1 means stretching
    k<1 means compressing
    """
    n = np.arange(len(signal))
    f = interp1d(n, signal, kind='linear', fill_value="extrapolate")
    n_new = np.arange(0, len(signal), 1/k)
    scaled = f(n_new)
    return scaled

def signal_addition(signal1: np.ndarray, signal2: np.ndarray) -> np.ndarray:
    """
    Add two signals point-wise.
    If they are of different lengths, pad with zeros on the shorter one.
    """
    max_len = max(len(signal1), len(signal2))
    s1 = np.pad(signal1, (0, max_len - len(signal1)))
    s2 = np.pad(signal2, (0, max_len - len(signal2)))
    return s1 + s2

def signal_multiplication(signal1: np.ndarray, signal2: np.ndarray) -> np.ndarray:
    """
    Multiply two signals.
    Should lengths be different, zero pad the shorter one.
    """
    max_len = max(len(signal1), len(signal2))
    s1 = np.pad(signal1, (0, max_len - len(signal1)))
    s2 = np.pad(signal2, (0, max_len - len(signal2)))
    return s1 * s2