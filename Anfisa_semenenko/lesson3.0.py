import faker
fake = faker.Faker('ru_RU')

def generate_name():
    return fake.country()
print(generate_name())