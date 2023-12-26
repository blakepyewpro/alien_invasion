import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Manages the player's ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image = pygame.image.load('assets/ship.bmp')
        self.rect = self.image.get_rect()

        #start the ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Modify ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        self.rect.x = self.x

    def center_ship(self):
        """Reset the ship's position."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)