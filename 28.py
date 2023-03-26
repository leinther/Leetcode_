def strStr(haystack, needle):
    if haystack==needle:
        return 0
    n = len(needle)
    curent = 0
    while curent!=len(haystack):
        print(haystack[curent:curent+n])
        if haystack[curent:curent+n] == needle:
            return curent
        curent+=1
    return -1

print (strStr("abc","c"))