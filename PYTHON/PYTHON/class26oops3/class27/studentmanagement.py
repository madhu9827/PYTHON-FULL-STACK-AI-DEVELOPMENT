class studentmanage:
    def __init__(self):
        self.students=[]
    def addstudent(self,id,name,age):
        student={"id":id,"name":name,"age":age}
        self.students.append(student)
        print("student added",student)
    def update_student(self,sid,new_name):
        for student in self.students:
            if student["id"]==sid:
                student["name"]=new_name
                print("Updated Student:", student)
                return
            print("Student with id", sid, "not found.")
obj=studentmanage()
obj.addstudent(1,"madhu",23)
obj.addstudent(2,"tanuj",26)
print(obj.__dict__)
obj.update_student(1,"madhu yadav")
print(obj.__dict__)

