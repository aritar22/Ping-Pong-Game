from random import *
from pygame import *

win_width = 700
win_length = 500
window = display.set_mode((700,500))
display.set_caption("Game")
background = transform.scale(image.load("background_brown.png"),(700, 500))
p1 = transform.scale(image.load("block_narrow.png"), (20, 100))
p2 = transform.scale(image.load("block_narrow.png"), (20, 100))


clock= time.Clock()
FPS=60
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image =  transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Paddle(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.x <635:
            self.rect.x += self.speed
    def update_r(self):
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 650:
            self.rect.x = (0,0)
            self.rect.y = -10
            lost=lost + 1   
game= True
while game != False:
    window.blit(background,(0,0))
    window.blit(p1,(75, 200))
    window.blit(p2,(625, 200))
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()