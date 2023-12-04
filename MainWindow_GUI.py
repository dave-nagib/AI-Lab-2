import sys

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGridLayout, QDialog, QLabel, QLineEdit
from LogicalInterface import LogicalInterface
from Connect4_GUI import Connect4Grid
from MiniMax import MiniMax
from MiniMaxWithPruning import MiniMaxWithPruning
from State import State


class MainWindow(QWidget):
    """
    Class to create the main window of the PyQt5 application.

    Attributes:
    - button1, button2: QPushButton
        The two buttons in the main window.
    - label1, label2: QLabel
        The labels associated with the buttons.
    """

    def __init__(self):
        """
        Constructor to initialize the main window.

        Sets up the layout and connects the button clicks to the respective functions.
        """

        super().__init__()

        # Setting up the window properties
        self.setWindowTitle("Main Window")
        self.setGeometry(200, 200, 600, 400)
        self.move(700, 200)

        # Creating the buttons and labels
        self.button1 = QPushButton("MiniMax")
        self.button1.setStyleSheet("Background-color: skyblue")
        self.button2 = QPushButton("MiniMax with pruning")
        self.button2.setStyleSheet("Background-color: skyblue")
        self.text_field = QLineEdit()
        self.text_field.setValidator(QIntValidator())  # Set QIntValidator to accept only integers

        # Creating the layout for the main window
        layout = QVBoxLayout()
        layout.addWidget(self.text_field)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        # Setting the layout for the main window
        self.setLayout(layout)

        # Connect the textChanged signal of QLineEdit to enable/disable buttons
        self.text_field.textChanged.connect(self.on_text_changed)

        # Disable buttons initially
        self.button1.setEnabled(False)
        self.button2.setEnabled(False)

        # Connecting the button clicks to the respective functions
        self.button1.clicked.connect(self.button1_clicked)
        self.button2.clicked.connect(self.button2_clicked)

        ##### 3amlto kda 34an a3ml call t7t
        self.k = None

    def on_text_changed(self):
        # Enable buttons only if there is text in the QLineEdit
        text = self.text_field.text().strip()
        self.k = int(text)
        self.button1.setEnabled(bool(text))
        self.button2.setEnabled(bool(text))

    def button1_clicked(self):
        """
        Function to handle the button1 click event.

        Saves the label of button1 as a string and opens the Connect4Window.
        """
        label_text = self.button1.text()
        print(label_text)
        connect4_grid = Connect4Grid(LogicalInterface(mmdepth = self.k, pruning = False))
        connect4_grid.exec_()

    def button2_clicked(self):
        """
        Function to handle the button2 click event.

        Saves the label of button2 as a string and opens the Connect4Window.
        """

        label_text = self.button2.text()
        print(label_text)
        connect4_grid = Connect4Grid(LogicalInterface(mmdepth = self.k, pruning = True))
        connect4_grid.exec_()


def main():
    """
    Main function to start the PyQt5 application.

    Creates and shows the main window.
    """
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
