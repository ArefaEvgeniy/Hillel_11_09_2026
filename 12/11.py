class Auto(object):

    def __init__(self, made, model, color, speed=300):
        self.made = made
        self.model = model
        self.color = color
        self.speed = speed

    def get_info(self, speed=0):
        print(f'Made: {self.made}, Model: {self.model}, Color: {self.color}, Speed: {speed}')


car_1 = Auto('Toyota', 'Camry', 'Red')
car_1.made = 'Toyota'
car_1.model = 'Camry'
car_1.color = 'Red'

car_2 = Auto('Honda', 'Civic', 'Blue')
# car_2.made = 'Honda'
# car_2.model = 'Civic'
# car_2.color = 'Blue'

car_1.get_info(160)
car_2.get_info(200)

