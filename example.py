import sys
from itertools import tee
from random import shuffle
from solver import Solver
from puzzle import Puzzle

#--------------------------------------------------------------------
# Function Definitions
#--------------------------------------------------------------------

# https://docs.python.org/3/library/itertools.html#itertools-recipes
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

#--------------------------------------------------------------------
# Main
#--------------------------------------------------------------------
width = int(sys.argv[1]) if len(sys.argv) > 1 else 3
board = range(width * width)
shuffle(board)
puzzle = Puzzle(board, width)

print 'Starting position'
print puzzle
print

move_seq = iter(Solver(puzzle).solve())
for sequence in move_seq:
  for from_state, to_state in pairwise(sequence):
    print
    print Puzzle.direction(from_state, to_state)
    print to_state
