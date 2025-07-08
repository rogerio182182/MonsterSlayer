import pygame


import random

from code.Const import SPAWN_INTERVAL_INICIAL, SPAWN_INTERVAL_LIMIT, RANKING_POS, c_gold, c_orange, \
    c_cyan
from code.DBProxy import input_name, save_ranking, init_DB, watch_ranking
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

    def map_space(self, grid_width=20, grid_height=12):
        grid = [[0 for _ in range(grid_width)] for _ in range(grid_height)]
        return grid

    def demo(self, window):
        self.som_dano = pygame.mixer.Sound('./asset/monsterDamage.mp3')
        pygame.mixer_music.load('./asset/demoMusic.wav')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.3)


        Player.load_image()
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
            player.update_invunarable()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return

                    if event.key == pygame.K_SPACE:
                        nova_skill = Entityfactory.get_entity("axe", origin=player)
                        nova_skill.use(player.grid_pos[0], player.grid_pos[1], player.direction)
                        player.skills_ativas.append(nova_skill)

                    player.handle_event(event)

            for skill in player.skills_ativas[:]:
                skill.update(delta_time)
                skill.check_collision(self.entity_list)
                if not skill.active:
                    player.skills_ativas.remove(skill)

            if current_time - self.spawn_timer >= self.spawn_interval:
                self.spawn_timer = current_time
                tipo = random.choice(["slime", "goblin"])
                novo_monstro = Entityfactory.get_entity(tipo)
                self.entity_list.append(novo_monstro)

                if self.spawn_interval > SPAWN_INTERVAL_LIMIT:
                    self.spawn_interval = max(SPAWN_INTERVAL_LIMIT, self.spawn_interval - 1000)

            window.blit(surf, rect)

            window.blit(player.image, player.rect.topleft)

            for entity in self.entity_list:
                if isinstance(entity, Monster):
                    entity.set_player_position(player.grid_pos)
                    entity.move_towards_player()
                window.blit(entity.image, entity.rect.topleft)

            for skill in player.skills_ativas:
                skill.draw(window)

            pygame.display.flip()

            resultado = EntityMediator.verify_hp(self.entity_list)

            if resultado == "game_over":
                init_DB()
                nome_jogador = input_name(window)
                save_ranking(nome_jogador, EntityMediator.slimes_mortos, EntityMediator.goblins_mortos)

                self.ranking(window,)

                EntityMediator.reset_counter()
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

    def ranking(self, window):
        pygame.mixer_music.load('./asset/ranking.mp3')
        pygame.mixer_music.play(-1)

        fundo = pygame.image.load('./asset/Ranking.jpg')
        fundo = pygame.transform.scale(fundo, window.get_size())
        window.blit(fundo, fundo.get_rect())

        fonte_titulo = pygame.font.Font('./asset/FontePetrock2.ttf', 72)
        fonte_texto = pygame.font.Font('./asset/FontePetrock2.ttf', 28)

        titulo = fonte_titulo.render("RANKING", True, (c_orange))
        window.blit(titulo, titulo.get_rect(center=RANKING_POS['Title']))

        cabecalho = fonte_texto.render("Nome - Slimes - Goblins - Pontos", True, (c_gold))
        window.blit(cabecalho, cabecalho.get_rect(center=RANKING_POS['Label']))


        top_scores = watch_ranking()

        for i, (nome, slimes, goblins, pontos) in enumerate(top_scores):
            if i in RANKING_POS:
                texto = f"{nome} | {slimes} | {goblins} | {pontos}"
                linha = fonte_texto.render(texto, True, (c_cyan))
                window.blit(linha, linha.get_rect(center=RANKING_POS[i]))

        pygame.display.flip()


        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    return
