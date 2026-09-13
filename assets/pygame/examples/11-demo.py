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
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if not running:
        break

    star.update(1, 0)
    screen.fill((17, 43, 65))
    star.draw(screen)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
