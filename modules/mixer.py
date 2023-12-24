import pygame.mixer

class Mixer:
    """Handles all sound effects for the game."""

    def __init__(self):
        """initialize mixer and set up sound objects."""
        pygame.mixer.init()

        self.gun_sound = pygame.mixer.Sound(open('assets/gun_shot.wav'))
        self.alien_hit_sound = pygame.mixer.Sound(open('assets/enemy_kill.wav'))
        self.ship_hit_sound = pygame.mixer.Sound(open('assets/player_hit.wav'))

    def play_gun_shot(self):
        """Plays gun sound."""
        self.gun_sound.play()

    def play_alien_hit(self):
        """Play alien hit sound."""
        self.alien_hit_sound.play()

    def play_ship_hit(self):
        """Play ship hit sound."""
        self.alien_hit_sound.play()