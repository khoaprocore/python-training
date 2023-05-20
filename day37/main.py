# class Student:
#     def __init__(self, id, name, marks):
#         self.id = id
#         self.name = name
#         self.marks = marks

#     @property
#     def average(self):
#         if len(self.marks) == 0:
#             raise ValueError("Marks is empty!")

#         avg = sum(self.marks) / len(self.marks)
#         return format(avg, '.2f')

#     def __str__(self) -> str:
#         marks = ', '.join(map(str, self.marks[:-1])) + f" and {self.marks[-1]}"
#         return f"<Student {self.id}, {self.name}, {marks}>"


# student_one = Student("SV001", "John", [7.8, 6.7, 9.5])

# # print(student_one.id)
# # print(student_one.name)
# # print(student_one.marks)

# print(student_one.average)
# print(student_one)

# The Country class defines attributes and methods to compare population density and determine if a
# country is considered big based on its population and area.

# class Country:

#     def __init__(self, name, population, area):
#         self.name = name
#         self.population = population
#         self.area = area
#         self.density = population / area
#         self.is_big = population > 250_000_000 or area > 3_000_000


#     def compare_pd(self, other):
#         result = ['smaller', 'larger'][self.density > other.density] # True - 1 | False - 0
#         return f'{self.name} has a {result} population density than {other.name}'


# australia = Country('Australia', 23545500, 7692024)
# andorra = Country('Andorra', 76098, 468)
# brazil = Country('Brazil', 202794000, 8515767)
# china = Country('China', 1393000000, 9597000)
# madagascar = Country('Madagascar', 26260000, 587000)


# print(australia.is_big == True)
# print(australia.compare_pd(andorra) == 'Australia has a smaller population density than Andorra')

# print(andorra.is_big == False)
# print(andorra.compare_pd(australia) == 'Andorra has a larger population density than Australia')

# print(brazil.is_big == True)
# print(brazil.compare_pd(china) == 'Brazil has a smaller population density than China')

# print(china.is_big == True)
# print(china.compare_pd(madagascar) == 'China has a larger population density than Madagascar')

# print(madagascar.is_big == False)
# print(madagascar.compare_pd(australia) == 'Madagascar has a larger population density than Australia')

# class Magic:
#     def replace(self, s, ch1, ch2):
#         return s.replace(ch1, ch2)

#     def str_length(self, s):
#         return len(s)

#     def trim(self, s):
#         return s.strip()

#     def list_slice(self, lst, t):
#         a, b = t
#         return lst[a-1:b] or -1

# magic = Magic()
# print(magic.trim("  python is awesome  ") == "python is awesome")
# print(magic.str_length("Hello world!") == 12)
# print(magic.list_slice([1, 2, 3, 4, 5], (2, 4))[0] == 2)
# print(magic.list_slice([1, 2, 3, 4, 5], (-1, 4)) == [4])
# print(magic.replace("AzErty-QwErty", 'E','e') == "Azerty-Qwerty")

# def people_sort(lst, attr):
#     if attr == 'firstname':


# class Student:
#     name = "Khoa"
#     age = 12


# student = Student()

# print(student.name)
# print(getattr(student, 'name1', "boy"))

# def people_sort(lst, attr):
#     return sorted(lst, key=lambda x: getattr(x, attr))


# class Person:
#     def __init__(self, firstname, lastname, age):
#         self.firstname = firstname
#         self.lastname = lastname
#         self.age = age


# p1 = Person('Michael', 'Smith', 40)
# p2 = Person('Alice', 'Waters', 21)
# p3 = Person('Zoey', 'Jones', 29)
# p4 = Person('Susan', 'Heffley', 43)
# p5 = Person('Bob', 'Fredericson', 70)
# p6 = Person('Braxton', 'Leighsonley', 2)
# p7 = Person('Joshua', 'Senoron', 99999999999999)
# people = [p1, p2, p3, p4, p5, p6, p7]


# print(people_sort(people, 'firstname') == [p2, p5, p6, p7, p1, p4, p3])
# print(people_sort(people, 'lastname') == [p5, p4, p3, p6, p7, p1, p2])
# print(people_sort(people, 'age') == [p6, p2, p3, p1, p4, p5, p7])


# class Memories:
#     def __init__(self):
#         self.memory = {}

#     def add(self, **attrs):
#         self.memory.update(attrs)

#     def remember(self, key):
#         return self.memory.get(key, False)
    

# memories = Memories()
# # Add to memories.
# memories.add(purpose="lol idk", social_life="What's that?", dream="money")
# memories.add(fears="code", languages=["english", "filipino", "python", "Java"])
# memories.add(favorite_number=404, is_gamer=True, race="Filipino", gender="M", name="Shane", embarassing_moments="dance with her.. oh god", omai_wa_mo_shindeiru="NANI?!")
# memories.add(strength_level="Over 9000!!!")

# # Test if we could remember.
# print(memories.remember("fears") == "code")
# print(memories.remember("race") == "Filipino")
# print(memories.remember("dream") == "money")
# print(memories.remember("is_gamer") == True)
# print(memories.remember("name") == "Shane")
# print(memories.remember("strength_level") == "Over 9000!!!")

class Employee:
    def __init__(self, full_name, **kwargs):
        fname, lname = full_name.split()
        self.name = fname
        self.lastname = lname

        for k, v in kwargs.items():
            
            setattr(self, k, v)

john = Employee('John Doe')
mary = Employee('Mary Major', salary=120000)
richard = Employee('Richard Roe', salary=110000, height=178)
giancarlo = Employee('Giancarlo Rossi', salary=115000, height=182, nationality='Italian')
peng = Employee('Peng Zhu', salary=500000, height=185, nationality='Chinese', subordinates=[i.lastname for i in (john, mary, richard, giancarlo)])


print(john.lastname == 'Doe')
print(mary.salary == 120000)
print(richard.height == 178)
print(giancarlo.nationality == 'Italian')
print(peng.subordinates == ['Doe', 'Major', 'Roe', 'Rossi'])