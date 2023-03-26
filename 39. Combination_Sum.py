def combinationSum(candidates, target):
    visited = []
    def contr(index, curent_list, sumary):
        if index >=len(candidates) or sumary>target:
            return
        if sumary==target:
            visited.append(curent_list.copy())
            return
        curent_list.append(candidates[index])
        contr(index,curent_list,sumary+candidates[index])
        curent_list.pop()
        contr(index+1,curent_list,sumary)
        
    contr(0,[],0)
    return visited
    
print(combinationSum([2,3,6,7],7))
