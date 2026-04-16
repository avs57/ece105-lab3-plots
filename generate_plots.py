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

def plot_histogram(sensor_a, sensor_b, ax):
    """Create an overlaid histogram of sensor temperatures.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Sensor A readings.
    sensor_b : numpy.ndarray
        Sensor B readings.
    ax : matplotlib.axes.Axes
        Axes object to draw the plot on.

    Returns
    -------
    None
        Modifies the given Axes in place.
    """
    ax.hist(sensor_a, bins=30, alpha=0.5, label='Sensor A')
    ax.hist(sensor_b, bins=30, alpha=0.5, label='Sensor B')

    mean_a = np.mean(sensor_a)
    mean_b = np.mean(sensor_b)

    ax.axvline(mean_a, color='blue', linestyle='dashed', linewidth=2)
    ax.axvline(mean_b, color='orange', linestyle='dashed', linewidth=2)

    ax.set_xlabel("Temperature (°C)")
    ax.set_ylabel("Frequency")
    ax.set_title("Temperature Distribution of Sensors")

    ax.legend()


def plot_boxplot(sensor_a, sensor_b, ax):
    """Create a side-by-side box plot for both sensors.

    Parameters
    ----------
    sensor_a : numpy.ndarray
        Sensor A readings.
    sensor_b : numpy.ndarray
        Sensor B readings.
    ax : matplotlib.axes.Axes
        Axes object to draw the plot on.

    Returns
    -------
    None
        Modifies the given Axes in place.
    """
    ax.boxplot([sensor_a, sensor_b], tick_labels=['Sensor A', 'Sensor B'])

    overall_mean = np.mean(np.concatenate([sensor_a, sensor_b]))

    ax.axhline(overall_mean, color='red', linestyle='dashed', linewidth=2, label='Overall Mean')

    ax.set_ylabel("Temperature (°C)")
    ax.set_title("Box Plot of Sensor Distributions")

    ax.legend()

def main():
    """Generate sensor data, create plots, and save the figure."""
    sensor_a, sensor_b, timestamps = generate_data(5140)  # replace with your last 4 digits

    fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes = axes.flatten()

    plot_scatter(sensor_a, sensor_b, timestamps, axes[0])
    plot_histogram(sensor_a, sensor_b, axes[1])
    plot_boxplot(sensor_a, sensor_b, axes[2])

    fig.tight_layout()
    fig.savefig("sensor_analysis.png", dpi=150, bbox_inches="tight")


if __name__ == "__main__":
    main()