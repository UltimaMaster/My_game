import pygame
import pygame.font


class Title(pygame.sprite.Sprite):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        # Название игры
        self.image = pygame.image.load('images/title.png')
        self.image = pygame.transform.scale(self.image, (500, 200))
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center[0], self.screen_rect.center[1] // 2
        
        # Фраза
        self.font = pygame.font.SysFont(None, 40)
        self.text_color = (200, 200, 200)
        info_text = 'Press SPACE to start'
        self.info_img = self.font.render(info_text, True, self.text_color)
        self.info_rect = self.info_img.get_rect()
        self.info_rect.center = self.screen_rect.center[0], self.screen_rect.center[1] // 2 * 3
        
        # Декор
        # Игрок
        self.starship = pygame.image.load('images/starship.png')
        self.starship = pygame.transform.scale(self.starship, (120, 120))
        self.starship = pygame.transform.rotate(self.starship, 90)
        self.starship_rect = self.starship.get_rect()
        self.starship_rect.center = self.screen_rect.center[0] + 300, self.screen_rect.center[1]
        
        # Противники
        self.enemy_ship = pygame.image.load('images/enemy_ship.png')
        self.enemy_ship = pygame.transform.scale(self.enemy_ship, (80, 80))
        self.enemy_ship = pygame.transform.rotate(self.enemy_ship, 180)
        self.enemy_ship_rect = self.starship.get_rect()
        # Три позиции
        self.enemy_ship_rect1 = self.screen_rect.center[0] - 400, self.screen_rect.center[1]
        self.enemy_ship_rect2 = self.screen_rect.center[0] - 300, self.screen_rect.center[1] + 50
        self.enemy_ship_rect3 = self.screen_rect.center[0] - 330, self.screen_rect.center[1] - 80
        
    def draw_title(self):
        # Отрисовка
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.starship, self.starship_rect)
        self.screen.blit(self.enemy_ship, self.enemy_ship_rect1)
        self.screen.blit(self.enemy_ship, self.enemy_ship_rect2)
        self.screen.blit(self.enemy_ship, self.enemy_ship_rect3)
    
    def draw_info(self):
        # Отрисовка информации о способе начать игру
        self.screen.blit(self.info_img, self.info_rect)
    
    def update(self):
        pass