class Gesture:

    def __init__(self, gestureType):
        self.gestureType = gestureType
        self.defeats = []
        self.PopulateDefeats()

    def PopulateDefeats(self):
        if self.gestureType == "rock":
            self.defeats.append("scissors")
            self.defeats.append("lizard")
        elif self.gestureType == "paper":
            self.defeats.append("rock")
            self.defeats.append("spock")
        elif self.gestureType == "scissors":
            self.defeats.append("paper")
            self.defeats.append("lizard")
        elif self.gestureType == "lizard":
            self.defeats.append("paper")
            self.defeats.append("spock")
        elif self.gestureType == "spock":
            self.defeats.append("scissors")
            self.defeats.append("rock")
