import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(PlayerReaderStub())

    def test_search_none(self):
        self.assertFalse(self.statistics.search("Notexist"))

    def test_search(self):
        testPlayerName = "Kurri"
        foundPlayer = self.statistics.search(testPlayerName)
        self.assertEqual(foundPlayer.name, testPlayerName)

    def test_team_search(self):
        testTeam = ["Semenko", "Kurri", "Gretzky"]
        foundTeam = [x.name for x in self.statistics.team("EDM")]
        self.assertEqual(foundTeam, testTeam)

    def test_top(self):
        testTop2 = ["Gretzky", "Lemieux"]
        foundTop2 = [x.name for x in self.statistics.top(2)]
        self.assertEqual(foundTop2, testTop2)
