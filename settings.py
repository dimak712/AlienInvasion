class Settings():

    def __init__(self):
        self.screen_width = 2000
        self.screen_height = 1300
        self.bg_color = (17, 26, 61)
        self.ship_speed = 1.5
        self.ship_limit = 1 # +1
        #bullet
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        #stars
        self.stars_allowed = 1000

        self.alien_speed = 5.0
        self.fleet_drop_speed = 20
        self.fleet_direcrion = 1
        
        self.speedup_scale = 3.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3.0
        self.alien_speed_factor = 1.0

        self.fleet_direction = 1

    def increase_speed(self):
        self.ship_speed += (self.ship_speed_factor * self.speedup_scale)
        self.bullet_speed += self.bullet_speed_factor * self.speedup_scale
        self.alien_speed += self.alien_speed_factor * self.speedup_scale