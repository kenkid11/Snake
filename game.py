# game.py

import pygame
import sys
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

class Game:
    def __init__(self):
        pygame.init()
        self.width = 600
        self.height = 400
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food(self.width, self.height)
        self.scoreboard = ScoreBoard()
        self.running = True

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction('up')
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction('down')
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction('left')
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction('right')

    def update(self):
        self.snake.move()
        if self.snake.check_collision_with_walls(self.width, self.height) or self.snake.check_collision_with_self():
            self.running = False
        if self.snake.check_collision_with_food(self.food):
            self.snake.grow()
            self.food.place_food(self.width, self.height)
            self.scoreboard.update_score()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.scoreboard.draw(self.screen)
        pygame.display.flip()
