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
            AUDIO_DIR / "cheer.wav",
            AUDIO_DIR / "cheer_2.wav",
            AUDIO_DIR / "cheer_3.wav",
            AUDIO_DIR / "cheer_4.wav"
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
        slap_sfx = pygame.mixer.Sound(AUDIO_DIR / "jinx-laugh.mp3")
        pygame.mixer.Sound.play(slap_sfx)

    @staticmethod
    def play_cheer_sound():
        musics = MusicService.get_cheer_musics()
        filename = random.choice(musics)
        cheer = pygame.mixer.Sound(filename)
        pygame.mixer.Sound.play(cheer)
