"""Given TicTacToe interface, without graphics or third-party dependencies.

Adapted from MarkmanGilad/Tic_Tac_Toe_2, solved,
commit 36416a995ce68c40e9799a792ef8c45c348ff451.
The immutable board is flattened; actions remain (row, col).
Rewards always use X's perspective: win=1, loss=-1, draw=0.
"""
from dataclasses import dataclass


@dataclass(frozen=True, eq=False)
class State:
    board: tuple = (0,) * 9
    player: int = 1
    end_of_game: int = 0

    def __hash__(self):
        return hash((self.board, self.player))

    def __eq__(self, other):
        if not isinstance(other, State):
            return NotImplemented
        return self.board == other.board and self.player == other.player

    def copy(self):
        return State(self.board, self.player, self.end_of_game)


class TicTacToe:
    def end_of_game(self, state):
        return state.end_of_game != 0

    def get_actions(self, state):
        if self.end_of_game(state):
            return []
        return [divmod(i, 3) for i, value in enumerate(state.board)
                if value == 0]

    def next_state(self, state, action):
        if action not in self.get_actions(state):
            raise ValueError('Illegal action or terminal state')
        row, col = action
        board = list(state.board)
        board[3 * row + col] = state.player
        lines = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                 (0, 3, 6), (1, 4, 7), (2, 5, 8),
                 (0, 4, 8), (2, 4, 6))
        result = 0
        for a, b, c in lines:
            if board[a] != 0 and board[a] == board[b] == board[c]:
                result = board[a]
                break
        if result == 0 and 0 not in board:
            result = 2
        next_state = State(tuple(board), -state.player, result)
        reward = 0 if result == 2 else result
        return next_state, reward
