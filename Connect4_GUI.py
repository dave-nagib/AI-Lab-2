from PyQt5.QtWidgets import QDialog, QGridLayout, QPushButton, QLabel
import MinimaxTree_GUI
from Node import Node

ROWS = 6
COLS = 7

##### da 7aga dummy agrb elrasm biha elmafrod enha tb2a kda 34an a3rf arsmha
graph_nodes = [
    Node(1, 10, [2, 3]),
    Node(2, 20, [4, 5]),
    Node(3, 30, [6]),
    Node(4, 40, []),
    Node(5, 50, []),
    Node(6, 60, [])]


class Connect4Grid(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Connect4 Grid")
        self.setGeometry(200, 200, 400, 400)
        self.move(850, 200)
        self.init_ui()
        self.connect4_tree_window = None  # Store a reference to the Connect4MinimaxTreeWindow

    def init_ui(self):
        # Create layout
        layout = QGridLayout()

        # Create button row
        row_buttons = []
        for col in range(COLS):
            button = QPushButton(f"Col {col + 1}")
            button.setMinimumSize(50, 50)
            button.setStyleSheet("background-color: white;")
            button.clicked.connect(lambda _, col=col: self.on_button_click(col + 1))
            layout.addWidget(button, 0, col)
            row_buttons.append(button)

        # Create button grid
        self.labels = []  # Add this line to store references to labels
        for row in range(ROWS):
            label_row = []
            for col in range(COLS):
                label = QLabel()
                label.setMinimumSize(50, 50)
                label.setStyleSheet("background-color: white; border-radius: 25px;")
                layout.addWidget(label, row + 1, col)  # Add 1 to row to leave space for the button row
                label_row.append(label)
            self.labels.append(label_row)

        button = QPushButton("View Minimax tree")
        button.setStyleSheet("background-color: white;")
        button.clicked.connect(self.on_view_tree_click)
        layout.addWidget(button, ROWS + 1, 0, 1, COLS)  # Span the entire row

        self.setStyleSheet("background-color: blue;")
        self.setLayout(layout)

    def on_button_click(self, col):
        self.update_labels(col)
        print(f"Button clicked in column {col}")

    ##### kda di na2sha bs t7dd turns w row da elmafrod a5od mn back eli hwa
    ##### max limit 5las eli ba2i
    def update_labels(self, col):
        self.labels[0][col - 1].setStyleSheet("background-color: red; border-radius: 25px;")

    def on_view_tree_click(self):
        if self.connect4_tree_window is None:
            self.connect4_tree_window = MinimaxTree_GUI.Connect4MinimaxTreeWindow(
                graph_nodes)  # Create an instance if not exists
        self.connect4_tree_window.exec_()  # Show the window