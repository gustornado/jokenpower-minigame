from core.config.types import ParticipantType, AttackType
from core.config import JOKENPO_UNITS

class Attack:
    def __init__(self, participant: ParticipantType, type: AttackType, start: int):
        self.participant = participant
        self.type = type
        self.start = start
        self.is_reaction = False
        self.damage = JOKENPO_UNITS[type]['damage']
        self.damage_countered = JOKENPO_UNITS[type]['damage_countered']
        self.weakness = JOKENPO_UNITS[type]['weakness']
        self.duration = JOKENPO_UNITS[type]['duration']
        self.end = start + JOKENPO_UNITS[type]['duration']
        self.invulnerable_time = start + JOKENPO_UNITS[type]['invulnerable_time']

    def set_reaction(self, is_reaction: bool):
        self.is_reaction = is_reaction