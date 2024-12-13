from PyQt5.QtCore import QPoint

from figure.ChessPiece import ChessPiece


class King(ChessPiece):
    def get_possible_moves(self):
        return [
            QPoint(self.position.x() + 1, self.position.y()),
            QPoint(self.position.x() - 1, self.position.y()),
            QPoint(self.position.x(), self.position.y() + 1),
            QPoint(self.position.x(), self.position.y() - 1),
            QPoint(self.position.x() + 1, self.position.y() + 1),
            QPoint(self.position.x() - 1, self.position.y() - 1),
            QPoint(self.position.x() + 1, self.position.y() - 1),
            QPoint(self.position.x() - 1, self.position.y() + 1)
        ]

    def get_image_path(self):
        return "images" + ("" if self.is_white else "/black") + "/king.png"

    def get_initial_position(self):
        return QPoint(4, 7) if self.is_white else QPoint(4, 0)