# game.py
import random

class Game:

    def __init__(self):
        self.number = self.player_number()
        self.attempts = 0

    def player_number(self):
        return str(random.randint(0000, 9999))

    def guess(self, guess):
        answer = []
        for i in range(4):
            if guess[i] == self.number[i]:
                answer.append("o")
            elif guess[i] in self.number:
                answer.append("x")

        return ''.join(answer)
    def quit_game(self,player_input):
        return player_input == 'N'


    def play(self):
        print("Welcome to the Guess the Number game!")
        print("The player needs to guess a four digit randomly generated number.")
        print("We will give some clues about the number. ")
        print("-------------")
        print("|           |")
        print("| GOOD LUCK |")
        print("|           |")
        print("-------------")


        while True:
            if self.attempts >=1:
                again = input("Do you want to continue to guess?(Y/N)")
                check_quit = self.quit_game(again)
                if again == "N":
                    print("You have guessed the number in {} attempts.".format(self.attempts))
                    print("Thanks for playing! Hope to see you again!")
                    break

            guess_number = input("Enter your guess: ")
            self.attempts += 1
            if not guess_number.isnumeric():
                print("Please enter the number! ")
                continue
            if len(guess_number) != 4:
                print("Please enter four digit!")
                continue

            check_answer = self.guess(guess_number)
            if check_answer == "oooo":
                print(" -----------------")
                print("|                 |")
                print("| Cngratulations! |")
                print("|                 |")
                print(" ------------------")
                print("You got the correct answer!")
                print("You have guessed the number in {} attempts.".format(self.attempts))
                print("Thanks for playing!")
                break
            if check_answer =='':
                continue
            else:
                print("Hint: {}".format(check_answer))
                print(" 'o' means that the number is correct and is in the right spot")
                print(" 'x' means that the number is correct and buis in the wrong spot")


if __name__ == "__main__":
    game = Game()
    game.play()

