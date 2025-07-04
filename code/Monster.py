from random import random
import pygame
import os
from code.Entity import Entity

class Monster(Entity):
    def __init__(self, name, grid_x, grid_y, tile_size, images_d, hp=10, speed=1):
        super().__init__(name, grid_x, grid_y, tile_size, images_d)
        self.hp = hp
        self.player_pos = None
        self.last_move_time = 0
        self.speed = speed

    def set_player_position(self, player_pos):
        self.player_pos = player_pos

    def move_towards_player(self):
        now = pygame.time.get_ticks()
        cooldown = int(1000 / self.speed)
        if now - self.last_move_time < cooldown:
            return
        self.last_move_time = now

        if not self.player_pos:
            return

        player_x, player_y = self.player_pos
        monster_x, monster_y = self.grid_pos

        dx = player_x - monster_x
        dy = player_y - monster_y

        eixo = 'x' if abs(dx) > abs(dy) else 'y'

        if random() < 0.4:
            eixo = 'y' if eixo == 'x' else 'x'

        move_x, move_y = 0, 0
        if eixo == 'x':
            move_x = 1 if dx > 0 else -1 if dx < 0 else 0
        else:
            move_y = 1 if dy > 0 else -1 if dy < 0 else 0

        self.move(move_x, move_y)

    @staticmethod
    def carregar_imagens(nome):
        caminho = os.path.join('asset', 'Monster', nome)
        imagens = {
            "down": pygame.image.load(os.path.join(caminho, 'down.png')).convert_alpha(),
            "up": pygame.image.load(os.path.join(caminho, 'up.png')).convert_alpha(),
            "left": pygame.image.load(os.path.join(caminho, 'left.png')).convert_alpha(),
            "right": pygame.image.load(os.path.join(caminho, 'right.png')).convert_alpha(),
        }
        return imagens