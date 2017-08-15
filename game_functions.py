#coding=utf8

import sys
import pygame
from bullet import Bullet 
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		#创建一颗子弹
		fire_bullet(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
	#按键和鼠标
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
	
def update_screen(ai_settings, screen, ship, aliens, bullets):
	#更新屏幕图像，并切换到新屏幕
	#每次循环重绘屏幕
	screen.fill(ai_settings.bg_color)

	#绘制子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	#aliens.blitme(screen)
	for alien in aliens.sprites():
		alien.blitme()

	#让最近绘制的屏幕可见
	pygame.display.flip()

def update_bullets(bullets):
	#删除出屏幕子弹
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def fire_bullet(ai_settings, screen, ship, bullets):
	new_bullet = Bullet(ai_settings, screen, ship)
	bullets.add(new_bullet)
	
def creat_fleet(ai_settings, screen, aliens):
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width 
	available_space_x = ai_settings.screen_width - 2 * alien_width
	number_alien_x = int(available_space_x / (2 * alien_width))

	#创建第一行外星人
	for alien_number in range(number_alien_x):
		alien = Alien(ai_settings, screen)
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		aliens.add(alien)