def create_array(n):
    res=[]
    i=1
    while i<=n: 
        res=res+[i]
        i+=1
    return res
        

print (create_array(5))