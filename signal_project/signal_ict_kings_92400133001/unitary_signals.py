"""
Module: unitary_signals
Purpose: Generate basic unitary signals - unit step, unit impulse, ramp
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Sequence

def unit_step(n: Sequence) -> np.ndarray:
    """
    Generate a unit step signal u[n].
    u[n] = 1 for n >= 0, else 0
    """
    n = np.asarray(n)
    signal = np.where(n >= 0, 1.0, 0.0)

    plt.figure()
    plt.stem(n, signal, basefmt=" ")
    plt.title("Unit Step Signal")
    plt.xlabel("n")
    plt.ylabel("u[n]")
    plt.grid(True)
    plt.show()

    return signal

def unit_impulse(n: Sequence) -> np.ndarray:
    """
    Generate a unit impulse (Kronecker delta) signal delta[n].
    delta[n] = 1 when n == 0 else 0
    """
    n = np.asarray(n)
    signal = np.where(n == 0, 1.0, 0.0)

    plt.figure()
    plt.stem(n, signal, basefmt=" ")
    plt.title("Unit Impulse Signal")
    plt.xlabel("n")
    plt.ylabel("delta[n]")
    plt.grid(True)
    plt.show()

    return signal

def ramp_signal(n: Sequence) -> np.ndarray:
    """
    Generate a ramp signal r[n].
    r[n] = n for n >= 0 else 0
    """
    n = np.asarray(n)
    signal = np.where(n >= 0, n, 0.0)

    plt.figure()
    plt.stem(n, signal, basefmt=" ")
    plt.title("Ramp Signal")
    plt.xlabel("n")
    plt.ylabel("r[n]")
    plt.grid(True)
    plt.show()

    return signal
