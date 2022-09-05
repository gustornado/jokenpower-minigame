from core.config.types import AttackType

FULL_HEALTH = 100
JOKENPO_UNITS = {
    AttackType.ROCK : {
        'damage' : 10,
        'duration' : 1000,
        'exposed_time' : 300
    },
    AttackType.PAPER : {
        'damage' : 1,
        'duration' : 700,
        'exposed_time' : 300
    },
    AttackType.SCISSORS : {
        'damage' : 3,
        'duration' : 700,
        'exposed_time' : 300
    }
}