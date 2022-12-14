class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games
    
    def __str__(self):
        return f"({self.nationality}) {self.name:30} {self.team} {self.goals:3} + {self.assists:3} = {self.goals+self.assists:3}"
