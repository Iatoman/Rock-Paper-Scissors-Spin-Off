# What are the rules for snake and Ibrahim?

# Scissors decapitate snake, scissors cut paper, 
# paper covers rock, rock crushes snake, snake poisons Ibrahim, Ibrahim smashes scissors, 
# scissors decapitate snake, snake eats paper, paper cuts Ibrahim, 
# Ibrahim vaporizes rock, and as it always has, rock crushes scissors.


class Participant:
    
    
    def __init__(self):
        self.name = ""
        self.points = 0
        self.choice = ""
    def choose(self):
        choices = ("rock","paper","scissor","snake","ibrahim")
        
        while True:
            self.name = input("Enter Your name please \n")
            if len(self.name) > 0 :
                break
            else:
                print("Please enter a name \n")
            
        
        while True:
            self.choice = input("{name}, select rock, paper, scissor, snake or Ibrahim: \n".format(name= self.name))
            if self.choice.lower() in choices:
                self.choice = self.choice.lower()
                print("{name} selects {choice} \n".format(name=self.name, choice = self.choice))
                break
            else:
                print("The weapon choice entered is not recognised \n")
    
    def incrementPoint(self):
        self.points+=1
    
    def toNumericalChoice(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2,
            "snake": 3,
            "ibrahim": 4,
        }
        return switcher[self.choice]

class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1, 1, -1],
            [1, 0, -1, -1, 1],
            [-1, 1, 0, 1, -1],
            [-1, 1, -1, 0, 1],
            [1, -1, 1, -1, 0],
            
        ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1,p2)
        self.awardPoints(result, p1, p2)
        
        
        
    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]
    
    def awardPoints(self, result, p1, p2):
        if result > 0:
           p1.incrementPoint()
           print('Round resulted in a win for {player1}\n'.format(player1 = p1.name))
        elif result < 0:
           p2.incrementPoint()
           print('Round resulted in a win for {player2}\n'.format(player2 = p2.name))
        else:
            print('Round resulted in a draw\n')
        
    def getResultAsString(self, result):
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
        }       
        return res[result]


class Game:
    def __init__(self):
        self.endGame = False
        self.participant = Participant()
        self.secondParticipant = Participant()
    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()

    def checkEndCondition(self):
        answer = input("Continue game y/n: \n")
        if answer == 'y':
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()
        else:
            print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}\n".format(p1name = self.participant.name, p1points= self.participant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True
    def determineWinner(self):
        resultString = "It's a Draw"
        if self.participant.points > self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.participant.name)
        elif self.participant.points < self.secondParticipant.points:
            resultString = "Winner is {name}".format(name=self.secondParticipant.name)
        print(resultString+'\n')

game = Game()
game.start()
