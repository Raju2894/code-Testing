class person():
    def __init__( self, x, y):
        self.x = x
        self.y = y
    def mup1(self):
        self.x = self.x - 1
    def mdw1(self):
        self.x = self.x + 1
    def lef(self):
        self.y = self.y - 1
    def righ(self):
        self.y = self.y + 1
    def checkwall(self):
        print " if X comes stop there and move to other side "

