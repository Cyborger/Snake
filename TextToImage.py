import pygame

class TextImage:
    def __init__(self, text, square_width, square_height):
        width = len(text[0]) * square_width
        height = len(text) * square_height
        self.sq_width = square_width
        self.sq_height = square_height
        self.image = pygame.Surface((width, height))
        self.rect = self.image.get_rect()
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.white = (255, 255, 255)
        self.DrawText(text)

    def SetPosition(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def DrawText(self, text_to_draw):
        for row in range(len(text_to_draw)):
            for char in range(len(text_to_draw[row])):
                char_value = text_to_draw[row][char]
                self.image.blit(self.GetSquare(char_value), (char * self.sq_width, row * self.sq_height))

    def GetSquare(self, char):
        color = None
        if char == 'r':
            color = self.red
        elif char == ' ':
            color = self.black
        elif char == 'w':
            color = self.white
        else:
            print("invalid char for drawing text")
        surface = pygame.Surface((self.sq_width, self.sq_height))
        surface.fill(color)
        return surface

title_screen = ["wwwww w   w wwwww w  ww wwwww",
                "w     ww  w w   w w w   w    ",
                "wwrww w r w wwrww rw    wwr  ",
                "    w w  ww w   w w w   w    ",
                "wwwww w   w w   w w  ww wwwww"]

press_anything = ["wwwww wwwww wwwww wwwww wwwww   wwwww w   w w   w wwwww w    w wwwww w   w wwww    wwwww wwwww   wwwww wwwww wwwww wwwww wwwww",
                  "w   w w   w w     w     w       w   w ww  w  w w    w   w    w   w   ww  w w         w   w   w   w       w   w   w w   w   w  ",
                  "wwwww wwwww www   wwwww wwwww   wwwww w w w   w     w   wwwwww   w   w w w w www     w   w   w   wwwww   w   wwwww wwwww   w  ",
                  "w     ww    w         w     w   w   w w  ww   w     w   w    w   w   w  ww w  w      w   w   w       w   w   w   w ww      w  ",
                  "w     w www wwwww wwwww wwwww   w   w w   w   w     w   w    w wwwww w   w wwww      w   wwwww   wwwww   w   w   w w www   w  "]

gameover = ["wwww  wwwww w   w wwwww wwwww w   w wwwww wwwww",
            "w     w   w ww ww w     w   w w   w w     w   w",
            "w www wwwww w w w www   w   w  w w  www   wwwww",
            "w  w  w   w w   w w     w   w  w w  w     ww   ",
            "wwww  w   w w   w wwwww wwwww   w   wwwww w www"]

paused = ["wwwww wwwww w   w wwwww wwwww wwww ",
          "w  ww w   w w   w w     w     w   w",
          "wwwww wwwww w   w wwwww www   w   w",
          "w     w   w w   w     w w     w   w",
          "w     w   w wwwww wwwww wwwww wwww "]
