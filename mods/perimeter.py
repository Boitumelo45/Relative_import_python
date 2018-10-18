from . import Point

class Perimeter(object):
	
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def perimeter(self):
		"""
		   The perimeter is the length of the outline of a shape
		   2(x + y)
		"""
		P = 0
		for i in Point(self.a, self.b).get_points():
			P += 2 * i
		
		return P

if __name__ == "__main__":
	p = Perimeter(4,2)
	print(p.perimeter())
  		
