import pygame

class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name

    def run(self, ):
        pass

    def map_space(self, grid_width= 20, grid_height= 12):
        grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]
        return grid

    def demo(self, window):
        pygame.mixer_music.load('./asset/demoMusic.wav')
        pygame.mixer_music.play(-1)
        surf = pygame.image.load('./asset/mapaDemo.jpg').convert_alpha()
        surf = pygame.transform.scale(surf, window.get_size())
        rect = surf.get_rect()
        window.blit(surf, rect)
        grid = self.map_space()

        pygame.display.flip()

        while True:
           for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_ESCAPE:
                       return

    def sorry(self, window):
        surf = pygame.image.load('./asset/Desculpas.png')
        surf = pygame.transform.scale(surf, window.get_size())
        rect = surf.get_rect()
        window.blit(surf, rect)
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    return