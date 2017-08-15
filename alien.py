#coding=utf8

import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
	def __init__(self, ai_settings, screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#载图
		self.image = pygame.image.load('images/alien.png')
		self.rect = self.image.get_rect()

		#初始生成在左上角
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#存储准确位置
		self.x = float(self.rect.x)

	def blitme(self):
		#绘制
		self.screen.blit(self.image, self.rect)
