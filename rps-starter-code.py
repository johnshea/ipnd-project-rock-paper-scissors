#!/usr/bin/env python3

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        result = None
        while result not in moves:
            result = str.lower(input(f"Enter your move ({moves}): "))
            result = str.strip(result)
        return result


class ReflectPlayer(Player):
    def __init__(self):
        self.opponent_last_move = None

    def move(self):
        if self.opponent_last_move is None:
            return moves[0]
        else:
            return self.opponent_last_move

    def learn(self, my_move, their_move):
        self.opponent_last_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_last_move = None

    def move(self):
        if self.my_last_move is None:
            index = 0
        else:
            index = moves.index(self.my_last_move)
            index = (index + 1) % len(moves)

        self.my_last_move = moves[index]

        return self.my_last_move


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Opponent played {move1}.\nYou played {move2}.")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        self.displayWinnerOfRound(move1, move2)

    def displayWinnerOfRound(self, move1, move2):
        p1_won_round = beats(move1, move2)
        winner = ""
        if p1_won_round:
            winner = "Opponent won"
            self.p1_score += 1
        elif move1 != move2:
            winner = "You won"
            self.p2_score += 1
        else:
            winner = "It was a tie"
        print(f"{winner} this round!")
        print(f"Current Score: Opponent: {self.p1_score} " +
              f"You: {self.p2_score}")

    def displayFinalMessage(self):
        print(f"\nFinal Score: Opponent: {self.p1_score} " +
              f"You: {self.p2_score}")
        winner = ""
        if self.p1_score > self.p2_score:
            winner = "Your opponent won"
        elif self.p2_score > self.p1_score:
            winner = "You won"
        else:
            winner = "It was a tie"
        print(f"{winner} this game!")

    def play_game(self):
        print("Game start!")
        number_of_rounds = self.prompt_for_number_of_rounds()
        for round in range(number_of_rounds):
            print(f"\nRound {round}:")
            self.play_round()
            print()
        print("Game over!")
        self.displayFinalMessage()

    def prompt_for_number_of_rounds(self):
        number_of_rounds = -1
        while number_of_rounds <= 0:
            response = input("Number of rounds to play (1 or more): ")
            try:
                number_of_rounds = int(response)
            except ValueError:
                number_of_rounds = -1
        return number_of_rounds


if __name__ == '__main__':
    game = Game(CyclePlayer(), HumanPlayer())
    game.play_game()
