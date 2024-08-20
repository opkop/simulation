TAB_CHISQUARE = {1: 5.99, 2: 9.49}

def poker_test():
    test_type = int(input("Choose test:\n 1. Three digit poker\n 2. Four digit poker\n"))
    if test_type not in [1, 2]:
        print("Choose 1 or 2")
        return

    num_generated = int(input("How many numbers generated: "))
    observed_freq = []

    if test_type == 2:
        freq_names = ["Four different digits", "Four same digits", "Three of a kind", "One Pair", "Two Pair"]
        probabilities = [0.504, 0.001, 0.036, 0.432, 0.027]
    else:
        freq_names = ["Three different digits", "Three same digits", "One Pair"]
        probabilities = [0.72, 0.01, 0.27]

    for name in freq_names:
        freq = int(input(f"Enter observed frequency of {name}: "))
        observed_freq.append(freq)

    if sum(observed_freq) != num_generated:
        print(f"Sum does not equal {num_generated}")
        return

    expected_freq = [p * num_generated for p in probabilities]
    chi_square = sum(((o - e) ** 2) / e for o, e in zip(observed_freq, expected_freq))

    print("\nObserved frequencies:", ' '.join(map(str, observed_freq)))
    print("Expected frequencies:", ' '.join(map(lambda x: str(int(x)), expected_freq)))
    print(f"\nChi-square: {chi_square}")
    print(f"Tabulated chi-square: {TAB_CHISQUARE[test_type]}")

    if chi_square <= TAB_CHISQUARE[test_type]:
        print("Numbers are independent.")
    else:
        print("Numbers are not independent.")

if __name__ == "__main__":
    poker_test()
