class ChessPiece:
    def __init__(self, is_white):
        self.is_white = is_white
        self.position = self.get_initial_position()

    def get_possible_moves(self):
        return []

    def get_image_path(self):
        raise NotImplementedError("This method should be overridden in derived classes.")

    def get_initial_position(self):
        raise NotImplementedError("This method should be overridden in derived classes.")