from app.config.enums import AttackType, ParticipantType
FULL_HEALTH = 100
JOKENPO_UNITS = {
    AttackType.ROCK : {
        'dano' : 10
    },
    AttackType.PAPER : {
        "dano" : 1
    },
    AttackType.SCISSORS : {
        "dano" : 3
    }
}