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
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        p1_won_round = beats(move1, move2)
        if p1_won_round:
            print("Player 1 won!")
            self.p1_score += 1
        elif move1 != move2:
            print("Player 2 won!")
            self.p2_score += 1
        else:
            print("It was a tie!")
        print(f"Player1: {self.p1_score}  Player 2: {self.p2_score}")

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(CyclePlayer(), HumanPlayer())
    game.play_game()
