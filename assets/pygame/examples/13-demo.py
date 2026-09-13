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
image = pygame.transform.scale(image, (40, 40))
stars = pygame.sprite.Group()
for column in range(5):
    for row in range(3):
        center = (60 + column * 80, 70 + row * 90)
        stars.add(MovingImage(image, center))

target_image = pygame.Surface((50, 100))
target_image.fill((245, 170, 45))
target_sprite = MovingImage(target_image, (560, 200))
target_group = pygame.sprite.GroupSingle(target_sprite)
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
    stars.update(dx, dy)
    pygame.sprite.groupcollide(
        target_group, stars, False, True
    )

    screen.fill((17, 43, 65))
    stars.draw(screen)
    target_group.draw(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
