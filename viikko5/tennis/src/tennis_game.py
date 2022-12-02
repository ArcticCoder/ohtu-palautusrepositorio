class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.score1 = 0
        self.score2 = 0

        self.result_text = ""

        self._advantage_cutoff = 4
        self._score_diff_to_win = 2

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.score1 = self.score1 + 1
        else:
            self.score2 = self.score2 + 1

    def get_score(self):
        self.result_text = ""
        self._score_to_result_call()
        return self.result_text 

    def _score_to_result_call(self):
        if self.score1 == self.score2:
            self._handle_tie()
        elif max(self.score1, self.score2) >= self._advantage_cutoff:
            self._handle_advantage_play()
        else:
            self._handle_normal_points()

    def _handle_tie(self):
        if self.score1 < self._advantage_cutoff:
            self.result_text = "-All"

        call = self._points_to_call(self.score1)
        self.result_text = call + self.result_text

    def _handle_advantage_play(self):
        score_diff = self.score1 - self. score2

        if score_diff > 0:
            lead_player = self.player1_name
        else:
            lead_player = self.player2_name

        self.result_text = f"Advantage {lead_player}"

        if abs(score_diff) >= self._score_diff_to_win:
            self.result_text = f"Win for {lead_player}"

    def _handle_normal_points(self):
        player1_call = self._points_to_call(self.score1)
        player2_call = self._points_to_call(self.score2)

        self.result_text = player1_call + "-" + player2_call

    def _points_to_call(self, points):
        mapping = {0:"Love", 1:"Fifteen", 2:"Thirty", 3:"Forty", 4:"Deuce"}
        if points in mapping:
            return mapping[points]
        return ""
