import pygame
from math import sqrt
import random

class Player(pygame.sprite.Sprite):

    """
    Player class, handles movement, collision and shooting. As well as
    rendering sprites and sprite sheets
    """
    
    def parse_spritesheet_row(self, x,y, width, height, row):
        
        """
        Parses sprite sheet by row
        """

        sprite = pygame.Surface((width,height))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprites_image, (0,0), (x,y,width,height))

        if row < 0:
            return [sprite]
        
        if row - 4 <= 0:
            return [sprite] + self.parse_spritesheet_row(x + width, y, width, height, row -1)

        return [sprite] + self.parse_spritesheet_row(x + width, y, width, height, row -1)
    
    def get_full_spritesheet(self, x,y, width, height, row, col):
        """
        Gets the full 2D list of the sprite sheet images
        """
        sprite_list = []
        adder = 0
        for _ in range(col):
            sprite_list += [self.parse_spritesheet_row(x,y + adder,width,height, row)]
            adder += 48
        self.sprite_sheet = sprite_list

    def __init__(self):
        super().__init__()
        self.sprites_image = pygame.transform.scale(pygame.image.load('assets/player/reimu.png'), (255,145)).convert_alpha()
        self.sprite_sheet = []
        self.get_full_spritesheet(0,0,32,48, 8, 3)
        # self.sprite_sheet = []
        self.image = self.sprite_sheet[0][0]
        self.rect = self.image.get_rect(center = (200,700))
        self.velX = 0
        self.velY = 0
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.speed = 6
        self.x = 100
        self.y = 100
        self.current_sprite = 0
        self.dead = False
        self.time1 = 0
        self.time2 = 0
        self.lives = 3
        self.top = False
        self.bottom = False
        self.right = False
        self.left = False
        self.invinc = False
        
    
    def move(self, group, live_label):
        """
        Handles player movement and interaction
        """
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed and not self.left:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed and not self.right:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed and not self.top:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed and not self.bottom:
            self.velY = self.speed
        
        self.rect.x += self.velX
        self.rect.y += self.velY
        self.rect = self.image.get_rect(center=self.rect.center)
        self.time1 = pygame.time.get_ticks()

        self.die(group, live_label)
        if self.dead and self.time1 - self.time2 > 500:
            self.dead = False
        
        if self.rect.y <= 0:
            self.top = True
        else:
            self.top = False
        if self.rect.y >= 800 - 70:
            self.bottom = True
        else: 
            self.bottom = False
        if self.rect.x >= 700 - 50:
            self.right = True
        else:
            self.right = False
        if self.rect.x <= 0:
            self.left = True
        else:
            self.left = False

    
    def idle_animation(self):
        """
        Handles player idle animation
        """
        if self.current_sprite >= 8:
            self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprite_sheet[0][int(self.current_sprite)], (50,70)).convert_alpha()
        self.current_sprite += .2
        self.rect = self.image.get_rect(center=self.rect.center)

    def direction_change(self,dir):
        """
        Handles left and right animations for player
        """
        if dir == "left":
            if self.current_sprite >= 7:
                self.current_sprite = 7
                self.image = pygame.transform.scale(self.sprite_sheet[1][int(self.current_sprite)], (50,70)).convert_alpha()
                self.rect = self.image.get_rect(center=self.rect.center)
                return
            self.image = pygame.transform.scale(self.sprite_sheet[1][int(self.current_sprite)], (50,70)).convert_alpha()
            self.current_sprite += .4
            self.rect = self.image.get_rect(center=self.rect.center)
        else:
            if self.current_sprite >= 7:
                self.current_sprite = 7
                self.image = pygame.transform.scale(self.sprite_sheet[2][int(self.current_sprite)], (50,70)).convert_alpha()
                self.rect = self.image.get_rect(center=self.rect.center)
                return
            self.image = pygame.transform.scale(self.sprite_sheet[2][int(self.current_sprite)], (50,70)).convert_alpha()
            self.current_sprite += .4
            self.rect = self.image.get_rect(center=self.rect.center)
    
    def die(self, group, live_label):
        """
        Handles player death
        """
        if not self.invinc:
            if pygame.sprite.spritecollide(self,group,dokill=False):
                for i in pygame.sprite.spritecollide(self,group,dokill=False):
                    print("killed")
                    i.kill()
                    self.rect = self.image.get_rect(center = (200,700))
                    self.dead = True
                    self.time2 = pygame.time.get_ticks()
                    self.lives -= 1
                    self.invinc = True
                    live_label.redraw(-1)
            
                
            

class Bullet(pygame.sprite.Sprite):

    """
    Sprite class for the bullet object of both the enemy and player
    """

    def __init__(self, asset,pos, type, speed=20, dir=1) -> None:
        super().__init__()
        self.image = asset.convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.speed = speed * dir
        self.type = type

    def draw(self, screen):
        """
        Draws the bullet to the screen
        """
        screen.blit(self.image, self.rect)

    def move(self):

        """
        Handles the bullets movement
        """

        self.rect.y -= self.speed
        self.rect = self.image.get_rect(center=self.rect.center)

        if self.rect.y <= -50:
            self.kill()
        

