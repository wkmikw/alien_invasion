#coding=utf8
#python alien_invasion.py
import sys
import pygame
from pygame.sprite import Group

import game_functions as gf 
from settings import Settings 
from ship import Ship
#from alien import Alien


def run_game():
	#初始化
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#创建飞船
	ship = Ship(ai_settings, screen)
	#创建子弹编组
	bullets = Group()
	#外星人编组
	aliens = Group()

	gf.creat_fleet(ai_settings, screen, ship, aliens)

	#开始游戏主循环
	while True:

		#监视键鼠
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
		gf.update_aliens(ai_settings, aliens)
		#print(len(bullets))

		#更新屏幕
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)



run_game()
 