class student:
    def accept(self):
        self.name=input("Enter student name: ")
        self.mark=int(input("Enter student total mark: "))
    def modify(self):
        self.oldmark=self.mark
        self.mark=int(input("Enter student total mark: "))
        print("Student name: ",self.name)
        print("Old mark: ",self.oldmark)
        print("New mark: ",self.mark)
s=student()
s.accept()
s.modify()