class GameStats:
    """Tracks player stats for Alien Invasion."""

    def __init__(self, ai_game):
        """Initialize stats."""
        self.settings = ai_game.settings
        self.high_score = 0
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ships_limit
        self.score = 0