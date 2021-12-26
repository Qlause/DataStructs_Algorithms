
class TicTacToe:
    def __init__(self):
        self.field = [1,2,3,
                      4,5,6,
                      7,8,9]
        self.winCondition = [{1,2,3},{4,5,6},
                             {7,8,9},{1,4,7},
                             {2,5,8},{3,6,9},
                             {1,5,9},{3,5,7}]
        
        self.player, self.computer = set(), set()
        self.playerTurn, self.gameOver = True, False
        self.computerWin, self.computerLoss, self.computerTied, self.games = 0, 0, 0, 1
        
    def printField(self):
        print(f"""
              -------
              |{self.field[0]}|{self.field[1]}|{self.field[2]}|
              |{self.field[3]}|{self.field[4]}|{self.field[5]}|
              |{self.field[6]}|{self.field[7]}|{self.field[8]}|
              -------
              """)
        
    def turn(self, value=1):
        isRemain = [i for i in self.field if type(i) is int]
        if len(isRemain) == 0: 
            self.computerTied = self.computerTied + 1
            return print("tied!!!")
        
        if self.gameOver == False:
            if self.playerTurn == True:
                if type(self.field[value - 1]) is int: 
                    self.field[value - 1] = "O"
                else: 
                    return print("Pilih Field Yang kosong")
                
                self.player.add(value)
                if self.winCheck(self.player) == True: 
                    self.gameOver = True
                    self.printField()
                    self.computerLoss = self.computerLoss + 1
                    return print("You win")
                self.playerTurn = False
                self.printField()
                if self.playerTurn == False:self.turn()
                
            else:
                value = self.getValue()
                if type(self.field[value - 1]) is int: 
                    self.field[value - 1] = "X"
                else: 
                    return print("Pilih Field Yang kosong")
                
                self.computer.add(value)
                if self.winCheck(self.computer) == True: 
                    self.gameOver = True
                    self.printField()
                    self.computerWin = self.computerWin + 1
                    return print("Computer Wins!")
                self.playerTurn = True
                self.printField()
            
        else: return print("Game Has Over")
    
    def winCheck(self, set):
        for num in range(len(self.winCondition)):
            if self.winCondition[num].issubset(set) == True: return True
            
        return False
    
    def resetGame(self):
        self.field = [1,2,3,
                      4,5,6,
                      7,8,9]
        self.winCondition = [{1,2,3},{4,5,6},
                             {7,8,9},{1,4,7},
                             {2,5,8},{3,6,9},
                             {1,5,9},{3,5,7}]
        
        self.player, self.computer = set(), set()
        self.playerTurn, self.gameOver = True, False
        self.games = self.games + 1
        
    def fieldUpdate(self,field, value, cOrp):
        new = [i for i in field]
        new[value - 1] = cOrp
        return new 
    
    def addValueTo(self, turn, value):
        new = turn.copy()
        new.add(value)
        return new
        
    def aiGame(self, field, player, computer, playerturn , remaincol):
        # get all posibility moves
        remainCol = [i for i in field if type(i) is int]
        Col = len(remainCol)
        
        # base case if computer win, loss, tied
        if self.winCheck(player) == True: return -1 - Col
        if self.winCheck(computer) == True: return 1 + Col
        if Col == 0: return 0
        
        # this will be executed when computer's turn (maximazing value)
        if playerturn == False:
            value = []
            for i in remainCol:
                result = self.aiGame(self.fieldUpdate(field, i, "X"), 
                                     player, 
                                     self.addValueTo(computer, i), 
                                     True,
                                     remaincol)
                value.append(result)
                if Col == 1 and result == 0: break
                if self.winCheck(self.addValueTo(computer, i)) == True: break
            
            # when stack has reached root graph, it will be return index of max value
            if Col == remaincol:
                return value.index(max(value))
            
            # return max value   
            return max(value)
        
        else:
            value = []
            for i in remainCol:
                result = self.aiGame(self.fieldUpdate(field, i, "O"), 
                                     self.addValueTo(player, i), 
                                     computer, 
                                     False,
                                     remaincol)
                value.append(result)
                if Col == 1 and result == 0: break
                if self.winCheck(self.addValueTo(player, i)) == True: break
            return min(value)
        
    def getValue(self):
        remaincol = [i for i in self.field if type(i) is int]
        value = self.aiGame(self.field, self.player, self.computer, self.playerTurn, len(remaincol))
        print("value selected by AI : ", remaincol[value])
        return remaincol[value]
      

import random
import time  

game = TicTacToe()

# i = 1

# while i < 1000:
#     x = 0
#     listChoices = [i for i in game.field if type(i) is int]
#     while listChoices:
#         turn = random.choice(listChoices)
#         game.turn(turn)
#         time.sleep(1)
#         listChoices.remove(turn)
#     i += 1
#     game.resetGame()


