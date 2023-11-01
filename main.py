from quad_implementation import Rectangle, Square
s = Square(5)
r = Rectangle(8,2)

print(f"square area = {s.get_area()}")
print(f"rectangle area = {r.get_area()}")
print(f"aggregated area is: {s+r}")