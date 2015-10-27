from base import Person

class Warrior(Person):
    hp = 100
    strength = 2
    accuracy = 5
    defense = 4
    attacks_by = "swings sword"


class Marksman(Person):
    hp = 100
    strength = 1
    accuracy = 8
    defense = 3
    attacks_by = "shoots an arrow"


class Madman(Person):
    hp = 100
    strength = 3
    accuracy = 3
    defense = 2
    attacks_by = "flails wildly"


class Mage(Person):
    hp = 200
    strength = 1
    accuracy = 6
    defense = 2
    attacks_by = "casts a spell"

class Scout(Person):
    hp = 150
    strength = 4
    accuracy = 6
    defense = 3
    attacks_by = "stabs with knives"

class Hunter(Person):
    hp = 100
    strength = 5
    accuracy = 6
    defense = 2
    attacks_by = "throws tomahawk"

class Barbarian(Person):
    hp = 175
    strength = 5
    accuracy =5
    defense = 3
    attacks_by = "swings ax"

class FloatingOrb(Person):
    hp = 75
    strength = 1
    accuracy = 5
    defense = 3
    attacks_by = "shoots laser"

class Overlord(Person):
    hp = 250
    strength = 6
    accuracy = 3
    defense = 4
    attacks_by = "Swings mace"

class OverGrownHamster(Person):
    hp = 50
    strength = 2
    accuracy = 2
    defense = 2
    attacks_by = "Bites really hard"

class OverLord(Person):
    hp = 50
    strength = 2
    accuracy = 2
    defense = 2
    attacks_by = "Lords over you"

