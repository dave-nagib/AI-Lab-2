from State import State
from MiniMax import MiniMax
from MiniMaxWithPruning import MiniMaxWithPruning
import time

ROWS = 6
COLS = 7

class LogicalInterface:

    def __init__(self, mmdepth: int, pruning: bool):
        self.__currState = State('0'*(ROWS*COLS), [0]*4, [0]*4, 1)
        self.__algorithm = MiniMaxWithPruning(mmdepth) if pruning else MiniMax(mmdepth)
        self.__totalTime = 0
        self.__totalTurns = 0

    def getStateColors(self):
        colors: list[list[str]] = []
        for i in range(ROWS):
            colors.append([])
            for j in range(COLS):
                match self.__currState.get_slot(i,j):
                    case '0':
                        colors[i].append('white')
                    case '1':
                        colors[i].append('red')
                    case '2':
                        colors[i].append('yellow')
        return colors
    
    def gameComplete(self) -> bool:
        for j in range (COLS):
            if self.__currState.get_slot(0,j) == '0': return False
        return True

    def logResults(self):
        chains1,chains2 = self.__currState.get_complete_chains()
        print(f'Player 1 score so far = {chains1}\nPlayer 2 score so far = {chains2}\n')
        # if chains1 > chains2:
        #     print("Player 1 has won!\n")
        # elif chains1 < chains2:
        #     print("Player 2 has won!\n")
        # else:
        #     print("It's a draw!")

    def userMove(self, col: int) -> bool:
        nextState = self.__currState.move_state(col-1)
        if nextState is not None: 
            self.__currState = nextState
            return True
        else:
            return False
        
    def computerMove(self):
        start = time.time()
        self.__currState = self.__algorithm.get_next_state(self.__currState)
        end = time.time()
        self.__totalTurns += 1
        self.__totalTime += (end-start)
        print(f'Time taken for AI\'s turn no.{self.__totalTurns} is {end-start:.4f} seconds. \nAverage turn time is {self.__totalTime/self.__totalTurns:.4f} seconds.')
        self.logDecisionTree()

    def logDecisionTree(self):
        self.__algorithm.getMiniMaxTree()