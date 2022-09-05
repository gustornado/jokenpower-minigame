from enum import Enum, auto

class AttackType(Enum):
    ROCK = auto()
    PAPER = auto()
    SCISSORS = auto()

class ParticipantType(Enum):
    PLAYER = auto()
    ENEMY = auto()