import pygame
from random import randint


class PowerUp(pygame.sprite.Sprite):
    def __init__(self, screen):
        # Инициализация усиления
        super().__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.color = (0, 255, 0)
        self.speed = 10
        
    def draw_power_up(self):
        # Отрисовка
        pygame.draw.rect(self.screen, self.color, self.rect)

    # Называем именем update, что пользоваться командой update у группы спрайтов
    def update(self):
        # Изменение положение снаряда
        self.rect.y += self.speed
        self.color = (randint(0, 255), randint(50, 255), randint(0, 255))