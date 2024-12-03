def abc():
    s=input("Enter string: ")
    cnt=len(s)
    n=" "
    for i in range(0,cnt):
        if i%2==0:
            print(s[i],end="")
abc()