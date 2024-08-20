def point_estimation(sample):
    return sum(sample) / len(sample)

def calculate_bias(sample_mean, population_mean):
    return sample_mean - population_mean

def main():
    # Sample data
    sample = [10, 12, 14, 15, 18, 21, 22, 23, 25, 28]
    population_mean = 20  # Given population mean

    # Calculate point estimation
    sample_mean = point_estimation(sample)
    print(f"Point Estimation (Sample Mean): {sample_mean}")

    # Calculate bias
    bias = calculate_bias(sample_mean, population_mean)
    print(f"Bias: {bias}")

if __name__ == "__main__":
    main()
