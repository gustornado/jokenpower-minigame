from core.config import FULL_HEALTH, JOKENPO_UNITS
from core.config.types import AttackType, ParticipantType

class Participant:
    def __init__(self, type: ParticipantType):
        self.health = FULL_HEALTH
        self.type = type

    def gets_damaged(self, attackType: AttackType) -> None:
        self.health -= JOKENPO_UNITS[attackType]['damage']

    def check_health(self) -> int:
        return self.health
    