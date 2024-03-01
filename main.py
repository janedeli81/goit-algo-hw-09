def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count
            if amount == 0:
                break
    return result

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [0] + [float('inf')]*amount
    track = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin:
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    track[i] = coin

    # Backtrack to find the coins used
    result = {}
    while amount > 0:
        coin = track[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin

    return result

# Example usage
amount = 113
greedy_result = find_coins_greedy(amount)
dp_result = find_min_coins(amount)

print("Greedy Algorithm:", greedy_result)
print("Dynamic Programming:", dp_result)
