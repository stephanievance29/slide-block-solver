import sys
from moveSequence import MoveSequence
from collections import deque

class Solver:
    """
    An '8-puzzle' solver
    - 'start' is a Puzzle instance
    """
    def __init__(self, start):
        self.start = start

    def solve(self):
        """
        Perform breadth-first search and return a MoveSequence of the solution,
        if it exists
        """
        queue = deque([MoveSequence(self.start)])
        if not queue:
          print 'No possible solution'
          sys.exit()

        seen  = set([self.start])
        if self.start.solved:
            return queue.pop()

        for seq in iter(queue.pop, None):
            for destination in seq.last.possible_moves:
                attempt = seq.branch(destination)
                if attempt.last not in seen:
                    seen.add(attempt.last)
                    queue.appendleft(attempt)
                    if attempt.last.solved:
                        return attempt

            if not queue:
              print 'No possible solution'
              sys.exit()
