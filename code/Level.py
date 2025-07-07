import pygame

import time
import random

from code.Const import SPAWN_INTERVAL_INICIAL, SPAWN_INTERVAL_LIMIT
from code.EntityFactory import Entityfactory
from code.EntityMediator import EntityMediator
from code.Monster import Monster

from code.Player import Player


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list = []
        self.spawn_timer = 0
        self.spawn_interval = SPAWN_INTERVAL_INICIAL


    def run(self, ):
        pass

    def map_space(self, grid_width= 20, grid_height= 12):
        grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]
        return grid

    def demo(self, window):
        self.som_dano = pygame.mixer.Sound('./asset/monsterDamage.mp3')
        pygame.mixer_music.load('./asset/demoMusic.wav')
        pygame.mixer_music.play(-1)

        font = pygame.font.SysFont(None, 28)
        start_time = pygame.time.get_ticks()

        Player.carregar_imagens()
        player = Entityfactory.get_entity("Player")
        self.entity_list.append(player)

        surf = pygame.image.load('./asset/mapaDemo.jpg').convert_alpha()
        surf = pygame.transform.scale(surf, window.get_size())
        rect = surf.get_rect()

        self.map_space()

        tipo = random.choice(["slime", "goblin"])
        novo_monstro = Entityfactory.get_entity(tipo)
        self.entity_list.append(novo_monstro)

        clock = pygame.time.Clock()

        while True:
            delta_time = clock.tick(60) / 1000
            current_time = pygame.time.get_ticks()

            EntityMediator.monster_collision(self.entity_list, player, self.som_dano)
            player.atualizar_invulnerabilidade()

            # Entrada do jogador
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

                    if event.key == pygame.K_SPACE:
                        nova_skill = Entityfactory.get_entity("axe", origin=player)
                        nova_skill.use(player.grid_pos[0], player.grid_pos[1], player.direction)
                        player.skills_ativas.append(nova_skill)

                    player.handle_event(event)

            # Atualiza skills
            for skill in player.skills_ativas[:]:
                skill.update(delta_time)
                skill.check_collision(self.entity_list)
                if not skill.active:
                    player.skills_ativas.remove(skill)

            # Spawning de monstros
            if current_time - self.spawn_timer >= self.spawn_interval:
                self.spawn_timer = current_time
                tipo = random.choice(["slime", "goblin"])
                novo_monstro = Entityfactory.get_entity(tipo)
                self.entity_list.append(novo_monstro)

                if self.spawn_interval > SPAWN_INTERVAL_LIMIT:
                    self.spawn_interval = max(SPAWN_INTERVAL_LIMIT, self.spawn_interval - 1000)

            # === DESENHO NA TELA (ORDEM IMPORTANTE) ===

            # Fundo
            window.blit(surf, rect)

            # Player
            window.blit(player.image, player.rect.topleft)

            # Monstros
            for entity in self.entity_list:
                if isinstance(entity, Monster):
                    entity.set_player_position(player.grid_pos)
                    entity.move_towards_player()
                window.blit(entity.image, entity.rect.topleft)

            # Skills
            for skill in player.skills_ativas:
                skill.draw(window)

            # Painel de informações
            elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
            info_text = [
                f"Tempo: {elapsed_time}s",
                f"Monstros: {len(self.entity_list)}",
                f"Spawn: {self.spawn_interval // 1000}s"
            ]

            pygame.draw.rect(window, (0, 0, 0), (0, 0, 200, len(info_text) * 30))
            for i, linha in enumerate(info_text):
                texto_surface = font.render(linha, True, (255, 255, 255))
                window.blit(texto_surface, (10, 10 + i * 30))

            # Atualiza a tela
            pygame.display.flip()

            # Verifica entidades sem HP
            EntityMediator.verify_hp(self.entity_list)

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