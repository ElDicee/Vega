class room:

    def __init__(self):
        self.surface = 10  # m2
        self.elements = [...]


class kitchen(room):
    def __init__(self):
        super().__init__()
        self.capacity = 50  # kwh

    def make_dinner(self):
        print("ñamm!")


