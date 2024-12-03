class mathop:
    def add(self):
        self.a=int(input("Enter first number:"))
        self.b=int(input("Enter second number:"))
        self.c=self.a+self.b
        print("Addition is:",self.c)
    def sub(self):
        self.a=int(input("Enter first number:"))
        self.b=int(input("Enter second number:"))
        self.c=self.a-self.b
        print("Subtraction is:",self.c)
    def mult(self):
        self.a=int(input("Enter first number:"))
        self.b=int(input("Enter second number:"))
        self.c=self.a*self.b
        print("Multiplication is:",self.c)
    def div(self):
        self.a=int(input("Enter first number:"))
        self.b=int(input("Enter second number:"))
        self.c=self.a/self.b
        print("Division is:",self.c)
obj=mathop()
while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.exit")
    ch=int(input("Enter choice to perform any operation:"))
    if ch==1:
        obj.add()
    elif ch==2:
        obj.sub()
    elif ch==3:
        obj.mult()
    elif ch==4:
        obj.div()
    elif ch==5:
        print("Program stop")
        break
    else:
        print("Wrong choice")
