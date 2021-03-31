def reverse(k): 
    str = "" 
    for i in k: 
        str = i + str 
    return str 

k = input('word:')
print ("awal : ",end="") 
print (k) 

print ("dibalik : ",end="") 
print (reverse(k)) 

