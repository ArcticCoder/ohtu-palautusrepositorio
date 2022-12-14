import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        response = requests.get(url).json()

        self._players = []
        for player_dict in response:
            player = Player(
                player_dict["name"],
                player_dict["nationality"],
                player_dict["assists"],
                player_dict["goals"],
                player_dict["penalties"],
                player_dict["team"],
                player_dict["games"]
            )

            self._players.append(player)

    @property
    def players(self):
        return self._players
