class PlayerStats:
    def __init__(self, player_list):
        self._players = player_list

    def top_scorers_by_nationality(self, nationality):
        filtered_list = [p for p in self._players if p.nationality == nationality]
        filtered_list.sort(key=lambda p: p.goals+p.assists, reverse=True)
        return filtered_list
