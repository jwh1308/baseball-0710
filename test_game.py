from unittest import TestCase

from game import Game


class TestGame(TestCase):
    def setUp(self):
        super().setUp()
        self.game = Game()

    def test_exception_when_input_is_not_exist(self):
        with self.assertRaises(TypeError):
            self.game.guess()
