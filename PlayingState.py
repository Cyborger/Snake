import GameState
import Snake
import pygame
import Berry
import random

class PlayingState(GameState.GameState):
    def __init__(self, game):
        super().__init__(game)
        self.snake = Snake.Snake()
        berry = Berry.Berry(96, 96)
        self.berries = [berry]
        self.berries_collected = 0
        self.max_berries = 1
        random.seed()

    def HandleEvents(self):
        events = pygame.event.get()
        self.HandleBasicEvents(events)
        self.HandleMovementKeypresses(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.Pause()

    def HandleMovementKeypresses(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.snake.ChangeDirection(Snake.Direction.UP)
                elif event.key == pygame.K_d:
                    self.snake.ChangeDirection(Snake.Direction.RIGHT)
                elif event.key == pygame.K_s:
                    self.snake.ChangeDirection(Snake.Direction.DOWN)
                elif event.key == pygame.K_a:
                    self.snake.ChangeDirection(Snake.Direction.LEFT)

    def Update(self):
        self.snake.Move()
        self.CheckForEatenBerries()
        self.snake.CheckOffScreen(self.game.screen_width,
                                  self.game.screen_height)
        self.snake.CheckDeath()
        self.CheckGameover()

    def DrawScreen(self):
        for piece in self.snake.pieces:
            self.game.screen.blit(piece.image, piece.rect)
        for berry in self.berries:
            self.game.screen.blit(berry.image, berry.rect)

    def CheckForEatenBerries(self):
        for berry in self.berries:
            if berry.IsEaten(self.snake):
                self.berries.remove(berry)
                self.berries_collected += 1
                self.snake.BerryEaten()
                self.GenerateBerries(self.max_berries - len(self.berries))

    def CheckGameover(self):
        if not self.snake.alive:
            self.game.Gameover()

    def GenerateBerries(self, number):
        for i in range(number):
            found_valid_location = False
            new_berry = Berry.Berry(0, 0)
            while not found_valid_location:
                generated_location = self.GenerateBerryPosition()
                new_berry.rect.x = generated_location[0]
                new_berry.rect.y = generated_location[1]
                for piece in self.snake.pieces:
                    if pygame.sprite.collide_rect(new_berry, piece):
                        found_valid_location = False
                        break
                    else:
                        found_valid_location = True
            self.berries.append(new_berry)

    def GenerateBerryPosition(self):
        possible_x = self.game.screen_width / 16 - 1
        possible_y = self.game.screen_height / 16 - 1
        gen_x = random.randint(0, possible_x)
        gen_y = random.randint(0, possible_y)
        return (gen_x * 16, gen_y * 16)

    def Reset(self):
        self.snake.ResetSize()
