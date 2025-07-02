import pygame

print('começo')
pygame.init()
window = pygame.display.set_mode(size=(1000, 600))

print('fim')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
