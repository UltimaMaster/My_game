import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, screen, starship):
        # Инициализация снаряда
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 2, 12)
        self.color = (255, 255, 0)
        self.speed = 10

        self.rect.centerx = starship.rect.centerx
        self.rect.top = starship.rect.top

    def draw_bullet(self):
        # Отрисовка (тут не загруженная картинка, а наш прямоугольник)
        pygame.draw.rect(self.screen, self.color, self.rect)

    # Называем именем update, что пользоваться командой update у группы спрайтов
    def update(self):
        # Изменение положение снаряда
        self.rect.y -= self.speed


