def weather_prediction():
    # Initial probabilities
    P0_N = 1.0  # Probability that today is not rainy
    P0_R = 0.0  # Probability that today is rainy
    
    # Transition probabilities
    P_RR = 0.4  # Probability that if today is rainy, tomorrow is also rainy
    P_RN = 0.6  # Probability that if today is rainy, tomorrow is not rainy
    P_NR = 0.2  # Probability that if today is not rainy, tomorrow is rainy
    P_NN = 0.8  # Probability that if today is not rainy, tomorrow is not rainy
    
    # Calculate probabilities for tomorrow
    P1_N = P_NN * P0_N + P_RN * P0_R
    P1_R = P_NR * P0_N + P_RR * P0_R
    
    # Calculate probabilities for the day after tomorrow
    P2_N = P_NN * P1_N + P_RN * P1_R
    P2_R = P_NR * P1_N + P_RR * P1_R
    
    return P2_N

# Output the result
probability_not_rain_day_after_tomorrow = weather_prediction()
print(f"Probability that it will not rain the day after tomorrow given that it is not raining today: {probability_not_rain_day_after_tomorrow:.2f}")

