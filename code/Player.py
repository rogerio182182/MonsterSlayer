import pygame
import os
from code.Entity import Entity



class Player(Entity):

    def __init__(self, name, grid_x, grid_y, tile_size, images_d):
        super().__init__(name,grid_x, grid_y, tile_size, images_d)
        self.grid_pos = (grid_x, grid_y)
        self.hp = 100
        self.speed = 1
        self.invulneravel = False
        self.tempo_invulneravel = 1000
        self.ultimo_dano = 0
        self.skills_ativas = []
        self.create_axe()



    def receber_dano(self, dano):
        tempo_atual = pygame.time.get_ticks()

        if not self.invulneravel:
            self.hp -= dano
            self.invulneravel = True
            self.ultimo_dano = tempo_atual
            print(f"Jogador levou {dano} de dano! HP atual: {self.hp}")

    def atualizar_invulnerabilidade(self):
        tempo_atual = pygame.time.get_ticks()
        if self.invulneravel and tempo_atual - self.ultimo_dano >= self.tempo_invulneravel:
            self.invulneravel = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                super().move(0, 1)
            elif event.key == pygame.K_UP:
                super().move(0, -1)
            elif event.key == pygame.K_RIGHT:
                super().move(1, 0)
            elif event.key == pygame.K_LEFT:
                super().move(-1, 0)

    @staticmethod
    def carregar_imagens():
        caminho = os.path.join('asset', 'Player')
        Player.images_d = {
            "up": pygame.image.load(os.path.join(caminho,  "p_up.png")).convert_alpha(),
            "down": pygame.image.load(os.path.join(caminho, "p_down.png")).convert_alpha(),
            "left": pygame.image.load(os.path.join(caminho, "p_left.png")).convert_alpha(),
            "right": pygame.image.load(os.path.join(caminho, "p_right.png")).convert_alpha(),
        }

    def create_axe(self):
        from code.EntityFactory import Entityfactory
        self.axe = Entityfactory.get_entity("axe", origin=self)