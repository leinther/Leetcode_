
def trans_air(num):
    
    dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000,}
 
    result = 0
    prev = 1 
    for i in num[::-1]:
        if dict[i]> prev :
            result+=dict[i]
        elif dict[i]< prev:
            result-=dict[i]
        else:
            result+=dict[i]
        prev = dict[i]
    
    return result
print(trans_air("IIIVV"))  
