from MiniMax import MiniMax
from State import State




initialBoard = '0' * 42
state = State(initialBoard, [0] * 4, [0] * 4, 1)
k = int(input("Enter Max Tree Depth: "))

minimax = MiniMax(2, k)

while True:
    state.print_connect_4_board()
    col = int(input("Enter column number: "))
    state = state.move_state(col-1)
    print()
    state.print_connect_4_board()
    print()
    state = minimax.get_next_state(state)
    minimax.getMiniMaxTree()
    