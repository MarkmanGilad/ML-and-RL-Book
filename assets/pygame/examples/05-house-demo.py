import pygame

pygame.init()
screen = pygame.display.set_mode((640, 400))
pygame.display.set_caption("House")

SKY = (135, 206, 235)
GRASS = (80, 170, 90)
WALL = (240, 220, 170)
ROOF = (180, 60, 50)
DOOR = (110, 70, 40)
GLASS = (200, 230, 255)
SUN = (250, 210, 60)
TRUNK = (120, 80, 40)
LEAVES = (40, 130, 60)
BLACK = (0, 0, 0)

screen.fill(SKY)
pygame.draw.rect(screen, GRASS, (0, 300, 640, 100))
pygame.draw.circle(screen, SUN, (560, 70), 40)
pygame.draw.rect(screen, WALL, (200, 180, 240, 120))
pygame.draw.polygon(screen, ROOF,
                    [(180, 180), (320, 90), (460, 180)])
pygame.draw.rect(screen, DOOR, (300, 220, 40, 80))
pygame.draw.rect(screen, GLASS, (225, 205, 50, 40))
pygame.draw.rect(screen, GLASS, (365, 205, 50, 40))
pygame.draw.line(screen, BLACK, (250, 205), (250, 245), 2)
pygame.draw.line(screen, BLACK, (225, 225), (275, 225), 2)
pygame.draw.line(screen, BLACK, (390, 205), (390, 245), 2)
pygame.draw.line(screen, BLACK, (365, 225), (415, 225), 2)
pygame.draw.rect(screen, TRUNK, (90, 240, 20, 60))
pygame.draw.ellipse(screen, LEAVES, (60, 170, 80, 90))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not running:
        break

    pygame.display.update()

pygame.quit()
