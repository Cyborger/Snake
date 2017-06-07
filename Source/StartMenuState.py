import GameState
import TextToImage
import pygame

class StartMenuState(GameState.GameState):
    def __init__(self, game):
        super().__init__(game)
        self.title_screen = TextToImage.TextImage(TextToImage.title_screen, 16, 16)
        self.title_screen.SetPosition(self.game.screen_width / 2 - self.title_screen.rect.width / 2,
                                      self.game.screen_height / 2 - self.title_screen.rect.height / 2)
        self.press_anything = TextToImage.TextImage(TextToImage.press_anything, 4, 4)
        self.press_anything.SetPosition(self.game.screen_width / 2 - self.press_anything.rect.width / 2,
                                        self.game.screen_height - self.press_anything.rect.height - 50)

    def HandleEvents(self):
        events = pygame.event.get()
        self.HandleBasicEvents(events)
        if self.IfKeyPressed(events):
            self.game.PlayGame()

    def DrawScreen(self):
        self.game.screen.blit(self.title_screen.image, self.title_screen.rect)
        self.game.screen.blit(self.press_anything.image, self.press_anything.rect)
