import pygame

pygame.init()
screen = pygame.display.set_mode((640, 400))
header = pygame.Surface((640, 80))
main = pygame.Surface((640, 320))
header.fill((0, 0, 255))
main.fill((211, 211, 211))
pygame.draw.line(main, (0, 0, 0),
                 (10, 10), (100, 100), 5)
pygame.draw.circle(main, (0, 180, 80),
                   (50, 50), 20, 2)
pygame.draw.circle(header, (230, 60, 80),
                   (150, 40), 30, 0)
pygame.draw.rect(main, (35, 160, 175),
                 (150, 30, 100, 60))
pygame.draw.ellipse(main, (125, 90, 190),
                    (290, 30, 130, 60), 3)
pygame.draw.polygon(main, (245, 170, 45),
                    [(460, 90), (510, 20), (560, 90)])
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

pygame.quit()
