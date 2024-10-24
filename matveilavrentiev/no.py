from  faker  import  Faker

fake =  Faker("ru_RU")

def generate():
    return fake.name()

print(generate())