class InvalidDateException(Exception):
    pass
class mydate:
    def accept(self):
        self.d=int(input("Enter Day : "))
        self.m=int(input("Enter Month : "))
        self.y=int(input("Enter Year : "))
    def display(self):
        try:
            if self.d>31:
                raise InvalidDateException("Day value is greater than 31")
            if self.m>12:
                raise InvalidDateException("Month value is greater than 12")
            print("Date is : ",self.d,"/",self.m,"/",self.y)
        except InvalidDateException as e:
            print(e)
obj=mydate()
obj.accept()
obj.display()