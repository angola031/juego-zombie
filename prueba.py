import pygame

# Inicializar pygame
pygame.init()

# Configurar la pantalla
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Ejemplo de Colisiones y Teclas")

# Cargar el sonido de golpe
golpe_sound = pygame.mixer.Sound('disparo.mp3')

# Definir los rectángulos de los objetos
objeto1_rect = pygame.Rect(100, 100, 50, 50)
objeto2_rect = pygame.Rect(200, 100, 50, 50)

# Variables para controlar la reproducción del sonido y el estado de la tecla
sound_playing = False
key_pressed = False

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                key_pressed = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                key_pressed = False

    # Obtener las coordenadas del mouse
    mouse_pos = pygame.mouse.get_pos()

    # Actualizar la posición del objeto 1 con las coordenadas del mouse
    objeto1_rect.center = mouse_pos

    # Verificar colisión entre los objetos
    if objeto1_rect.colliderect(objeto2_rect) and key_pressed:
        if not sound_playing:
            # Reproducir el sonido de golpe solo si no se está reproduciendo actualmente
            golpe_sound.play(-1)  # -1 indica reproducción en bucle
            sound_playing = True
    else:
        if sound_playing:
            # Detener la reproducción del sonido
            golpe_sound.stop()
            sound_playing = False

    # Dibujar los objetos en pantalla
    pygame.draw.rect(screen, (255, 0, 0), objeto1_rect)
    pygame.draw.rect(screen, (0, 255, 0), objeto2_rect)

    # Actualizar la pantalla
    pygame.display.update()

# Finalizar pygame
pygame.quit()
