class student:
    def getstudent(self):
        self.rollno=int(input("Enter student roll number : "))
        self.name=input("Enter student name : ")
        self.age=int(input("Enter student age : "))
        self.gender=input("Enter student gender : ")
    def putstudent(self):
        print("Student Roll number : ",self.rollno)
        print("Student Name : ",self.name)
        print("Student Age : ",self.age)
        print("Student gender : ",self.gender)
class test(student):
    def getmarks(self):
        self.marathi=int(input("Enter marks for marathi : "))
        self.hindi=int(input("Enter marks for hindi : "))
        self.english=int(input("Enter marks for english : "))
    def putmarks(self):
        print("Marks for Students : ")
        print("Marathi : ",self.marathi)
        print("hindi : ",self.hindi)
        print("English : ",self.english)
        print("Total : ",self.marathi+self.hindi+self.english)
obj=["s1","s2","s3"]
for i in range(0,3):
    obj[i]=test()
    obj[i].getstudent()
    obj[i].getmarks()
    print("Display details of student : ")
    obj[i].putstudent()
    obj[i].putmarks()
    