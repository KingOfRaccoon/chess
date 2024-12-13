from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QComboBox, QWidget
from PyQt5.QtGui import QPainter, QColor, QPixmap
from PyQt5.QtCore import QPoint
import sys

from figure.Bishop import Bishop
from figure.King import King
from figure.Knight import Knight
from figure.Pawn import Pawn
from figure.Queen import Queen
from figure.Rook import Rook


class ChessBoard(QWidget):
    BOARD_SIZE = 8

    def __init__(self):
        super().__init__()
        self.selected_piece = None
        self.highlighted_cells = []
        self.setMinimumSize(600, 600)
        self.cell_size = self.width() // self.BOARD_SIZE

    def set_selected_piece(self, piece):
        self.selected_piece = piece
        self.highlighted_cells = piece.get_possible_moves() if piece else []
        self.update()

    def mousePressEvent(self, event):
        if not self.selected_piece:
            return

        click_x = event.x() // self.cell_size
        click_y = event.y() // self.cell_size
        clicked_cell = QPoint(click_x, click_y)

        if clicked_cell in self.highlighted_cells:
            print(f"Moving piece to {clicked_cell}")
            self.selected_piece.position = clicked_cell
            self.highlighted_cells = self.selected_piece.get_possible_moves()
            self.update()
        else:
            print(f"Invalid move to {clicked_cell}")

    def paintEvent(self, event):
        painter = QPainter(self)
        self.cell_size = self.width() // self.BOARD_SIZE

        # Draw board
        for row in range(self.BOARD_SIZE):
            for col in range(self.BOARD_SIZE):
                color = QColor(255, 255, 255) if (row + col) % 2 == 0 else QColor(125, 135, 150)
                painter.fillRect(col * self.cell_size, row * self.cell_size, self.cell_size, self.cell_size, color)

        # Draw selected piece
        if self.selected_piece:
            pos = self.selected_piece.position
            image_path = self.selected_piece.get_image_path()
            piece_image = QPixmap(image_path)
            if not piece_image.isNull():
                painter.drawPixmap(pos.x() * self.cell_size, pos.y() * self.cell_size, self.cell_size, self.cell_size, piece_image)

        # Highlight possible moves
        painter.setBrush(QColor(0, 0, 255, 100))
        for move in self.highlighted_cells:
            painter.drawRect(move.x() * self.cell_size, move.y() * self.cell_size, self.cell_size, self.cell_size)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Шахматная доска")

        self.chess_board = ChessBoard()
        self.piece_selector = QComboBox()
        self.init_ui()

    def init_ui(self):
        pieces = ["Ничего не выбрано", "Белая пешка", "Белая ладья", "Белый конь", "Белый слон", "Белый ферзь", "Белый король",
                  "Черная пешка", "Черная ладья", "Черный конь", "Черный слон", "Черный ферзь", "Черный король"]
        self.piece_selector.addItems(pieces)
        self.piece_selector.currentIndexChanged.connect(self.piece_selected)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Выберите фигуру:"))
        layout.addWidget(self.piece_selector)
        layout.addWidget(self.chess_board)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def piece_selected(self, index):
        if index == 0:
            self.chess_board.set_selected_piece(None)
            return

        piece_name = self.piece_selector.currentText()
        is_white = "Бел" in piece_name

        if "пешка" in piece_name:
            piece = Pawn(is_white)
        elif "ладья" in piece_name:
            piece = Rook(is_white)
        elif "конь" in piece_name:
            piece = Knight(is_white)
        elif "слон" in piece_name:
            piece = Bishop(is_white)
        elif "ферзь" in piece_name:
            piece = Queen(is_white)
        elif "король" in piece_name:
            piece = King(is_white)
        else:
            piece = None

        self.chess_board.set_selected_piece(piece)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())