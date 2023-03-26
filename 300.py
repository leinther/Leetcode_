def lengthOfLIS(nums):
    n = len(nums)
    dp = [1] *n
    
    for i in range(1, len(nums)):
          for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)  
    

    return dp
     
print (lengthOfLIS([10,9,2,5,3,7,101,18])) 

