import pygame
import random


class EnemyShip(pygame.sprite.Sprite):
    # Инициализация
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        
        self.image = pygame.image.load('images/enemy_ship.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.image = pygame.transform.rotate(self.image, 90)

        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Скорость
        self.speed = 1
        
        self.step_x = 0
        self.step_y = 0
        self.max_step_y = 0
        
        
        self.move_arrow_x = 1
        self.move_arrow_y = 1

    def draw_enemy_ship(self):
        # Отрисовка
        self.screen.blit(self.image, self.rect)

    # Называем именем update, что пользоваться командой update у группы спрайтов
    def update(self):
        # Изменение положение врага
        # Ритмичное движение вверх-низ и постепенное снижение
        if self.step_y > 10 + 2 * self.speed + self.max_step_y:
            self.move_arrow_y = -1
        if self.step_y < -10 - 2 * self.speed + self.max_step_y:
            self.move_arrow_y = 1
        if self.move_arrow_y == 1:
            self.step_y += self.speed
            self.rect.y += self.speed
        else:
            self.step_y -= self.speed
            self.rect.y -= self.speed
        self.max_step_y += self.speed * 0.5
        
        # Ограниченно-хаотичное движение вбок
        if self.step_x > 10:
            self.move_arrow_x = -1
        if self.step_x < -10:
            self.move_arrow_x = 1
        if self.move_arrow_x == 1:
            self.step_x += 1
            self.rect.x += random.randint(0, 5)
        else:
            self.step_x -= 1
            self.rect.x -= random.randint(0, 5)



