import pygame
from math import pi as PI

# Initialize Pygame
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Doraemon")
clock = pygame.time.Clock()

SKY_BLUE = (3, 173, 240)
RED = (230, 23, 55)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen.fill(WHITE)

# Face
pygame.draw.circle(screen, BLACK, (400,400),202)
pygame.draw.circle(screen, SKY_BLUE, (400,400),200)
pygame.draw.circle(screen, BLACK, (400,450),162)
pygame.draw.circle(screen, WHITE, (400,450),160)

# Eyes
pygame.draw.ellipse(screen, BLACK, (419, 249,82,102), 0)
pygame.draw.ellipse(screen, WHITE, (420, 250,80,100), 0)
pygame.draw.circle(screen, BLACK, (450, 300),10)

pygame.draw.ellipse(screen, BLACK, (299, 249,82,102), 0)
pygame.draw.ellipse(screen, WHITE, (300, 250,80,100), 0)
pygame.draw.circle(screen, BLACK, (350, 300),10)

# Nose
pygame.draw.line(screen, BLACK, (400, 350), (400, 500), 3)
pygame.draw.arc(screen, BLACK, (325, 350, 150, 150), PI, PI/16, 3)
pygame.draw.circle(screen, BLACK, (400, 350),32)
pygame.draw.circle(screen, RED, (400, 350),30)

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    clock.tick(60)  