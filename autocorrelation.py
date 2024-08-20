import numpy as np

def autocorrelation_test(random_numbers, lag, start_index):
    N = len(random_numbers)
    M = (N - start_index - lag) // lag
    
    if M < 1:
        raise ValueError("M must be at least 1. Increase N or decrease the lag.")

    Pim = 0.0
    for k in range(M + 1):
        Pim += random_numbers[start_index + k * lag] * random_numbers[start_index + (k + 1) * lag]
    Pim = (Pim / (M + 1)) - 0.25

    sigma_im = np.sqrt((13 * M + 7) / (12 * (M + 1)))
    z0 = Pim / sigma_im
    
    return Pim, sigma_im, z0

def main():
    # Example list of random numbers
    random_numbers = [
       0.12, 0.01, 0.23, 0.28, 0.89, 0.31, 0.64, 0.28, 0.83, 0.93,
       0.99, 0.15, 0.33, 0.35, 0.91, 0.41, 0.60, 0.27, 0.75, 0.88,
       0.68, 0.49, 0.05, 0.43, 0.95, 0.58, 0.19, 0.36, 0.69, 0.87
    ]
    
    lag = int(input("Enter the lag value for autocorrelation test: "))
    start_index = int(input("Enter the start index for autocorrelation test: "))

    if start_index < 0 or start_index >= len(random_numbers):
        print("Invalid start index. It must be between 0 and the length of the random number sequence minus 1.")
        return
    
    try: 
        Pim, sigma_im, z0 = autocorrelation_test(random_numbers, lag, start_index)
        print(f"Autocorrelation coefficient Pim for lag {lag} and start index {start_index}: {Pim}")
        print(f"Standard deviation sigma_im: {sigma_im}")
        print(f"Test statistic z0: {z0}")
        
        # Determine independence based on z0
        critical_value = 1.96  # for a 5% significance level
        if abs(z0) > critical_value:
            print(f"The sequence is not independent (|z0| > {critical_value}).")
        else:
            print(f"The sequence is independent (|z0| <= {critical_value}).")
        
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
