from venv import create


class IProduct:
    def release(self):
        pass


class Car(IProduct):
    def release(self):
        print("Car released")

class Truck(IProduct):
    def release(self):
        print("Truck released")

class IWorkShop:
    def create(self):
        pass

class CarWorkshop(IWorkShop):
    def create(self):
        return Car()

class TruckWorkshop(IWorkShop):
    def create(self):
        return Truck()

if __name__ == "__main__":
    creator = CarWorkshop()
    car = creator.create()

    creator = TruckWorkshop()
    truck = creator.create()

    car.release()
    truck.release()