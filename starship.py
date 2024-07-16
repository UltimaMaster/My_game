import pygame


class Starship():
    def __init__(self, screen):
        # Инициализация
        self.screen = screen
        self.image = pygame.image.load('images/starship.png')
        self.image = pygame.transform.scale(self.image, (120, 120))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.create_starship()

        self.move_right = False
        self.move_left = False

    def draw_starship(self):
        # Отрисовка
        self.screen.blit(self.image, self.rect)

    def update_starship(self):
        # Изменение положения корабля
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 3
        if self.move_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 3

    def create_starship(self):
        # Размещает по центру внизу корабль
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom



