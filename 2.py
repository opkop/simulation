def coke_pepsi_prediction():
    # Initial probabilities
    P0_C = 0.0  # Probability of purchasing Coke initially
    P0_P = 1.0  # Probability of purchasing Pepsi initially
    
    # Transition probabilities
    P_CC = 0.9  # Probability of staying with Coke
    P_PC = 0.2  # Probability of switching to Coke from Pepsi
    
    # Calculate probabilities after one purchase
    P1_C = P_PC * P0_P + P_CC * P0_C
    P1_P = (1 - P_PC) * P0_P + (1 - P_CC) * P0_C  # Since P(PP) = 1 - P_PC and P(CP) = 1 - P_CC
    
    # Calculate probabilities after two purchases
    P2_C = P_PC * P1_P + P_CC * P1_C
    P2_P = (1 - P_PC) * P1_P + (1 - P_CC) * P1_C
    
    return P2_C

# Output the result
probability_coke_after_two_purchases = coke_pepsi_prediction()
print(f"Probability of purchasing Coke two purchases from now given currently purchasing Pepsi: {probability_coke_after_two_purchases:.2f}")
