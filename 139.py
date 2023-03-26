def wordBreak(s, wordDict):
    dp = [True] + [False] * len(s)
    n = len(s)  
    wordDict = set(wordDict)
    
    
    for i in range(1,n+1):
        for j in range(i):
            if dp[j] and s[j:i] in wordDict:
                dp[i]=True  
                break
    
    
    
    return dp[n]
    

                

    
print(wordBreak( s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))