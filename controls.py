import pygame, sys, time
from bullet import Bullet
from enemyship import EnemyShip


def events(screen, starship, bullets_group):
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
                new_bullet = Bullet(screen, starship)
                bullets_group.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # вправо
            if event.key == pygame.K_RIGHT:
                starship.move_right = False
            # влево
            if event.key == pygame.K_LEFT:
                starship.move_left = False


def update(bg_color, screen, starship, enemy_ships_group, bullets_group, score):
    # Общее обновление всех объектов
    screen.fill(bg_color)
    score.draw_info()
    for bullet in bullets_group.sprites():
        bullet.draw_bullet()
    starship.draw_starship()
    for enemy in enemy_ships_group.sprites():
        enemy.draw_enemy_ship()
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
        print(stats.score)
        score.draw_info()
        check_high_score(stats, score)


def starship_destroy(screen, starship, enemy_ships_group, bullets_group, stats):
    # Потеря жизни корабля и перезагрузка
    if stats.starship_left_lives > 0:
        stats.starship_left_lives -= 1
        enemy_ships_group.empty()
        bullets_group.empty()
        starship.create_starship()
        create_army(screen, enemy_ships_group)
        time.sleep(2)
    else:
        stats.run_game = False
        # Открываем засавку


def update_enemy_ships(screen, starship, enemy_ships_group, bullets_group, stats):
    # Обновление состояния врагов
    enemy_ships_group.update()
    # Если враги касаются корабля
    if pygame.sprite.spritecollideany(starship, enemy_ships_group):
        starship_destroy(screen, starship, enemy_ships_group, bullets_group, stats)
    enemy_check(screen, starship, enemy_ships_group, bullets_group, stats)


def enemy_check(screen, starship, enemy_ships_group, bullets_group, stats):
    # Проверка на касание врагом нижнего края экрана
    screen_rect = screen.get_rect()
    for enemy in enemy_ships_group.sprites():
        if enemy.rect.bottom >= screen_rect.bottom:
            # Пусть будет потеря жизни
            starship_destroy(screen, starship, enemy_ships_group, bullets_group, stats)
            break


def create_army(screen, enemy_ships_group):
    # Создание врагов
    enemy_ship = EnemyShip(screen)
    # Ищем оптимальное количество врагов на площадь исходя из размера экрана (1200 * 800)
    enemy_ship_width = enemy_ship.rect.width
    enemy_ships_number_horizontal = (1200 - 2 * enemy_ship_width) // enemy_ship_width
    enemy_ship_height = enemy_ship.rect.height
    enemy_ships_number_vertical = (800 - 120 - 2 * enemy_ship_height) // enemy_ship_height

    for j in range(enemy_ships_number_vertical - 2):
        for i in range(enemy_ships_number_horizontal):
            # Создаем врагов и упорядочим их по горизонтали
            enemy_ship = EnemyShip(screen)
            enemy_ship.rect.x = enemy_ship_width + enemy_ship_width * i
            enemy_ship.rect.y = enemy_ship_height + enemy_ship_height * j
            enemy_ships_group.add(enemy_ship)


def new_level(screen, starship, enemy_ships_group, bullets_group, stats):
    # Начать новый уровень, если враги уничтожены
    if len(enemy_ships_group) == 0:
        bullets_group.empty()
        starship.create_starship()
        create_army(screen, enemy_ships_group)


def check_high_score(stats, score):
    # Проверка рекорда
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        # Отрисовка рекорда(может не понадобиться тут)
        score.high_score_image()
        with open('data/high_score.txt', 'w') as file:
            file.write(str(stats.high_score))
