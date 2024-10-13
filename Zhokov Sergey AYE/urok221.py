import faker
fake = faker.Faker('ru_RU')

def generate_name():
    return fake.text()

print(generate_name())