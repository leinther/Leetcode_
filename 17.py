def letterCombinations(digits):
    if digits == "":
        return []
    number = {"2": ["a","b","c"], "3":["d","e","f"], "4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"] ,"8":["t","u","v"] ,"9":["w","x","y","z"]}
    number = [number[i] for i in digits]
    visited  = []
            
    def dfs(ind,path):
        if len(path) == 3:
            return 
        
        
            
        
        
    
    
print (letterCombinations("237"))       #[['a', 'b', 'c'], ['d', 'e', 'f'],["p","q","r","s"]]
                                        #["ad","ae","af","bd","be","bf","cd","ce","cf"] digits = "23"
                                        #digits = "2" ["a","b","c"]