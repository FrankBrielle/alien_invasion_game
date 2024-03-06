import pygame

class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана.
        self.screen_widght = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        

        # Настройки корабля
        #self.ship_speed = 12
        self.ship_limit = 3

        # Параметры снаряда.
        #self.bullet_speed = 8
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 100
        #self.bullet_image = pygame.image.load('images/bullet.png')

        # Настройки пришельцев
       # self.alien_speed = 6
        self.fleet_drop_speed = 6
        

        # Темп ускорения игры
        self.speedup_scale = 1.2
        # темп роста стоимости пришельцев
        self.score_scale = 1.5

        self.initialize_dynamics_settings()
    
    def initialize_dynamics_settings(self):
        '''Инициализирует натсройки, изменяющиеся в ходе игры'''
        self.ship_speed_factor = 9
        self.bullet_speed_factor = 8
        self.alien_speed_factor = 5

        # fleet_direction =1 означает движение вправо, а -1 влево.
        self.fleet_direction = 1

        # Подсчет очков
        self.alien_points = 10

    def increase_speed(self):
        '''Увеличивает настройки скорости и стоимости пришельцев.'''
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        

