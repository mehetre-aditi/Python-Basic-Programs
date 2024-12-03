class myclass:
    def getstring(self):
        self.mystr=input("Enter any string : ")
    def reversestring(self):
        s=self.mystr
        cnt=len(s)
        i=cnt-1
        r=""
        while(i>=0):
            r=r+s[i]
            i=i-1
        print("String in reverse: ",r)
obj=myclass()
obj.getstring()
obj.reversestring()