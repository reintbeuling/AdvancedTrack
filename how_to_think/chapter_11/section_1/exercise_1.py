#Rewrite the distance function from the chapter titled
# fruitful functions so that it takes two point as parameters
# instead of four numbers


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

def print_point(pt):
    print('{0},{1}'.format(pt.x,pt.y))

def mid_point(p1,p2):
    mx = (p1.x + p2.x)/2
    my = (p1.y + p2.y)/2
    return Point(mx,my)

def distance(p1,p2):
    dx = (p2.x - p1.x)
    dy = (p2.y - p1.y)
    dsquared = dx*dx + dy*dy
    result = dsquared**0.5
    return result

q = Point(3,4)
w = Point(10,10)
r = mid_point(q,w)
d = distance(q,w)

print_point(q)
print_point(w)
print_point(r)
print(d)

#now test how pushing works