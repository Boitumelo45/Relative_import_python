from mods import Perimeter, Point

if __name__ == "__main__":
	point_1 = Point(43,2)
	print("Point: {}".format(point_1.get_points()))
	p = Perimeter(4,2)
	print("Perimeter = {}".format(p.perimeter()))
