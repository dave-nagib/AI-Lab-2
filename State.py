ROWS = 6
COLS = 7


class State:

    def __init__(self, board: str, chainCounts1: list[int], chainCounts2: list[int], nextTurn: int):
        self.__board = board
        self.__chains1 = chainCounts1
        self.__chains2 = chainCounts2
        self.__nextTurn = nextTurn

    def get_board(self):
        return self.__board

    def get_utility(self):
        return self.__chains1[3] - self.__chains2[3]
    
    def get_complete_chains(self):
        return self.__chains1[3], self.__chains2[3]


    def get_slot(self,i,j):
        if i*COLS+j in range(0, ROWS*COLS):
            return self.__board[i*COLS+j]
        else:
            return None

    def move_state(self, col: int):
        row = -1
        # Get the row where the piece will drop
        while self.get_slot(row + 1, col) == '0': row += 1
        # If the column is full, return None
        if row == -1: return None
        # Get the new state's string
        newBoard = self.__board[: row * COLS + col] + str(self.__nextTurn) + self.__board[row * COLS + col + 1:]
        chains1copy = [self.__chains1[i] for i in range(4)]
        chains2copy = [self.__chains2[i] for i in range(4)]
        newState = State(newBoard, chains1copy, chains2copy, 3 - self.__nextTurn)
        # Update chain counts of each player
        newState.__update_chains(row, col, str(self.__nextTurn))
        return newState

    def get_neighbors(self):
        neighbors = []
        for choice in range(0, COLS):
            neighbor = self.move_state(choice)
            if neighbor: neighbors.append(neighbor)
        return neighbors

    def __update_chains(self, x: int, y: int, pieceP: str):

        # Each offset represents a direction of right diagonal, horizontal, left diagonal, vertical
        offsets = [(1, 1), (0, 1), (-1, 1), (1, 0)]

        # Set proponent and opponent chain lists and pieces
        if pieceP == '1':
            chainsP, chainsO = self.__chains1, self.__chains2
        else:
            chainsP, chainsO = self.__chains2, self.__chains1
        pieceO = str(3 - int(pieceP))

        # Go in each direction forwards and backwards
        for (offsetRow, offsetCol) in offsets:

            # Remember boundaries in both directions
            boundaryF = None
            boundaryB = None

            # Get the slot touching the chain in the forward direction
            chainLenF = 0
            row, col = x + offsetRow, y + offsetCol
            slot = self.get_slot(row, col)

            # Touching piece is a proponent piece
            if slot == pieceP:
                # Count the chain length of the proponent
                while slot == pieceP:
                    chainLenF += 1
                    row, col = row + offsetRow, col + offsetCol
                    slot = self.get_slot(row, col)
                # Remember the boundary on which we stopped
                boundaryF = slot
                # Subtract the old chain's length that is touching the slot in the forward direction
                if (chainLenF in range(1, 5)):
                    chainsP[chainLenF - 1] -= 1  # 1 <= length <= 4
                else:
                    chainsP[3] -= (chainLenF - 3)  # length > 4
            # Touching piece is an oponent piece
            elif slot == pieceO:
                # The current proponent chain stops with boundary of opponent piece
                boundaryF = pieceO
                # Count the chain length of the opponent
                chainO = 0
                while slot == pieceO:
                    chainO += 1
                    row, col = row + offsetRow, col + offsetCol
                    slot = self.get_slot(row, col)
                # If the chain length < 4 and the other side of the chain is blocked,
                # this chain is taken out of the opponents chain list.
                if chainO < 4 and (slot is None or slot == pieceP):
                    chainsO[chainO - 1] -= 1
            # Touching an empty space or a board end
            else:
                boundaryF = slot

            # Get the slot touching the chain in the backward direction
            chainLenB = 0
            row, col = x - offsetRow, y - offsetCol
            slot = self.get_slot(row, col)

            # Touching piece is a proponent piece
            if slot == pieceP:
                # Count the chain length of the proponent
                while slot == pieceP:
                    chainLenB += 1
                    row, col = row - offsetRow, col - offsetCol
                    slot = self.get_slot(row, col)
                # Remember the boundary on which we stopped
                boundaryB = slot
                # Subtract the old chain's length that is touching the slot in the backward direction
                if chainLenB in range(1, 5):
                    chainsP[chainLenB - 1] -= 1  # 1 <= length <= 4
                else:
                    chainsP[3] -= (chainLenB - 3)  # length > 4
            # Touching piece is an opponent piece
            elif slot == pieceO:
                # The current proponent chain stops with boundary of opponent piece
                boundaryB = pieceO
                # Count the chain length of the opponent
                chainO = 0
                while slot == pieceO:
                    chainO += 1
                    row, col = row - offsetRow, col - offsetCol
                    slot = self.get_slot(row, col)
                # If the chain length < 4 and the other side of the chain is blocked,
                # this chain is taken out of the opponents chain list.
                if chainO < 4 and (slot is None or slot == pieceP):
                    chainsO[chainO - 1] -= 1
            # Touching an empty space or a board end
            else:
                boundaryB = slot

            newChainLen = chainLenF + chainLenB + 1
            # If the newly created chain's length is less than 4, and its blocked by both sides, then it should not be considered
            if newChainLen < 4 and (boundaryF == pieceO or boundaryF is None) and (
                    boundaryB == pieceO or boundaryB is None): continue
            # Add the new chain length to the chains otherwise
            if (newChainLen in range(1, 5)):
                chainsP[newChainLen - 1] += 1
            elif (newChainLen >= 5):
                chainsP[3] += (newChainLen - 3)

    def get_heuristic(self):
        h = 0
        for i in range(1, 3):
            h += pow(2,(i + 1)) * self.__chains1[i]
            h -= pow(2,(i + 1)) * self.__chains2[i]
        h += 100*self.__chains1[3]
        h -= 100*self.__chains2[3]
        return h

    def print_connect_4_board(self):
        if len(self.__board) != ROWS*COLS:
            raise ValueError("Input string must be of size 42 for a 6x7 Connect 4 board.")

        for row in range(0, ROWS):
            for col in range(0, COLS):
                print(self.__board[row * COLS + col], end=" ")
            print()