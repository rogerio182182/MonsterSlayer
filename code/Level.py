import pygame


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name

    def run(self, ):
        pass

    def sorry(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Desculpas.png')
        self.rect = self.surf.get_rect()
        self.window.blit(source=self.surf, dest=self.rect)
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()