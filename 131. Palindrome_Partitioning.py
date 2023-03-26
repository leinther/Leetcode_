def partition(s):
    visited = []

    def dfs(index,cur_list,s):

        if index >= len(s):
            return visited
        res = s[index:]
        if res == res[::-1]:
            cur_list.append(res)
        dfs (index+1,cur_list,s)     
    
    
    
    dfs (0,[],s)
    return visited[0]+visited[1]
print (partition("aab"))

#[["a","a","b"],["aa","b"]]


#[a,a,b] [a+a,a+b] [a+a+b]
#[b,a,a,b] [ba,ab] [baa,b]