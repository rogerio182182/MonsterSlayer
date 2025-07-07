from random import choice

import pygame

from code.Monster import Monster
from code.Player import Player
from code.Const import MONSTER_LIST
from code.Skill import Skill


class Entityfactory:
    images_loaded = {}

    @staticmethod
    def get_entity(entity_name: str, origin=None):
        match entity_name:
            case 'Player':
                return Player("hero", 10, 6, 50, Player.images_d )
            case 'slime' | 'goblin':

               dados = MONSTER_LIST[entity_name]
               x, y = choice(Monster.get_spawn_points_borda())
               key = dados["images_key"]

               if key not in Entityfactory.images_loaded:
                   Entityfactory.images_loaded[key] = Monster.carregar_imagens(key)

               return Monster(
                   entity_name,
                   x,
                   y,
                   50,
                   Entityfactory.images_loaded[key],
                   hp=dados["hp"],
                   dano=dados['dano'],
                   speed=dados["speed"]
               )

            case 'axe':
               key = "axe"
               if key not in Entityfactory.images_loaded:
                   axe_images = {
                       "up": pygame.image.load('./asset/axe/axe_up.png').convert_alpha(),
                       "down": pygame.image.load('./asset/axe/axe_down.png').convert_alpha(),
                       "left": pygame.image.load('./asset/axe/axe_left.png').convert_alpha(),
                       "right": pygame.image.load('./asset/axe/axe_right.png').convert_alpha(),
                   }
                   Entityfactory.images_loaded[key] = axe_images


               grid_x, grid_y = origin.grid_pos

               return Skill(
                   name="axe_throw",
                   grid_x= grid_x,
                   grid_y= grid_y,
                   tile_size=origin.tile_size,
                   images_d=Entityfactory.images_loaded[key],
                   direction=origin.direction
               )
               raise ValueError(f"Entidade '{entity_name}' não encontrada.")