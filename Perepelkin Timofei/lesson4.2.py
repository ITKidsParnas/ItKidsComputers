import faker
fake = faker.Faker('ru_RU')

def generate_name():
    return fake.address()
print(generate_name())