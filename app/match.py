from app.config.enums import AttackType, ParticipantType
from app.participant import Participant

class Match:
    def __init__(self):
        self.Player = Participant(ParticipantType.PLAYER)
        self.Enemy = Participant(ParticipantType.ENEMY)
    
    def __get_participant(self, type: ParticipantType) -> Participant:
        return self.Player if type == ParticipantType.PLAYER else self.Enemy
    
    def __get_opponent(self, type: ParticipantType) -> Participant:
        return self.Enemy if type == ParticipantType.PLAYER else self.Player


    def participant_attacks(self, whoAttacks: ParticipantType, typeOfAttack: AttackType):
        self.__get_opponent(whoAttacks).gets_damaged(typeOfAttack)
    
    def check_health(self, player: ParticipantType) -> int:
        return self.__get_participant(player).check_health()