import math


class MiniMaxWithPruning:
    def __init__(self, playerValue, maxTreeDepth):
        self.agentFunction = self.get_next_max_State
        self.player = playerValue
        self.maxTreeDepth = maxTreeDepth

    def __init__(self, is_minimizer, playerValue, maxTreeDepth):
        self.agentFunction = self.get_next_min_State if is_minimizer else self.get_next_max_State
        self.player = playerValue
        self.maxTreeDepth = maxTreeDepth

    def get_next_state(self, state):
        return self.agentFunction(state)

    def get_next_max_State(self, state):
        successors = state.get_neighbors()

        maxStateValue = float('-inf')
        maxState = None

        for successor in successors:
            if self.min_value(successor, self.maxTreeDepth) > maxStateValue:
                maxState = successor

        return maxState

    def get_next_min_State(self, state):
        successors = state.get_neighbors()

        minStateValue = float('inf')
        minState = None

        for successor in successors:
            if self.max_value(successor, self.maxTreeDepth) < minStateValue:
                minState = successor

        return minState

    def max_value(self, state, alpha, beta, level):
        if level == 0:
            return state.get_heuristic()

        value = float('-inf')

        successors = state.get_neighbors()

        if len(successors) == 0:
            return state.get_utility()

        for successor in successors:
            value = max(value, self.min_value(successor, level - 1))

            if value >= beta:
                return value

            alpha = max(alpha, value)

        return value

    def min_value(self, state, alpha, beta, level):
        if level == 0:
            return state.get_heuristic()

        value = float('inf')

        successors = state.get_neighbors()

        if len(successors) == 0:
            return state.get_utility()

        for successor in successors:
            value = min(value, self.max_value(successor, level - 1))

            if value <= alpha:
                return value

            beta = min(beta, value)

        return value