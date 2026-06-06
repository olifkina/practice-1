import math

class Shape3D:
    def __init__(self, density, owner):
        self.density = density
        self.owner = owner

    def get_volume(self):
        pass

    def get_surface_area(self):
        pass

    def get_type(self):
        pass

    def print_info(self):
        pass

class Sphere(Shape3D):
    def __init__(self, density, owner, radius):
        super().__init__(density, owner)
        self.radius = radius

    def get_volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

    def get_surface_area(self):
        return 4 * math.pi * (self.radius ** 2)

    def get_type(self):
        return "Sphere"

    def print_info(self):
        print(f"Шар | Владелец: {self.owner} | Плотность: {self.density} | Радиус: {self.radius} | V: {round(self.get_volume(), 2)} | S: {round(self.get_surface_area(), 2)}")

class Parallelepiped(Shape3D):
    def __init__(self, density, owner, length, width, height):
        super().__init__(density, owner)
        self.length = length
        self.width = width
        self.height = height

    def get_volume(self):
        return self.length * self.width * self.height

    def get_surface_area(self):
        return 2 * (self.length * self.width + self.width * self.height + self.length * self.height)

    def get_type(self):
        return "Parallelepiped"

    def print_info(self):
        print(f"Параллелепипед | Владелец: {self.owner} | Плотность: {self.density} | Ребра: {self.length}x{self.width}x{self.height} | V: {round(self.get_volume(), 2)} | S: {round(self.get_surface_area(), 2)}")

class Cylinder(Shape3D):
    def __init__(self, density, owner, x, y, r, h):
        super().__init__(density, owner)
        self.x = x
        self.y = y
        self.r = r
        self.h = h

    def get_volume(self):
        return math.pi * (self.r ** 2) * self.h

    def get_surface_area(self):
        return 2 * math.pi * self.r * (self.r + self.h)

    def get_type(self):
        return "Cylinder"

    def print_info(self):
        print(f"Цилиндр | Владелец: {self.owner} | Плотность: {self.density} | Центр: ({self.x};{self.y}) | R: {self.r} H: {self.h} | V: {round(self.get_volume(), 2)} | S: {round(self.get_surface_area(), 2)}")
