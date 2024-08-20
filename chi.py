INTERVALS, TABULATED_VALUE = 10, 16.919

def main():
    seed, a, c, m, n = 7, 5, 3, 100, 100
    lb, ub = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90], [9, 19, 29, 39, 49, 59, 69, 79, 89, 99]
    observed = [0] * INTERVALS
    expected = n // INTERVALS

    x = seed
    numbers = [(x := (a * x + c) % m) for _ in range(n)]

    for num in numbers:
        observed[next(i for i, (low, high) in enumerate(zip(lb, ub)) if low <= num <= high)] += 1

    chi_square_sum = sum(((o - expected) ** 2) / expected for o in observed)

    print("The random numbers are:", ' '.join(map(str, numbers)))
    print("\nS.No \t Oi \t Ei \t ((Oi-Ei)^2 / Ei)")
    for i, o in enumerate(observed, 1):
        print(f"{i} \t {o} \t {expected} \t {((o - expected) ** 2) / expected:.4f}")

    print(f"\nTotal \t {sum(observed)} \t\t {chi_square_sum:.4f}")
    result = "not rejected; the random numbers are uniform" if chi_square_sum <= TABULATED_VALUE else "rejected; the random numbers are not uniform"
    print(f"Calculated value = {chi_square_sum:.4f} {'<=' if chi_square_sum <= TABULATED_VALUE else '>'} Tabulated value = {TABULATED_VALUE}. The null hypothesis is {result}.")

if __name__ == "__main__":
    main()
