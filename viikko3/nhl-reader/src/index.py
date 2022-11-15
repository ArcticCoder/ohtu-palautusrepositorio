from player_reader import PlayerReader
from player_stats import PlayerStats

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"

    players = PlayerReader(url).players
    stats = PlayerStats(players).top_scorers_by_nationality("FIN")

    for player in stats:
        print(player)

if __name__ == "__main__":
    main()
