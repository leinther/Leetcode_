def maxSubArray(nums):
    dp = [0] * len(nums)

    dp[0] = nums[0]
    for i in range(1, len(nums)):
      dp[i] = max(nums[i], dp[i - 1] + nums[i])

    return dp
print (maxSubArray([-2,1]))