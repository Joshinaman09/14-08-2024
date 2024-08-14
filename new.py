class Car:
  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  def display_info(self):
    print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Create a Car object
my_car = Car("Toyota", "Camry", 2022)

# Call the display method
my_car.display_info()