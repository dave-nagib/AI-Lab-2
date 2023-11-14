import math
from Node import Node
from random import randint


class MiniMax:
    def __init__(self, playerValue: int, maxTreeDepth: int):
        self.agentFunction = self.get_next_min_State
        self.player = playerValue
        self.maxTreeDepth = maxTreeDepth
        self.minimaxTree = None

    # def __init__(self, is_minimizer: bool, playerValue: int, maxTreeDepth: int):
    #     self.agentFunction = self.get_next_min_State if is_minimizer else self.get_next_max_State
    #     self.player = playerValue
    #     self.maxTreeDepth = maxTreeDepth

    def get_next_state(self, state):
        return self.agentFunction(state)

    def get_next_max_State(self, state):
        successors = state.get_neighbors()

        maxStateValue = float('-inf')
        maxState = None

        for successor in successors:
            value = self.max_value(successor, self.maxTreeDepth)
            print(value)
            if value > maxStateValue:
                maxState = successor
                maxStateValue = value

        return maxState

    def get_next_min_State(self, state):
        successors = state.get_neighbors()

        minStateValue = float('inf')
        minState = None
        self.minimaxTree = Node(randint(1, 10000), 0, [])
    
        for successor in successors:

            node = Node(randint(1, 10000), 0, [])
            self.minimaxTree.children.append(node)

            value = self.max_value(successor, self.maxTreeDepth, node)
            node.value = value

            if value < minStateValue:
                minState = successor
                minStateValue = value
                # successor.print_connect_4_board()

        self.minimaxTree.value = minStateValue
        return minState
    

    def max_value(self, state, level, node):
        value = float('-inf')

        if level == 0:
            value = state.get_heuristic()
            node.value = value
            return value

        successors = state.get_neighbors()

        if len(successors) == 0:
            value = state.get_utility()

        for successor in successors:
            successorNode = Node(randint(1, 10000), 0, [])
            node.children.append(successorNode)
            successorNodeMaxValue = self.min_value(successor, level - 1, successorNode)
            successorNode.value = successorNodeMaxValue
            value = max(value, successorNodeMaxValue)
            successorNode.value = value

        return value

    def min_value(self, state, level, node):
        value = float('inf')

        if level == 0:
            value = state.get_heuristic()
            node.value = value
            return value


        successors = state.get_neighbors()

        if len(successors) == 0:
            value = state.get_utility()

        for successor in successors:
            successorNode = Node(randint(1, 10000), 0, [])
            node.children.append(successorNode)
            successorNodeMaxValue = self.max_value(successor, level - 1, successorNode)
            successorNode.value = successorNodeMaxValue
            value = min(value, successorNodeMaxValue)
        
        return value
    
    def getMiniMaxTree(self):
        print(self.minimaxTree.value)
        for successor in self.minimaxTree.children:
            self.__getMiniMaxTree(successor, 1)

    def __getMiniMaxTree(self, node, level):
        print("\t" * level, end='')
        print(node.value)

        if len(node.children[0].children) == 0:
            print("\t" * (level + 1), end='')
            for child in node.children:
                print(child.value, end=' ')
            print()
        else:
            for child in node.children:
                self.__getMiniMaxTree(child, level + 1)

