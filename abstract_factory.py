from abc import ABCMeta, abstractmethod


class IEngine(metaclass=ABCMeta):
    @abstractmethod
    def release_engine(self):
        pass

class JapaneseEngine(IEngine):
    def release_engine(self):
        print("Японський двигун")

class UkrainianEngine(IEngine):
    def release_engine(self):
        print("Український двигун")

class ICar(metaclass=ABCMeta):
    @abstractmethod
    def release_car(self):
        pass

class JapaneseCar(ICar):
    def release_car(self,engine:IEngine):
        print("Японська машина")
        engine.release_engine()

class UkrainianCar(ICar):
    def release_car(self,engine:IEngine):
        print("Українська машина")
        engine.release_engine()


class IFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_engine(self,car_type:str) -> IEngine:
        pass

    @abstractmethod
    def create_car(self) -> ICar:
        pass

class JapaneseFactory(IFactory):
    def create_engine(self):
        return JapaneseEngine()

    def create_car(self) -> ICar:
        return JapaneseCar()

class UkrainianFactory(IFactory):
    def create_engine(self):
        return UkrainianEngine()

    def create_car(self) -> ICar:
        return UkrainianCar()


if __name__ == "__main__":
    j_fabric = JapaneseFactory()
    j_engine = j_fabric.create_engine()
    j_car = j_fabric.create_car()

    j_car.release_car(j_engine)

    u_fabric = UkrainianFactory()
    u_engine = u_fabric.create_engine()
    u_car = u_fabric.create_car()
    u_car.release_car(u_engine)