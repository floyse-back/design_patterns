

class DatabaseHelper:
    __database_connection = None
    __data = ''

    def __new__(cls):
        if cls.__database_connection is None:
            cls.__database_connection = object.__new__(cls)
            print('New connection created')
        return cls.__database_connection

    def select_data(self) -> str:
        return self.__data

    def insert_data(self, data: str):
        self.__data = data

if __name__ == '__main__':
    connection1 = DatabaseHelper()
    connection1.insert_data('Hello')

    connection2 = DatabaseHelper()
    print(connection2.select_data())