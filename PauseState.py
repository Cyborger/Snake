import GameState
import TextToImage
import pygame

class PauseState(GameState.GameState):
    def __init__(self, game):
        super().__init__(game)
        self.pause_image = TextToImage.TextImage(TextToImage.paused, 16, 16)
        self.pause_image.SetPosition(self.game.screen_width / 2 - self.pause_image.rect.width / 2,
                                      self.game.screen_height / 2 - self.pause_image.rect.height / 2)

    def HandleEvents(self):
        events = pygame.event.get()
        self.HandleBasicEvents(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.PlayGame()

    def DrawScreen(self):
        self.game.screen.blit(self.pause_image.image, self.pause_image.rect)
