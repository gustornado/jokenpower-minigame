from core.platform_pygame import Platform
from core.match import Match
from core.config.types import AttackType, ParticipantType
from core.aux.attack import Attack
from core.config import JOKENPO_UNITS

# Testes temporariamente desabilitados porque lógica nova de dano foi implementada
# def create_match() -> Match:
#     return Match()

# def participant_attacks_opponent(whoAttacks: ParticipantType, whoIsAttacked: ParticipantType, typeOfAttack: AttackType) -> bool:
#     match = create_match()
#     healthBefore = match.check_health(whoIsAttacked)
#     match.participant_attacks(Attack(whoAttacks, typeOfAttack, 100000))
#     return healthBefore == match.check_health(whoIsAttacked) + JOKENPO_UNITS[typeOfAttack]['damage']


# def test_player_attacks_enemy():
#     assert participant_attacks_opponent(ParticipantType.PLAYER, ParticipantType.ENEMY, AttackType.ROCK)

# def test_enemy_attacks_player():
#     assert participant_attacks_opponent(ParticipantType.ENEMY, ParticipantType.PLAYER, AttackType.ROCK)

# def test_only_rocks_until_win():
#     match = create_match()
#     for _ in range(10):
#         match.participant_attacks(Attack(ParticipantType.PLAYER, AttackType.ROCK, 10000))
#     assert match.check_health(ParticipantType.ENEMY) == 0

# def test_counter():
#     match = create_match()
#     playerHealthBefore = match.check_health(ParticipantType.PLAYER)
#     enemyHealthBefore = match.check_health(ParticipantType.ENEMY)
#     match.participant_attacks(ParticipantType.PLAYER, AttackType.ROCK, 5000) # finaliza 6000 (1s depois)
#     match.participant_attacks(ParticipantType.ENEMY, AttackType.PAPER, 5800)
#     assert playerHealthBefore  == match.check_health(ParticipantType.PLAYER) + JOKENPO_UNITS[AttackType.ROCK]['damage'] * 2
#     assert enemyHealthBefore == match.check_health(ParticipantType.ENEMY) 
