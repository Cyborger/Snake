import pygame

class Berry(pygame.sprite.Sprite):
    def __init__(self, x, y):
        width = height = 16
        red = (255, 0, 0)
        self.image = pygame.Surface((width, height))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def IsEaten(self, snake):
        for piece in snake.pieces:
            if pygame.sprite.collide_rect(self, piece):
                return True

        return False
