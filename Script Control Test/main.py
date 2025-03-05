
class information:
    def __init__(self):
        self.value = 0
        pass
    def iterate(self, addition):
        self.value = self.value + addition
        ...




test = information()


def update(add):
    test.iterate(add)
    ...


def read():
    return test.value