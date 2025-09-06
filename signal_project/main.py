"""
Main script for testing signal_ict_kings package
Generates and plots:
1. Unit Step & Unit Impulse
2. Sine Wave & Time Shifted Sine
3. Addition of Unit Step + Ramp
4. Multiplication of Sine × Cosine
5. Exponential Signal
"""

import numpy as np
import matplotlib.pyplot as plt
import signal_ict_kings_92400133001 as sik   # import your package

# 1. Unit Step and Impulse
n = np.arange(20)
step = sik.unit_step(n)
impulse = sik.unit_impulse(n)

plt.figure()
plt.stem(n, step)
plt.title("Unit Step Signal")
plt.grid(True)

plt.figure()
plt.stem(n, impulse)
plt.title("Unit Impulse Signal")
plt.grid(True)

# 2. Sine wave and Time-shifted Sine
t = np.linspace(0, 1, 500)
sine = sik.sine_wave(2, 5, 0, t)
sine_shifted = sik.time_shift(sine, 5)

plt.figure()
plt.plot(t, sine, label="Original Sine")
plt.plot(t, sine_shifted, label="Shifted Sine (+5)")
plt.legend()
plt.title("Time Shifting of Sine Wave")
plt.grid(True)

# 3. Addition of Step + Ramp
ramp = sik.ramp_signal(n)
added = sik.signal_addition(step, ramp)

plt.figure()
plt.stem(n, added)
plt.title("Addition: Step + Ramp Signal")
plt.grid(True)

# 4. Multiplication of Sine × Cosine
cosine = sik.cosine_wave(2, 5, 0, t)
multiplied = sik.signal_multiplication(sine, cosine)

plt.figure()
plt.plot(t, multiplied)
plt.title("Multiplication: Sine × Cosine")
plt.grid(True)

# 5. Exponential Signal (Discrete-time)
n_exp = np.arange(20)
exp_signal = np.exp(0.2 * n_exp)   # exponential growth

plt.figure()
plt.stem(n_exp, exp_signal)
plt.title("Exponential Signal")
plt.grid(True)

# 👉 Show ALL plots at once
plt.show()
