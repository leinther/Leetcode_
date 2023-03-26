def maxProfit(prices):
    dp = [0] * (len(prices))
    minimum = prices[0]
    for i in range(1, len(prices)):
        if prices[i]<minimum:
            minimum = prices[i]
        dp[i] = max (dp[i-1], prices[i]-minimum)
    return dp
        
            
        
    

    
    
print (maxProfit([2,1,2,0,1]))