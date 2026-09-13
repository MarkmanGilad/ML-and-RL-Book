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
clock = pygame.time.Clock()
image = pygame.image.load("img/star.png").convert_alpha()
image = pygame.transform.scale(image, (60, 60))
star = MovingImage(image, (320, 200))
other = MovingImage(image, (370, 200))
star.mask = pygame.mask.from_surface(star.image)
other.mask = pygame.mask.from_surface(other.image)
star.radius = other.radius = 30
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
    hit = pygame.sprite.collide_mask(star, other) is not None
    screen.fill((190, 225, 250) if hit else (17, 43, 65))
    star.draw(screen)
    other.draw(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
