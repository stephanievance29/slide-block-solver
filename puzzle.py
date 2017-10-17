class Puzzle:
    empty_space = 0

    """
    A class representing an '8-puzzle'.
    - 'board' is a list of integer entries 0...width^2 - 1
    """
    def __init__(self, board, width, empty_space_location=None):

        # Set class attributes
        self.board = board
        self.width = width
        self.empty_space = empty_space_location if empty_space_location is not None else self.board.index(Puzzle.empty_space)

    @property
    def solved(self):
        """
        The puzzle is solved if the board's numbers are in increasing
        order from left to right and the '0' tile is in the last
        position on the board
        """
        return self.board == list(range(1, self.width * self.width)) + [Puzzle.empty_space]

    @property
    def possible_moves(self):
        """
        A generator for the possible moves for the empty space
        Possibilities: -1 (left), +1 (right), -width (up), or +width (down)
        """
        # Up, down
        for dest in (self.empty_space - self.width, self.empty_space + self.width):
            if 0 <= dest < len(self.board):
                yield dest

        # Left, right
        for dest in (self.empty_space - 1, self.empty_space + 1):
            if dest // self.width == self.empty_space // self.width:
                yield dest

    def move(self, destination):
        """
        Move the empty space to the specified index.
        """
        board = self.board[:]
        board[self.empty_space], board[destination] = board[destination], board[self.empty_space]
        return Puzzle(board, self.width, destination)

    @staticmethod
    def direction(start, end):
        """
        The direction of the movement of the empty_space (L, R, U, or D)
        from start position to end position.
        """
        if start is None:
            return None

        return {-start.width: 'U',
                -1: 'L',
                 0: None,
                 +1: 'R',
                 +start.width: 'D'
               }[end.empty_space - start.empty_space]

    def __str__(self):
        return "\n".join(str(self.board[start : start + self.width])
                         for start in range(0, len(self.board), self.width))

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        h = 0
        for value, i in enumerate(self.board):
            h ^= value << i
        return h
