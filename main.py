import turtle

class Shape:
    def __init__(self, sides, length, color):
        self.sides = sides
        self.length = length
        self.color = color
        self.t = turtle.Turtle()

    def draw(self):
        self.t.pencolor(self.color)
        for _ in range(self.sides):
            self.t.forward(self.length)
            self.t.right(360 / self.sides)

class Square(Shape):
    def __init__(self, length, color):
        super().__init__(4, length, color)

class Triangle(Shape):
    def __init__(self, length, color):
        super().__init__(3, length, color)

class Pentagon(Shape):
    def __init__(self, length, color):
        super().__init__(5, length, color)

def main():
    turtle.speed(0)
    turtle.bgcolor("black")

    square = Square(100, "red")
    square.draw()

    triangle = Triangle(100, "blue")
    triangle.t.penup()
    triangle.t.goto(-150, 0)
    triangle.t.pendown()
    triangle.draw()

    pentagon = Pentagon(100, "green")
    pentagon.t.penup()
    pentagon.t.goto(150, 0)
    pentagon.t.pendown()
    pentagon.draw()

    turtle.done()

if __name__ == "__main__":
    main()
