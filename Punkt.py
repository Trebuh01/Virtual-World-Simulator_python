class Punkt:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, Punkt):
            return False
        return self.x == other.x and self.y == other.y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y
