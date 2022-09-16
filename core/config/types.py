from enum import Enum, auto

class AttackType(Enum):
    ROCK = 'Rock'
    PAPER = 'Paper'
    SCISSORS = 'Scissors'

class ParticipantType(Enum):
    PLAYER = 'Main'
    ENEMY = 'Enemy'

class KeyType(Enum):
    ROCK_BUTTON = auto()
    PAPER_BUTTON = auto()
    SCISSORS_BUTTON = auto()