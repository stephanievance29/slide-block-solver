class MoveSequence:
    """
    Represents the successive states of a puzzle taken to reach an end state.
    """
    def __init__(self, last, prev_empty_spaces=None):
        self.last = last
        self.prev_empty_spaces = prev_empty_spaces or []

    def branch(self, destination):
        """
        Makes a MoveSequence with the same history followed by a move of
        the empty space to the specified destination index.
        """
        return MoveSequence(self.last.move(destination),
                            self.prev_empty_spaces + [self.last.empty_space])

    def __iter__(self):
        """
        Generator of puzzle states, starting with the initial configuration
        """
        states = [self.last]
        for empty_space in reversed(self.prev_empty_spaces):
            states.append(states[-1].move(empty_space))
        yield reversed(states)
