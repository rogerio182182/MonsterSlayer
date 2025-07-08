import time
from code.Entity import Entity
from code.EntityMediator import EntityMediator


class Skill(Entity):
    def __init__(self, name: str, grid_x, grid_y, tile_size, images_d: dict, direction):
        super().__init__(name, grid_x, grid_y, tile_size, images_d)

        self.hp = 1
        self.dano = 10
        self.direction = direction
        self.speed = 5
        self.duration = 5
        self.active = False
        self.start_time = None

        self.grid_pos = (grid_x, grid_y)
        self.tile_size = tile_size
        self.x = grid_x * tile_size
        self.y = grid_y * tile_size

        self.images_d = images_d

        direction_map_reverse = {
            (0, -1): "up",
            (0, 1): "down",
            (-1, 0): "left",
            (1, 0): "right"
        }

        if isinstance(self.direction, str):
            dir_key = self.direction
        else:
            dir_key = direction_map_reverse.get(self.direction, "down")

        self.image = images_d.get(dir_key, list(images_d.values())[0])
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def use(self, grid_x, grid_y, direction):
        self.grid_pos = (grid_x, grid_y)
        self.x = grid_x * self.tile_size
        self.y = grid_y * self.tile_size
        self.direction = direction
        self.active = True
        self.start_time = time.time()

        direction_map_reverse = {
            (0, -1): "up",
            (0, 1): "down",
            (-1, 0): "left",
            (1, 0): "right"
        }

        if isinstance(direction, str):
            dir_key = direction
        else:
            dir_key = direction_map_reverse.get(direction, "down")

        self.image = self.images_d.get(dir_key, list(self.images_d.values())[0])
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update(self, delta_time):
        if not self.active:
            return

        direction_map = {
            "up": (0, -1),
            "down": (0, 1),
            "left": (-1, 0),
            "right": (1, 0)
        }

        if isinstance(self.direction, str):
            move_x, move_y = direction_map.get(self.direction, (0, 0))
        else:
            move_x, move_y = self.direction

        self.x += move_x * self.speed * self.tile_size * delta_time
        self.y += move_y * self.speed * self.tile_size * delta_time

        self.rect.topleft = (self.x, self.y)

        if time.time() - self.start_time >= self.duration:
            self.active = False

    def draw(self, surface):
        if self.active and self.image:
            surface.blit(self.image, (self.x, self.y))


    def check_collision(self, entity_list):
        if not self.active:
            return

        EntityMediator.skill_collision(self, entity_list)