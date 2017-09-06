#coding=utf8

class GameStats(object):
	"""初始化"""
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()

	def reset_stats():
		#初始化
		self.ships_left = self.ai_settings.ship_limit
