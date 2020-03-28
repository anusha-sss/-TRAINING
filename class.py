class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

Point1 = Point()
Point1.x = 1
Point1.y = 30
print(Point1.x + Point1.y)
Point1.draw()

Point2 = Point()
Point2.move()
