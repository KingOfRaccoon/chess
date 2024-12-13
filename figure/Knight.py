from PyQt5.QtCore import QPoint

from figure.ChessPiece import ChessPiece


class Knight(ChessPiece):
    def get_possible_moves(self):
        return [
            QPoint(self.position.x() + 2, self.position.y() + 1),
            QPoint(self.position.x() + 2, self.position.y() - 1),
            QPoint(self.position.x() - 2, self.position.y() + 1),
            QPoint(self.position.x() - 2, self.position.y() - 1),
            QPoint(self.position.x() + 1, self.position.y() + 2),
            QPoint(self.position.x() + 1, self.position.y() - 2),
            QPoint(self.position.x() - 1, self.position.y() + 2),
            QPoint(self.position.x() - 1, self.position.y() - 2)
        ]

    def get_image_path(self):
        return "images" + ("" if self.is_white else "/black") + "/knight.png"

    def get_initial_position(self):
        return QPoint(1, 7) if self.is_white else QPoint(1, 0)