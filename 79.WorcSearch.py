def exist(board, word):
    word = [i for i in word]
    ans = []
    
    for i in word:
        for e in board:
            if i in e:
                ans.append(i)
                e.remove(i)
                break
    
    if ans == word:
        return True 
    else:
        return False
    
    
    


print (exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
[["a","b"],
 ["c","d"]]