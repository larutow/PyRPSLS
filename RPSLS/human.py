from player import Player


class Human(Player):

    def __init__(self, name):
        super(Human, self).__init__(name)
        self.name = name

    def ChooseGesture(self):
        print(self.name+" - Enter Gesture Type")
        for gesture in self.availableGestures:
            print(gesture.gestureType)
        self.EnterValidChoice()

    def EnterValidChoice(self):
        validEntry = 1
        while validEntry != 0:
            userEntry = input()
            for each in self.availableGestures:
                if userEntry == each.gestureType:
                    self.chosenGesture = each
                    validEntry = 0
                    break
            if validEntry != 0:
                print("Input did not match any of the available gestures, please reenter")
