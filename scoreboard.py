# scoreboard.py

import pygame

class ScoreBoard:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont(None, 35)

    def update_score(self):
        self.score += 1

    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, [0, 0])
