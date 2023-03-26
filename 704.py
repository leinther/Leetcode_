def search(nums, target):
    def bin_search(nums,target,start,end):
        if start>end:
            return -1
        mid = (start+end)//2
        if target==nums[mid]:
            return mid

        elif target<nums[mid]:
            return bin_search(nums,target,start,mid-1)
        else:
            return bin_search(nums,target,mid+1,end)
    return bin_search(nums,target,0,len(nums)-1)   

print(search(nums = [-1,0,3,5,9,12], target = 2))