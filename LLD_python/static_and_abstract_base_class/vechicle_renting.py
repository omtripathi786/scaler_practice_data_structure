from abc import ABC, abstractmethod


# Implement Rentable class
class Rentable(ABC):
    @abstractmethod
    def rent(self):
        pass

    @abstractmethod
    def return_item(self):
        pass


# Implement the Car class and its methods
class Car(Rentable):
    def __init__(self, car_model):
        self.car_model = car_model
        self.is_rented = False

    def rent(self):
        if not self.is_rented:
            self.is_rented = True
            print(f"Car {self.car_model} is now rented.")
        else:
            print(f"Car {self.car_model} is already rented.")

    def return_item(self):
        if self.is_rented:
            self.is_rented = False
            print(f"Car {self.car_model} is now returned.")
        else:
            print(f"Car {self.car_model} is not rented.")


# Implement the Bicycle class and its methods
class Bicycle(Rentable):
    def __init__(self, bicycle_model):
        self.bicycle_model = bicycle_model
        self.is_rented = False

    def rent(self):
        if not self.is_rented:
            self.is_rented = True
            print(f"Cycle {self.bicycle_model} is now rented.")
        else:
            print(f"Cycle {self.bicycle_model} is already rented.")

    def return_item(self):
        if self.is_rented:
            self.is_rented = False
            print(f"Cycle {self.bicycle_model} is now returned.")
        else:
            print(f"Cycle {self.bicycle_model} is not rented.")


# Example usage
if __name__ == "__main__":
    # Test Car
    car = Car("Tesla Model 3")
    car.rent()          # Car Tesla Model 3 is now rented.
    car.rent()          # Car Tesla Model 3 is already rented.
    car.return_item()   # Car Tesla Model 3 is now returned.
    car.return_item()   # Car Tesla Model 3 is not rented.

    # Test Bicycle
    bicycle = Bicycle("Mountain Bike")
    bicycle.rent()          # Cycle Mountain Bike is now rented.
    bicycle.rent()          # Cycle Mountain Bike is already rented.
    bicycle.return_item()   # Cycle Mountain Bike is now returned.
    bicycle.return_item()   # Cycle Mountain Bike is not rented.
