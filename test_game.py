from unittest import TestCase

from game import Game


class TestGame(TestCase):
    def setUp(self):
        super().setUp()
        self.game = Game()

    def assert_ilegal_argument(self, guess_num):
        try:
            self.game.guess(guess_num)
            self.fail()
        except TypeError:
            pass

    def test_exception_when_invalid_input(self):
        self.assert_ilegal_argument(None)
        self.assert_ilegal_argument('34')
        self.assert_ilegal_argument('3434')
        self.assert_ilegal_argument('34r')
        self.assert_ilegal_argument('344')
