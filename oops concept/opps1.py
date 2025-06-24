# 1]create a car class with attribute like brand,model and year.include a method to display full details of the car.

class Car:
   
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year:", self.year)


my_car = Car("Honda", "City", 2022)

my_car.show_details()
