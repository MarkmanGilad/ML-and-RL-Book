import pygame

class MovingImage(pygame.sprite.Sprite):
    def __init__(self, image, center):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center=center)

    def update(self, dx, dy):
        self.rect.move_ip(dx, dy)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

pygame.init()
screen = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Two sprites")
clock = pygame.time.Clock()
image = pygame.image.load("img/star.png").convert_alpha()
big = pygame.transform.scale(image, (60, 60))
small = pygame.transform.scale(image, (40, 40))
star = MovingImage(big, (320, 200))
other = MovingImage(small, (100, 100))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not running:
        break

    keys = pygame.key.get_pressed()
    dx = 3 * (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT])
    dy = 3 * (keys[pygame.K_DOWN] - keys[pygame.K_UP])
    star.update(dx, dy)
    other.update(1, 1)

    screen.fill((17, 43, 65))
    star.draw(screen)
    other.draw(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
