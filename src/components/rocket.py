import random

import pygame

from src.components.scoreboard import Scoreboard
from src.config import Config
from src.services.music_service import MusicService
from src.services.visualization_service import VisualizationService


class Rocket(pygame.sprite.Sprite):
    def __init__(self, player_position):
        super().__init__()
        self.new_spd = 5
        self.new_y = 0

        self.new_x = 180
        self.can_score = True

        self._load_hand()

    def reset(self, player_position):
        self.can_score = True
        self.new_y = -40
        self.new_x = 180

    def _load_hand(self):
       
        self.image = VisualizationService.get_rocket_image()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
    

    def move(self, scoreboard: Scoreboard, player_position):
        self.new_y += self.new_spd

        self.rect.center = (self.new_x, self.new_y)

        if self.rect.top > player_position.y - 35 and self.can_score:
            # print(int(player_position.x), int(player_position.y))
            scoreboard.increase_current_score()
            self.can_score = False

            MusicService.play_score_sound()

            if scoreboard.get_current_score() % 5 == 0:
                MusicService.play_cheer_sound()

        if self.rect.top > Config.HEIGHT:
            self.rect.bottom = 0
            # Play Gunshot Sound
            self.new_spd = 5

            self.new_x = player_position.x
            self.new_y = -40

            self.can_score = True

    def draw(self, screen):
        dotted_line = VisualizationService.get_dotted_line()
        screen.blit(dotted_line, (0, self.rect.y))
        screen.blit(self.image, self.rect)
