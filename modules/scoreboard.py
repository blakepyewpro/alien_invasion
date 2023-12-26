import pygame.font
from pygame.sprite import Group

from modules.ship import Ship

class Scoreboard:
    """This class tracks the score for the current game."""

    def __init__(self, ai_game):
        """Inits data necessary for drawing the scoreboard."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        self._prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """Creates rendered image of the game score."""
        rounded_score = round(self.stats.score, -1)
        score_str = f'{rounded_score:,}'
        self.score_image = self.font.render(score_str, True, self.text_color, 
                                            self.settings.bg_color)
        
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def draw_score(self):
        """Draws prepped scores to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.hs_image, self.hs_rect)
        self.screen.blit(self.lvl_image, self.lvl_rect)
        self.ships.draw(self.screen)

    def _prep_high_score(self):
        rounded_hs = round(self.stats.high_score, -1)
        hs_str = f'{rounded_hs:,}'
        self.hs_image = self.font.render(hs_str, True, self.text_color, 
                                         self.settings.bg_color)
        self.hs_rect = self.hs_image.get_rect()
        self.hs_rect.centerx = self.screen_rect.centerx
        self.hs_rect.top = self.score_rect.top

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self._prep_high_score()

    def prep_level(self):
        lvl_str = f'lvl: {self.stats.level}'
        self.lvl_image = self.font.render(lvl_str, True, self.text_color,
                                          self.settings.bg_color)
        self.lvl_rect = self.lvl_image.get_rect()
        self.lvl_rect.right = self.score_rect.right
        self.lvl_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)