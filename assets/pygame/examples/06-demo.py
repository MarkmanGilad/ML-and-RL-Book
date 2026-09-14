import pygame

pygame.init()
screen = pygame.display.set_mode((640, 400))
image = pygame.image.load("img/star.png").convert_alpha()
image = pygame.transform.scale(image, (80, 80))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not running:
        break

    screen.fill((17, 43, 65))
    screen.blit(image, (280, 160))
    pygame.display.update()

pygame.quit()
