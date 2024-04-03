import pygame



# Tamaño del sprite de Ash
ASH_ANCHO = 16
ASH_ALTO = 16

# Velocidad de movimiento de Ash (número más bajo = más lento)
VEL_MOVIMIENTO = 1.0  # Ajustado según preferencias

# Índices de los sprites de Ash según su descripción
SPRITES_ASH = {
    "caminar_abajo_1": 0,
    "pausado_abajo": 1,
    "caminar_abajo_2": 2,
    "caminar_arriba_1": 3,
    "pausado_arriba": 4,
    "caminar_arriba_2": 5,
    "caminar_izquierda_1": 6,
    "caminar_izquierda_2": 7,
    "caminar_derecha_1": 8,
    "caminar_derecha_2": 9
}

def cargar_ash_sprite(indice):
    """Cargar el sprite de Ash en el índice dado"""
    ash_sprite_sheet = pygame.image.load('./sprites/ash.png')
    x = indice * (ASH_ANCHO + 1)  # Cada sprite está separado por 1 píxel
    ash_sprite = ash_sprite_sheet.subsurface(pygame.Rect(x, 0, ASH_ANCHO, ASH_ALTO))
    return ash_sprite

def mover_ash(teclas, ash_x, ash_y, ANCHO, ALTO):
    """Mover a Ash por el mapa"""
    if teclas[pygame.K_LEFT]:
        if ash_x > 0:
            ash_x -= VEL_MOVIMIENTO
    if teclas[pygame.K_RIGHT]:
        if ash_x < ANCHO - ASH_ANCHO:
            ash_x += VEL_MOVIMIENTO
    if teclas[pygame.K_UP]:
        if ash_y > 0:
            ash_y -= VEL_MOVIMIENTO
    if teclas[pygame.K_DOWN]:
        if ash_y < ALTO - ASH_ALTO:
            ash_y += VEL_MOVIMIENTO
    
    return ash_x, ash_y

def actualizar_posicion_ash(teclas, ash_x, ash_y, ANCHO, ALTO):
    """Actualizar la posición de Ash según las teclas presionadas"""
    return mover_ash(teclas, ash_x, ash_y, ANCHO, ALTO)
