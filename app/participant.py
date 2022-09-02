from app.config import FULL_HEALTH, JOKENPO_UNITS
from app.config.enums import AttackType, ParticipantType

class Participant:
    def __init__(self, type: ParticipantType):
        self.health = FULL_HEALTH
        self.type = type

    def gets_damaged(self, attackType: AttackType) -> None:
        self.health -= JOKENPO_UNITS[attackType]['dano']

    def check_health(self) -> int:
        return self.health
    