import pygame.image

from code.Const import W_WIDTH, W_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))


    def run(self):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, 'LEVEL' )
            elif menu_return == MENU_OPTION[1]:
                level = Level.sorry(self, window=None)
            elif menu_return == MENU_OPTION[2]:
                pass
            elif menu_return == MENU_OPTION[3]:
                pass
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            pass




