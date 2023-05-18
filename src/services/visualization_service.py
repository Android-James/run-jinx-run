import pygame

from paths import ASSETS_DIR, MENU_DIR
from src.config import Config
from src.utils.tools import sine


class VisualizationService:
    @staticmethod
    def get_bullet_image():
        return pygame.image.load(ASSETS_DIR / "bullet.png").convert_alpha()
    
    @staticmethod
    def get_rocket_image():
        return pygame.image.load(ASSETS_DIR / "rocket.png").convert_alpha()

    @staticmethod
    def get_player_image():
        return pygame.image.load(ASSETS_DIR / "vi.png").convert_alpha()

    @staticmethod
    def get_background_image():
        return pygame.image.load(ASSETS_DIR / "bg.png").convert_alpha()

    @staticmethod
    def get_score_backing():
        return pygame.image.load(ASSETS_DIR / "scoreboard.png").convert_alpha()

    @staticmethod
    def get_press_key_image():
        return pygame.image.load(MENU_DIR / "press_any_key.png").convert_alpha()

    @staticmethod
    def get_title_image():
        return pygame.image.load(MENU_DIR / "title.png").convert_alpha()

    @staticmethod
    def get_you_won_image():
        return pygame.image.load(MENU_DIR / "won.png").convert_alpha()

    @staticmethod
    def get_vi_and_jinx_image():
        return pygame.image.load(MENU_DIR / "vi_and_jinx.png").convert_alpha()

    @staticmethod
    def get_main_font():
        return pygame.font.Font(ASSETS_DIR / "VT323-Regular.ttf", 40)

    @staticmethod
    def get_credit_font_font():
        return pygame.font.Font(ASSETS_DIR / "VT323-Regular.ttf", 18)

    @staticmethod
    def get_score_font():
        return pygame.font.Font(ASSETS_DIR / "VT323-Regular.ttf", 26)

    @staticmethod
    def load_main_game_displays():
        pygame.display.set_caption("Run Jinx Run")
        run_jinx_run = VisualizationService.get_title_image()
        pygame.display.set_icon(run_jinx_run)

    @staticmethod
    def draw_background_with_scroll(screen, scroll):
        background = VisualizationService.get_background_image()
        screen.blit(background, (0, scroll))

    @staticmethod
    def draw_author_credits(screen):
        credit_font = VisualizationService.get_credit_font_font()
        riot_credits = credit_font.render("Copyright Riot Games", True, (250, 250, 250))
        credits_rect = riot_credits.get_rect(center=(Config.WIDTH // 2, 620))
        screen.blit(riot_credits, credits_rect)

    @staticmethod
    def draw_best_score(screen, max_score):
        score_font = VisualizationService.get_score_font()
        best_score = score_font.render(f"Best: {max_score}", True, (0, 0, 0))
        best_score_rect = best_score.get_rect(center=(Config.WIDTH // 2, 260))
        screen.blit(best_score, best_score_rect)

    @staticmethod
    def draw_title(screen):
        y = sine(200.0, 1280, 10.0, 0)
        title = VisualizationService.get_title_image()
        screen.blit(title, (60, y))
        vi_and_jinx = VisualizationService.get_vi_and_jinx_image()
        screen.blit(vi_and_jinx, (0, 220))

    @staticmethod
    def draw_win(screen):
        y = sine(200.0, 1280, 10.0, 0)
        title = VisualizationService.get_you_won_image()
        screen.blit(title, (40, y))
        vi_and_jinx = VisualizationService.get_vi_and_jinx_image()
        screen.blit(vi_and_jinx, (0, 220))

    @staticmethod
    def draw_press_key(screen, press_y):
        press_key = VisualizationService.get_press_key_image()
        screen.blit(press_key, (60, press_y))

    @staticmethod
    def draw_main_menu(screen, max_score, press_y):
        VisualizationService.draw_author_credits(screen)
        VisualizationService.draw_best_score(screen, max_score)
        VisualizationService.draw_title(screen)
        VisualizationService.draw_press_key(screen, press_y)

    @staticmethod
    def draw_winning_menu(screen, max_score, press_y):
        VisualizationService.draw_author_credits(screen)
        VisualizationService.draw_best_score(screen, max_score)
        VisualizationService.draw_win(screen)
        VisualizationService.draw_press_key(screen, press_y)
