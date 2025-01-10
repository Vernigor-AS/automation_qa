import random
import os
from datetime import date

from data.data import Person, Color, Date
from faker import Faker


faker_ru = Faker(['ru_RU'])
faker_en = Faker(['En'])
Faker.seed()



def generated_person():
    yield Person(
        full_name=faker_ru.first_name() + " " + faker_ru.last_name() + " " + faker_ru.middle_name(),
        email=faker_ru.email(),
        current_address=faker_ru.address(),
        permanent_address=faker_ru.address()
    )


def generated_person_webtable_page():
    yield Person(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        email=faker_ru.email(),
        age=random.randint(10, 80),
        salary=random.randint(1, 8000000),
        department=faker_ru.job()
    )

def generated_person_form_page():
    yield Person(
        first_name=faker_ru.first_name(),
        last_name=faker_ru.last_name(),
        email=faker_ru.email(),
        mobile=faker_ru.msisdn(),
        birth=generate_birth_date(),
        current_address=faker_ru.address()
    )

def generated_file():
    path = f'{os.getcwd()}\\filetest{random.randint(0, 999)}.txt'
    with open(path, "w+") as file:
        file.write(f'Hello all{random.randint(0, 999)}')
    return file.name, path

def generated_subject():
    subjects = ["Hindi", "English", "Maths", "Physics", "Chemistry", "Biology", "Computer Science", "Commerce", "Accounting", "Economics", "Arts", "Social Studies", "History", "Civics"]
    return random.choice(subjects)


def generate_birth_date(max_year=2005):
    year = random.randint(1900, max_year)
    month = random.randint(1, 12)

    if month in [1, 3, 5, 7, 8, 10, 12]:
        day = random.randint(1, 31)
    elif month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    else:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)
    return date(year, month, day)

def generated_color():
    yield Color(
        color_name=["Red", "Blue", "Green", "Yellow", "Purple", "Black",
                    "White", "Voilet", "Indigo", "Magenta", "Aqua"]
    )

def generated_date():
    yield Date(
        year=faker_en.year(),
        month=faker_en.month_name(),
        day=faker_en.day_of_month(),
        time='12:00'
    )