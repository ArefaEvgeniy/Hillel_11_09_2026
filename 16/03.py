class MyIter:
    def __init__(self, data):
        self.data = data

    def __next__(self):
        self.data += self.data
        return self.data


iter = MyIter(2)
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
print(next(iter))
