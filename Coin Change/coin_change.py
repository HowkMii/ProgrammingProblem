# DP Solution to the Coin Change algorithm:
def count(coins, n, sum):
    # Do not include any coin if the sum of coins is 0:
    if (sum == 0):
        return 1

    # No solution if the sum is subzero:
    if (sum < 0):
        return 0

    # If no coins but solution is above zero, still no solution:
    if (n <= 0):
        return 0

    # Recursive function includes coins[n-1], excluding coins[n-1]
    return count(coins, n - 1, sum) + count(coins, n, sum-coins[n-1])

# Different coin values and dynamic sum:
coins = [1, 2, 3]
finalSum = 13
print(count(coins, len(coins), finalSum))
