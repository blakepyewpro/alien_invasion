import pygame.mixer

class Mixer:
    """Handles all sound effects for the game."""

    def __init__(self):
        """initialize mixer and set up sound objects."""
        pygame.mixer.init()

        self.gun_sound = pygame.mixer.Sound(open('assets/gun_shot.wav'))
        self.alien_hit_sound = pygame.mixer.Sound(open('assets/enemy_kill.wav'))
        self.player_loss_sound = pygame.mixer.Sound(
            open('assets/player_loss.wav'))
        self.start_sound = pygame.mixer.Sound(open('assets/game_start.wav'))

    def play_gun_shot(self):
        """Plays gun sound."""
        self.gun_sound.play()

    def play_alien_hit(self):
        """Play alien hit sound."""
        self.alien_hit_sound.play()

    def play_player_loss(self):
        """Play ship hit sound."""
        self.player_loss_sound.play()

    def play_start(self):
        """Play game start sound."""
        self.start_sound.play()