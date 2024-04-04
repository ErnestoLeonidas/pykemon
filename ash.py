import pygame

# Tamaño del sprite de Ash
ASH_ANCHO = 16
ASH_ALTO = 16

# Velocidad de movimiento de Ash (número más bajo = más lento)
VEL_MOVIMIENTO = 0.5  # Ajustado según preferencias

# Definir una nueva variable para controlar la velocidad de alternancia de los sprites
FRAME_RATE = 10  # Ajusta este valor según sea necesario

# Agregar un contador de frames
frame_contador = 0


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

def actualizar_sprite_abajo(indice, teclas):
    """Actualizar el sprite de Ash cuando se mueve hacia abajo"""
    global frame_contador  # Para acceder a la variable frame_contador definida fuera de esta función
    if teclas[pygame.K_DOWN]:
        if indice % 2 == 0:
            return pygame.image.load('./sprites/down_walk_1.png')
        else:
            return pygame.image.load('./sprites/down_walk_2.png')
    else:
        return pygame.image.load('./sprites/down_stop.png')

def actualizar_sprite_arriba(indice, teclas):
    """Actualizar el sprite de Ash cuando se mueve hacia arriba"""
    global frame_contador  # Para acceder a la variable frame_contador definida fuera de esta función
    if teclas[pygame.K_UP]:
        if indice % 2 == 0:
            return pygame.image.load('./sprites/top_walk_1.png')
        else:
            return pygame.image.load('./sprites/top_walk_2.png')
    else:
        return pygame.image.load('./sprites/top_stop.png')
