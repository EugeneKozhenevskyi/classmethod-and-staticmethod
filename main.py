class Circle:
    pi = 3.14

    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self) -> float:
        return self.pi * self.radius ** 2

    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)

    @staticmethod
    def check_radius(radius) -> bool:
        return radius > 0
