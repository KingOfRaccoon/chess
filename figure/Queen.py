from PyQt5.QtCore import QPoint

from figure.ChessPiece import ChessPiece


class Queen(ChessPiece):
    def get_possible_moves(self):
        moves = []

        for i in range(1, 8):
            moves.extend([
                QPoint(self.position.x() + i, self.position.y() + i),
                QPoint(self.position.x() - i, self.position.y() - i),
                QPoint(self.position.x() + i, self.position.y() - i),
                QPoint(self.position.x() - i, self.position.y() + i),
                QPoint(self.position.x() + i, self.position.y()),
                QPoint(self.position.x() - i, self.position.y()),
                QPoint(self.position.x(), self.position.y() + i),
                QPoint(self.position.x(), self.position.y() - i)
            ])
        filterMoves = filter(lambda it: 0 <= it.x() < 8 and 0 <= it.y() < 8, moves)
        return list(filterMoves)

    def get_image_path(self):
        return "images" + ("" if self.is_white else "/black") + "/queen.png"

    def get_initial_position(self):
        return QPoint(3, 7) if self.is_white else QPoint(3, 0)