class Enemy(Player):

    """
    Enemy class, inherits from player and handles movement, sprite sheet,
    shooting and more.
    """

    def __init__(self,move=[], starty=0, startx = -20) -> None:
        super().__init__()
        self.sprites_image = pygame.image.load('assets/player/enemy.png')
        self.sheet_parse = self.parse_spritesheet_row(0,0, 31,32,12)
        self.image = pygame.transform.scale(self.sheet_parse[0], (40,50)).convert_alpha()
        self.rect = self.image.get_rect(center = (startx, starty))
        self.move_pattern = move
        self.move_state = 0
        self.complete_movement = True
        self.vx = 1
        self.vy = 1
        self.hp = 6
        self.shoot_num = 0

    def move(self, group_player_bullets, score):
        """
        Handles movement of the enemy sprite
        """
        x = self.move_pattern[self.move_state][0]
        y = self.move_pattern[self.move_state][1]
        
        pythad_dist = self.pythagoras_distance(x, y)

        if pythad_dist != 0:
            dir = self.direction(x,y)
            if dir[0] < 0 and self.vx > 0:
                self.vx *= -1
            elif dir[0] > 0 and self.vx < 0:
                self.vx *= -1
            if dir[1] < 0 and self.vy > 0:
                self.vy *= -1
            elif dir[1] > 0 and self.vy < 0:
                self.vy *= -1

            if self.rect.x != x:
                self.rect.x += self.vx
            if self.rect.y != y:
                self.rect.y += self.vy

            self.rect = self.image.get_rect(center=self.rect.center)
        else:
            if self.move_state < len(self.move_pattern) -1:
                    self.move_state += 1

        self.check_collide(group_player_bullets, score)

        if self.rect.x == -50 or self.rect.y == -50:
            self.kill()

    def pythagoras_distance(self, x,y):
        """
        Returns the pythagoras distance between a point and the sprites location
        """
        return sqrt((x - self.rect.x)**2 + (y - self.rect.y) ** 2)
    
    def direction(self, x, y):
        """
        Returns the direction of where the sprite needs to go
        """
        return (x - self.rect.x , y - self.rect.y)
    
    def check_collide(self,group, score):
        """
        Checks collision between the enemy sprite and the bullet
        """
        if pygame.sprite.spritecollide(self,group,dokill=False):
            for i in pygame.sprite.spritecollide(self,group,dokill=False):
                i.kill()
            self.damage(score)

    def damage(self, score):
        """
        Handles how the enemies take damage
        """
        self.hp -= 1
        if self.hp == 0:
            self.death(score)

    def death(self, score):
        """
        Handles enemy death
        """
        score.redraw(1000)
        self.kill()

    def shoot(self,bullet_sprite, group):
        """
        Handles enemy shooting
        """
        should_shoot_rand = random.randint(0,50)
        if int(self.shoot_num) == 1:
            if should_shoot_rand == 1:
                group.add(Bullet(bullet_sprite,(self.rect.center[0],self.rect.center[1] - 48), len(group.sprites()) - 1,10,  -1))
                self.shoot_num = 0
        else:
            self.shoot_num += (1/ 10)
        


class Button(pygame.sprite.Sprite):

    """
    Button class for the main menu and score
    """

    def __init__(self, text, pos) -> None:
        super().__init__()
        self.color = "#454647"
        self.text = text
        self.font = pygame.font.SysFont('MS Mincho', 50) 
        self.image = self.font.render(text, False, self.color)
        self.rect = self.image.get_rect(midbottom = pos)
        self.active = False

    def redraw(self):
        """
        Redraws the buttons to update their state
        """
        if self.active:
            self.color = "#f5f7fa"
        else:
            self.color = "#454647"
        self.image = self.font.render(self.text, False, self.color)

    def Broadcast(self):
        """
        Returns a string to tell what button type it is for 
        later logic.
        """
        return self.text
    
class Label(pygame.sprite.Sprite):

    """
    Label class that inherits from Button, 
    used for UI elements like lives and score.
    """

    def __init__(self, text, num, ypos) -> None:
        super().__init__()
        self.num = num
        self.text = text
        self.color = "#f5f7fa"
        self.font = pygame.font.SysFont('MS Mincho', 50) 
        self.image = self.font.render(f"{self.text}: {self.num}", False, self.color)
        self.rect = self.image.get_rect(center = (70,ypos))
    
    def redraw(self, new_num):
        """
        Redraws the label to update its state
        """
        self.num += new_num
        self.image = self.font.render(f"{self.text}: {self.num}", False, self.color)
