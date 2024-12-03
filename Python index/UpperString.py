class myclass:
    def getstring(self):
        self.mystr=input("Enter the String : ")
    def printstring(self):
        s=self.mystr
        print("String in uppercase : ",s.upper())
obj=myclass()
obj.getstring()
obj.printstring()