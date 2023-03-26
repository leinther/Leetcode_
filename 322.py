def coinChange(coins, amount):
    dp = [0] + [amount + 1] * amount
    
    for coin in coins:
        for i in range(coin,amount+1):
            dp[i] = min(dp[i],dp[i-coin]+1)

    return dp
        


print (coinChange(coins = [1,2,5], amount = 11))


