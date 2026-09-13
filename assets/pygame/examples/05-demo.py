import pygame

pygame.init()
screen = pygame.display.set_mode((640, 400))
clock = pygame.time.Clock()
header = pygame.Surface((640, 80))
main = pygame.Surface((640, 320))
header.fill((0, 0, 255))
main.fill((211, 211, 211))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not running:
        break

    screen.blit(header, (0, 0))
    screen.blit(main, (0, 80))
    pygame.display.update()
    clock.tick(60)

pygame.quit()
