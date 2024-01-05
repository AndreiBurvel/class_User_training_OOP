from list_password_often import password_often

class User:
    """Класс пользователя с исенем, паролем и секретом(доступным по паролю)"""
    def __init__(self, name, password):
        """Инициализация атрибутов класса."""
        self.name = name
        self.password = password
        self.__secret = 'Python - лучший ЯП.'

    @staticmethod
    def examination(value):
        """Проверка пароля по наличию цифры в пароле."""
        for i in value:
            if i in '0123456789':
                return True
        return False

    @property
    def password(self):
        """Возврат значения пароля."""
        return self.__password
    @password.setter
    def password(self, value):
        """Установка пароля если он удовлетворяет всем проверкам."""
        if not isinstance(value, str):
            raise TypeError('Пароль должен быть строкой.')
        if len(value) < 4:
            raise ValueError('Длина пароля должна быть больше 4 смволов.')
        if len(value) > 12:
            raise ValueError('Длина пароля должна быть меньше 12 смволов.')
        if not User.examination(value):
            raise ValueError('В пароле должна присутствовать цифра.')
        if value in password_often:
            raise ValueError('Это слишком распространённый пароль, попробуйте другой.')
        self.__password = value

    @property
    def secret(self):
        """Возвращает секрет если пароль верен."""
        get = input('Your password: ')
        if get == self.password:
            return self.__secret
        raise ValueError('Вы не имеете доступ к данному материалу.')

max = User('Max', 'gruden1')
print(max.secret)