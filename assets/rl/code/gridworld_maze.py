"""5x5 maze environment with the same interface as gridworld.py.

The board is the 5x5 maze from MarkmanGilad/GridWorld (Environement.py,
commit 6a839da5b2123e2e61e39d7451f7350f2b364541): eight -1 cells act as
walls, the goal is the bottom-right cell.
"""
from gridworld import Action

ROWS = COLS = 5
START = (0, 0)
GOAL = (4, 4)
WALLS = [(1, 0), (1, 1), (1, 2), (1, 4),
         (3, 1), (3, 2), (3, 3), (3, 4)]
GOAL_REWARD = 1
WALL_REWARD = -1
STEP_REWARD = 0


class GridWorld:
    def __init__(self):
        self.states = [(r, c) for r in range(ROWS) for c in range(COLS)]
        self.start = START
        self.terminal_rewards = {wall: WALL_REWARD for wall in WALLS}
        self.terminal_rewards[GOAL] = GOAL_REWARD

    def end_of_game(self, state):
        return state in self.terminal_rewards

    def get_actions(self, state):
        if self.end_of_game(state):
            return []
        r, c = state
        return [a for a, valid in ((Action.UP, r > 0),
                                   (Action.DOWN, r < ROWS - 1),
                                   (Action.LEFT, c > 0),
                                   (Action.RIGHT, c < COLS - 1)) if valid]

    def move(self, state, action):
        if self.end_of_game(state):
            raise ValueError('No transition from a terminal state')
        if action not in self.get_actions(state):
            raise ValueError('Illegal action')
        dr, dc = {Action.UP: (-1, 0), Action.DOWN: (1, 0),
                  Action.LEFT: (0, -1), Action.RIGHT: (0, 1)}[action]
        next_state = (state[0] + dr, state[1] + dc)
        return next_state, self.terminal_rewards.get(next_state, STEP_REWARD)

    __call__ = move
