import random
from characters.perks import *
from characters.skills import *
from characters.character import PlayerCharacter


def _greater_value(initial_body, initial_mind, initial_spirit):
    if initial_spirit > initial_mind and initial_spirit > initial_body:
        return "spirit"
    elif initial_mind > initial_body:
        return "mind"
    return "body"


def _get_better_for_body():
    _skills = []
    _perks = []
    # choose perks
    choice = random.choice(perks_for_body)
    _perks.append(choice)
    while True:
        choice = random.choice(perks_for_body)
        if choice not in _perks:
            _perks.append(choice)
            break
    choice = random.choice(perks_in_general)
    _perks.append(choice)

    # choose skills
    i = 1
    while i <= 3:
        choice = random.choice(skills_for_body)
        if choice not in _skills:
            _skills.append(choice)
            i += 1

    return [_skills, _perks]


def _get_better_for_mind():
    _skills = []
    _perks = []
    # choose perks
    choice = random.choice(perks_for_mind)
    _perks.append(choice)
    while True:
        choice = random.choice(perks_for_mind)
        if choice not in _perks:
            _perks.append(choice)
            break
    choice = random.choice(perks_in_general)
    _perks.append(choice)

    # choose skills
    i = 1
    while i <= 3:
        choice = random.choice(skills_for_mind)
        if choice not in _skills:
            _skills.append(choice)
            i += 1

    return [_skills, _perks]


def _get_better_for_spirit():
    _skills = []
    _perks = []
    # choose perks
    choice = random.choice(perks_for_spirit)
    _perks.append(choice)
    choice = random.choice(perks_in_general)
    _perks.append(choice)
    while True:
        choice = random.choice(perks_in_general)
        if choice not in _perks:
            _perks.append(choice)
            break

    # choose skills
    i = 1
    while i <= 2:
        choice = random.choice(skills_for_spirit)
        if choice not in _skills:
            _skills.append(choice)
            i += 1
    choice = random.choice(skills_for_mind)
    _skills.append(choice)

    return [_skills, _perks]


def generate_npc(initial_body=0, initial_mind=0, initial_spirit=0):
    _perks = []
    _skills = []

    if initial_body == 0:
        initial_body = random.randint(2, 4)
        initial_mind = random.randint(2, 4)
        initial_spirit = random.randint(2, 4)

    big = _greater_value(initial_body, initial_mind, initial_spirit)

    match big:
        case "body":
            output = _get_better_for_body()
        case "mind":
            output = _get_better_for_mind()
        case _:
            output = _get_better_for_spirit()

    # noinspection PyUnboundLocalVariable
    _skills = output[0]
    _perks = output[1]
    npc = PlayerCharacter(initial_body, initial_mind, initial_spirit, _skills, _perks)

    return npc
