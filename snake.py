# snake.py

import pygame

class Snake:
    def __init__(self):
        self.body = [(100, 100), (90, 100), (80, 100)]
        self.direction = 'right'

    def move(self):
        head_x, head_y = self.body[0]
        if self.direction == 'up':
            new_head = (head_x, head_y - 10)
        elif self.direction == 'down':
            new_head = (head_x, head_y + 10)
        elif self.direction == 'left':
            new_head = (head_x - 10, head_y)
        elif self.direction == 'right':
            new_head = (head_x + 10, head_y)

        self.body = [new_head] + self.body[:-1]

    def change_direction(self, direction):
        opposite_directions = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
        if direction != opposite_directions[self.direction]:
            self.direction = direction

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision_with_walls(self, width, height):
        head_x, head_y = self.body[0]
        return head_x < 0 or head_x >= width or head_y < 0 or head_y >= height

    def check_collision_with_self(self):
        head = self.body[0]
        return head in self.body[1:]

    def check_collision_with_food(self, food):
        return self.body[0] == food.position

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), (*segment, 10, 10))
