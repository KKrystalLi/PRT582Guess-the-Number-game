import unittest
from game import Game

class TestGame(unittest.TestCase):

    def test_player_number(self):
        game = Game()
        number = game.player_number()
        self.assertEqual(len(number), 4)
        self.assertTrue(1000 <= int(number) <= 9999)


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

if __name__ == "__main__":
    unittest.main()