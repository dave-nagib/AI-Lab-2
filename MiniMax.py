import math
from Node import Node
from random import randint

from State import State


class MiniMax:
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

            successorNodeMinValue = self.max_value(successor, self.maxTreeDepth, successorNode)

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

            successorNode = Node(randint(1, 10000), 0, [])
            self.minimaxTree.children.append(successorNode)

            successorNodeMaxValue = self.max_value(successor, self.maxTreeDepth, successorNode)

            if successorNodeMaxValue < minStateValue:
                minState = successor
                minStateValue = successorNodeMaxValue

        self.minimaxTree.value = minStateValue
        return minState
    

    def max_value(self, state: State, level: int, maximizerNode: Node):
        maximizerNode.value = float('-inf')

        successors = state.get_neighbors()

        if len(successors) == 0:
            maximizerNode.value = state.get_utility()
            return maximizerNode.value
        elif level == 0:
            maximizerNode.value = state.get_heuristic()
            return maximizerNode.value

        tempValue = maximizerNode.value
        for successor in successors:
            successorNode = Node(randint(1, 10000), 0, [])
            maximizerNode.children.append(successorNode)
            successorNodeMinValue = self.min_value(successor, level-1, successorNode)
            tempValue = max(tempValue, successorNodeMinValue)
        maximizerNode.value = tempValue

        return maximizerNode.value


    def min_value(self, state: State, level: int, minimzerNode: Node):
        minimzerNode.value = float('inf')

        successors = state.get_neighbors()

        if len(successors) == 0:
            minimzerNode.value = state.get_utility()
            return minimzerNode.value
        elif level == 0:
            minimzerNode.value = state.get_heuristic()
            return minimzerNode.value

        tempValue = minimzerNode.value
        for successor in successors:
            successorNode = Node(randint(1, 10000), 0, [])
            minimzerNode.children.append(successorNode)
            successorNodeMaxValue = self.max_value(successor, level - 1, successorNode)
            tempValue = min(tempValue, successorNodeMaxValue)
        minimzerNode.value = tempValue

        return minimzerNode.value
    
    def getMiniMaxTree(self):
        self.__file = open("mmtree.txt", "w")
        self.__file.write(str(self.minimaxTree.value) + '\n')
        for successor in self.minimaxTree.children:
            self.__getMiniMaxTree(successor, 1)
        self.__file.close()

    def __getMiniMaxTree(self, node, level):
        self.__file.write("|   " * (level-1) + "|___")
        self.__file.write(str(node.value) + '\n')

        if len(node.children) > 0 and len(node.children[0].children) == 0:
            self.__file.write("|   " * (level) + "|___")
            for child in node.children:
                self.__file.write(str(child.value) + " ")
            self.__file.write('\n')
        else:
            for child in node.children:
                self.__getMiniMaxTree(child, level + 1)

