from random import randint

def attack_damage(modifiers):
    roll = randint(1,8)
    return modifiers + roll