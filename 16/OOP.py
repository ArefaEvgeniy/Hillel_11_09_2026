import time


class BaseClass:
    def get_data(self):
        ...

    def process_data(self):
        ...

    def print_data(self):
        ...


class Processor(BaseClass):
    def get_data(self):
        ...

    def process_data(self):
        ...


class Memory(BaseClass):
    def get_data(self):
        ...


class Processors(BaseClass):
    def get_data(self):
        ...

    def process_data(self):
        ...

    def print_data(self):
        ...


class Temperature(BaseClass):
    def get_data(self):
        ...

    def process_data(self):
        ...

    def print_data(self):
        ...


class App:
    def __init__(self):
        self.data = [Processor(), Memory(), Processors(), Temperature()]

    def run(self):
        while True:
            for obj in self.data:
                obj.get_data()
                obj.process_data()
                obj.print_data()

            time.sleep(3)


App().run()
