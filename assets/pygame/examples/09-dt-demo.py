import pygame

pygame.init()
screen = pygame.display.set_mode((640, 400))
clock = pygame.time.Clock()
x, y = 40.0, 200
radius = 20
speed_x = 180.0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not running:
        break

    dt = clock.tick(60) / 1000
    x += speed_x * dt
    if x >= 640 - radius:
        x = 640 - radius
        speed_x = -abs(speed_x)
    elif x <= radius:
        x = radius
        speed_x = abs(speed_x)

    screen.fill((17, 43, 65))
    pygame.draw.circle(screen, (45, 190, 180),
                       (round(x), y), radius)
    pygame.display.update()

pygame.quit()
