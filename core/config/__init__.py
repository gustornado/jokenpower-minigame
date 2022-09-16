from core.config.types import AttackType

FULL_HEALTH = 100
JOKENPO_UNITS = {
    AttackType.ROCK : {
        'damage' : 10,
        'damage_countered' : 20,
        'duration' : 1000,
        'invulnerable_time' : 700,
        'weakness' : AttackType.PAPER
    },
    AttackType.PAPER : {
        'damage' : 1,
        'damage_countered' : 20,
        'duration' : 700,
        'invulnerable_time' : 400,
        'weakness' : AttackType.SCISSORS
    },
    AttackType.SCISSORS : {
        'damage' : 3,
        'damage_countered' : 20,
        'duration' : 700,
        'invulnerable_time' : 400,
        'weakness' : AttackType.ROCK
    }
}