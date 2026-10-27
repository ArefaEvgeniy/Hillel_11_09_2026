class Woman:
    """
    sfsfs
    sdfsdfse
    dsfsfe
    """
    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        """
        计算体重
        dfsdfew
        :return:
        """
        if self.__weight < 50:
            return self.__weight * 1.1
        elif self.__weight > 70:
            return self.__weight * 0.9
        return self.__weight


woman_1 = Woman("Alice", 30, 100)
print(woman_1.name)
print(woman_1._age)
print(woman_1._Woman__weight)
print(woman_1.get_weight())
