class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

    def refuel(self):
        return "Refueling..."


class Car(Vehicle):
    def __init__(self, make, model, year, num_doors):
        # Call the parent's constructor
        super().__init__(make, model, year)
        self.num_doors = num_doors

    def get_info(self):
        # Override to add door information
        return f"{self.year} {self.make} {self.model} ({self.num_doors} doors)"


class ElectricCar(Car):
    def __init__(self, make, model, year, num_doors, battery_range):
        # Call the parent's (Car's) constructor
        super().__init__(make, model, year, num_doors)
        self.battery_range = battery_range

    def get_info(self):
        # Override to add battery information
        return f"{self.year} {self.make} {self.model} ({self.num_doors} doors) - {self.battery_range}km range"

    def refuel(self):
        # Override to change refueling behavior
        return "Recharging..."
