import pandas as pd

users_df = pd.read_csv("users.csv")
flights_df = pd.read_csv("flights.csv")
hotels_df = pd.read_csv("hotels.csv")

# Merge the necessary information from the dataframes to create a unified dataset
merged_df = pd.merge(users_df, flights_df, left_on='code', right_on='userCode')
merged_df = pd.merge(merged_df, hotels_df, on='travelCode')

# Implement the Dynamic Programming Algorithm
def maximize_attractions(cities, budget):
    num_cities = len(cities)
    budget = int(budget)  # Convert budget to integer

    
    # Create a 2D table to store the maximum number of attractions for each state
    dp = [[0] * (budget + 1) for _ in range(num_cities + 1)]

    # Iterate over the cities and budget
    for i in range(1, num_cities + 1):
        city = cities[i - 1]
        attraction_cost = merged_df.loc[merged_df['city'] == city, 'attraction_cost'].values[0]
        attraction_count = merged_df.loc[merged_df['city'] == city, 'attraction_count'].values[0]
        
        for j in range(1, budget + 1):
            if attraction_cost > j:
                # If the attraction cost is higher than the remaining budget, skip it
                dp[i][j] = dp[i - 1][j]
            else:
                # Consider whether to visit the current attraction or skip it
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - attraction_cost] + attraction_count)

    # Backtrack to find the selected attractions
    selected_attractions = []
    i = num_cities
    j = budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            city = cities[i - 1]
            selected_attractions.append(city)
            j -= merged_df.loc[merged_df['city'] == city, 'attraction_cost'].values[0]
        i -= 1

    # Return the recommended cities
    return selected_attractions[::-1]

# Track the Optimal Solution
def get_recommendations(user, budget, num_cities):
    # Get the list of cities the user wants to visit
    user_cities = ['city1', 'city2', 'city3']  # Replace with actual user input

    # Apply the dynamic programming algorithm to get the maximum attractions
    recommended_cities = maximize_attractions(user_cities, budget)

    if 'city' in merged_df.columns:
        recommended_cities = maximize_attractions(user_cities, budget)
    else:
        print("Error: 'city' column not found in the merged DataFrame.")

    return recommended_cities

# Prompt the user for input
user = input("Enter user name: ")
budget = float(input("Enter budget: "))
num_cities = int(input("Enter number of cities: "))

# Example usage
recommendations = get_recommendations(user, budget, num_cities)
print(recommendations)
print("Merged DataFrame:")
print(merged_df)
