#!/usr/bin/env python3

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

import random

class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

class HumanPlayer(Player):
    def move(self):
        result = None
        while result not in moves:
            result = str.strip(str.lower(input(f"Enter your move ({moves}): ")))
        return result

class ReflectPlayer(Player):
    def __init__(self):
        self.opponent_last_move = None

    def move(self):
        if self.opponent_last_move == None:
          return moves[0]
        else:
          return self.opponent_last_move

    def learn(self, my_move, their_move):
        self.opponent_last_move = their_move

class CyclePlayer(Player):
    def __init__(self):
        self.my_last_move = None

    def move(self):
        if self.my_last_move == None:
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

    def displayFinalMessage(self):
        print(f"\nFinal Score: Opponent: {self.p1_score}  You: {self.p2_score}")
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
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            print()
        print("Game over!")
        self.displayFinalMessage()


if __name__ == '__main__':
    game = Game(CyclePlayer(), HumanPlayer())
    game.play_game()
