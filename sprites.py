import pygame
from math import sqrt
class Player(pygame.sprite.Sprite):
    
    def parse_spritesheet_row(self, x,y, width, height, row):

        sprite = pygame.Surface((width,height))
        sprite.set_colorkey((0,0,0))
        sprite.blit(self.sprites_image, (0,0), (x,y,width,height))

        if row < 0:
            return [sprite]
        
        if row - 4 <= 0:
            return [sprite] + self.parse_spritesheet_row(x + width, y, width, height, row -1)

        return [sprite] + self.parse_spritesheet_row(x + width, y, width, height, row -1)
    
    def get_full_spritesheet(self, x,y, width, height, row, col):
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
        self.speed = 4
        self.x = 100
        self.y = 100
        self.current_sprite = 0
    
    def move(self):
        self.velX = 0
        self.velY = 0
        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed
        if self.up_pressed and not self.down_pressed:
            self.velY = -self.speed
        if self.down_pressed and not self.up_pressed:
            self.velY = self.speed
        
        self.rect.x += self.velX
        self.rect.y += self.velY
        self.rect = self.image.get_rect(center=self.rect.center)


    
    def idle_animation(self):
        if self.current_sprite >= 8:
            self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprite_sheet[0][int(self.current_sprite)], (50,70)).convert_alpha()
        self.current_sprite += .2
        self.rect = self.image.get_rect(center=self.rect.center)

    def direction_change(self,dir):
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
            

class Bullet(pygame.sprite.Sprite):
    def __init__(self, asset,pos, type) -> None:
        super().__init__()
        self.image = asset.convert_alpha()
        self.rect = self.image.get_rect(center = pos)
        self.speed = 20
        self.type = type

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y -= self.speed
        self.rect = self.image.get_rect(center=self.rect.center)

        if self.rect.y <= -50 or self.check_collision():
            self.kill()
    
    def check_collision(self):
        return self.rect.collidepoint(Enemy().rect.midbottom)
        

class Enemy(Player):
    def __init__(self, move=[]) -> None:
        super().__init__()
        self.sheet = pygame.image.load('assets/player/enemy.png')
        self.image = self.sheet
        self.rect = self.image.get_rect(center = (400, 200))
        self.move_pattern = move
        self.move_state = 0
        self.complete_movement = True
        self.vx = 1
        self.vy = 1

    def move(self, move_pattern):
        x = move_pattern[self.move_state][0]
        y = move_pattern[self.move_state][1]

        pythad_dist = self.pythagoras_distance(x, y)
        # print(self.move_state)
        # print(len(move_pattern))
        
        # print(self.pythagoras_distance(move_pattern[self.move_state][0], move_pattern[self.move_state][1]))
        # print(self.pythagoras_distance(move_pattern[0], move_pattern[1]) <= (0, 0))
        if pythad_dist != 0:
            dir = self.direction(x,y)
            if dir[0] < 0 and self.vx > 0:
                self.vx *= -1
            elif dir[0] > 0 and self.vx < 0:
                self.vx *= 1
            if dir[1] < 0 and self.vy > 0:
                self.vy *= -1
            elif dir[1] > 0 and self.vy < 0:
                self.vy *= 1

            if self.rect.x != x:
                self.rect.x += self.vx
            if self.rect.y != y:
                self.rect.y += self.vy
        else:
            if self.move_state < len(move_pattern) -1:
                    self.move_state += 1

    def pythagoras_distance(self, x,y):
        return sqrt((self.rect.x - x) + (self.rect.y - y) ** 2)
    
    def direction(self, x, y):
        return (x - self.rect.x , y - self.rect.y)
        


class Button(pygame.sprite.Sprite):

    def __init__(self, text, pos) -> None:
        super().__init__()
        self.color = "#454647"
        self.text = text
        self.font = pygame.font.SysFont('MS Mincho', 50) 
        self.image = self.font.render(text, False, self.color)
        self.rect = self.image.get_rect(midbottom = pos)
        self.active = False

    def redraw(self):
        if self.active:
            self.color = "#f5f7fa"
        else:
            self.color = "#454647"
        self.image = self.font.render(self.text, False, self.color)
    def Broadcast(self):
        return self.text