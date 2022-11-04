import pygame
pygame.init()


screen = pygame.display.set_mode((320, 240))

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screen.fill((255, 255, 255))
                pygame.display.flip()