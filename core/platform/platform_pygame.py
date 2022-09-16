import core.config.display as DisplayConfig
import pygame
from core.platform.participant import Participant
from core.config.types import AttackType, ParticipantType, KeyType
import core.platform.config.keys as InputKey
from core.match import Match
from core.platform.bot import Bot
from core.platform.save import Save


class PlatformPygame:
    def __init__(self):
        self.now = 0
        pygame.init()
        pygame.display.set_caption(DisplayConfig.TITLE)
        self._screen = pygame.display.set_mode((DisplayConfig.WIDTH, DisplayConfig.HEIGHT))
        self._clock = pygame.time.Clock()
        self.pygame = pygame
        self._player = self._create_participant(ParticipantType.PLAYER)
        self._enemy = self._create_participant(ParticipantType.ENEMY)
        self.match = Match()
        self.state = self.match.get_state()
        self.match.subscribe(self.on_participant_movement_do)
        self.bot = Bot(pygame, self.match)
        self.save = Save()


    def draw_participants(self):
        self._player.draw(self._screen)
        self._player.update()
        self._enemy.draw(self._screen)
        self._enemy.update()


    def update(self):
        self._check_damage()
        self.pygame.display.update()
    

    def set_framerate(self, framerate: int):
        self._clock.tick(framerate)


    def now(self) -> int:
        return self.pygame.time.get_ticks()
    
    def update_current_time(self):
        self.now = self.pygame.time.get_ticks()


    def check_player_attack(self):
        key = self._check_key()
        if key != None:
            self._player_try_initiate_attack(key)
        

    def check_exit(self):
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                self.save.save_remanescent_cache()
                self.pygame.quit()
                exit()
            self.bot.check_if_bot_attacks(event, self.now)
    

    def on_participant_movement_do(self):
        for (participant, attack) in self.state.items():
            a_type = None if attack == None else attack.type
            self._change_sprite(participant, a_type)
            


    def _check_key(self):
        keys = pygame.key.get_pressed()
        key = None
        if keys[InputKey.PLAYER_ROCK_BUTTON]:
            key = KeyType.ROCK_BUTTON
        elif keys[InputKey.PLAYER_PAPER_BUTTON]:
            key = KeyType.PAPER_BUTTON
        elif keys[InputKey.PLAYER_SCISSORS_BUTTON]:
            key = KeyType.SCISSORS_BUTTON
        return key

    def _player_try_initiate_attack(self, key: KeyType):
        self.match.participant_attacks(key, self.now)

    def _check_damage(self):
        damage = self.match.check_damage(self.now)
        if damage:
            participant, atk_info = list(damage.items())[0]
            print(f'{participant.value} levou ataque {atk_info["attack"].type.value} e levou dano {atk_info["damage"]}')
            self.match.participant_gets_damaged(participant, atk_info['damage'])
            self.save.add_to_cache(participant, atk_info['attack'], atk_info['damage'], self.now)
        return damage

    def _change_sprite(self, participant: ParticipantType, atk_type: AttackType):
        participant_sprite = self._get_participant(participant).sprite
        participant_sprite.image = participant_sprite.all_images[atk_type]
        participant_sprite.image_type = atk_type



    def _create_participant(self, type: ParticipantType) -> pygame.sprite.GroupSingle:
        participant = self.pygame.sprite.GroupSingle()
        participant.add(Participant(type))
        return participant
    

    def _get_participant(self, type: ParticipantType) -> pygame.sprite.GroupSingle:
        return self._player if type == ParticipantType.PLAYER else self._enemy
            