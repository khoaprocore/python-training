"""
class HocSinh
object
"""


class SchoolBoy:
    def __init__(self, id, grade, clas, name, phone_number):
        self.id = id
        self.grade = grade
        self.clas = clas
        self.name = name
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.id}, {self.grade}, {self.clas}, {self.name}, {self.phone_number}"


school_boy1 = SchoolBoy("HS014", 6, "6/1", "Dang Khoa", "0974500342")

print(school_boy1)
