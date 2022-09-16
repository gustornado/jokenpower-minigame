from core.conflict_manager import ConflictManager
from core.aux.attack import Attack
from core.config.types import ParticipantType, AttackType
from core.config import JOKENPO_UNITS


def test_attack_before_allowed():
    timing = ConflictManager()
    assert True == timing.try_initiate_attack(Attack(ParticipantType.PLAYER, AttackType.SCISSORS, 100))
    assert False == timing.try_initiate_attack(Attack(ParticipantType.PLAYER, AttackType.PAPER, 200))

def test_only_one_attack_hit():
    timing = ConflictManager()
    for now in range(0,2020,10):
        if now == 100:
            assert True == timing.try_initiate_attack(Attack(ParticipantType.ENEMY, AttackType.ROCK, 100))
        elif now == 2000:
            assert True == timing.try_initiate_attack(Attack(ParticipantType.PLAYER, AttackType.SCISSORS, 2000))
        
        attackers = timing.check_damage(now)
        if now == 1100:
            assert len(attackers) == 1
            assert ParticipantType.ENEMY not in attackers
            assert ParticipantType.PLAYER in attackers # damage taken
        else:
            assert len(attackers) == 0

def test_damage_is_only_assigned_one_time():
    timing = ConflictManager()
    for now in range(0, 740, 10):
        if now == 10:
            assert True == timing.try_initiate_attack(Attack(ParticipantType.PLAYER, AttackType.SCISSORS, 10))

        attackers = timing.check_damage(now)
        if now == 700:
            assert len(attackers) == 0
        elif now == 710:
            assert len(attackers) == 1
        elif now == 720:
            assert len(attackers) == 0

def test_possible_to_react_to_attack():
    timing = ConflictManager()
    for now in range(0, 700, 10):
        if now == 10:
            assert True == timing.try_initiate_attack(Attack(ParticipantType.ENEMY, AttackType.SCISSORS, 10))
        elif now == 600:
            assert True == timing.try_initiate_attack(Attack(ParticipantType.PLAYER, AttackType.ROCK, 600))

        attackers = timing.check_damage(now)
        if now == 600:
            assert len(attackers) == 1
            assert ParticipantType.ENEMY in attackers
            assert ParticipantType.PLAYER not in attackers
            assert attackers[ParticipantType.ENEMY] == JOKENPO_UNITS[AttackType.SCISSORS]['damage_countered']
        else:
            assert len(attackers) == 0

def test_feint_on_rock_attack():
    timing = ConflictManager()
    for now in range(0,1020, 10):
        if now == 10:
            assert True == timing.try_initiate_attack(Attack(ParticipantType.PLAYER, AttackType.ROCK, 10))
        elif now == 500:
            assert True == timing.try_initiate_attack(Attack(ParticipantType.PLAYER, AttackType.SCISSORS, 500))
        
        attackers = timing.check_damage(now)
        if now == 1010:
            assert len(attackers) == 1
            assert 3 in attackers.values()
        else: 
            assert len(attackers) == 0

def test_not_feint_on_scissor_attack():
    timing = ConflictManager()
    for now in range(0,1020, 10):
        if now == 10:
            assert True == timing.try_initiate_attack(Attack(ParticipantType.PLAYER, AttackType.SCISSORS, 10))
        elif now == 500:
            assert False == timing.try_initiate_attack(Attack(ParticipantType.PLAYER, AttackType.PAPER, 500))
        
        attackers = timing.check_damage(now)
        if now == 710:
            assert len(attackers) == 1
            assert 3 in attackers.values()
        else: 
            assert len(attackers) == 0