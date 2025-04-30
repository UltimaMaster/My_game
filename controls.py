import pygame, sys, time
from bullet import Bullet
from enemyship import EnemyShip
from power_up import PowerUp
import random


def events(screen, starship, bullets_group, stats, title):
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # вправо
            if event.key == pygame.K_RIGHT:
                starship.move_right = True
            # влево
            if event.key == pygame.K_LEFT:
                starship.move_left = True
            # пробел
            if event.key == pygame.K_SPACE:
                if stats.run_game:
                    create_bullets(screen, starship,  bullets_group, stats)
                else:
                    stats.run_game = True
                    time.sleep(2)
                    
        elif event.type == pygame.KEYUP:
            # вправо
            if event.key == pygame.K_RIGHT:
                starship.move_right = False
            # влево
            if event.key == pygame.K_LEFT:
                starship.move_left = False


def update(bg_color, screen, starship, enemy_ships_group, bullets_group, power_up_group, score):
    # Общее обновление всех объектов
    screen.fill(bg_color)
    # космос...
    w, h = screen.get_size()
    for i in range(100):
        screen.fill(pygame.Color('white'),
                    (random.random() * w,
                     random.random() * h, 4, 4))
    
    score.draw_info()
    for bullet in bullets_group.sprites():
        bullet.draw_bullet()
    starship.draw_starship()
    for enemy in enemy_ships_group.sprites():
        enemy.draw_enemy_ship()
    for power_up in power_up_group.sprites():
        power_up.draw_power_up()
    if len(enemy_ships_group) == 0:
        update_level_info(score)
    pygame.display.flip()


def update_bullets(screen, enemy_ships_group, bullets_group, stats, score):
    # Обновление состояния снарядов
    bullets_group.update()
    for bullet in bullets_group.copy():
        if bullet.rect.bottom <= screen.get_rect().top:
            bullets_group.remove(bullet)
    # Проверка на коллизию снарядов и врагов
    collisions = pygame.sprite.groupcollide(bullets_group, enemy_ships_group, True, True)
    if collisions:
        for col in collisions.values():
            stats.score += 100 * len(col)
        score.draw_info()
        check_high_score(stats, score)


def starship_destroy(screen, starship, enemy_ships_group, bullets_group, stats, score, clock):
    # Потеря жизни корабля и перезагрузка
    if stats.starship_left_lives > 0:
        stats.starship_left_lives -= 1
        enemy_ships_group.empty()
        bullets_group.empty()
        starship.create_starship()
        create_army(screen, enemy_ships_group, stats)
        time.sleep(2)
    else:
        now_time = time.thread_time()
        while now_time + 0.2 > time.thread_time():
            print(111)
            update_game_over_info(score)
            pygame.display.flip()
            clock.tick(30)
        stats.run_game = False
        # Открываем засавку


def update_enemy_ships(screen, starship, enemy_ships_group, bullets_group, stats, score, clock):
    # Обновление состояния врагов
    enemy_ships_group.update()
    # Если враги касаются корабля
    if pygame.sprite.spritecollideany(starship, enemy_ships_group):
        starship_destroy(screen, starship, enemy_ships_group, bullets_group, stats, score, clock)
    enemy_check(screen, starship, enemy_ships_group, bullets_group, stats, score, clock)


def enemy_check(screen, starship, enemy_ships_group, bullets_group, stats, score, clock):
    # Проверка на касание врагом нижнего края экрана
    screen_rect = screen.get_rect()
    for enemy in enemy_ships_group.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            # Пусть будет потеря жизни
            starship_destroy(screen, starship, enemy_ships_group, bullets_group, stats, score, clock)
            break


