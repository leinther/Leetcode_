def findDuplicate(nums):
    dp = [0]*len(nums)

    for num in nums:
        dp[num] +=1
        if dp[num]==2:
            return num
    return dp    

        

   
    
    
print(findDuplicate([1,3,4,2,2]))   #[1,2,3,4,5,6]
                                   # 1+2+3+4+5+6