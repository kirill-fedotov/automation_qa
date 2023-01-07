from data.data import Person, Color, Date
from faker import Faker

faker_ru = Faker('ru_Ru')
faker_en = Faker('En')
Faker.seed()


def generated_color():
    yield Color("Red", "Blue", "Green", "Yellow", "Purple")


def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address(),
    )


def generated_date():
    yield Date(
        day=faker_en.day_of_month(),
        month=faker_en.month_name(),
        year=faker_en.year(),
        time="12:00"
    )
