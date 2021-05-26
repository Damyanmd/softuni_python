class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, new_radius):
        self.radius = new_radius

    def get_area(self):
        result = round(Circle.pi * self.radius**2, 2)
        return result

    def get_circumference(self):
        result = round(Circle.pi * (self.radius + self.radius), 2)
        return result