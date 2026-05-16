from pygame import *
import pygame.sprite
#окно
window_height = 700
window_width = 500
display.set_caption('Ping-Pong')
window = display.set_mode((window_width, window_height))
#классы
class GameSprite(sprite.Sprite):
 #конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):


       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed


       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player_left(GameSprite):
    def __init__(self, image, player_x, player_y, size_x, size_y, player_speed):
        def update(self):
            keys = key.get_pressed()
            if keys[K_W] and self.rect.y > 70:
                self.rect.y -= self.speed
            if keys[K_S] and self.rect.y < window_height - 70:
                self.rect.y += self.speed
player1 = Player_left('wall.png', 350, 50, 70, 70, 3)
class Player_right(GameSprite):
    def __init__(self, image, player_x, player_y, size_x, size_y, player_speed):
        def update(self):
            keys = key.get_pressed()
            if keys[K_UP] and self.rect.y > 70:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < window_height - 70:
                self.rect.y += self.speed
player2 = Player_right('wall.png', 350, 450, 70, 70, 3)
class Ball(GameSprite):
    def __init__(self, image, player_x, player_y, size_x, size_y, player_speed):
        def update(self):
            if self.rect.y >=50:
                self.speed = self.speed * -1
            if self.rect.y <= window_height - 50:
                self.speed = self.speed * -1

ball = Ball('tennis_ball.png', 350, 250, 50, 50, 4)
ball2 = Ball('tennis_ball.png', 350, 250, 50, 50, 5)            
#игровой цикл
game = True
while game:
    player1.reset()
    player2.reset()
    ball.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False