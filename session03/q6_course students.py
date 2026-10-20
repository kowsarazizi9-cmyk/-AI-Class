class Student:
    def __init__(self, name, id_student):
        self.name = name
        self.id_student = id_student
        self.grades = {}
        
    def add_grade(self, course, grade):
        if 0 <= grade <= 20:
            self.grades[course] = grade
        else:
            print("invalid grade")
        
    def average(self):
        if len(self.grades) == 0:
            return 0
        total = sum(self.grades.values())
        return total / len(self.grades)

    def best_courses(self):
        if len(self.grades) == 0:
            return "None"
        return max(self.grades, key=self.grades.get)
    
    def courses_failed(self):
        failed_list = []
        for course, grade in self.grades.items():
            if grade < 10:
                failed_list.append(course)
        return failed_list
    
    def status(self):
        avg = self.average()
        if avg >= 17:
            return "Excellent"
        elif avg >= 14:
            return "Good"
        elif avg >= 12:
            return "Normal"
        else:
            return "Probtion"
    
    def report(self):
        print(f"student: {self.name}| id:{self.id_student}")
        for course, grade in self.grades.items():
            print(f"{course}: {grade}")
        print(f"average: {self.average()}")
        print(f"best course: {self.best_courses()}")
        print(f"failed course: {self.courses_failed()}")
        print(f"students: {self.status()}")

sara = Student("Sara Ahmadi ", "40312345")
sara.add_grade("Math", 15)
sara.add_grade("Physics", 10)
sara.add_grade("Programing", 13)
sara.add_grade("English", 16)

kosar = Student("Kosar Azizi", "40359712")
kosar.add_grade("Math", 16)
kosar.add_grade("Physics", 14)
kosar.add_grade("Programing", 10)
kosar.add_grade("English", 8)

print("Sara Ahmadi: ")
sara.report()
print("Kosar Azizi: ")
kosar.report()
print("invalid")
sara.add_grade("Chemistry", 25)


class Classroom:
    def __init__(self):
        self.students =[]
        
    def add_student(self, student):
        self.students.append(student)
        
    def top_student(self):
        if len(self.students) ==0:
            return "No student in class"
        top = max(self.students, key=lambda s: s.average())
        return top.name
    
    def average_class(self):
        if len(self.students) == 0:
            return 0
        total_av =sum(s.average() for s in self.students)
        return total_av / len(self.students)
    
print("class test: ")
class_a =Classroom()
class_a.add_student(sara)
class_a.add_student(kosar)

print("Top student: ", class_a.top_student())
print("average: ", class_a.average_class())
