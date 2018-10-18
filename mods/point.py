class Point(object):
	def __init__(self, a, b):
		self.a = a
		self.b = b
	
	def get_points(self):
		data =  [self.a, self.b]
		return data

if __name__ == "__main__":
	
	p = Point(2,3)
	print("Coordinates: {}".format(p.get_points()))

