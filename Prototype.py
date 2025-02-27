import copy

class Sheep:
    __name = ''
    __params = {'Weight': 20, 'Height': .34}

    def __init__(self, donor : 'Sheep' = None):
        if donor is not None:
            self.__name = donor.get_name()
            self.__params = copy.deepcopy(donor.get_params())

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_params(self):
        return self.__params

    def set_weight(self,weight):
        self.__params['Weight'] = weight

    def clone(self):
        return Sheep(self)

if __name__ == '__main__':
    sheep_donor: Sheep = Sheep()
    sheep_donor.set_name('Donor')

    sheep_clone: Sheep = sheep_donor.clone()
    sheep_clone.set_name('Clone')
    print(f"Donor: {sheep_donor.get_name()}, Clone: {sheep_clone.get_name()}")
    print(f"Donor: {sheep_donor.get_params()}, Clone: {sheep_clone.get_params()}")