def create_army(screen, enemy_ships_group, stats):
    # Создание врагов
    enemy_ship = EnemyShip(screen)
    
    # Ищем оптимальное количество врагов на площадь исходя из размера экрана (1200 * 800)
    enemy_ship_width = enemy_ship.rect.width
    enemy_ship_height = enemy_ship.rect.height
    
    enemy_ships_number_horizontal = (1200 - 2 * enemy_ship_width) // enemy_ship_width
    enemy_ships_number_vertical = (800 - 120 - 2 * enemy_ship_height) // enemy_ship_height

    for j in range(enemy_ships_number_vertical - 2):
        for i in range(enemy_ships_number_horizontal):
            # Создаем врагов и упорядочим их по горизонтали
            enemy_ship = EnemyShip(screen)
            enemy_ship.rect.x = enemy_ship_width + enemy_ship_width * i
            enemy_ship.rect.y = enemy_ship_height + enemy_ship_height * j
            # Регулируем скорость врагов
            enemy_ship.speed = stats.current_level * 0.5
            enemy_ships_group.add(enemy_ship)


def create_bullets(screen, starship, bullets_group, stats):
    bullet = Bullet(screen, starship)
    weapon_power = stats.weapon_power if stats.weapon_power < 10 else 10
    # Попробуем расставлять по параболе
    for i in range(-weapon_power // 2 + 1, weapon_power // 2 + 1):
        bullet = Bullet(screen, starship)
        bullet.rect.centerx = starship.rect.centerx + i * 10
        bullet.rect.top = starship.rect.top + i * i * 5
        bullets_group.add(bullet)


def create_power_up(screen, power_up_group):
    power_up = PowerUp(screen)
    power_up.rect.top = screen.get_rect().top
    power_up.rect.centerx = screen.get_rect().centerx + random.randint(-500, 500)
    power_up_group.add(power_up)


def new_level(bg_color, screen, starship, enemy_ships_group, bullets_group, pow_up_group, stats, score, title, clock):
    # Начать новый уровень, если враги уничтожены
    if len(enemy_ships_group) == 0:
        stats.current_level += 1
        # Подчищаем лишнее
        for power_up in pow_up_group.copy():
            pow_up_group.remove(power_up)
        now_time = time.thread_time()
        while now_time + 0.2 > time.thread_time():
            events(screen, starship, bullets_group, stats, title)
            starship.update_starship()
            update(bg_color, screen, starship, enemy_ships_group, bullets_group, pow_up_group, score)
            update_bullets(screen, enemy_ships_group, bullets_group, stats, score)
            update_enemy_ships(screen, starship, enemy_ships_group, bullets_group, stats, score, clock)
            update_level_info(score)
            clock.tick(30)
        bullets_group.empty()
        starship.create_starship()
        create_army(screen, enemy_ships_group, stats)


def check_high_score(stats, score):
    # Проверка рекорда
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        # Отрисовка рекорда(может не понадобиться тут)
        score.high_score_image()
        with open('data/high_score.txt', 'w') as file:
            file.write(str(stats.high_score))


FRAME_COUNT = 0


def update_title(bg_color, screen, title):
    global FRAME_COUNT
    screen.fill(bg_color)
    title.draw_title()
    if FRAME_COUNT % 30 < 15:
        title.draw_info()
    FRAME_COUNT += 1
    pygame.display.flip()


def update_level_info(score):
    score.draw_in_game_info_image(f'Level {score.stats.current_level}', font_size=60)


def update_game_over_info(score):
    score.draw_in_game_info_image(f'<GAME OVER>', (400, 350), font_size=80)


def update_power_up(screen, starship, power_up_group, stats):
    if len(power_up_group) == 0:
        create_power_up(screen, power_up_group)
    # Обновление усиления
    power_up_group.update()
    for power_up in power_up_group.copy():
        if power_up.rect.bottom >= screen.get_rect().bottom:
            power_up_group.remove(power_up)
    # Проверка на коллизию усиления и корабля
    collisions = pygame.sprite.groupcollide([starship], power_up_group, False, True)
    if collisions:
        for col in collisions.values():
            stats.weapon_power += 2

    