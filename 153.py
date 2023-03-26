def findMin(nums):
    def binary_search(nums,start,end):
        mid = (start + end)//2
        left,right = nums[mid],nums[mid]
        
        for i in nums[:mid]:
            if i<left:
                left = i

        for e in nums[mid:]:
            if e<right:
                right = e
            
        if left>right:
            return right
        else:
            return left
        
    
    return binary_search (nums,0,(len(nums)-1))
    
print (findMin(nums = [11,13,15,17]))