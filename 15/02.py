class MyClass:
    def __init__(self, value):
        self.value = value

    def display(self):  # self = obj_1
        print(f"MyClass value: {self.value}")  # obj_1.value

    @staticmethod
    def formula(x, y):  # self = obj_1, x = 3, y = 4
        return (x ** 2 + y ** 2) ** 0.5


obj_1 = MyClass(10)
print(obj_1.value)
obj_1.display()  # -> display(obj_1)
print(obj_1.formula(3, 4))  # -> formula(obj_1, 3, 4)  -> staticmethod  -> formula(3, 4)

print(MyClass.formula(3, 4))  # -> formula(3, 4)  -> staticmethod  -> formula(3, 4)
