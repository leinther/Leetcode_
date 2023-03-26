def rob(nums):
    prev1 = 0 
    prev2 = 0 
    
    for num in nums:
        dp = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = dp

    return prev1
    
    
print (rob([1,2,3,1]))