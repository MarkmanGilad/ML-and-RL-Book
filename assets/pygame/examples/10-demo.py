import pygame

pygame.init()
screen = pygame.display.set_mode((640, 400))
clock = pygame.time.Clock()
image = pygame.image.load("img/star.png").convert_alpha()
image = pygame.transform.scale(image, (80, 80))
rect = image.get_rect(center=(320, 200))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not running:
        break

    screen.fill((17, 43, 65))
    screen.blit(image, rect)
    pygame.draw.rect(screen, (245, 170, 45), rect, 2)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
