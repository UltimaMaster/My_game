import pygame.font


class Score():
    # Подсчет инфо игры
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 40)
        self.score_image()
        self.high_score_image()

    def score_image(self):
        # Текст в картинку
        score_text = 'SCORE: ' + str(self.stats.score)
        self.score_img = self.font.render(score_text, True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 50
        self.score_rect.top = 30

    def high_score_image(self):
        # Текст рекорда в картинку
        high_score_text = 'HIGHSCORE: ' + str(self.stats.high_score)
        self.high_score_img = self.font.render(high_score_text, True, self.text_color, (0, 0, 0))
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 30

    def left_lives_image(self):
        # Текст в картинку
        left_lives_text = 'LIFES: ' + str(self.stats.starship_left_lives)
        self.left_lives_img = self.font.render(left_lives_text, True, self.text_color, (0, 0, 0))
        self.left_lives_rect = self.left_lives_img.get_rect()
        self.left_lives_rect.left = 50
        self.left_lives_rect.top = 30

    def draw_info(self):
        # Отрисуем счет
        self.score_image()
        self.high_score_image()
        self.left_lives_image()
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_score_img, self.high_score_rect)
        self.screen.blit(self.left_lives_img, self.left_lives_rect)


