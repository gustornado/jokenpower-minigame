from core.config.types import ParticipantType, KeyType, AttackType
from typing import Callable
from core.auxiliar.attack import Attack
from core.participant import Participant
from core.conflict_manager import ConflictManager

class Match:
    def __init__(self):
        self.Player = Participant(ParticipantType.PLAYER)
        self.Enemy = Participant(ParticipantType.ENEMY)
        self.ConflictManager = ConflictManager()
    

    def participant_attacks(self, key: KeyType, now: int, participant: ParticipantType = ParticipantType.PLAYER):
        attack = self._generate_attack_info(key, now, participant)
        attack_validated = self.ConflictManager.try_initiate_attack(attack)
        return attack_validated


    def participant_gets_damaged(self, participant: ParticipantType, damage: int):
        self.__get_participant(participant).gets_damaged(damage)
        # print(f'{self.Player')


    def check_health(self, player: ParticipantType) -> int:
        return self.__get_participant(player).check_health()
    
    
    def check_damage(self, now: int) -> dict:
        return self.ConflictManager.check_damage(now)
    
    def get_state(self):
        return self.ConflictManager.state
    
    def subscribe(self, action: Callable):
        self.ConflictManager.queue.subscribe(action)



    def _generate_attack_info(self, key: KeyType, now: int, participant: ParticipantType) -> Attack:
        key_to_attack = {
            KeyType.ROCK_BUTTON : AttackType.ROCK,
            KeyType.PAPER_BUTTON : AttackType.PAPER,
            KeyType.SCISSORS_BUTTON : AttackType.SCISSORS
        }
        atk_type = key_to_attack[key]
        return Attack(participant, atk_type, now)

        
    def __get_participant(self, type: ParticipantType) -> Participant:
        return self.Player if type == ParticipantType.PLAYER else self.Enemy
    
    def __get_opponent(self, type: ParticipantType) -> Participant:
        return self.Enemy if type == ParticipantType.PLAYER else self.Player
