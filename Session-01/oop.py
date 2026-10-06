class student:
    def __init__(self, name, student_id, major,age):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.age = age
        
    def info(self):
        print("name :", self.name)
        print("id : ", self.student_id)
        print("major : ", self.major)
        print("age : ", self.age)
        print("__" * 10)
        
student1 =student("Kosar", 114, "Camputer", 20)
student2= student("Sara", 118, "Math", 21)
student3= student("Zahra", 124, "physic", 24)

student1.info()
student2.info()
student3.info()

