import pygame.font


class Score():
    # Подсчет инфо игры
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 40)

    def score_image(self):
        # Текст в картинку
        score_text = 'SCORE: ' + str(self.stats.score)
        self.score_img = self.font.render(score_text, True, self.text_color)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 50
        self.score_rect.top = 30

    def high_score_image(self):
        # Текст рекорда в картинку
        high_score_text = 'HIGHSCORE: ' + str(self.stats.high_score)
        self.high_score_img = self.font.render(high_score_text, True, self.text_color)
        self.high_score_rect = self.high_score_img.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 30

    def left_lives_image(self):
        # Текст в картинку
        left_lives_text = 'LIFES: ' + str(self.stats.starship_left_lives)
        self.left_lives_img = self.font.render(left_lives_text, True, self.text_color)
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
    
    def draw_in_game_info_image(self, info_text, info_coords: tuple = None, font_size: int = 40):
        # Текст в картинку
        text = info_text
        font = pygame.font.SysFont(None, font_size)
        self.text_img = font.render(text, True, self.text_color)
        self.text_rect = self.left_lives_img.get_rect()
        if not info_coords:
            self.text_rect.centerx = self.screen_rect.centerx - 20
            self.text_rect.centery = self.screen_rect.centery * 1.5 // 2
        else:
            self.text_rect.center = info_coords
        self.screen.blit(self.text_img, self.text_rect)


