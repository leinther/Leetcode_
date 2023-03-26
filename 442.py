def findDuplicates(nums):
    ans =[]
    nums.sort()
    
    prev = 0
    
    for i in nums:
        if i==prev:
            ans.append(i)
            continue
        prev=i
        
    return ans
    
    
print(findDuplicates([1]))      