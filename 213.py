def rob(nums):
    n = len(nums)
    

    
    def rob (l,r):
        dp1 = 0
        dp2 = 0
        for i in range(l,r+1):
            temp = dp1
            dp1 = max(dp1,dp2+nums[i])
            dp2 = temp
        
        return dp1    
            
    return max(rob(0,n-1),rob(1,n-2)) 


print (rob([2,3,2]))# [4,1,2,7,5,3,1]((n - i)-1)*-1