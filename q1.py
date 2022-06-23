class Square:
    def __init__(self, w):
        self.area = w ** 2

    def get_area(self):
        return self.area

    def __add__(self, other):
        return self.get_area() + other.get_area()


class Rectangle:
    def __init__(self, w, h):
        self.area = w*h

    def get_area(self):
        return self.area

    def __add__(self, other):
        return self.get_area() + other.get_area()


if __name__ == "__main__":
    s = Square(5)
    r = Rectangle(8, 2)

    print(f"square area = {s.get_area()}")
    print(f"rectangle area = {r.get_area()}")

    print(f"aggregated area is: {s+r}")
