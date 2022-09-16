import pygame
from os import path
from core.config.types import ParticipantType, AttackType
import core.config.display as DisplayConfig

class Participant(pygame.sprite.Sprite):
    def __init__(self, type: ParticipantType):
        super().__init__()
        self.all_images = self.__set_all_images()
        self.image_type = None
        self.image = self.all_images[None]
        self.rect = self.image.get_rect(center = self.__participant_pos(type))
    
    def __set_all_images(self):
        attack_types = {
            AttackType.ROCK : 'rock',
            AttackType.PAPER : 'paper',
            AttackType.SCISSORS : 'scissors',
            None : 'default'
        }
        for (type, img) in attack_types.items():
            attack_types[type] = pygame.image.load(path.join('assets', 'img', f'{img}.png')).convert_alpha()
        return attack_types

    def __participant_pos(self, type: ParticipantType) -> tuple:
        padding = 200
        x = padding if type == ParticipantType.PLAYER else DisplayConfig.WIDTH - padding
        y = int(DisplayConfig.HEIGHT / 2)
        return (x, y)
