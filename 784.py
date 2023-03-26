def letterCasePermutation(s):
    s = s.lower()
    ans = []
    lenght = len(s)
    
    def dfs(i, res = ""):
        if i<lenght:
            dfs (i+1, res + s[i])
            if s[i].islower():
                dfs(i+1,res + s[i].upper())
        else:
            ans.append(res)
            
    dfs (0)   
            
            
        
    
    
    
    return ans
    
print (letterCasePermutation("a1b2"))