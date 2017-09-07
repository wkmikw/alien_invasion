#coding=utf8

class Settings(object):
	"""存储所有设置"""
	def __init__(self):
		#初始化游戏静态设置
		#屏幕设置
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)
		self.ship_speed_factor = 1.5

		#子弹设置
		self.bullet_speed_factor = 3
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		
		#外星人设置
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10 #origin 10
		# fleet_direction为1表示向右，-1表示向左
		self.fleet_direction = 1

		#飞船数量
		self.ship_limit = 3

		# the speed for up-class
		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		# the moving settings
		self.ship_speed_factor = 1.5
		self.bullet_speed_factor = 3
		self.alien_speed_factor = 1

		# fleet_direction为1表示向右，-1表示向左
		self.fleet_direction = 1

	def increase_speed(self):
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale




