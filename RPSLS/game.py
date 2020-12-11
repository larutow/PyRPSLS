import random
from player import Player
from human import Human
from ai import Ai


class Game:

    def __init__(self):
        self.menuOptions = ["1P Game", "2P Game", "Game Setup", "Rules / Help", "Exit Game"]
        self.p1 = Player("P1")
        self.p2 = Player("P2")
        self.bestOf = 3
        self.mode = "RPSLS"
        self.gameOptions = ["Toggle P1AI", "Toggle RPS Classic Mode"]
        self.p1AI = False

    def PlayGame(self):
        while (self.p1.score < (self.bestOf / 2) + 1) and (self.p2.score < (self.bestOf / 2) + 1):
            #clear console
            self.p1.ChooseGesture()
            #clear console
            self.p2.ChooseGesture()
            self.ShowGestures()
            self.CompareGestures()
            self.ShowScores()

        else:
            self.AnnounceVictor()
            self.EndGameOptions()

    def EndGameOptions(self):
        self.p1.score = 0
        self.p1.score = 0

        userInput = input("Play again? - Y for yes, N or other char - home menu")
        if userInput == "Y" or userInput == "y":
            self.PlayGame()
        else:
            self.DontPlayAgain()

    def DontPlayAgain(self):
        #clear console
        self.MainMenu()

    def AnnounceVictor(self):
        if(self.p1.score > self.p2.score):
            print("Game Over - P1 wins: "+self.p1.score+" - "+self.p2.score)
        else:
            print("Game Over - P2 wins: P2," + self.p2.score + " - P1," + self.p1.score)

    def ShowScores(self):
        print("Scoreboard:"+self.p1.name+" - "+self.p2.name)
        print(self.p1.score+" - "+self.p2.score)
        input("Enter any key to continue.")

    def CompareGestures(self):
        p1win = False
        if self.p1.chosenGesture.gestureType == self.p2.chosenGesture.gestureType:
            print("Draw, no one scores points")
            return

        for gesture in self.p1.chosenGesture.defeats:
            if self.p2.chosenGesture.gestureType == gesture:
                self.UpdateScore(self.p1)
                p1win = True
                break

        if p1win == False:
            self.UpdateScore(self.p2)

    def ShowGestures(self):
        print("Press any key to show & compare both players selected gestures")
        input()
        print(self.p1.name+" chose:"+self.p1.chosenGesture.gestureType)
        print(self.p2.name+" chose:"+self.p2.chosenGesture.gestureType)


    def UpdateScore(self, player):
        print(player.name+" won the round")
        player.score += 1

    def StartGame(self):
        print("Welcome to Rock - Paper - Lizard - Spock. Enter any key to continue.")
        input()
        self.MainMenu()

    def MainMenu(self):

        userInput = input("Press 1 for Human vs AI, Press 2 for Human vs Human")

        if userInput != '1' and userInput != '2':
            self.MainMenu()

        if userInput == "1":
            self.p1 = Human("P1")
            self.p2 = Ai("P2", random)
            #console clear
            self.PlayGame()
        else:
            self.p1 = Human("P1")
            self.p2 = Human("P2")
            #console clear
            self.PlayGame()
