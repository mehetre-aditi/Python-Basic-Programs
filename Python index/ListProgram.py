a=[1,1,2,3,5,8,13,21,34,55,89]
cnt=len(a)
print("Length of a list : ",cnt)
for i in range(0,cnt):
    if a[i]<5:
        print(a[i],end=" ")