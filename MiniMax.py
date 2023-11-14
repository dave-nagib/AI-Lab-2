import math


class MiniMax:
    def __init__(self, playerValue: int, maxTreeDepth: int):
        self.agentFunction = self.get_next_min_State
        self.player = playerValue
        self.maxTreeDepth = maxTreeDepth

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

        for successor in successors:
            value = self.max_value(successor, self.maxTreeDepth)
            # print(value)
            if value < minStateValue:
                minState = successor
                minStateValue = value
                # successor.print_connect_4_board()

        return minState

    def max_value(self, state, level):
        if level == 0:
            # print()
            # state.print_connect_4_board()
            # print(state.get_heuristic())
            return state.get_heuristic()

        value = float('-inf')

        successors = state.get_neighbors()

        if len(successors) == 0:
            return state.get_utility()

        for successor in successors:
            value = max(value, self.min_value(successor, level - 1))

        return value

    def min_value(self, state, level):
        if level == 0:
            # print()
            # state.print_connect_4_board()
            # print(state.get_heuristic())
            return state.get_heuristic()

        value = float('inf')

        successors = state.get_neighbors()

        if len(successors) == 0:
            return state.get_utility()

        for successor in successors:
            value = min(value, self.max_value(successor, level - 1))

        return value