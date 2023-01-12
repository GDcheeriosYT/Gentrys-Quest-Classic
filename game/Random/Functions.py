import random

random_character_names = [
    "pooper man",
    "Hot guy",
    "Brayden"
]

random_item_names = [
    "The Meow",
    "kfc fries",
    "lucas's iphone"
]


def get_random_name(character_name=True):
    if character_name:
        return random.choice(random_character_names)
    else:
        return random.choice(random_item_names)


def determine_crit(crit_rate):
    if random.uniform(0, 100) < crit_rate:
        return True
    else:
        return False


def generate_artifact_star_rating(difficulty):
    # generate a star rating
    rate = int(10000 / difficulty)
    random_number = random.randint(0, rate)
    if random_number <= 25:
        return 5

    elif random_number <= 100:
        return 4

    elif random_number <= 250:
        return 3

    elif random_number <= 1000:
        return 2

    elif random_number <= 10000:
        return 1


def test():
    y = 1
    while y <= 5:
        x = 0
        while x < 10:
            print(f"#{x}. {generate_artifact_star_rating(y)} {y}")
            x += 1

        y += 1