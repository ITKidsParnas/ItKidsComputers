import faker

fake = faker.Faker("jp-JP")

def generate_name():
    return fake.text()

print(generate_name())