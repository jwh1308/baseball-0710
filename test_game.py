from unittest import TestCase

from game import Game


class TestGame(TestCase):
    def setUp(self):
        super().setUp()
        self.game = Game()

    def generate_question(self, question):
        self.game.question = question

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

    def assert_matched_number(self, actual, solved, strike, ball):
        self.assertIsNotNone(actual)
        self.assertEqual(solved, actual.get_solved())
        self.assertEqual(strike, actual.get_strike())
        self.assertEqual(ball, actual.get_ball())

    def test_guess_perfect_answer(self):
        self.generate_question('123')
        self.assert_matched_number(self.game.guess('123'), True, 3, 0)

    def test_guess_wrong_answer(self):
        self.generate_question('123')
        self.assert_matched_number(self.game.guess('456'), False, 0, 0)

    def test_guess_partial_correct(self):
        self.generate_question('123')
        self.assert_matched_number(self.game.guess('124'), False, 2, 0)
        self.assert_matched_number(self.game.guess('314'), False, 0, 2)
        self.assert_matched_number(self.game.guess('329'), False, 1, 1)
