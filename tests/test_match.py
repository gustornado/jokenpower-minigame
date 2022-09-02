from app.match import Match
from app.config.enums import AttackType, ParticipantType
from app.config import JOKENPO_UNITS

def create_game() -> Match:
    return Match()

def participant_attacks_opponent(whoAttacks: ParticipantType, whoIsAttacked: ParticipantType, typeOfAttack: AttackType) -> bool:
    game = create_game()
    healthBefore = game.check_health(whoIsAttacked)
    game.participant_attacks(whoAttacks, typeOfAttack)
    return healthBefore == game.check_health(whoIsAttacked) + JOKENPO_UNITS[typeOfAttack]['dano']


def test_player_attacks_enemy():
    assert participant_attacks_opponent(ParticipantType.PLAYER, ParticipantType.ENEMY, AttackType.ROCK)

def test_enemy_attacks_player():
    assert participant_attacks_opponent(ParticipantType.ENEMY, ParticipantType.PLAYER, AttackType.ROCK)

def test_only_rocks_until_win():
    game = create_game()
    for _ in range(10):
        game.participant_attacks(ParticipantType.PLAYER, AttackType.ROCK)
    assert game.check_health(ParticipantType.ENEMY) == 0

# ---- TODO: precisa de um controller de tempo; utilizar o do pygame ----
# def test_counter():
#     game = create_game()
#     playerHealthBefore = game.check_health(ParticipantType.PLAYER)
#     enemyHealthBefore = game.check_health(ParticipantType.ENEMY)
#     game.participant_attacks(ParticipantType.PLAYER, AttackType.ROCK)
#     game.participant_attacks(ParticipantType.ENEMY, AttackType.PAPER)
#     assert playerHealthBefore  == game.check_health(ParticipantType.PLAYER) + JOKENPO_UNITS[AttackType.ROCK]['dano'] * 2
#     assert enemyHealthBefore == game.check_health(ParticipantType.ENEMY) 
