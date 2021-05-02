# Snek 1.0
# Author : Dhammike Piyumal
# Last Update : 02/05/2021

# -------------------------------------------------------------------------------

import pygame
import time
import random

# -------------------------------------------------------------------------------

# Initializing the pygame

pygame.init()

# Defining the colors

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Defining the width and the height of the Game window

width, height = 600, 400

# Defining the Game Display with Pygame

game_display = pygame.display.set_mode((width, height))

# Providing a title for the Game window

pygame.display.set_caption("DP's Snake Game")

clock = pygame.time.Clock()

# snake_size is the number of pixels that is the width or height
# singlel cell of the snake.

snake_size = 10

# snake_seed is the rate which the pixels move when the snake is moving.
# In here, the rate is 15 pixels per second.

snake_speed = 15

# Following are the fonts used in various situations within the game.

message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)
instruction_font = pygame.font.SysFont('ubuntu', 20)

# -------------------------------------------------------------------------------


def print_score(score):
    text = score_font.render("Score : " + str(score), True, green)
    game_display.blit(text, [0, 0])


def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, white, [
                         pixel[0], pixel[1], snake_size, snake_size])
    # rect(surface, color, rect) has been used.
    # rect has 4 parameters. starting x coordinate, starting y coordinate,
    #  width or the rectangle and the height of the rectangle.


def run_game():

    # Initializing the starting game state

    game_over = False
    game_close = False

    x = width / 2
    y = height / 2

    x_speed = 0
    y_speed = 0

    snake_pixels = []
    snake_length = 1

    target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    # The main game loop

    while not game_over:

        while game_close:
            game_display.fill(black)

            game_over_message = message_font.render("Game Over", True, red)

            instruction_message = instruction_font.render(
                "Press Q to QUIT or R to RESTART!", True, green)

            game_display.blit(game_over_message, [width / 3, height / 3])

            game_display.blit(instruction_message, [width / 4, height / 2])

            print_score(snake_length - 1)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        run_game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = - snake_size
                    y_speed = 0

                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0

                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = - snake_size

                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size

        if x >= width or x < 0 or y >= height or y < 0:
            game_close = True

        x += x_speed
        y += y_speed

        game_display.fill(black)

        pygame.draw.rect(game_display, green, [
                         target_x, target_y, snake_size, snake_size])

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        for pixel in snake_pixels[: -1]:
            if pixel == [x, y]:
                game_close = True

        draw_snake(snake_size, snake_pixels)

        print_score(snake_length - 1)

        pygame.display.update()

        if x == target_x and y == target_y:
            target_x = round(random.randrange(
                0, width - snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(
                0, height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


run_game()
