def trans_air(nums):
    out = 0
    for i in range(len(nums)):

        out = out^nums[i]
    return out
   

print(trans_air([2,1,4,1,2]))  #[1,2,2] 