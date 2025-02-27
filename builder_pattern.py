from abc import ABCMeta

class Phone:
    def __init__(self):
        self.data:str = ''

    def about_phone(self):
        return self.data

    def append_data(self,string:str):
        self.data += string

class IDeveloper(metaclass=ABCMeta):
    def create_display(self):
        pass
    def create_box(self):
        pass
    def system_install(self):
        pass
    def get_phone(self):
        pass

class AndroidDeveloper(IDeveloper):

    def __init__(self):
        self.__phone = Phone()

    def create_display(self):
        self.__phone.append_data('Display: Samsung')

    def create_box(self):
        self.__phone.append_data('Box: Samsung')

    def system_install(self):
        self.__phone.append_data('System: Android')

    def get_phone(self):
        return self.__phone


class IPhoneDeveloper(IDeveloper):
    def __init__(self):
        self.__phone = Phone()

    def create_display(self):
        self.__phone.append_data('Display: Apple')

    def create_box(self):
        self.__phone.append_data('Box: Apple')

    def system_install(self):
        self.__phone.append_data('System: iOS')

    def get_phone(self):
        return self.__phone

class Director:
    def __init__(self,developer:IDeveloper):
        self.__developer = developer

    def set_developer(self, developer:IDeveloper):
        self.__developer = developer

    def mount_only_phone(self):
        self.__developer.create_display()
        self.__developer.create_box()
        return self.__developer.get_phone()

    def mount_full_phone(self):
        self.__developer.create_display()
        self.__developer.create_box()
        self.__developer.system_install()
        return self.__developer.get_phone()

if __name__ == "__main__":
    android_dev = AndroidDeveloper()
    director = Director(android_dev)

    samsung:Phone = director.mount_full_phone()
    print(samsung.about_phone())

    apple_dev = IPhoneDeveloper()
    director.set_developer(apple_dev)

    ios:Phone = director.mount_only_phone()
    print(ios.about_phone())
    