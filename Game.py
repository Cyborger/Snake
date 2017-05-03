import pygame
import PlayingState
import StartMenuState
import GameoverState

class Game:
    def __init__(self):
        pygame.init()
        # Set size of screen (unscaled)
        self.screen_width = 768
        self.screen_height = 432
        self.screen_dimensions = (self.screen_width, self.screen_height)
        self.screen = pygame.Surface(self.screen_dimensions)
        # Create actual screen that the previous screen will be scaled then blitted to
        self.display_info = pygame.display.Info()
        self.render_screen = pygame.display.set_mode((self.display_info.current_w, self.display_info.current_h), pygame.FULLSCREEN)
        # Define states
        self.start_menu_state = StartMenuState.StartMenuState(self)
        self.playing_state = PlayingState.PlayingState(self)
        self.gameover_state = GameoverState.GameoverState(self)
            # Highscores
            # Pause
        self.current_state = None
        # When running is false, the program will end
        self.running = True

    def Start(self):
        self.current_state = self.start_menu_state
        self.GameLoop()

    def GameLoop(self):
        while self.running:
            self.current_state.HandleEvents()
            self.current_state.Update()
            self.current_state.ClearScreen()
            self.current_state.DrawScreen()
            self.current_state.UpdateDisplay()
            self.current_state.HandleFPS(10)

    def PlayGame(self):
        self.ChangeState(self.playing_state)

    def PauseGame(self):
        pass

    def Gameover(self):
        self.ChangeState(self.gameover_state)

    def ReturnToStartMenu(self):
        pass

    def GoToHighscores(self):
        pass

    def ChangeState(self, state):
        self.current_state = state
