"""Charm the Commuter - draft forecast for an imaginary city."""

CITY = "Velmora"

FORECAST = [
    "Good morning, Velmora - the city that floats one inch above its river every Tuesday, so mind the gap, it's wetter than it looks.",
    "Today: marmalade sunshine until 9, then a brief, polite rain that only falls on people who forgot to compliment the tram driver.",
    "The 7:42 air-tram will smell of toasted almonds and arrive three minutes early, apologising in three languages; the pigeons have agreed to carpool.",
    "By evening, a low fog of cinnamon will roll in off Lake Unwritten - visibility poor, pastries excellent, strangers unusually likely to share umbrellas and secrets.",
    "Tonight the moon does overtime, so night-shift bakers get double stars and everyone else gets home by following the warm smell of bread. Sleep well, commuters - tomorrow we hover again.",
]


def main():
    print(f"Forecast for {CITY}")
    for line in FORECAST:
        print(line)


if __name__ == "__main__":
    main()
