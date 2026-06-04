from config.settings import GOLDEN_ZONE

def calculate_health(latest):

    total = len(GOLDEN_ZONE)

    score = 0

    for parameter, (low, high) in GOLDEN_ZONE.items():

        value = latest[parameter]

        if low <= value <= high:

            score += 1

    return round(
        (score / total) * 100,
        2
    )

