# Модифікуйте клас Група (завдання минулої лекції) так, щоб при спробі
# додавання до групи більше 10-ти студентів, було порушено виняток користувача.
# Таким чином потрібно створити ще й виняток користувача для цієї ситуації. І
# обробити його поза межами класу. Тобто. потрібно перехопити цей виняток, при
# спробі додавання 11-го студента


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years old"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"


class GroupOverflowError(Exception):
    def __init__(self, message="У групі не може бути більше 10 студентів!"):
        self.message = message
        super().__init__(self.message)


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupOverflowError("У групі вже 10 студентів! Більше додавати не можна.")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join([str(student) for student in self.group])
        return f'Number:{self.number}\n{all_students}'


mygr = Group("GR1")
for item in range(10):
    mygr.add_student(Student("Male", 20, "student"+str(item), "student"+str(item), "AG88"+str(item)))
print(mygr)
print(len(mygr.group))

try:
    mygr.add_student(Student("Male", 20, "student"+"11", "student"+"11", "AG88"+"11"))
except GroupOverflowError as e:
    print(e)
print(len(mygr.group))
