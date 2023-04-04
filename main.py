import pygame

pygame.init()
dis = pygame.display.set_mode((400,300))
pygame.display.update()
pygame.display.set_caption("coolhuip_snake_game_v0.1")

game_over = False
while not game_over:
    for event in pygame.event.get():
        print(event)    # prints out all the actions that take place on screen

pygame.quit()
quit()
