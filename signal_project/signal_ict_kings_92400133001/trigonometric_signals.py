"""
Module: trigonometric_signals
Purpose: Generate sine, cosine, and exponential signals
"""

import numpy as np
import matplotlib.pyplot as plt

def sine_wave(A: float, f: float, phi: float, t: np.ndarray) -> np.ndarray:
    """Generate a sine wave: A * sin(2*pi*f*t + phi)"""
    signal = A * np.sin(2 * np.pi * f * t + phi)

    plt.figure()
    plt.plot(t, signal)
    plt.title("Sine Wave")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

    return signal

def cosine_wave(A: float, f: float, phi: float, t: np.ndarray) -> np.ndarray:
    """Generate a cosine wave: A * cos(2*pi*f*t + phi)"""
    signal = A * np.cos(2 * np.pi * f * t + phi)

    plt.figure()
    plt.plot(t, signal)
    plt.title("Cosine Wave")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

    return signal

def exponential_signal(A: float, a: float, t: np.ndarray) -> np.ndarray:
    """Generate an exponential signal: A * exp(a * t)"""
    signal = A * np.exp(a * t)

    plt.figure()
    plt.plot(t, signal)
    plt.title("Exponential Signal")
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.show()

    return signal
