from typing import Callable
from core.config.types import ParticipantType, AttackType

class Queue:
    def __init__(self):
        self._actions_after_movement = []

    def subscribe(self, do_when_participant_move: Callable):
        self._actions_after_movement.append(do_when_participant_move)
    
    def emit(self):
        for action in self._actions_after_movement:
            action()
