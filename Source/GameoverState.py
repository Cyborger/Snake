import GameState
import TextToImage
import time


class GameoverState(GameState.GameState):
    def __init__(self, game):
        super().__init__(game)
        self.gameover = TextToImage.TextImage(TextToImage.gameover, 16, 16)
        self.gameover.SetPosition(self.game.screen_width / 2 - self.gameover.rect.width / 2,
                              self.game.screen_height / 2 - self.gameover.rect.height / 2)
        self.wait = 0

    def Update(self):
        self.wait += 1
        if self.wait > 30:
            self.wait = 0
            self.game.ReturnToStartMenu()

    def DrawScreen(self):
        self.game.screen.blit(self.gameover.image, self.gameover.rect)
