import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Manages an individual alien."""

    def __init__(self, ai_game):
        """Initialize alien and import relevant data"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('assets/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def check_edges(self):
        """Check if edge of rect is past the edge of a screen"""
        return (self.rect.right > self.screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """Changes position per screen redraw."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x