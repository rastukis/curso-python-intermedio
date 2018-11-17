class Circle:

    def __init__(self, radio):
        self.radio = radio

    @property
    def area(self):

        return 3.1416 * (self.radio * 2)

circle_instance = Circle(10)

print(circle_instance.area)