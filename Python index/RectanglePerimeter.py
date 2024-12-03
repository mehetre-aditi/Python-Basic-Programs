class rectangle:
    def __init__(self,l2,w2):
        self.l=l2
        self.w=w2
    def area(self):
        self.a=self.l*self.w
        print("Area of reactngle : ",self.a)
    def perimeter(self):
        self.p=2*(self.l+self.w)
        print("Perimeter of rectangle : ",self.p)
l1=int(input("Enter length : "))
w1=int(input("Enter the breadth : "))
obj=rectangle(l1,w1)
obj.area()
obj.perimeter()
