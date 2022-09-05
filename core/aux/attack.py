from core.config.types import ParticipantType, AttackType
from core.config import JOKENPO_UNITS

class Attack:
    def __init__(self, participant: ParticipantType, type: AttackType, start: int):
        self.participant = participant
        self.type = type
        self.start = start
        self.duration = JOKENPO_UNITS[type]['duration']
        self.damage = JOKENPO_UNITS[type]['damage']
        self.exposed_time = JOKENPO_UNITS[type]['exposed_time']
