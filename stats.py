import pygame.font


class Stats():
    # Вся статистика игры
    def __init__(self):
        self.starship_left_lives = 2
        self.run_game = False
        self.score = 0
        self.current_level = 1
        self.weapon_power = 1
        with open('data/high_score.txt', 'r') as file:
            self.high_score = int(file.readline())

    def reset_stats(self):
        # сброс статистики
        self.starship_left_lives = 2
        self.score = 0
        self.current_level = 1
        self.weapon_power = 1
