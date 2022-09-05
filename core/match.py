from core.config.types import ParticipantType
from core.aux.attack import Attack
from core.participant import Participant
from core.conflict_manager import ConflictManager

class Match:
    def __init__(self):
        self.Player = Participant(ParticipantType.PLAYER)
        self.Enemy = Participant(ParticipantType.ENEMY)
        self.Timing = ConflictManager()
    
    def __get_participant(self, type: ParticipantType) -> Participant:
        return self.Player if type == ParticipantType.PLAYER else self.Enemy
    
    def __get_opponent(self, type: ParticipantType) -> Participant:
        return self.Enemy if type == ParticipantType.PLAYER else self.Player

    def __initiate_attack(self, atk: Attack):
        self.Timing.try_initiate_attack(atk)


    def participant_attacks(self, atk: Attack):
        self.__initiate_attack(atk)
        # return self.opponent_gets_damaged(atk)
    
    def opponent_gets_damaged(self, atk: Attack):
        self.__get_opponent(atk.participant).gets_damaged(atk.type)
    
    def check_health(self, player: ParticipantType) -> int:
        return self.__get_participant(player).check_health()

    def damage_check(self):
        pass

