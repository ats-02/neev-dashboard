def plunger_health(current_shots):

    expected_life = 100000

    remaining = expected_life - current_shots

    health = (
        remaining / expected_life
    ) * 100

    return {

        "remaining": remaining,

        "health": round(
            health,
            2
        )
    }

