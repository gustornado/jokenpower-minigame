from core.conflict_manager import ConflictManager
from core.aux.attack import Attack
from core.config.types import ParticipantType, AttackType


def test_if_damage_is_not_assigned_before_duration_of_attack():
    timing = ConflictManager()
    assert True == timing.try_initiate_attack(Attack(ParticipantType.PLAYER, AttackType.SCISSORS, 1))
    now = 701
    assert len(timing.check_situation(now)) == 0
    now = 702
    assert len(timing.check_situation(now)) == 1
    

def test_only_one_attack_hit():
    timing = ConflictManager()
    assert True == timing.try_initiate_attack(Attack(ParticipantType.ENEMY, AttackType.ROCK, 100))
    assert True == timing.try_initiate_attack(Attack(ParticipantType.PLAYER, AttackType.SCISSORS, 2000))
    now = 2100
    attackers = timing.check_situation(now)
    assert len(attackers) == 1
    for key in attackers:
        assert key == ParticipantType.ENEMY