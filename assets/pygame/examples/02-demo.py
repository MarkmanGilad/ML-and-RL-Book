import pygame

pygame.init()
WIDTH, HEIGHT = 640, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Pygame Window")
running = True

while running:
    pygame.display.update()
