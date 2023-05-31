import pygame as pg     # Needed to develop the game
import random as rand   # Generate objects randomly
import time             # Time manipulation

# GLOBAL VAR's
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 460
INITIAL_DIRECTION = 'RIGHT'

# Colors
midnight_blue = pg.Color(25, 25, 112)
mint_cream = pg.Color(245, 255, 250)
crimson_red = pg.Color(220, 20, 60)
lawn_green = pg.Color(124, 252, 0)
orange_red = pg.Color(255, 69, 0)

pg.init()   # Initialize the PyGame window
display_screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption('codge_SnakeGame')   # Set title of application
game_clock = pg.time.Clock()   # Create a Clock object to set refresh rate

# Snake
snake_speed = 15   # Speed of snake
snake_position = [100, 50]   # Default position of Snake
snake_body = [   # First 4 blocks of snake body
    [100, 50],
    [90, 50],
    [80, 50],
    [70, 50],
]
snake_direction = INITIAL_DIRECTION

# Fruit
fruit_position = [
    rand.randrange(1, (SCREEN_WIDTH // 10)) * 10,
    rand.randrange(1, (SCREEN_HEIGHT // 10)) * 10,
]
fruit_spawn = True;

