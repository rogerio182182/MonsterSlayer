import pygame

import time
import random

from code.Const import SPAWN_INTERVAL_INICIAL, SPAWN_INTERVAL_LIMIT
from code.EntityFactory import Entityfactory
from code.Monster import Monster

from code.Player import Player


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.monsters = []
        self.spawn_timer = 0
        self.spawn_interval = SPAWN_INTERVAL_INICIAL

    def run(self, ):
        pass

    def map_space(self, grid_width= 20, grid_height= 12):
        grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]
        return grid

    def demo(self, window):
        pygame.mixer_music.load('./asset/demoMusic.wav')
        pygame.mixer_music.play(-1)

        font = pygame.font.SysFont(None, 28)

        # Contador de tempo jogado
        start_time = pygame.time.get_ticks()

        Player.carregar_imagens()
        player = Entityfactory.get_entity("Player")
        surf = pygame.image.load('./asset/mapaDemo.jpg').convert_alpha()
        surf = pygame.transform.scale(surf, window.get_size())
        rect = surf.get_rect()
        self.map_space()

        tipo = random.choice(["slime", "goblin"])
        novo_monstro = Entityfactory.get_entity(tipo)
        self.monsters.append(novo_monstro)

        while True:
            current_time = pygame.time.get_ticks()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return
                    player.handle_event(event)



            if current_time - self.spawn_timer >= self.spawn_interval:
                self.spawn_timer = current_time

                tipo = random.choice(["slime", "goblin"])
                novo_monstro = Entityfactory.get_entity(tipo)
                self.monsters.append(novo_monstro)

                if self.spawn_interval > SPAWN_INTERVAL_LIMIT:
                    self.spawn_interval = max(SPAWN_INTERVAL_LIMIT, self.spawn_interval - 1000)

            window.blit(surf, rect)
            window.blit(player.image, player.rect.topleft)

            for monstro in self.monsters:
                monstro.set_player_position(player.grid_pos)
                monstro.move_towards_player()
                window.blit(monstro.image, monstro.rect.topleft)

            # Atualiza tempo jogado
            elapsed_time = (pygame.time.get_ticks() - start_time) // 1000  # em segundos

            # Texto do painel
            info_text = [
                f"Tempo: {elapsed_time}s",
                f"Monstros: {len(self.monsters)}",
                f"Spawn: {self.spawn_interval // 1000}s"
            ]

            # Desenha fundo do painel
            pygame.draw.rect(window, (0, 0, 0), (0, 0, 200, len(info_text) * 30))  # fundo preto

            # Renderiza os textos
            for i, linha in enumerate(info_text):
                texto_surface = font.render(linha, True, (255, 255, 255))  # texto branco
                window.blit(texto_surface, (10, 10 + i * 30))
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