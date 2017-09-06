#coding=utf8

class GameStats():
	"""初始化"""
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()
		self.game_active = True
		
	def reset_stats(self):
		#初始化
		self.ships_left = self.ai_settings.ship_limit
