def search(nums, target):
    low = 0 
    high = len(nums)-1
    mid = (low+high)//2 
    
    if nums[mid]==target:
        return True
    
    
    for i in nums[:mid]:
        if i == target:
            return True
    for e in nums[mid:]:
        if e == target:
            return True
    return False 

print(search(nums = [2,5,6,0,0,1,2], target = 3))