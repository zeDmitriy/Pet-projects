import random
from os import listdir
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT

pygame.init()

FPS = pygame.time.Clock()

screen = width, height = 1200, 800

BLACK = 0, 0, 0
WHITE = 255, 255, 255
GREEN = 0, 128, 0
RED = 255, 0, 0

font = pygame.font.SysFont('Verdana', 20, 1, 1)

main_surface = pygame.display.set_mode(screen)

IMGS_PATH = 'goose'

player_imgs = [pygame.image.load(IMGS_PATH + '/' + file).convert_alpha() for file in listdir(IMGS_PATH)]
player = player_imgs[0]
player_rect = player.get_rect()
player_speed = 5

def create_enemy():
    enemy = pygame.image.load('enemy.png').convert_alpha()
    enemy_rect = pygame.Rect(width, random.randint(0, (height - 72)), *enemy.get_size())
    enemy_speed = random.randint(2, 5)
    return [enemy, enemy_rect, enemy_speed]

def create_gift():
    gift = pygame.transform.scale(pygame.image.load('bonus.png').convert_alpha(), (100, 200))
    gift_rect = pygame.Rect(random.randint(0, (width - 100)), 0, *gift.get_size())
    gift_speed = random.randint(2, 5)
    return [gift, gift_rect, gift_speed]

bg = pygame.transform.scale(pygame.image.load('background.png').convert(), screen)
bgX = 0
bgX2 = bg.get_width()
bg_speed = 3

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 3500)  

CREATE_GIFTS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_GIFTS, 3500)

CHANGE_IMGS = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMGS, 125)

img_index = 0
scores =0
enemies = []
giftys = []

is_working = True

while is_working:
    FPS.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())

        if event.type == CREATE_GIFTS:
            giftys.append(create_gift()) 

        if event.type == CHANGE_IMGS:
            img_index += 1 
            if img_index == len(player_imgs):
                img_index = 0
            player = player_imgs[img_index]       

    pressed_keys = pygame.key.get_pressed()

    bgX -= bg_speed
    bgX2 -= bg_speed

    if bgX < -bg.get_width():
        bgX = bg.get_width()

    if bgX2 < -bg.get_width():
        bgX2 = bg.get_width()    

    main_surface.blit(bg, (bgX, 0))
    main_surface.blit(bg, (bgX2, 0))

    main_surface.blit(player, player_rect)
    main_surface.blit(font.render(str(scores), True, RED), (width - 50, 0))

    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])

        if enemy[1].left < 0:
            enemies.pop(enemies.index(enemy))

        if player_rect.colliderect(enemy[1]):
           is_working = False  

    for gift in giftys:
        gift[1] = gift[1].move(0, gift[2])
        main_surface.blit(gift[0], gift[1])

        if gift[1].bottom >= height:
            giftys.pop(giftys.index(gift))

        if player_rect.colliderect(gift[1]):
            giftys.pop(giftys.index(gift)) 
            scores += 1         

    if pressed_keys[K_DOWN] and not player_rect.bottom >= height:
        player_rect = player_rect.move(0, player_speed)

    if pressed_keys[K_UP] and not player_rect.top <=0:
        player_rect = player_rect.move(0, -player_speed)

    if pressed_keys[K_LEFT] and not player_rect.left <=0:
        player_rect = player_rect.move(-player_speed, 0)   

    if pressed_keys[K_RIGHT] and not player_rect.right >= width:
        player_rect = player_rect.move(player_speed, 0)    

    pygame.display.flip()    