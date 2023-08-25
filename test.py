import unittest
from unittest.mock import patch
from game import Game

class TestGame(unittest.TestCase):

    def test_player_number(self):
        game = Game()
        number = game.player_number()
        self.assertEqual(len(number), 4)
        self.assertTrue(0000 <= int(number) <= 9999)


    def test_check_guess(self):
        game = Game()
        game.number = "0987"
        self.assertEqual(game.guess("0977"), "ooxo")
        self.assertEqual(game.guess("4321"), "")
        self.assertEqual(game.guess("1243"), "")
        self.assertEqual(game.guess("9078"), "xxxx")

    def test_quit_game(self):
        game = Game()
        self.assertTrue(game.quit_game('N'))
        self.assertTrue(game.quit_game('N'))
        self.assertFalse(game.quit_game('1234'))

    @patch('builtins.input', return_value='N')
    def test_game_ends_on_quit(self, mock_input):
        game = Game()
        game.play()



if __name__ == "__main__":
    unittest.main()


