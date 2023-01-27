"""
+ class: cái gì đó chung chung, không cụ thể - blueprint
ví dụ: con gái, con trai, cặp sách, laptop, đồng hồ, đàn ông, đàn bà, con chim, sinh viên, ...
+ object: cái gì đó cụ thể - house
ví dụ: người bạn thân tên Lan, con mèo tên Mimi, sinh viên tên Khoa, truong Dong Khoi
"""


class Student:
    """
    + method: 1 hàm bên trong class
    + thuộc tính:
    - mã số sinh viên
    - tên
    - tuổi
    - điểm
    """
    def __init__(self, id, name, age, grades):
        self.id = id
        self.name = name
        self.age = age
        self.grades = grades

    def __str__(self):
        return f"{self.id} - {self.age} - {self.name} and {self.grades}"

    def average(self):
        return sum(self.grades) / len(self.grades)


# Create student objects
student_one = Student("SV001", "Bob", 23, [98, 67, 75, 88])
student_two = Student("SV002", "Khoa", 12, [50, 75, 36, 87])

# grades = student_one.grades
# total = sum(grades)
# length = len(grades)
#
# average = total / length
# print(f"Average: {average:.2f}")

print(student_one.average())
print(student_two.average())
