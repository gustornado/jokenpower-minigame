from core.config.types import ParticipantType
from core.aux.attack import Attack

class ConflictManager():
    def __init__(self):
        self.situation = {
            ParticipantType.PLAYER : None,
            ParticipantType.ENEMY  : None
        }

    def try_initiate_attack(self, atk: Attack) -> bool:
        if not self.__is_participant_moving(atk.participant):
            self.__update_participant_situation(atk)
            return True
        return False

    def check_situation(self, now : int):
        if self.__is_any_participant_moving():
            return self.__update_situation(now)
        return None

    def __is_participant_moving(self, participant : ParticipantType) -> bool:
        return self.situation[participant] != None

    def __is_any_participant_moving(self) -> bool:
        return len(['attacked' for attack in self.situation.values() if attack != None]) > 0

    def __update_participant_situation(self, atk : Attack):
        self.situation[atk.participant] = atk
    
    def __update_situation(self, now : int):
        attackers = {}
        for (participant, atk) in self.situation.items():
            if self.__can_damage(now, participant, atk):
                self.situation[participant] = None
                attackers[participant] = atk
        return attackers

    def __can_damage(self, now : int, participant: ParticipantType, atk : Attack) -> bool:
        return self.__is_participant_moving(participant) and self.__has_finished_attack(now, atk)

    def __has_finished_attack(self, now : int, atk : Attack) -> bool:
        return now > atk.start + atk.duration
    
        



    
