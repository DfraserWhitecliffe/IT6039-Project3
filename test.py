import unittest
import bowling_game

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = bowling_game.BowlingGame()

    def test_gutter_game(self):
        for i in range(0, 20):
            self.game.rolls(0)
        assert self.game.score()==0

    def test_all_0nes(self):
        self.rollMany(1, 20)
        assert self.game.score()==20

    def test_one_spare(self):
        self.game.rolls(5)
        self.game.rolls(5)
        self.game.rolls(3)
        self.rollMany(0,17)
        assert self.game.score()==16

    def test_one_strike(self):
        self.game.rolls(10)
        self.game.rolls(4)
        self.game.rolls(3)
        self.rollMany(0,16)
        assert  self.game.score()==24

    def test_perfect_game(self):
        self.rollMany(10,12)
        assert self.game.score()==300

    def test_one_spare(self):
        self.rollMany(5,21)
        assert self.game.score()==150

    def rollMany(self, pins,rolls):
        
        for i in range(rolls):
            self.game.rolls(pins)

