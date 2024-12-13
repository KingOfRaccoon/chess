from PyQt5.QtCore import QPoint

from figure.ChessPiece import ChessPiece


class Rook(ChessPiece):
    def get_possible_moves(self):
        moves = []
        for i in range(1, 8):
            moves.extend([
                QPoint(self.position.x() + i, self.position.y()),
                QPoint(self.position.x() - i, self.position.y()),
                QPoint(self.position.x(), self.position.y() + i),
                QPoint(self.position.x(), self.position.y() - i)
            ])
        return moves

    def get_image_path(self):
        return "images" + ("" if self.is_white else "/black") + "/rook.png"

    def get_initial_position(self):
        return QPoint(0, 7) if self.is_white else QPoint(0, 0)
