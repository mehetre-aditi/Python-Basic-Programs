class shape:
    pass
class square(shape):
    def __init__(self,l2):
        self.l=l2
    def sarea(self):
        a=self.l*self.l
        print("Area of square= ",a)
    def sperimeter(self):
        p=4*self.l
        print("Perimeter of square= ",p)
class circle(shape):
    def __init__(self,r2):
        self.r=r2
    def carea(self):
        a=3.14*self.r*self.r
        print("Area of circle= ",a)
    def circumference(self):
        c=2*3.14*self.r
        print("Area of circle= ",c)
l1=int(input("Enter length of the square:"))
obj=square(l1)
obj.sarea()
obj.sperimeter()
r1=int(input("Enter radius of circle:"))
obj=circle(r1)
obj.carea()
obj.circumference()

