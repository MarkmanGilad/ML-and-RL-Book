"""Given 4x4 environment for the book; adapted from MarkmanGilad/GridWorld.

Source commit: 6a839da5b2123e2e61e39d7451f7350f2b364541.
No graphics are needed by the learning algorithms.
"""
from enum import IntEnum

ROWS = COLS = 4
START = (0, 0)
GOAL = (ROWS - 1, COLS - 1)
LOSS = (1, 2)
GOAL_REWARD = 1
LOSS_REWARD = -1
STEP_REWARD = 0


class Action(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


class GridWorld:
    def __init__(self):
        self.states = [(r, c) for r in range(ROWS) for c in range(COLS)]
        self.start = START
        self.terminal_rewards = {LOSS: LOSS_REWARD, GOAL: GOAL_REWARD}

    def end_of_game(self, state):
        return state in self.terminal_rewards

    def get_actions(self, state):
        if self.end_of_game(state):
            return []
        # All four actions are legal everywhere; moving into the edge of
        # the board keeps the agent in place (see move).
        return [Action.UP, Action.DOWN, Action.LEFT, Action.RIGHT]

    def move(self, state, action):
        if self.end_of_game(state):
            raise ValueError('No transition from a terminal state')
        if action not in self.get_actions(state):
            raise ValueError('Illegal action')
        dr, dc = {Action.UP: (-1, 0), Action.DOWN: (1, 0),
                  Action.LEFT: (0, -1), Action.RIGHT: (0, 1)}[action]
        next_state = (min(max(state[0] + dr, 0), ROWS - 1),
                      min(max(state[1] + dc, 0), COLS - 1))
        return next_state, self.terminal_rewards.get(next_state, STEP_REWARD)

    __call__ = move
