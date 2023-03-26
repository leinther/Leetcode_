def longestConsecutive(nums):
    numbers = list(set(nums))
    count = 0
    for num in numbers:
        if num-1 in numbers:
            continue
        lenght = 0 
        while num in numbers:
            num+=1
            lenght+=1
        count = max(count,lenght)
            
            
        
    
    
    return count
        

    #[0,3,7,2,5,8,4,6,0,1]
    #[9,1,4,7,3,-1,0,5,8,-1,6]
    #[0,-1]
    #[100,4,200,1,3,2]
    
print(longestConsecutive(nums = [9,1,4,7,3,-1,0,5,8,-1,6]))