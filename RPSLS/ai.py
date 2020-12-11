from player import Player

class Ai(Player):
    def __init__(self, name):
        super(Ai, self).__init__(name)
        self.name = name