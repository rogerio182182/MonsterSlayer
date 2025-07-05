from abc import ABC, abstractmethod

import pygame


class Entity(ABC):

    def __init__(self, name: str,grid_x, grid_y, tile_size, images_d: dict):
        self.name = name
        self.grid_pos = (grid_x, grid_y)
        self.tile_size = tile_size
        self.direction = "down"
        self.images = images_d
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect(topleft=(grid_x * tile_size, grid_y * tile_size))

    def move(self, dx, dy):
        x, y = self.grid_pos
        new_x = x + dx
        new_y = y + dy


        if 0 <= new_x < 20 and 0 <= new_y < 12:
            self.grid_pos = (new_x, new_y)
            self.rect.topleft = (new_x * self.tile_size, new_y * self.tile_size)

        if dx > 0:
            self.direction = "right"
        elif dx < 0:
            self.direction = "left"
        elif dy > 0:
            self.direction = "down"
        elif dy < 0:
            self.direction = "up"


        self.rect.topleft = (self.grid_pos[0] * self.tile_size, self.grid_pos[1] * self.tile_size)
        self.image = self.images[self.direction]

    def draw(self, surface):
        surface.blit(self.image, self.rect)

