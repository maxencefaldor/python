from q7 import Vehicle, Car, ElectricCar


def test_vehicle():
    v = Vehicle("Ford", "Ranger", 2021)
    print(v.get_info())
    print(v.refuel())
    assert v.get_info() == "2021 Ford Ranger"
    assert v.refuel() == "Refueling..."


def test_car():
    c = Car("Honda", "Civic", 2023, 4)
    print(c.get_info())
    print(c.refuel())
    assert c.get_info() == "2023 Honda Civic (4 doors)"
    assert c.refuel() == "Refueling..."  # Inherited from Vehicle
    assert isinstance(c, Vehicle)


def test_electric_car():
    ec = ElectricCar("Tesla", "Model 3", 2024, 4, 500)
    print(ec.get_info())
    print(ec.refuel())
    assert ec.get_info() == "2024 Tesla Model 3 (4 doors) - 500km range"
    assert ec.refuel() == "Recharging..."  # Overridden
    assert isinstance(ec, Car)
    assert isinstance(ec, Vehicle)


if __name__ == "__main__":
    test_vehicle()
    test_car()
    test_electric_car()
