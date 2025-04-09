import faker
fake = faker.Faker('ru_RU')

def generate_name():
    return fake.ipv4()

print(generate_name())












