import pygame

class GameState:
    def __init__(self, game):
        self.game = game
        self.buttons = []
        self.clock = pygame.time.Clock()

    # Overwrite this function to choose what events should be checked
    def HandleEvents(self):
        events = pygame.event.get()
        self.HandleBasicEvents(events)

    # Overwrite this function to choose what to Update
    def Update(self):
        self.UpdateSprites()
        self.UpdateButtons()

    # Clear the screen before drawing the next frame
    def ClearScreen(self):
        black = (0, 0, 0)
        self.game.screen.fill(black)

    # Overwrite this function to choose what to draw
    def DrawScreen(self):
        pass

    # Scale the screen that everything is blitted to and then blit it to the actual display
    def UpdateDisplay(self):
        scaled_screen = pygame.transform.scale(self.game.screen, (self.game.rs_width,
                                                                  self.game.rs_height))
        self.game.render_screen.blit(scaled_screen, (0, 0))
        pygame.display.flip()

    # Control the amount of loops per second
    def HandleFPS(self, frames_per_second):
        self.clock.tick(frames_per_second)

# ------------------------------------------------------------------------------
    # Only handle basic events (wanting to exit the program)
    def HandleBasicEvents(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.game.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    self.game.running = False

    def IfKeyPressed(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                return True
        return False

    # Handle the basic events but also check to see any buttons are being pressed
    def HandleButtonEvents(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    if button.hovered:
                        button.Clicked()

    def UpdateSprites(self):
        pass

    # Check to see if mouse is hovering over any buttons, will call button.Hovered() if true
    def UpdateButtons(self):
        mouse_pos = self.GetMousePos()
        for button in self.buttons:
            button.Update(mouse_pos)

    # Get accurate position of the mouse for objects like buttons
    def GetMousePos(self):
        # Mouse position needs to be scaled due to the scaling of the screen
        unscaled_mouse_pos = pygame.mouse.get_pos()
        x = unscaled_mouse_pos[0] * (self.game.screen_width / self.game.display_info.current_w)
        y = unscaled_mouse_pos[1] * (self.game.screen_height / self.game.display_info.current_h )
        return (x, y)
