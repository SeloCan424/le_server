import pygame
import time
from client import Client

client = Client('127.0.0.1', 8001)
client.run()

pygame.init()
screen = pygame.display.set_mode((600, 600))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: pygame.quit()

    pressing = pygame.key.get_pressed()
    if pressing[pygame.K_d]:
        client.x += 1
        time.sleep(0.5)