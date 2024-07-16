import pygame


class EnemyShip(pygame.sprite.Sprite):
    # Инициализация
    def __init__(self, screen):
        super(EnemyShip, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/enemy_ship.png')

        self.image = pygame.transform.scale(self.image, (80, 80))
        self.image = pygame.transform.rotate(self.image, 90)

        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def draw_enemy_ship(self):
        # Отрисовка
        self.screen.blit(self.image, self.rect)

    # Называем именем update, что пользоваться командой update у группы спрайтов
    def update(self):
        # Изменение положение врага
        self.rect.y += 1



