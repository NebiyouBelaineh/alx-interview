#!/usr/bin/python3
"""Make change challenge"""
def makeChange(coins, total):
    """Given a pile of coins of different values,
    determine the fewest number of coins needed
    to meet a given amount total
    """
    if total <= 0:
        return 0
    
    # Initialize a list to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: no coins are needed to make the amount 0

    # Compute the minimum number of coins needed for each amount from 1 to total
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means that total cannot be made with the given coins
    return dp[total] if dp[total] != float('inf') else -1
