import faker 
fake = faker.Faker('ru-RU')

def generate_name():
    return fake.ipv4()

print(generate_name())