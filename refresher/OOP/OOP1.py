class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student("Rolf", (90, 90, 93, 78, 90))
student2 = Student("Bob", (100, 90, 97, 84, 90))


print(student.name)
print(student.average_grade())

print(student2.name)
print(student2.average_grade())











# student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}
#
# def average(sequence):
#     return sum(sequence) / len(sequence)
#
#
# print(average(student["grades"]))
# print(student.average())


