import pygame

pygame.init()
screen = pygame.display.set_mode((640, 400))
x, y = 320, 200
color = (45, 190, 180)
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color = (245, 170, 45)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                color = (45, 190, 180)
    if not running:
        break

    screen.fill((17, 43, 65))
    pygame.draw.circle(screen, color, (x, y), 25)
    pygame.display.update()

pygame.quit()
