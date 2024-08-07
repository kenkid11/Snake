# food.py

import pygame
import random

class Food:
    def __init__(self, width, height):
        self.position = (0, 0)
        self.color = (255, 0, 0)
        self.place_food(width, height)

    def place_food(self, width, height):
        self.position = (random.randint(0, (width - 10) // 10) * 10, random.randint(0, (height - 10) // 10) * 10)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (*self.position, 10, 10))
