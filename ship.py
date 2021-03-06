#coding=utf8

import pygame

class Ship(object):
	"""初始化"""
	def __init__(self, ai_settings, screen):
		self.screen = screen
		self.ai_settings = ai_settings

		#加载飞船图像并获取外接矩形
		self.image = pygame.image.load('images/ship.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#将每艘新飞船放置屏幕底部中央
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		# 在center中存储浮点数
		self.center = float(self.rect.centerx)

		#移动标志
		self.moving_right = False
		self.moving_left = False


	def blitme(self):
		'''在指定位置绘制飞船'''
		self.screen.blit(self.image,self.rect)

	def update(self):
		# 根据标识调整飞船位置
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.ai_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.ai_settings.ship_speed_factor

		self.rect.centerx = self.center

	def center_ship(self):
		#reset the ship
		self.center = self.screen_rect.centerx 