import pygame, controls, time
from starship import Starship
from pygame.sprite import Group
from stats import Stats
from score import Score
from title import Title


# Основной метод
def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Игра")
    bg_color = (0, 0, 0)
    starship = Starship(screen)
    bullets_group = Group()
    enemy_group = Group()
    power_up_group = Group()
    stats = Stats()
    score = Score(screen, stats)
    title = Title(screen)
    
    clock = pygame.time.Clock()

    while True:
        controls.events(screen, starship, bullets_group, stats, title)
        if stats.run_game:
            controls.new_level(bg_color, screen, starship, enemy_group, bullets_group, power_up_group,
                               stats, score, title, clock)
            starship.update_starship()
            controls.update(bg_color, screen, starship, enemy_group, bullets_group, power_up_group, score)
            controls.update_bullets(screen, enemy_group, bullets_group, stats, score)
            controls.update_enemy_ships(screen, starship, enemy_group, bullets_group, stats, score, clock)
            controls.update_power_up(screen, starship, power_up_group, stats)
        else:
            controls.update_title(bg_color, screen, title)
            # Сброс состояния
            stats.reset_stats()
            starship = Starship(screen)
            bullets_group = Group()
            enemy_group = Group()
            power_up_group = Group()
            stats = Stats()
            score = Score(screen, stats)
            title = Title(screen)
        clock.tick(30)

run()