"""Given, graphics-free puzzle interface for the book.

Adapted from MarkmanGilad/PuzzleNumber-AI, Puzzle_Number_AI_solved,
commit a79bbb81aeb547f10fd7b1c4a967b0d5b80bec08.
Tuple states replace State/NumPy objects; actions move the blank.
"""
from enum import IntEnum


class Action(IntEnum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3


class Puzzle:
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    def get_actions(self, state):
        row, col = divmod(state.index(0), 3)
        return [a for a, legal in ((Action.DOWN, row < 2),
                                   (Action.RIGHT, col < 2),
                                   (Action.UP, row > 0),
                                   (Action.LEFT, col > 0)) if legal]

    def __call__(self, state, action):
        if action not in self.get_actions(state):
            raise ValueError('Illegal action')
        blank = state.index(0)
        offset = {Action.UP: -3, Action.DOWN: 3,
                  Action.RIGHT: 1, Action.LEFT: -1}[action]
        board = list(state)
        target = blank + offset
        board[blank], board[target] = board[target], board[blank]
        next_state = tuple(board)
        return next_state, int(next_state == self.goal)
