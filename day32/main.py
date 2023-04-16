import array, sys

class Student:
    def __init__(self):
        self.name = "John"
        self.age = 100
        self.is_married = True

student_info = ["John Smith", 24, False, Student()]
print(sys.getsizeof(student_info))

numbers = array.array('i', [1, 2, 3, 2])
print(sys.getsizeof(numbers))
