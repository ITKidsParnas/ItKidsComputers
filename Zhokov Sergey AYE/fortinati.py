import random

def random_phrase():
    phrases = ["Фортинати", "Бабажи"]
    return random.choice(phrases)

if __name__ == "__main__":
    print(random_phrase())