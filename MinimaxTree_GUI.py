from PyQt5.QtWidgets import QDialog, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import networkx as nx


class Connect4MinimaxTreeWindow(QDialog):
    def __init__(self, graph_nodes):
        super().__init__()

        self.setWindowTitle("Connect4 Minimax Tree")
        self.setGeometry(500, 500, 600, 600)

        # Create layout
        self.layout = QVBoxLayout()

        # Create FigureCanvas
        self.canvas = FigureCanvas(plt.Figure())
        self.layout.addWidget(self.canvas)

        self.graph_nodes = graph_nodes
        self.init_ui()

    def init_ui(self):
        G = nx.Graph()
        pos = {}

        # Create nodes and edges based on the given graph structure
        for node in self.graph_nodes:
            G.add_node(node.id, label=str(node.value))

        # Calculate positions
        self.calculate_positions(G, self.graph_nodes[0], pos, 0, 0, 2)

        # Draw the graph on the FigureCanvas
        self.draw_generic_graph(G, pos)

        # Set layout for the dialog
        self.setLayout(self.layout)

    def calculate_positions(self, graph, node, pos, x, y, layer_height):
        if node is not None:
            pos[node.id] = (x, y)
            i = 0
            for child_id in node.children:
                self.calculate_positions(graph, self.graph_nodes[child_id - 1], pos, 2 * x + (i - 1) * layer_height,
                                         y - 1, layer_height / 2)
                i += 1
                graph.add_edge(node.id, child_id)

    def draw_generic_graph(self, graph, pos):
        ax = self.canvas.figure.add_subplot(111)

        nx.draw(graph, pos, with_labels=True, labels=nx.get_node_attributes(graph, 'label'),
                node_size=700, node_color="skyblue", font_size=10, font_color="black",
                font_weight="bold", ax=ax)

        ax.set_axis_off()
        self.canvas.draw()
