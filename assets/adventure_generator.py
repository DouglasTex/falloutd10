from adventures import *
import random


def generate_plot():
    result = random.choice(threat) + " quer " + random.choice(want) + " " + random.choice(target)
    return result


def generate_location():
    return random.choice(location)


def generate_challenge():
    return random.choice(challenge)


def generate_important_npc():
    result = random.choice(npc_type) + " " + random.choice(npc_feature)
    return result

