import pygame

pygame.init()
screen = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Close the window")
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not running:
        break

    pygame.display.update()

pygame.quit()
