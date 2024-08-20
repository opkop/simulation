import numpy as np

def empirical_distribution_function(sample, value):
    # EDF is the proportion of sample points less than or equal to the given value
    return np.sum(sample <= value) / len(sample)

def uniform_cdf(value):
    # CDF of a uniform distribution on [0, 1]
    if value < 0:
        return 0.0
    elif value > 1:
        return 1.0
    else:
        return value

def kolmogorov_smirnov_test(sample):
    # Sort the sample
    sample_sorted = np.sort(sample)
    n = len(sample)
    
    # Calculate the K-S statistic
    ks_statistic = 0
    for i in range(n):
        edf = (i + 1) / n
        cdf = uniform_cdf(sample_sorted[i])
        ks_statistic = max(ks_statistic, abs(edf - cdf), abs(cdf - (i / n)))

    # Calculate the p-value using the Kolmogorov distribution
    # Approximation for p-value based on K-S statistic
    sqrt_n = np.sqrt(n)
    p_value = 1 - np.exp(-2 * (ks_statistic * sqrt_n) ** 2)

    return ks_statistic, p_value

# Example set of numbers to test for randomness
sample = np.array([0.44, 0.81, 0.14, 0.05, 0.93])  # Replace with your own sample

# Perform the K-S test against the uniform distribution
ks_statistic, p_value = kolmogorov_smirnov_test(sample)

print(f"K-S Statistic: {ks_statistic}")
print(f"P-value: {p_value}")

# Interpretation of the p-value
alpha = 0.05  # Significance level
if p_value < alpha:
    print("Reject the null hypothesis: The sample is not uniformly distributed.")
else:
    print("Fail to reject the null hypothesis: The sample is uniformly distributed.")
