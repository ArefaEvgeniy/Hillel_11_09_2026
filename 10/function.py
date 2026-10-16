import time


def get_data():

    def get_processor(data):
        new_data = []
        ...
        return new_data

    def get_memory(data):
        new_data = []
        ...
        return new_data

    def get_processors(data):
        new_data = []
        ...
        return new_data

    data = {}
    data = get_processor(data)
    data = get_memory(data)
    data = get_processors(data)

    return data


def process_data(data):
    new_data = {}
    ...
    return new_data


def print_data(data):
    ...


def main():
    while True:
        data = get_data()
        new_data = process_data(data)
        print_data(new_data)
        time.sleep(2)


main()
