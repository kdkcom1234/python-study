class Car:
  brand = ""
  model = ""
  year = ""

  def __init__(self, brand, model, year) -> None:
    self.brand = brand
    self.model = model
    self.year = year

  def start_engine(self):
    print("Engine started")

class ElectricCar(Car):
  battery_size = 0

  def __init__(self, brand, model, year, battery_size) -> None:
    super().__init__(brand, model, year)
    self.battery_size = battery_size

  def start_engine(self):
    print("Slient Engine started")

class Convertible(Car):
  roof_status = False

  def __init__(self, brand, model, year) -> None:
    super().__init__(brand, model, year)
    self.roof_status = False

  def toggle_roof(self):
    self.roof_status = not(self.roof_status)

class LuxuryElectricConvertible(ElectricCar, Convertible):
  pass 

car = Car(brand="Kia", model="Niro", year="2020")
print(car.brand, car.model, car.year)
car.start_engine()

ev_car = ElectricCar(brand="Kia", model="EV6", year="2022", battery_size=5000)
print(ev_car.brand, ev_car.model, ev_car.year, ev_car.battery_size)
ev_car.start_engine()

print("----------")
lux_car= LuxuryElectricConvertible(brand="Porshe", model="Vision", year="2024", battery_size=10000)
print(lux_car.brand, lux_car.model, lux_car.year, lux_car.battery_size)
print(lux_car.roof_status)
lux_car.toggle_roof()
print(lux_car.roof_status)