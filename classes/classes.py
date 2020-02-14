class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        pass

    def __repr__(self):
        pass

    def __lt__(self):
        pass

    def __gt__(self):
        pass

r1 = Rectangle(10, 20)
print(r1.width)
print(r1.perimeter)
