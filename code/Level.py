import pygame

class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name

    def run(self, ):
        pass



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