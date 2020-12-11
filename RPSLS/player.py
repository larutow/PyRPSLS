from gesture import Gesture

class Player:

    def __init__(self, name):
        self.availableGestures = [Gesture("rock"), Gesture("paper"), Gesture("scissors"), Gesture("lizard"), Gesture("spock")]
        self.chosenGesture = Gesture("NULL")
        self.name = name
        self.score = 0

    #ChooseGesture should be implemented, virtual

    def ScoreIncrease(self):
        self.score += 1