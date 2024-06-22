class Person():
    def __init__(self, name, family):
        self.name = name
        self.family = family
        self.qual = 1

    def info(self):
        print(f'Имя: {self.name}\nФамилия: {self.family}\nКвалификация: {self.qual}\n')

    def goodbye(self):
        print(f'До свидания, {self.name}{self.family}\n')

pirston = Person("John", "Pirston")
pirston.info()
pirston.goodbye()

morgan = Person('Arthur','Morgan')
morgan.info()
morgan.goodbye()

takahashi = Person("Kenshi","Takahashi")
takahashi.info()
takahashi.goodbye()

input('Нажмите Enter что бы завершить программу\n')