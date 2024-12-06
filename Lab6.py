class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password

    def set_password(self, new_password):
        self._password = new_password
        print("Пароль успешно изменён")

    def check_password(self, password):
        return self._password == password


if __name__ == "__main__":
    user = UserAccount('join_doe', 'Dan@email.com', 'initial.password123')
    print(user.check_password('initial.password123'))
    user.set_password('new.secure.password456')

    print(user.check_password('new.secure.password456'))
    print(user.check_password('initial.password123'))


class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def get_info(self):
        return f'Марка: {self.make}, Модель: {self.model}'

class Car(Vehicle):
    def __init__(self, make, model, fuel_type):
        super().__init__(make, model)
        self.fuel_type = fuel_type

    def get_info(self):
        base_info = super().get_info()
        return f'{base_info}, Тип топлива: {self.fuel_type}'

vehicle = Vehicle('Toyota', 'Camry')
print(vehicle.get_info())

car = Car('Nissan', 'Skyline', 'Бензин')
print(car.get_info())


