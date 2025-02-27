import abc
from abc import ABCMeta

class IScale(metaclass=ABCMeta):
    @abc.abstractmethod
    def get_weight(self):
        pass

class UkraineScales(IScale):
    def __init__(self,weight):
        self.__current_weight = weight

    def get_weight(self):
        return self.__current_weight

class BritishScales(IScale):
    def __init__(self,weight):
        self.__current_weight = weight

    def get_weight(self):
        return self.__current_weight

class AdapterForBritishScales(IScale):
    def __init__(self,british_scales:BritishScales):
        self.__british_scales = british_scales

    def get_weight(self):
        return self.__british_scales.get_weight() * .453

if __name__ == "__main__":
    kg: float = 55
    lb: float = 55

    uScales = UkraineScales(kg)
    bScales = AdapterForBritishScales(BritishScales(lb))

    print(f"Ukraine: {uScales.get_weight()}kg")
    print(f"British: {bScales.get_weight()}lb")
