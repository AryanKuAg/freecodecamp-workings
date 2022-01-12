class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return "Too big for picture."
        picture = ''
        for row in range(self.height):
            for col in range(self.width):
                picture += "*"
            picture += "\n"
        return picture

    def get_amount_inside(self, otherShape):  # future
        mywidth = self.width
        myheight = self.height
        otherwidth = otherShape.width
        otherheight = otherShape.height
        width = mywidth // otherwidth
        height = myheight // otherheight
        return width * height

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side_length):
        self.width = side_length
        self.height = side_length

    def set_side(self, side):
        self.width = side
        self.height = side

    def __str__(self):
        return f"Square(side={self.width})"

    def set_width(self, side):
        self.width = side

    def set_height(self, side):
        self.height = side

########################################
