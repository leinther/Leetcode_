def miss(nums):
    nums_sort = sorted(nums) #[0,1] #[0,1,2]


    for i in range(len(nums_sort)+1):
        if i not in nums:
            return i
    



print(miss([0,1]))  
