import pygame
from random import randint, choice
from core.match import Match
from core.config.types import KeyType, ParticipantType


class Bot:
    def __init__(self, pygame: pygame, match: Match):
        self.timer = pygame.time
        self.match = match
        self.attack_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.attack_timer, self._get_interval())

    def check_if_bot_attacks(self, event, now: int):
        if event.type == self.attack_timer:
            self._attack(now)

    def _attack(self, now: int):
        # print(f'attack: {now}')
        self._try_initiate_attack(now)

    def _get_interval(self):
        return randint(1500, 3000)
        # return randint(100000, 100000)
    
    def _generate_key(self):
        return choice([KeyType.ROCK_BUTTON, KeyType.PAPER_BUTTON, KeyType.SCISSORS_BUTTON])
    
    def _try_initiate_attack(self, now: int):
        self.match.participant_attacks(self._generate_key(), now, ParticipantType.ENEMY)
