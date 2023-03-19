from core.config.types import AttackType, ParticipantType
from core.auxiliar.attack import Attack
from core.auxiliar.queue import Queue

class ConflictManager():
    def __init__(self):
        self.state = {
            ParticipantType.PLAYER : None,
            ParticipantType.ENEMY  : None
        }
        self.queue = Queue()


    def try_initiate_attack(self, atk: Attack) -> bool:
        is_initiated = False
        if not self.__is_participant_moving(atk.participant):
            if self.__is_counter_attack(atk):
                self.__counter_attack(atk)
            else:
                self.__initiate_attack(atk)
            is_initiated = True
        elif self.__is_feint(atk):
            self.__feint(atk)
            is_initiated = True
        return is_initiated


    def check_damage(self, now : int) -> dict:
        attackers = {}
        if self.__is_any_participant_moving():
            attackers = self.__check_attacks_end(now, attackers)
        return attackers
    

    def __is_participant_moving(self, participant : ParticipantType) -> bool:
        return self.state[participant] != None


    def __is_any_participant_moving(self) -> bool:
        return len(['attacked' for attack in self.state.values() if attack != None]) > 0


    def __initiate_attack(self, atk : Attack, is_counter: bool=False):
        self.state[atk.participant] = atk
        self.__emit_event_to_platform()
    

    def __check_attacks_end(self, now : int, attackers : dict) -> dict:
        for (participant, atk) in self.state.items():
            if self.__can_damage(now, participant, atk):
                attackers[self.__get_opponent(participant)] = {'damage': self.__calculate_damage(atk), 'attack': atk}
                self.__clear_participant_state(participant)
                self.__emit_event_to_platform()
        return attackers


    def __can_damage(self, now : int, participant: ParticipantType, atk : Attack) -> bool:
        return self.__is_participant_moving(participant) and self.__has_finished_attack(now, atk)


    def __has_finished_attack(self, now : int, atk : Attack) -> bool:
        return now >= atk.end
    

    def __is_counter_attack(self, atk : Attack) -> bool:
        opponent_atk = self.state[self.__get_opponent(atk.participant)]
        if opponent_atk != None:
            is_counter_attack_time = opponent_atk.invulnerable_time < atk.start < opponent_atk.end
            is_weakness = atk.type == opponent_atk.weakness
            return is_counter_attack_time and is_weakness
        return False


    def __counter_attack(self, atk : Attack):
        atk.end = atk.start
        atk.set_reaction(True)
        self.__clear_participant_state(self.__get_opponent(atk.participant))
        self.__initiate_attack(atk, True)


    def __calculate_damage(self, atk : Attack) -> int:
        return atk.damage_countered if atk.is_reaction else atk.damage
    

    def __is_condition_to_feint(self, atk : Attack) -> bool:
        return self.state[atk.participant].type == AttackType.ROCK and atk.type != AttackType.ROCK
    

    def __is_feint(self, atk : Attack) -> bool:
        return self.__is_participant_moving(atk.participant) and self.__is_condition_to_feint(atk)
    

    def __feint(self, atk: Attack):
        if self.__is_feint(atk):
            last_attack_end = self.state[atk.participant].end
            atk.end = last_attack_end
            self.state[atk.participant] = atk
            self.__initiate_attack(atk)


    def __get_opponent(self, participant: ParticipantType) -> ParticipantType:
        return ParticipantType.ENEMY if participant == ParticipantType.PLAYER else ParticipantType.PLAYER
    

    def __clear_participant_state(self, participant : ParticipantType):
        self.state[participant] = None
    

    def __emit_event_to_platform(self):
        self.queue.emit()