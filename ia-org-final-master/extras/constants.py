
#Colores
GREEN = (145, 210, 144)
YELLOW = (255, 237, 81)
YE = (200, 200, 80)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
# GREEN2 = (0, 0, 0)
GREEN2 = (0, 153, 0)
WHITE = (181, 225, 174)
WHITE2 = (255, 255, 255)
BLACK = (0, 0, 0)

#Pantalla
WIDTH = 520
HEIGHT = 540
size = (WIDTH, HEIGHT)
COLS = 7
ROWS = [[2, 3, 4],
        list(range(0, 7)),
        list(range(0, 7)),
        list(range(0, 7)),
        list(range(0, 7)),
        list(range(1, 6)), [3]]
PosicionPA = 110
distanciaHex = 44

tipos = {GREEN2 : BLUE, BLUE : RED, RED : GREEN2}