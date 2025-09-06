📦 signal_ict_kings
A Python package for basic signal processing experiments. This package provides functions to generate common discrete and continuous signals, and perform basic operations such as shifting, scaling, addition, and multiplication.
________________________________________
🔧 Installation
First, clone or download the project, navigate to the root folder, and install with:
pip install .
Or, if you already built a wheel:
pip install dist/signal_ict_kings-0.1.0-py3-none-any.whl
________________________________________
📂 Package Structure
signal_ict_kings/
│
├── __init__.py
├── unitary_signals.py        # Unit step, impulse, ramp
├── trigonometric_signals.py  # Sine and cosine waves
├── exponential_signals.py    # Exponential signals
├── operations.py             # Time shifting, scaling, addition, multiplication
└── main.py                   # Example usage (plots)
________________________________________
🧩 Modules & Functions
1. unitary_signals
•	unit_step(n) → Generate a unit step sequence.
•	unit_impulse(n) → Generate a unit impulse sequence.
•	ramp_signal(n) → Generate a ramp sequence.
2. trigonometric_signals
•	sine_wave(A, f, phi, t) → Generate sine wave.
•	cosine_wave(A, f, phi, t) → Generate cosine wave.
3. exponential_signals
•	exponential_signal(n, a) → Generate exponential signal (growth/decay).
4. operations
•	time_shift(x, k) → Shift signal by k units.
•	time_scale(x, k) → Scale signal in time by factor k.
•	signal_addition(x, y) → Add two signals.
•	signal_multiplication(x, y) → Multiply two signals.
________________________________________
🚀 Usage Example
import numpy as np
import matplotlib.pyplot as plt
import signal_ict_kings_92400133001 as sik

# Example: Unit step and impulse
n = np.arange(20)
step = sik.unit_step(n)
impulse = sik.unit_impulse(n)

plt.stem(n, step)
plt.title("Unit Step Signal")
plt.show()

plt.stem(n, impulse)
plt.title("Unit Impulse Signal")
plt.show()

# Example: Sine wave
t = np.linspace(0, 1, 500)
sine = sik.sine_wave(2, 5, 0, t)

plt.plot(t, sine)
plt.title("Sine Wave (Amplitude=2, f=5Hz)")
plt.show()
________________________________________
📊 Full Demo
Run the included main.py to see all available signals and operations in action:
python main.py
This will display: - Unit step, impulse, and ramp - Sine & cosine waves - Exponential signal - Time shifting & scaling - Signal addition & multiplication
________________________________________
✍️ Author
Kings
