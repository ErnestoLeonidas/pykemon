import pygame
import ash

# Inicializar pygame
pygame.init()

# Dimensiones iniciales de la ventana
ANCHO = 128  # Ajustado según preferencias
ALTO = 128   # Ajustado según preferencias

# Escalado fijo
escalado = 6.0  # Ajustado según preferencias

# Crear la ventana
ventana = pygame.display.set_mode((int(ANCHO * escalado), int(ALTO * escalado)))
pygame.display.set_caption('Spritesheet')

# Cargar imagen de Pueblo Paleta
spritesheet = pygame.image.load('./sprites/palletTown.png')

# Dimensiones de la imagen recortada
x_sprite = 336
y_sprite = 23
ancho_sprite = 128
alto_sprite = 128

# Posición inicial de Ash
ash_x = 100  # Ajustado según preferencias
ash_y = 100  # Ajustado según preferencias

# Índice actual del sprite de Ash
indice_ash = 0

# Antes del bucle principal
teclas_anterior = pygame.key.get_pressed()

# Bucle principal
ejecutando = True
# Dentro del bucle principal
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Manejar eventos de teclado para mover a Ash
    teclas = pygame.key.get_pressed()
    ash_x, ash_y = ash.actualizar_posicion_ash(teclas, ash_x, ash_y, ANCHO, ALTO)

    # Incrementar el contador de frames
    ash.frame_contador += 1
    
    # Cambiar el índice del sprite de Ash si el contador ha alcanzado el valor deseado
    if ash.frame_contador >= ash.FRAME_RATE:
        indice_ash = (indice_ash + 1) % 10  # Selecciona uno de los 10 sprites de Ash
        ash.frame_contador = 0  # Reinicia el contador

    # Dibujar la imagen recortada en la ventana
    ventana.blit(pygame.transform.scale(spritesheet.subsurface((x_sprite, y_sprite, ancho_sprite, alto_sprite)), (int(ancho_sprite * escalado), int(alto_sprite * escalado))), (0, 0))

    # Obtener el sprite actual de Ash
    if teclas[pygame.K_DOWN]:
        ash_sprite = ash.actualizar_sprite_abajo(indice_ash, teclas)
    elif teclas[pygame.K_UP]:
        ash_sprite = ash.actualizar_sprite_arriba(indice_ash, teclas)
    elif teclas[pygame.K_LEFT]:
        ash_sprite = ash.actualizar_sprite_izquierda(indice_ash, teclas)
    elif teclas[pygame.K_RIGHT]:
        ash_sprite = ash.actualizar_sprite_derecha(indice_ash, teclas)
    else:
        ash_sprite = ash.actualizar_sprite_abajo(indice_ash, teclas)  # Utilizamos la función de abajo como valor por defecto

    # Dibujar el sprite de Ash en la ventana
    ventana.blit(pygame.transform.scale(ash_sprite, (int(ash.ASH_ANCHO * escalado), int(ash.ASH_ALTO * escalado))), (int(ash_x * escalado), int(ash_y * escalado)))

    # Actualizar la pantalla
    pygame.display.flip()


# Salir de pygame
pygame.quit()
