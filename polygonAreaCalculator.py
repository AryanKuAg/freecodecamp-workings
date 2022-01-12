

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self):
        pass

    def set_height(self):
        pass

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
