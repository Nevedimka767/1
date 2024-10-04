class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def get_info(self):
        return f"{self.make}{self.model}{self.year}"
my_car = Car("SsangYong ", "Korando ", 2013)
print(my_car.get_info())
