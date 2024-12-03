t=(1,1,2,2,3,3,4,4,5)
print(t)
abc=[]
print("repeated elements in given tuple: ")
for i in range(0,len(t)):
    if(t.count(t[i]>1)):
        if t[i] not in abc:
            abc.append(t[i])
print(abc)