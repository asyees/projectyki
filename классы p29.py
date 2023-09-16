class Student:
    default_greeting = 'Привет! Это программа поможет тебе узнать информацию о выдуманном студенте!'

    def init(self, name, surname, age):
        self.budj = None
        self.__cabinet = None
        self.name = name
        self.surname = surname
        self.age = age

    @classmethod
    def speciality_change(cls, speciality):
        cls.speciality = speciality

    @classmethod
    def vartist_change(cls, cina):
        cls.vartist = int(cina)

    def auditory(self):
        match self.speciality:
            case 'Python':
                self.__cabinet = 33
            case 'UI/UX':
                self.__cabinet = 121
            case 'Data Science':
                self.__cabinet = 104
            case _:
                self.__cabinet = "Don't have speciality"

    def budj_or_kontract(self):
        match self.vartist:
            case 0:
                self.budj = 'budjet'
            case v if 10000 > v > 0:
                self.budj = 'contract'
            case v if v > 10000:
                self.budj = f'zaborgovannist - {self.vartist - 10000} uah'
            case _:
                self.budj = '?'

    def info(self):
        return f'name: {self.name}, surname: {self.surname}, age: {self.age}\n' \
               f'speciality: {self.speciality}\n' \
               f'cabinet: {self.__cabinet}\n' \
               f'vartist navchannya: {self.vartist}'

    @classmethod
    def example_classic_method(cls, value):
        cls.example_var = value
        print(f'Set value to {value} in example_var')

    @classmethod
    def change_greeting(cls, greeting = 'Кажется пользователю было лень указать новое приветствие.'):
        cls.default_greeting = greeting

    @classmethod
    def info_about_programm(cls):
        print(cls.default_greeting)

    @staticmethod
    def end():
        print('Thank you for using our app!')




def main():
    Student.info_about_programm()
    while True:
        try:
            select = input('Do you want to know info about student? (y/n) ')
            if select == 'y':
                name, surname, age, speciality, price = \
                    map(str, input('enter name, surname, age, speciality, price (use space): ').split(maxsplit=5))
                Student.speciality_change(speciality)
                Student.vartist_change(price)
                stud = Student(name, surname, age)
                stud.auditory()
                stud.budj_or_kontract()
                print(stud.info())
            elif select == 'n':
                Student.end()
        except:
            print('Wrong data')

