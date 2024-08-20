def multiplicative_congruential_method(X0, m, a, n):
    random_numbers = []
    X = X0
    for _ in range(n):
        X = (a * X) % m
        random_numbers.append(X)
    return random_numbers

# Parameters
X0 = 13  # Seed value
m = 1000  # Modulus
a = 15    # Multiplier
n = 50    # Number of random numbers to generate

# Generate random numbers
random_numbers = multiplicative_congruential_method(X0, m, a, n)

# Print the random numbers in a list
print(f"Random number: {random_numbers}")
