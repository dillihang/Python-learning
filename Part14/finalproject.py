import pygame
import random

class SpaceShooter:
    """
    Main game class for Space Shooter.

    Note: The player, enemy, and bullet polygons were generated 
    using AI and not manually drawn by the developer.

    Handles game initialization, main loop, event handling, 
    rendering, enemy and bullet management, player stats, 
    and game states (main menu, gameplay, game over). 
    Also manages background stars and collision detection.
    """
    def __init__(self):
        pygame.init()
        self.display = pygame.display.set_mode((1280, 960))
        pygame.display.set_caption("Space Shooter")
        self.clock = pygame.time.Clock()

        self.mouse_x, self.mouse_y = 0, 0
        self.player_bullets_list = []
        self.enemies_bullets_list = []
        self.enemies_list = []
        self.stars_list = []  
        self.enemy_cooldown = 0
        self.player_score = 0
        self.star_cooldown = 0
        self.player_life = 3

        self.controls()
        self.game_state()

    def game_state(self):
        """
        Controls transitions between game states: 
        'Main Menu', 'Start' (gameplay), and 'Game over'.
        Loops until the player chooses to quit.
        """
        state = "Main Menu"
        while state != "Quit":   
            if state == "Main Menu":
                state = self.main_screen()  
            elif state == "Start":
                state = self.run()          
            elif state == "Game over":
                state = self.game_over_screen()
    
    def controls(self):
        """
        Initializes the player's movement and shooting flags.
        """
        self.to_up = False
        self.to_down = False
        self.to_right = False
        self.to_left = False
        self.to_shoot = False
    
    def cooldown_reset(self):
        """
        Resets the game by reinitializing the SpaceShooter instance.
        """
        self.__init__()
    
    def event_listener(self):
        """
        Processes pygame events including keyboard and mouse input.
        Handles player movement, shooting, pause, and quitting.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.to_right = True
                if event.key == pygame.K_a:
                    self.to_left = True
                if event.key == pygame.K_w:
                    self.to_up = True
                if event.key == pygame.K_s:
                    self.to_down = True
                if event.key == pygame.K_SPACE:
                    self.to_shoot = True
                if event.key == pygame.K_ESCAPE:
                    self.paused = not self.paused
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.to_right = False
                if event.key == pygame.K_a:
                    self.to_left = False
                if event.key == pygame.K_w:
                    self.to_up = False
                if event.key == pygame.K_s:
                    self.to_down = False
                if event.key == pygame.K_SPACE:
                    self.to_shoot = False

            
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_x, self.mouse_y = event.pos

    def main_screen(self):
        """
        Displays the main menu screen with a start button.
        Returns 'Start' when the player clicks to begin.
        """
        while True:
            self.event_listener()
            self.display.fill((0, 0, 0))
            game_font = pygame.font.SysFont("Arial", 100)
            main_screen = game_font.render(f"Welcome to Space Shooter", True, (255, 0, 0))
            self.display.blit(main_screen, (640 - (main_screen.get_width()//2), 200 - (main_screen.get_height()//2)))
            
            game_font2 = pygame.font.SysFont("Arial", 24)
            start_button = pygame.Rect(600, 600, 62, 30)
            pygame.draw.rect(self.display, (255,0,0), start_button)
            start_txt = game_font2.render(f"START", True, (0, 0, 0))
            self.display.blit(start_txt, (600, 600))
            if start_button.collidepoint(self.mouse_x, self.mouse_y):
                return "Start"

            pygame.display.flip()
            self.clock.tick(60)
    
    def game_over_screen(self):
        """
        Displays the game over screen with the final score
        and a restart button. Resets the game if restart is selected.
        """
        while True:           
            self.event_listener()
            self.display.fill((0, 0, 0))
            game_font = pygame.font.SysFont("Arial", 200)
            main_screen = game_font.render(f"GAME OVER", True, (255, 0, 0))
            self.display.blit(main_screen, (600 - (main_screen.get_width()//2), 400 - (main_screen.get_height()//2)))

            game_font2 = pygame.font.SysFont("Arial", 25)   

            final_score = game_font2.render(f"Your Score: {self.player_score}", True, (255, 0, 0))
            self.display.blit(final_score, (600 - (final_score.get_width()//2), 700 - (final_score.get_height()//2)))
            
            start_button = pygame.Rect(600, 600, 62, 30)
            pygame.draw.rect(self.display, (255,0,0), start_button)
            start_txt = game_font2.render(f"START", True, (0, 0, 0))
            self.display.blit(start_txt, (600, 600))
            if start_button.collidepoint(self.mouse_x, self.mouse_y):
                self.cooldown_reset()
                return "Start"

            pygame.display.flip()
            self.clock.tick(60)
    
    def player_ammo(self):
        """
        Updates and draws all player bullets on the screen.
        Removes bullets that leave the display area.
        """
        for bullets in self.player_bullets_list:   
            bullets.update(self)
            bullets.draw(self.display)
        self.player_bullets_list = [bullet for bullet in self.player_bullets_list if bullet.position_y >0]
    
    def enemy_ammo(self):
        """
        Updates and draws all enemy bullets on the screen.
        Removes bullets that leave the display area.
        """
        for ammo in self.enemies_bullets_list:
            ammo.update(self)
            ammo.draw(self.display)
        self.enemies_bullets_list = [ammo for ammo in self.enemies_bullets_list if ammo.position_y <= 960]

    def random_enemies(self):
        """
        Spawns random enemies at intervals, choosing from different types.
        Manages enemy spawn cooldown.
        """
        enemy_class_list = [BasicEnemy, AggressiveEnemy, Drone]
        if self.enemy_cooldown == 0:
            random_enemy_class = random.choice(enemy_class_list)
            enemy_instance = random_enemy_class()
            self.enemies_list.append(enemy_instance)
            self.enemy_cooldown +=50
        
        if self.enemy_cooldown >0:
            self.enemy_cooldown -=1
    
    def spawn_random_enemies(self):
        """
        Updates and draws all active enemies.
        Removes enemies that move off the screen.
        """
        for enemies in self.enemies_list:
            enemies.update(self)
            enemies.draw(self.display)
        self.enemies_list = [enemy for enemy in self.enemies_list if enemy.position_y <=960]

    def spawn_bg_stars(self):
        """
        Spawns and updates background stars to create a starfield effect.
        Manages star spawn cooldown and removes stars off-screen.
        """
        if self.star_cooldown == 0:
            self.stars_list.append(Background_star())
            self.star_cooldown +=5

        if self.star_cooldown>=0:
            self.star_cooldown -=1

        for stars in self.stars_list:
            stars.update()
            stars.draw(self.display)
            
        self.stars_list = [stars for stars in self.stars_list if stars.position_y <=960]

    def check_player_hits(self):
        """
        Checks collisions between player bullets and enemies.
        Updates score and removes collided bullets and enemies.
        """
        for bullet in self.player_bullets_list:
            for enemy in self.enemies_list:
                if bullet.does_collide(enemy):
                    enemy.position_x = -1000
                    enemy.position_y = -1000
                    bullet.position_x = - 2000
                    bullet.position_y = - 2000

                    self.player_bullets_list = [bullet for bullet in self.player_bullets_list if bullet.position_y > 0] 
                    self.enemies_list.remove(enemy)
                    self.player_score +=1
    
    def check_enemy_bullet_hits(self):
        """
        Checks collisions between enemy bullets and the player.
        Reduces player life and removes bullets that hit the player.
        """
        for bullet in self.enemies_bullets_list:
            if bullet.does_collide(self.player):
                bullet.position_x = -5000
                bullet.position_y = -5000
                self.enemies_bullets_list = [bullet for bullet in self.enemies_bullets_list if bullet.position_y < 960]
                self.player_life -=1

    def check_enemy_collides(self):
        """
        Checks collisions between enemies and the player.
        Reduces player life and removes collided enemies.
        """
        for enemy in self.enemies_list:
            if enemy.does_collide(self.player):
                enemy.position_x = -4000
                enemy.position_y = -4000
                self.enemies_list = [enemy for enemy in self.enemies_list if not enemy.does_collide(self.player)]
                self.player_life -=1
     
    def run(self):
        """
        Main gameplay loop.
        Handles event listening, pausing, rendering, 
        updating player, enemies, bullets, background stars, 
        and collision detection.
        Returns 'Game over' when the player has no lives left.
        """
        self.player = Player(1280/2, 900, speed = 5, width=30, height=40)
        self.paused = False
               
        while True:
            self.event_listener()
            if self.paused:
                continue

            if self.player_life <= 0:
                break
                           
            self.display.fill((0,0,0))

            self.spawn_bg_stars()

            game_font = pygame.font.SysFont("Arial", 24)
            Point_text = game_font.render(f"Points: {self.player_score}", True, (255, 0, 0))
            life_text = game_font.render(f"Lives left: {self.player_life}", True, (255, 0, 0))
            self.display.blit(Point_text, (1110, 10))
            self.display.blit(life_text, (10, 10))
            
            self.player.draw(self.display)
            self.player.update(self)

            self.random_enemies()
            self.spawn_random_enemies()
            self.player_ammo()
            self.enemy_ammo()
            self.check_player_hits()
            self.check_enemy_bullet_hits()
            self.check_enemy_collides()
            
            pygame.display.flip()
            self.clock.tick(60)
        
        return "Game over"


class Sprite:
    """
    Base class for all game objects with position, speed, size, and image.

    Provides methods to draw and update objects (to be overridden)
    and to check collisions with other sprites.
    """
    def __init__(self, position_x: int, position_y: int, speed = 0, width = None, height = None, image = None):
        self.position_x = position_x
        self.position_y = position_y
        self.speed = speed
        self.width = width
        self.height = height
        self.image = image
    
    def draw(self, surface):
        pass
    
    def update(self):
        pass

    def does_collide(self, another: "Sprite"):
        """
        Returns True if this sprite collides with another sprite.
        Uses axis-aligned bounding box (AABB) collision detection.
        """
        return (
            self.position_x < another.position_x + self.width and
            self.position_x + self.width > another.position_x and 
            self.position_y < another.position_y + self.height and
            self.position_y + self.height > another.position_y
        )
    

class Player(Sprite):
    """
    Player-controlled spaceship.

    Handles drawing the ship with cockpit and thruster graphics,
    updating movement based on player input, and shooting bullets.
    """
    def __init__(self, position_x, position_y, speed=0, width=None, height=None, image=None):
        super().__init__(position_x, position_y, speed, width, height, image)
        self.player_cool_down = 0
    
    def draw(self, surface):

        points = [
            (self.position_x, self.position_y - self.height//2),          
            (self.position_x - self.width//2, self.position_y + self.height//2),  
            (self.position_x + self.width//2, self.position_y + self.height//2)   
        ]
        pygame.draw.polygon(surface, (200, 200, 200), points)
        pygame.draw.aalines(surface, (230, 230, 230), True, points)


        cockpit_points = [
            (self.position_x, self.position_y - self.height//6),          
            (self.position_x - self.width//5, self.position_y),           
            (self.position_x + self.width//5, self.position_y)            
        ]
        pygame.draw.polygon(surface, (100, 100, 255), cockpit_points)
        pygame.draw.aalines(surface, (150, 150, 255), True, cockpit_points)


        pygame.draw.polygon(surface, (255, 100, 0), [
            (self.position_x - self.width//4, self.position_y + self.height//2),  
            (self.position_x + self.width//4, self.position_y + self.height//2),  
            (self.position_x, self.position_y + self.height//2 + 10)              
        ])
    
    def update(self, game: "SpaceShooter"):
        if game.to_right and self.position_x<=1280-self.width:
            self.position_x += self.speed
        if game.to_left and self.position_x>0 + self.width:
            self.position_x -= self.speed
        if game.to_up and self.position_y >0 + self.height:
            self.position_y -= self.speed
        if game.to_down and self.position_y<=960-self.height:
            self.position_y += self.speed
        
        if game.to_shoot and self.player_cool_down == 0:
                bullets = Bullet(self.position_x, self.position_y, speed = 10)
                game.player_bullets_list.append(bullets)
                self.player_cool_down=20
        
        if self.player_cool_down > 0: 
            self.player_cool_down -= 1

class Background_star(Sprite):
    """
    Represents a star in the background.

    Moves downward slowly to simulate starfield movement.
    """
    def __init__(self, speed=0, image=None):
        super().__init__(random.randint(1,1200), random.randint(1,300), 0.5, random.randint(1,3), random.randint(1,3), image)

    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.position_x, self.position_y), self.width)

    def update(self):
        self.position_y += self.speed
                        

class BasicEnemy(Sprite):
    """
    Standard enemy type.

    Moves downward and shoots bullets at intervals.
    """
    def __init__(self, width=None, height=None, image=None):
        super().__init__(random.randint(1,1280), random.randint(-200, -50), 1, 50, 40, image)
        self.basic_e_cooldown = 0

    def draw(self, surface):
        
        pygame.draw.ellipse(surface, (0, 255, 0), 
                           (self.position_x - self.width//2, self.position_y - self.height//4, 
                            self.width, self.height//2))
        
        pygame.draw.circle(surface, (100, 255, 100), 
                          (self.position_x, self.position_y + self.height//8), 
                          self.width//4)
    
    def update(self, game: "SpaceShooter"):
        self.position_y += self.speed

        if self.basic_e_cooldown == 0:
            basic_e_bullets = Bullet(self.position_x, self.position_y, width=10, height=10, speed = 3, colour = (0, 150, 255))
            game.enemies_bullets_list.append(basic_e_bullets)
            self.basic_e_cooldown=150
        
        if self.basic_e_cooldown > 0: 
            self.basic_e_cooldown -= 1

class AggressiveEnemy(Sprite):
    """
    Enemy type that moves faster than BasicEnemy.

    Moves downward in a straight line, does not shoot.
    """
    def __init__(self, speed=0, width=None, height=None, image=None):
        super().__init__(random.randint(1,1280), random.randint(-200,-50), 5, 50, 40, image)

    def draw(self, surface):

        points = [
            (self.position_x, self.position_y + self.height//2),          
            (self.position_x - self.width//2, self.position_y - self.height//2),  
            (self.position_x - self.width//4, self.position_y - self.height//4),  
            (self.position_x + self.width//4, self.position_y - self.height//4),  
            (self.position_x + self.width//2, self.position_y - self.height//2)   
        ]
        pygame.draw.polygon(surface, (255, 50, 50), points)
        
        
        pygame.draw.circle(surface, (255, 255, 0), 
                          (self.position_x, self.position_y + self.height//6),  
                          self.width//8)
        
    def update(self, game: "SpaceShooter"):
        self.position_y += self.speed

class Drone(Sprite):
    """
    Enemy that actively follows the player.

    Moves toward the player's position and shoots bullets at intervals.
    """
    def __init__(self, speed=0, width=None, height=None, image=None):
        super().__init__(random.randint(1,1280), random.randint(-600,-100), 2, 20, 20, image)
        self.drone_cooldown = 0

    def draw(self, surface):
        
        pygame.draw.circle(surface, (0, 100, 255), (self.position_x, self.position_y), self.width//3)
        pygame.draw.circle(surface, (255, 0, 0),(self.position_x - self.width//3, self.position_y + self.height//4), self.width//6)
        pygame.draw.circle(surface, (255, 0, 0),(self.position_x + self.width//3, self.position_y + self.height//4), self.width//6)
        
    def update(self, game: "SpaceShooter"):
        
        if self.position_x < game.player.position_x:
            self.position_x += self.speed
        elif self.position_x > game.player.position_x:
            self.position_x -= self.speed
            
        if self.position_y < game.player.position_y:
            self.position_y += self.speed
        elif self.position_y > game.player.position_y:
            self.position_y -= self.speed
        
        if self.drone_cooldown == 0:
            drone_bullets = Bullet(self.position_x, self.position_y, width=1, height=1, speed = 10, colour = (255, 105, 180))
            game.enemies_bullets_list.append(drone_bullets)
            self.drone_cooldown=100
        
        if self.drone_cooldown > 0: 
            self.drone_cooldown -= 1


# class Asteroids(Sprite):
#     def __init__(self, position_x, position_y, speed=0, width=None, height=None, image=None):
#         super().__init__(position_x, position_y, speed, width, height, image)

#     def draw(self, surface):
#         points = []
#         for i in range(8):
#             angle = (i / 8) * 2 * math.pi
#             variation = random.uniform(0.7, 1.3)
#             x = self.position_x + math.cos(angle) * (self.width//2) * variation
#             y = self.position_y + math.sin(angle) * (self.height//2) * variation
#             points.append((x, y))
        
#         pygame.draw.polygon(surface, (150, 150, 150), points)
#         pygame.draw.aalines(surface, (100, 100, 100), True, points)
        
#     def update(self):
#         pass
        

class Bullet(Sprite):
    """
    Represents a bullet shot by the player or an enemy.

    Moves either up (player) or down (enemy) and checks for collisions.
    """
    def __init__(self, position_x, position_y, speed=0, width=5, height=5, image=None, colour = (255, 255, 0)):
        super().__init__(position_x, position_y, speed, width, height, image)
        self.colour = colour
    
    def draw(self, surface):
        pygame.draw.circle(surface, self.colour, (self.position_x, self.position_y), self.width)
        pygame.draw.circle(surface, self.colour, (self.position_x, self.position_y), self.width +2, 1)
        
        

    def update(self, game: "SpaceShooter"):
        if self in game.player_bullets_list:
            self.position_y -= self.speed
           
        else:
            self.position_y += self.speed
            
                
if __name__ == "__main__":
    SpaceShooter()