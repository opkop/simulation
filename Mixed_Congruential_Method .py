def mixed_congruential_method(X0, m, a, c, n):
    random_numbers = []
    X = X0
    for _ in range(n):
        X = (a * X + c) % m
        random_numbers.append(X)
    return random_numbers

# Parameters
X0 = 11  # Seed value
m = 100  # Modulus
a = 5    # Multiplier
c = 13   # Increment
n = 50   # Number of random numbers to generate

# Generate random numbers
random_numbers = mixed_congruential_method(X0, m, a, c, n)

# Print the random numbers in a list
print(f"Random number: {random_numbers}")
