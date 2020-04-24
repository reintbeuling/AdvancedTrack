
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
def print_point(pt):
    print('Points: ({0},{1})'.format(pt.x,pt.y))

class Rectangle:
    def __init__(self, posn, w, h):
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return '({0}, {1}, {2})'.format(self.corner, self.width, self.height)

    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        self.corner.x += dx
        self.corner.y += dy

q = Point(10,5)
print_point(q)

r = Rectangle(q, 100, 50)
print('rectangle:',r)
r.grow(25,-10)
print('grown rectangle:',r)
