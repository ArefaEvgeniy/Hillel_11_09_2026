class MyIter:
    def __init__(self, data):
        self.data = data.split()
        self.index = 0

    def __next__(self):
        if self.index < len(self.data):
            word = self.data[self.index]
            self.index += 1
            return word.title().strip(",.")
        else:
            raise StopIteration


class MyStr(str):
    def __iter__(self):
        return MyIter(self)


my_str = MyStr("This is a sample, string FOR testing.")

for item in my_str:
    print(item)
