import pygame


class gameBoard():
    def __init__(self, size):
        self.size = size
        self.width = self.size[0]
        self.height = self.size[1]

    def board(self):
        self.squearex = " ---"
        self.squarey = "|   "

        self.x = self.squearex * self.width + "\n"
        self.y = self.squarey * (self.width + 1) + "\n"

        return (self.x + self.y) * self.height + self.x





game = gameBoard([3,3])
print game.board()