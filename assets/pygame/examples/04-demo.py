import pygame

pygame.init()
screen = pygame.display.set_mode((640, 400))
clock = pygame.time.Clock()
FPS = 60
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not running:
        break

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
