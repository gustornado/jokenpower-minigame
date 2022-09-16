from core.config import FULL_HEALTH, JOKENPO_UNITS
from core.config.types import AttackType, ParticipantType

class Participant:
    def __init__(self, type: ParticipantType):
        # self.health = FULL_HEALTH
        self.total_damage = 0
        self.type = type

    def gets_damaged(self, damage: int) -> None:
        self.total_damage += damage

    def check_health(self) -> int:
        return self.health
    