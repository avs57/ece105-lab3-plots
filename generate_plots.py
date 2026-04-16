"""
Generate publication-quality sensor data visualizations.

This script creates synthetic temperature sensor data using NumPy
and produces scatter, histogram, and box plot visualizations saved
as PNG files.

Usage:
    python generate_plots.py
"""

import numpy as np
import matplotlib.pyplot as plt


def generate_data(seed):
    """Generate synthetic temperature sensor readings.

    Parameters
    ----------
    seed : int
        Random number generator seed for reproducibility.

    Returns
    -------
    sensor_a : numpy.ndarray
        Temperature readings from sensor A in Celsius, shape (200,).
    sensor_b : numpy.ndarray
        Temperature readings from sensor B in Celsius, shape (200,).
    timestamps : numpy.ndarray
        Measurement timestamps in seconds, shape (200,).
    """
    rng = np.random.default_rng(seed=seed)
    sensor_a = rng.normal(loc=25.0, scale=3.0, size=200)
    sensor_b = rng.normal(loc=27.0, scale=4.5, size=200)
    timestamps = rng.uniform(low=0.0, high=10.0, size=200)
    return sensor_a, sensor_b, timestamps

def plot_scatter(sensor_a, sensor_b, timestamps, ax):
    """Create a scatter plot of sensor readings vs time.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Sensor A readings.
    sensor_b : numpy.ndarray
        Sensor B readings.
    timestamps : numpy.ndarray
        Time values in seconds.
    ax : matplotlib.axes.Axes
        Axes object to draw the plot on.

    Returns
    -------
    None
        Modifies the given Axes in place.
    """
    ax.scatter(timestamps, sensor_a, color='blue', label='Sensor A')
    ax.scatter(timestamps, sensor_b, color='orange', label='Sensor B')

    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Sensor Readings vs Time")

    ax.legend()