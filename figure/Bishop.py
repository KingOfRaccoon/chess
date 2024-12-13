from PyQt5.QtCore import QPoint

from figure.ChessPiece import ChessPiece


class Bishop(ChessPiece):
    def get_possible_moves(self):
        moves = []
        for i in range(1, 8):
            moves.extend([
                QPoint(self.position.x() + i, self.position.y() + i),
                QPoint(self.position.x() - i, self.position.y() - i),
                QPoint(self.position.x() + i, self.position.y() - i),
                QPoint(self.position.x() - i, self.position.y() + i)
            ])
        return moves

    def get_image_path(self):
        return "images" + ("" if self.is_white else "/black") + "/bishop.png"

    def get_initial_position(self):
        return QPoint(2, 7) if self.is_white else QPoint(2, 0)