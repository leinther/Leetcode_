def removeDuplicates(nums):
    
    start = nums[0]
    end = nums[-1]
    ans = []
    for i in range(start,end+1):
        ans.append(i)
    
    return end, ans    
    
          
    



   

print(removeDuplicates([1,1,2]))