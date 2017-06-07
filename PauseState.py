import GameState
import TextToImage
import pygame

class PauseState(GameState.GameState):
    def __init__(self, game):
        super().__init__(game)

    def HandleEvents(self):
        events = pygame.event.get()
        self.HandleBasicEvents(events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.PlayGame()

    def DrawScreen(self):
        pass
