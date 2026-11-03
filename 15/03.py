class Car:
    total = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.count()

    @classmethod
    def count(cls):
        cls.total += 1


print(f"Total cars: {Car.total}")
car_1 = Car("Toyota", "Camry")
print(f"Total cars: {Car.total}")
car_2 = Car("Honda", "Civic")
car_3 = Car("Ford", "Mustang")
print(f"Total cars: {car_3.total}")
print(f"Total cars: {car_1.total}")


class Truck(Car):
    total = 0

    def __init__(self, make, model, payload):
        super().__init__(make, model)
        self.payload = payload


print(f"Total trucks: {Truck.total}")
truck_1 = Truck("Ford", "F-150", 1000)
truck_2 = Truck("Chevrolet", "Silverado", 1200)
print(f"Total cars: {Car.total}")
print(f"Total trucks: {Truck.total}")
