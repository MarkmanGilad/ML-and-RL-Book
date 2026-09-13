"""Book adaptation of the solved PuzzleNumber-AI/AI_Agent.py.

Commit a79bbb81aeb547f10fd7b1c4a967b0d5b80bec08.
All 9! states, in-place sweeps, gamma=.95 and accuracy=.001.
No graphics, delays or per-state debug printing.
"""
from itertools import permutations
from puzzle_env import Puzzle

GAMMA = 0.95
ACCURACY = 0.001


def init_values():
    return {state: 0.0 for state in permutations(range(9))}


def value_iteration(env, values, gamma=GAMMA, accuracy=ACCURACY):
    sweeps = 0
    while True:
        delta = 0.0
        for state, old_value in values.items():
            if state == env.goal:
                continue
            best_value = float('-inf')
            for action in env.get_actions(state):
                next_state, reward = env(state, action)
                candidate = reward + gamma * values[next_state]
                best_value = max(best_value, candidate)
            values[state] = best_value
            delta = max(delta, abs(old_value - best_value))
        sweeps += 1
        if delta < accuracy:
            return sweeps


def get_action(env, state, values, gamma=GAMMA):
    if state == env.goal:
        return None
    best_action = None
    best_value = float('-inf')
    for action in env.get_actions(state):
        next_state, reward = env(state, action)
        candidate = reward + gamma * values[next_state]
        if candidate > best_value:
            best_value = candidate
            best_action = action
    return best_action


def solve(env, start, values):
    state = start
    path = [state]
    seen = {state}
    while state != env.goal:
        action = get_action(env, state, values)
        state, _ = env(state, action)
        if state in seen:
            raise ValueError('No solution from this table and start state')
        seen.add(state)
        path.append(state)
    return path


if __name__ == '__main__':
    env = Puzzle()
    values = init_values()
    sweeps = value_iteration(env, values)
    start = (1, 2, 3, 4, 5, 6, 0, 7, 8)
    path = solve(env, start, values)
    print(f'States: {len(values)}, sweeps: {sweeps}')
    for state in path:
        print(state)
