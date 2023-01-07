import random

from data.data import Person
from faker import Faker

faker_ru = Faker('en_US')
Faker.seed()


from data.data import Person, Color, Date
from faker import Faker

faker_ru = Faker('ru_Ru')
faker_en = Faker('En')
Faker.seed()


def generated_color():
    yield Color("Red", "Blue", "Green", "Yellow", "Purple")


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name(),
        firstname=faker_ru.first_name(),
        lastname=faker_ru.last_name(),
        age=random.randint(15, 80),
        salary=random.randint(1000, 100000),
        mobile_number=faker_ru.msisdn(),
        department=faker_ru.job(),
        email=faker_ru.email(),
        current_address=faker_ru.street_address(),
        permanent_address=faker_ru.street_address(),
    )


def generated_file():
    path = rf'C:\Users\XXX\PycharmProjects\automation_qa\filetest{random.randint(0, 999)}.txt'
    file = open(path, 'w+')
    file.write(f'Hello{random.randint(0, 999)}')
    file.close()
    return file.name, path
    
    
def generated_date():
    yield Date(
        day=faker_en.day_of_month(),
        month=faker_en.month_name(),
        year=faker_en.year(),
        time="12:00"
    )
