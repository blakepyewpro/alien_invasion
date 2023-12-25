import pygame.font

class Scoreboard:
    """This class tracks the score for the current game."""

    def __init__(self, ai_game):
        """Inits data necessary for drawing the scoreboard."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

    def prep_score(self):
        """Creates rendered image of the game score."""
        rounded_score = round(self.stats.score, -1)
        score_str = f'{rounded_score:,}'
        self.score_image = self.font.render(score_str, True, self.text_color, 
                                            self.settings.bg_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.screen_rect.top = 20

    def draw_score(self):
        """Draws prepped score to the screen."""
        self.screen.blit(self.score_image, self.score_rect)