import pygame
import PlayingState
import StartMenuState
import GameoverState
import sys


class Game:
    def __init__(self):
        pygame.init()
        # Set size of screen (unscaled)
        self.screen_width = 768
        self.screen_height = 432
        self.screen_dimensions = (self.screen_width, self.screen_height)
        self.screen = pygame.Surface(self.screen_dimensions)
        # self.screen will be blitted to the actual screen display
        self.display_info = pygame.display.Info()
        self.rs_width = 0
        self.rs_height = 0
        if sys.platform != "linux":
            self.rs_width = self.display_info.current_w
            self.rs_height = self.display_info.current_h
        else:
            self.rs_width = self.screen_width
            self.rs_height = self.screen_height

        self.render_screen = pygame.display.set_mode((self.rs_width, self.rs_height))
        # Define states
        self.start_menu_state = StartMenuState.StartMenuState(self)
        self.playing_state = PlayingState.PlayingState(self)
        self.gameover_state = GameoverState.GameoverState(self)
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

    def Gameover(self):
        self.ChangeState(self.gameover_state)

    def ReturnToStartMenu(self):
        self.playing_state.Reset()
        self.current_state = self.start_menu_state

    def ChangeState(self, state):
        self.current_state = state
