def search(nums, target):
    low = 0 
    high = len(nums)-1
    
    mid = (low+high)//2 
    
    for i in nums[:mid]:
        if i == target:
            return nums.index(i)
    for e in nums[mid:]:
        if e == target:
            return nums.index(e)
    return -1 

print(search(nums = [1], target = 0))