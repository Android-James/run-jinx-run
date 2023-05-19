import random

import pygame

from paths import AUDIO_DIR


class MusicService:
    @staticmethod
    def get_background_musics():
        return [
            AUDIO_DIR / "enemy_instru.mp3",
            AUDIO_DIR / "playground_instru.mp3",
            AUDIO_DIR / "snakes_instru.mp3",
        ]

    @staticmethod
    def get_cheer_musics():
        return [
            AUDIO_DIR / "cheer.ogg",
            AUDIO_DIR / "cheer_2.ogg",
            AUDIO_DIR / "cheer_3.ogg",
            AUDIO_DIR / "cheer_4.ogg"
        ]
    
    @staticmethod
    def get_jinx_musics():
        return [
            AUDIO_DIR / "jinx.ogg",
            AUDIO_DIR / "jinx_2.mp3",
            AUDIO_DIR / "jinx_3.ogg",
            AUDIO_DIR / "jinx_4.ogg",
            AUDIO_DIR / "jinx_5.ogg",
            AUDIO_DIR / "jinx_6.ogg",
        ]

    @staticmethod
    def start_background_music():
        if pygame.mixer.music.get_busy():
            return

        musics = MusicService.get_background_musics()
        filename = random.choice(musics)
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

    @staticmethod
    def play_score_sound():
        score_sfx = pygame.mixer.Sound(AUDIO_DIR / "score.wav")
        pygame.mixer.Sound.play(score_sfx)

    @staticmethod
    def play_laugh_sound():
        jinx = MusicService.get_jinx_musics()
        jinx_laugh = random.choice(jinx)
        laugh = pygame.mixer.Sound(jinx_laugh)
        pygame.mixer.Sound.play(laugh)

    @staticmethod
    def play_cheer_sound():
        musics = MusicService.get_cheer_musics()
        filename = random.choice(musics)
        cheer = pygame.mixer.Sound(filename)
        pygame.mixer.Sound.play(cheer)
