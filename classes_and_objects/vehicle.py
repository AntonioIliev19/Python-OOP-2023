class Vehicle:
    def __init__(self, mileage: float, max_speed: int = 150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []


car = Vehicle(20)

print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.max_speed = 200
car.gadgets.append('Hudly Wireless')
print(car.max_speed)
print(car.gadgets)