#c
c_orange = 255, 140, 0
c_gold = 255, 215, 0
c_grey = 200, 200, 200
c_white = 255, 255, 255
c_blue = 70, 130, 180

#g
grid_width = 20
grid_height = 12



#M
MENU_OPTION = ('jogar versão - DEMO',
               'jogar versão - COMPLETA',
               'ranking',
               'configuraçoes',
               'exit')

MONSTER_LIST = {
    "slime": {
        'hp': 20,
        "speed": 1,
        "images_key": "slime",

    },
    "goblin": {
        'hp': 50,
        "speed": 2,
        "images_key": "goblin",

    }
}
#s

SPAWN_INTERVAL_INICIAL = 20000
SPAWN_INTERVAL_LIMIT = 5000


SPAWN_POINTS_BORDA = [
    *[(x, 0) for x in range(20)],
    *[(x, 11) for x in range(20)],
    *[(0, y) for y in range(1, 11)],
    *[(19, y) for y in range(1, 11)],
]

#W
W_WIDTH = 1000
W_HEIGHT = 600