import pygame, controls
from starship import Starship
from pygame.sprite import Group
from stats import Stats
from score import Score


# Основной метод
def run():
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Игра")
    bg_color = (0, 0, 0)
    starship = Starship(screen)
    bullets_group = Group()
    enemy_ships_group = Group()
    controls.create_army(screen, enemy_ships_group)
    stats = Stats()
    score = Score(screen, stats)

    while True:
        controls.events(screen, starship, bullets_group)
        if stats.run_game:
            starship.update_starship()
            controls.update(bg_color, screen, starship, enemy_ships_group, bullets_group, score)
            controls.update_bullets(screen, enemy_ships_group, bullets_group, stats, score)
            controls.update_enemy_ships(screen, starship, enemy_ships_group, bullets_group, stats)
            controls.new_level(screen, starship, enemy_ships_group, bullets_group, stats)

run()