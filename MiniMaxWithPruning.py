import math
from Node import Node
from random import randint

from State import State

class MiniMaxWithPruning:
    def __init__(self, maxTreeDepth: int):
        self.agentFunction = self.get_next_min_State
        self.maxTreeDepth = maxTreeDepth
        self.minimaxTree = None

    def get_next_state(self, state):
        return self.agentFunction(state)

    def get_next_max_State(self, state):
        successors = state.get_neighbors()

        maxStateValue = float('-inf')
        maxState = None
        self.minimaxTree = Node(randint(1, 10000), 0, [])

        for successor in successors:
            successorNode = Node(randint(1, 10000), 0, [])
            self.minimaxTree.children.append(successorNode)

            successorNodeMinValue = self.min_value(successor, self.maxTreeDepth, successorNode, float('-inf'), float('inf'))

            if successorNodeMinValue > maxStateValue:
                maxState = successor
                maxStateValue = successorNodeMinValue

        return maxState

    def get_next_min_State(self, state: State):
        successors = state.get_neighbors()

        minStateValue = float('inf')
        minState = None
        self.minimaxTree = Node(randint(1, 10000), 0, [])

        for successor in successors:
            successorNode = Node(randint(1, 10000), 'x', [])
            self.minimaxTree.children.append(successorNode)
    
        for i in range(7):
            successorNodeMaxValue = self.max_value(successors[i], self.maxTreeDepth, self.minimaxTree.children[i], float('-inf'), float('inf'))

            if successorNodeMaxValue < minStateValue:
                minState = successors[i]
                minStateValue = successorNodeMaxValue

        self.minimaxTree.value = minStateValue
        return minState
    

    def max_value(self, state: State, level: int, maximizerNode: Node, alpha, beta):
        maximizerNode.value = float('-inf')

        if level == 0:
            maximizerNode.value = state.get_heuristic()
            return maximizerNode.value

        successors = state.get_neighbors()

        if len(successors) == 0:
            maximizerNode.value = state.get_utility()

        for i in range(len(successors)):
            maximizerNode.children.append(Node(randint(1, 10000), 'x', []))

        tempValue = maximizerNode.value
        for i in range(len(successors)):
            successorNodeMinValue = self.min_value(successors[i], level-1, maximizerNode.children[i], alpha, beta)
            tempValue = max(tempValue, successorNodeMinValue)
            if tempValue >= beta:
                break
            alpha = max(alpha, tempValue)

        maximizerNode.value = tempValue
        return maximizerNode.value


    def min_value(self, state: State, level: int, minimzerNode: Node, alpha, beta):
        minimzerNode.value = float('inf')

        if level == 0:
            minimzerNode.value = state.get_heuristic()
            return minimzerNode.value

        successors = state.get_neighbors()

        if len(successors) == 0:
            minimzerNode.value = state.get_utility()

        for i in range(len(successors)):
            minimzerNode.children.append(Node(randint(1, 10000), 'x', []))

        tempValue = minimzerNode.value
        for i in range(len(successors)):
            successorNodeMaxValue = self.max_value(successors[i], level - 1, minimzerNode.children[i], alpha, beta)
            tempValue = min(tempValue, successorNodeMaxValue)
            if tempValue <= alpha:
                break
            beta = min(beta, tempValue)
        
        minimzerNode.value = tempValue
        return minimzerNode.value
    
    def getMiniMaxTree(self):
        self.__file = open("mmwptree.txt", "w")
        self.__file.write(str(self.minimaxTree.value) + '\n')
        for successor in self.minimaxTree.children:
            self.__getMiniMaxTree(successor, 1)
        self.__file.close()

    def __getMiniMaxTree(self, node, level):
        self.__file.write("|   " * (level-1) + "|___")
        self.__file.write(str(node.value) + '\n')

        if(len(node.children) == 0):
            self.__file.write("|   " * (level) + '\n')
            return
        if len(node.children[0].children) == 0:
            self.__file.write("|   " * (level) + "|___")
            for child in node.children:
                self.__file.write(str(child.value) + " ")
            self.__file.write('\n')
        else:
            for child in node.children:
                self.__getMiniMaxTree(child, level + 1)