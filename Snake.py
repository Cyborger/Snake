import pygame
import SnakePiece
from enum import Enum
import copy

class Direction(Enum):
    NONE = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class Snake:
    def __init__(self):
        self.block_size = 16
        starting_piece_1 = SnakePiece.SnakePiece(0, 0)
        starting_piece_2 = SnakePiece.SnakePiece(16, 0)
        self.pieces = [starting_piece_1, starting_piece_2]
        self.direction = Direction.NONE
        self.new_direction = Direction.NONE
        self.growing = False
        self.alive = True

    def ChangeDirection(self, direction):
        new_direction = direction.value % 2
        current_direction = self.direction.value % 2
        if not new_direction == current_direction or self.direction == Direction.NONE:
            self.new_direction = direction

    def Move(self):
        self.direction = self.new_direction
        if self.direction == Direction.UP:
            self.MoveY(-self.block_size)
        elif self.direction == Direction.RIGHT:
            self.MoveX(self.block_size)
        elif self.direction == Direction.DOWN:
            self.MoveY(self.block_size)
        elif self.direction == Direction.LEFT:
            self.MoveX(-self.block_size)

    def MoveX(self, x):
        held_position = copy.copy(self.pieces[0].rect)
        self.pieces[0].rect.x += x
        self.MoveRestOfPieces(held_position)

    def MoveY(self, y):
        held_position = copy.copy(self.pieces[0].rect)
        self.pieces[0].rect.y += y
        self.MoveRestOfPieces(held_position)

    def MoveRestOfPieces(self, position_of_first_piece):
        held_position = position_of_first_piece
        for piece in self.pieces[1:]:
            previous_position = copy.copy(piece.rect)
            piece.rect = copy.copy(held_position)
            held_position = copy.copy(previous_position)
            if piece == self.pieces[-1]:
                if self.growing:
                    new_piece = SnakePiece.SnakePiece(held_position.x, held_position.y)
                    self.pieces.append(new_piece)
                    self.growing = False

    def CheckOffScreen(self, screen_width, screen_height):
        self.CheckHorizontalOffScreen(screen_width)
        self.CheckVerticalOffScreen(screen_height)

    def CheckHorizontalOffScreen(self, screen_width):
        for piece in self.pieces:
            if piece.rect.x < 0:
                piece.rect.x = screen_width - 16
            elif piece.rect.x >= screen_width:
                piece.rect.x = 0

    def CheckVerticalOffScreen(self, screen_height):
        for piece in self.pieces:
            if piece.rect.y < 0:
                piece.rect.y = screen_height - 16
            elif piece.rect.y >= screen_height:
                piece.rect.y = 0

    def BerryEaten(self):
        self.growing = True
