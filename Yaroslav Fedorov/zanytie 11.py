import faker

fake = faker.Faker()

def generate_fake():
    return fake.name()
print(generate_fake())