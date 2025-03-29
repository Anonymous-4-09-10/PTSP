import numpy as np
import matplotlib.pyplot as plt
from utils import binomial_prob, poisson_prob
from scipy.stats import rayleigh, expon

def plot_distribution(distribution_type):
    # Parameters for each distribution
    n_samples = 1000
    x = np.linspace(-5, 5, 1000)

    if distribution_type == "gaussian":
        # Gaussian (Normal) Distribution
        mean, std_dev = 0, 1
        y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)
        title = "Gaussian Distribution"
        color = 'blue'

    elif distribution_type == "laplacian":
        # Laplacian Distribution
        mean, b = 0, 1
        y = (1 / (2 * b)) * np.exp(-np.abs(x - mean) / b)
        title = "Laplacian Distribution"
        color = 'green'

    elif distribution_type == "uniform":
        # Uniform Distribution
        low, high = -5, 5
        y = np.ones_like(x) / (high - low)
        title = "Uniform Distribution"
        color = 'orange'

    elif distribution_type == "normal":
        # Normal Distribution (same as Gaussian)
        mean, std_dev = 0, 1
        y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)
        title = "Normal Distribution"
        color = 'purple'

    elif distribution_type == "binomial":
        # Binomial Distribution
        n, p = 10, 0.5
        x_binomial = np.arange(0, n + 1)
        y = np.array([binomial_prob(k, n, p) for k in x_binomial])
        title = "Binomial Distribution"
        color = 'red'

        # Plotting Binomial Distribution as a histogram
        plt.bar(x_binomial, y, color=color, edgecolor='black')
        plt.xlabel("k (Successes)")
        plt.ylabel("Probability")
        plt.title(title)
        plt.show()
        return

    elif distribution_type == "rayleigh" or distribution_type == "raili":
        # Rayleigh Distribution
        scale = 1
        y = rayleigh.pdf(x, scale=scale)
        plt.xlim(0,5)
        title = "Rayleigh Distribution"
        color = 'cyan'

    elif distribution_type == "poisson":
        # Poisson Distribution
        lambda_ = 5
        x_poisson = np.arange(0, 20)
        y = np.array([poisson_prob(k, lambda_) for k in x_poisson])
        title = "Poisson Distribution"
        color = 'magenta'

        # Plotting Poisson Distribution as a histogram
        plt.bar(x_poisson, y, color=color, edgecolor='black')
        plt.xlabel("k (Events)")
        plt.ylabel("Probability")
        plt.title(title)
        plt.show()
        return

    elif distribution_type == "exponential":
        # Exponential Distribution
        scale = 1  # Scale parameter (lambda = 1/scale)
        x = np.linspace(0, 10, 1000)  # Range of values

        # Compute PDF and CDF
        y = expon.pdf(x, scale=scale)
        title = 'Exponential Distribution'
        color = 'brown'  # Define color for exponential distribution
        plt.xlabel('x')
        plt.ylabel('Probability')
        plt.title(title)
        plt.grid()

    # Plotting the distribution
    plt.plot(x, y, label=distribution_type, color=color)
    plt.fill_between(x, y, alpha=0.3, color=color)
    plt.title(title, fontsize=16, fontweight='bold')
    plt.xlabel("x", fontsize=12)
    plt.ylabel("Density", fontsize=12)
    plt.legend()  # Add this to ensure the legend is populated
    plt.grid(True)
    plt.show()
