import numpy as np
import math

def confidence_interval(sample, confidence_level, population_mean):
    n = len(sample)
    sample_mean = np.mean(sample)
    sample_std_dev = np.std(sample, ddof=1)  # Sample standard deviation
    std_err = sample_std_dev / math.sqrt(n)  # Standard error of the mean
    
    # Z-score for the confidence level (e.g., 95% confidence level corresponds to a Z-score of 1.96)
    z_score = {
        0.90: 1.645,
        0.95: 1.96,
        0.99: 2.576
    }[confidence_level]

    margin_of_error = z_score * std_err
    return sample_mean - margin_of_error, sample_mean + margin_of_error

def main():
    # Sample data
    sample = [10, 12, 14, 15, 18, 21, 22, 23, 25, 28]
    confidence_level = 0.95  # 95% confidence level
    population_mean = 20  # Given population mean (not used in calculation but mentioned in the problem statement)

    # Calculate confidence interval
    lower_bound, upper_bound = confidence_interval(sample, confidence_level, population_mean)
    print(f"Confidence Interval: ({lower_bound}, {upper_bound})")

if __name__ == "__main__":
    main()
