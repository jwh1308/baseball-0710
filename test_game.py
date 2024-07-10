from unittest import TestCase

from game import Game, GameResult


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

    def test_guess_perfect_answer(self):
        self.game.question = '123'
        actual: GameResult = self.game.guess('123')

        self.assertIsNotNone(actual)
        self.assertEqual(True, actual.get_solved())
        self.assertEqual(3, actual.get_strike())
        self.assertEqual(0, actual.get_ball())

    def test_guess_wrong_answer(self):
        self.game.question = '123'
        actual: GameResult = self.game.guess('456')

        self.assertIsNotNone(actual)
        self.assertEqual(False, actual.get_solved())
        self.assertEqual(0, actual.get_strike())
        self.assertEqual(0, actual.get_ball())
