import sys
import time

import pygame

from src.components.game_status import GameStatus
from src.components.bullets import Bullets
from src.components.rocket import Rocket
from src.components.player import Player
from src.components.scoreboard import Scoreboard
from src.global_state import GlobalState
from src.services.music_service import MusicService
from src.services.visualization_service import VisualizationService
from src.utils.tools import update_background_using_scroll, update_press_key, is_close_app_event

GlobalState.load_main_screen()
VisualizationService.load_main_game_displays()

scoreboard = Scoreboard()


# Sprite Setup
P1 = Player()
B1 = Bullets()
B2 = Bullets()
B3 = Bullets()
B4 = Bullets()
R1 = Rocket()

# Sprite Groups
enemies = pygame.sprite.Group()
enemies.add(B1)
enemies.add(B2)
enemies.add(B3)
enemies.add(B4)
enemies.add(R1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(B1)
all_sprites.add(B2)
all_sprites.add(B3)
all_sprites.add(B4)
all_sprites.add(R1)


# Game Phases
def main_menu_phase():
    scoreboard.reset_current_score()

    events = pygame.event.get()

    for event in events:
        if is_close_app_event(event):
            GlobalState.GAME_STATE = GameStatus.GAME_END
            return

        if event.type == pygame.KEYDOWN:
            GlobalState.GAME_STATE = GameStatus.GAMEPLAY

    GlobalState.SCROLL = update_background_using_scroll(GlobalState.SCROLL)
    VisualizationService.draw_background_with_scroll(GlobalState.SCREEN, GlobalState.SCROLL)
    GlobalState.PRESS_Y = update_press_key(GlobalState.PRESS_Y)
    VisualizationService.draw_main_menu(GlobalState.SCREEN, scoreboard.get_max_score(), GlobalState.PRESS_Y)


def gameplay_phase():
    events = pygame.event.get()

    for event in events:
        if is_close_app_event(event):
            game_over()
            return

    P1.update()
    B1.move(scoreboard, P1.player_position)
    B2.move(scoreboard, P1.player_position)
    B3.move(scoreboard, P1.player_position)
    B4.move(scoreboard, P1.player_position)
    R1.move(scoreboard, P1.player_position)

    GlobalState.SCROLL = update_background_using_scroll(GlobalState.SCROLL)
    VisualizationService.draw_background_with_scroll(GlobalState.SCREEN, GlobalState.SCROLL)

    P1.draw(GlobalState.SCREEN)
    B1.draw(GlobalState.SCREEN)
    B2.draw(GlobalState.SCREEN)
    B3.draw(GlobalState.SCREEN)
    B4.draw(GlobalState.SCREEN)
    R1.draw(GlobalState.SCREEN)
    scoreboard.draw(GlobalState.SCREEN)
    
    if scoreboard.get_current_score() > 99:
        winning_phase()

    if pygame.sprite.spritecollide(P1, enemies, False, pygame.sprite.collide_mask):
        scoreboard.update_max_score()
        MusicService.play_laugh_sound()
        time.sleep(0.5)
        game_over()


def winning_phase():
    P1.reset()
    B1.reset()
    B2.reset()
    B3.reset()
    B4.reset()
    R1.reset()

    events = pygame.event.get()

    for event in events:
        if is_close_app_event(event):
            GlobalState.GAME_STATE = GameStatus.GAME_END
            return

        if event.type == pygame.KEYDOWN:
            GlobalState.GAME_STATE = GameStatus.MAIN_MENU

    GlobalState.SCROLL = update_background_using_scroll(GlobalState.SCROLL)
    VisualizationService.draw_background_with_scroll(GlobalState.SCREEN, GlobalState.SCROLL)
    GlobalState.PRESS_Y = update_press_key(GlobalState.PRESS_Y)
    VisualizationService.draw_winning_menu(GlobalState.SCREEN, scoreboard.get_max_score(), GlobalState.PRESS_Y)



def exit_game_phase():
    pygame.quit()
    sys.exit()


def game_over():
    P1.reset()
    B1.reset()
    B2.reset()
    B3.reset()
    B4.reset()
    R1.reset()
    GlobalState.GAME_STATE = GameStatus.MAIN_MENU
    time.sleep(0.5)

