def searchMatrix(matrix, target):
    start = 0
    end = len(matrix)-1
    mid = (start+end)//2
    
    for i in matrix[mid]:
        if i == target:
            return True 
        
    for left in matrix[:mid]:
        for l in left:
            if l == target:
                return True 
    for right in matrix[mid:]:
            for r in right:
                if r == target:
                    return True 
    return False
    
    
    
print (searchMatrix(matrix = [[1],[3]], target = 3))