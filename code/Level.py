import pygame

from code.Const import c_white, W_HEIGHT
from code.EntityFactory import Entityfactory
from code.Monster import Monster

from code.Player import Player


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

        Player.carregar_imagens()
        player = Entityfactory.get_entity("Player")
        Monster.carregar_imagens('slime')
        Monster.carregar_imagens('goblin')
        slime = Entityfactory.get_entity('slime')
        goblin = Entityfactory.get_entity('goblin')
        surf = pygame.image.load('./asset/mapaDemo.jpg').convert_alpha()
        surf = pygame.transform.scale(surf, window.get_size())
        rect = surf.get_rect()
        self.map_space()
        clock = pygame.time.Clock()


        while True:
           clock.tick(60)
           for event in pygame.event.get():
               if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_ESCAPE:
                       return
                   player.handle_event(event)

           window.blit(surf, rect)
           window.blit(player.image, player.rect.topleft)
           slime.set_player_position(player.grid_pos)
           slime.move_towards_player()
           window.blit(slime.image, slime.rect.topleft)

           goblin.set_player_position(player.grid_pos)
           goblin.move_towards_player()
           window.blit(goblin.image, goblin.rect.topleft)
           pygame.display.flip()

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