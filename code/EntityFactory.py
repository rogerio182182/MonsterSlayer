from code.Monster import Monster
from code.Player import Player
from code.Const import MONSTER_LIST

class Entityfactory:
    images_loaded = {}

    @staticmethod
    def get_entity(entity_name: str,):
        match entity_name:
            case 'Player':
                return Player("hero", 10, 6, 50, Player.images_d )
            case 'slime' | 'goblin':

               dados = MONSTER_LIST[entity_name]
               key = dados["images_key"]

               if key not in Entityfactory.images_loaded:
                   Entityfactory.images_loaded[key] = Monster.carregar_imagens(key)

               return Monster(
                   entity_name,
                   dados["grid_x"],
                   dados["grid_y"],
                   50,
                   Entityfactory.images_loaded[key],
                   hp=dados["hp"],
                   speed=dados["speed"]
            )
            case _:
                raise ValueError(f"Entidade '{entity_name}' não encontrada.")