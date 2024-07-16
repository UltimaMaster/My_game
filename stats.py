import pygame.font


class Stats():
    # Вся статистика игры
    def __init__(self):
        self.starship_left_lives = 2
        self.run_game = True
        self.score = 0
        with open('data/high_score.txt', 'r') as file:
            self.high_score = int(file.readline())

    def reset_stats(self):
        # сброс статистики
        self.starship_left_lives = 2
        self.score = 0
