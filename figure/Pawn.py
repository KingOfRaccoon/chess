from PyQt5.QtCore import QPoint

from figure.ChessPiece import ChessPiece


class Pawn(ChessPiece):
    def get_possible_moves(self):
        direction = -1 if self.is_white else 1
        return [QPoint(self.position.x(), self.position.y() + direction)]

    def get_image_path(self):
        return "images" + ("" if self.is_white else "/black") + "/pawn.png"

    def get_initial_position(self):
        return QPoint(0, 6) if self.is_white else QPoint(0, 1)
