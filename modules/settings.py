class Settings:
    """A class to store all Alien Invasion settings."""

    def __init__(self):
        """Initialize the game's settings."""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.fullscreen = False

        #ship settings
        self.ships_limit = 2

        #bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        #alien settings
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.init_dynamic_settings()

    def init_dynamic_settings(self):
        """Resets settings that change during the game."""
        #legacy ship speed = 1.5
        self.ship_speed = 1.8
        #legacy bullet speed = 2.5
        self.bullet_speed = 3
        #legacy alien speed = 1
        self.alien_speed = 1.2

        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)