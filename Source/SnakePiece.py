import pygame

class SnakePiece(pygame.sprite.Sprite):
    def __init__(self, x, y, color = (255, 255, 255)):
        width = height = 16
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
