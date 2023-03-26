def climbStairs(s):
    if s == s[::-1]:
        return s
    
    dp = s[0]
    temp = ""
    
    
    for i in range(len(s)):
        for e in range(len(s)-1,i,-1):
            if s[i] == s[e]:
                temp = s[i:e+1]
                if s[i:e+1] == temp[::-1]:
                    if len(s[i:e+1])>len(dp):
                        dp = s[i:e+1]
                        
    return dp
    
print (climbStairs("cccc")) 