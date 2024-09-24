class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model
        Car.total_cars += 1

    def get_brand(self):
        return self.__brand + " !"

    def full_name(self):
        return f"{self.__brand} {self.model}"

    def fuel_type(self):
        return "Petrol or diesel"


class ElectricCar(Car):
    def __init__(self, brand, model, battery_Size):
        super().__init__(brand, model)
        self.battery_Size = battery_Size

    def fuel_type(self):
        return "Electric charge"


my_tesla = ElectricCar("Tesla", "Model S", "85kWh")
# print(my_tesla.model)
# print(my_tesla.full_name())
# print(my_tesla.get_brand())
print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")
print(safari.fuel_type())

print(safari.total_cars)


# my_car = Car("Toyota", "Corolla")
# print(my_car.brand)
# print(my_car.model)

# my_new_car = Car("Honda", "Civic")
# print(my_new_car.brand)
# print(my_new_car.model)

# print(my_car.full_name())
