import pygame
import pygame.image

from code.Const import W_WIDTH, c_gold, c_white, MENU_OPTION, c_grey, c_orange


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.jpg')
        self.rect = self.surf.get_rect()

    def run(self, ):
        pygame.mixer_music.load('./asset/MenuMusic.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(120, 'Monster', c_gold, ((W_WIDTH / 2), 70))
            self.menu_text(100, 'Slayer', c_gold, ((W_WIDTH / 2), 150))

            for i in range(len(MENU_OPTION)):
                self.menu_text(50, MENU_OPTION[i], c_white, ((W_WIDTH / 2), 280 + 60 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
     #  font = pygame.font.SysFont(None, size= text_size)
        font = pygame.font.Font('./asset/FontePetrock.ttf', size=text_size)
        text_surface = font.render(text, True, text_color).convert_alpha()
        text_rect = text_surface.get_rect(center=text_center_pos)
        self.window.blit(source=text_surface, dest=text_rect)
