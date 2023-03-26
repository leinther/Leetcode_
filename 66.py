def plusOne(digits):
    for i in range(len(digits)-1,-1,-1):
        if i == 0 and digits[i]==9:
            digits[i]=0
            digits.insert(0,1)
            break
        if digits[i]== 9:
            digits[i]=0
   
        else:
            digits[i]=digits[i]+1
            break
            
    return digits
    
    
print (plusOne(digits = [5559]))