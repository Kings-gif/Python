from setuptools import setup, find_packages

setup(
    name="signal_ict_kings",        # unique name for TestPyPI
    version="0.1.0",
    author="Kings",
    description="Signal processing experiments package",
    packages=find_packages(),        # automatically finds your package folder
    install_requires=[
        "numpy",
        "matplotlib"
    ],
    python_requires=">=3.10",
)
