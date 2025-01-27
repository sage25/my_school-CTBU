class Home:
	def __init__(self, area, type):
		# 实际面积 可用面积 家具 户型
		self.area = area
		self.type = type
		self.usable_area = self.area
		self.furniture_list = []
			

	def __str__(self):
		return "这个房子实际面积是%d，户型是%s，可用面积是%d，家具有%s"%(self.area, self.type, self.usable_area, str(self.furniture_list))

	def add_furniture(self, furniture):
		self.furniture_list.append(furniture.type)
		self.usable_area = self.usable_area - furniture.get_area()
 
class Bed:
	def __init__(self, type, area):
		self.type = type
		self.area = area
	
	def get_type(self):
		return self.type

	def get_area(self):
		return self.area


home1 = Home(150, "三室一厅")
bed = Bed("双人床", 4)
home1.add_furniture(bed)
print(home1)
