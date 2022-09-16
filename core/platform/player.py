import pygame
import core.platform.config.keys as InputKey
from core.config.types import AttackType, ParticipantType
from core.platform.participant import Participant

class Player(Participant):
    def __init__(self, type: ParticipantType):
        super().__init__(type)

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[InputKey.PLAYER_ROCK_BUTTON]:
            attack = AttackType.ROCK
        elif keys[InputKey.PLAYER_PAPER_BUTTON]:
            attack = AttackType.PAPER
        elif keys[InputKey.PLAYER_SCISSORS_BUTTON]:
            attack = AttackType.SCISSORS