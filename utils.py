from math import comb, factorial
import numpy as np

def binomial_prob(k, n, p):
    # Binomial distribution probability mass function
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

def poisson_prob(k, lambda_):
    # Poisson distribution probability mass function
    return (np.exp(-lambda_) * lambda_**k) / factorial(k)


