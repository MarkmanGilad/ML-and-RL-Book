"""Policy Iteration on the given 4x4 GridWorld interface.

Adapted from MarkmanGilad/GridWorld, commit
6a839da5b2123e2e61e39d7451f7350f2b364541.
"""
from gridworld import Action, COLS, GOAL, ROWS, GridWorld


def initial_policy(env):
    policy = {}
    for state in env.states:
        if env.end_of_game(state):
            continue
        action = Action.DOWN
        if state == (GOAL[0], GOAL[1] - 1):
            action = Action.RIGHT
        policy[state] = action
    return policy


def policy_eval(env, policy, values, gamma=0.9, accuracy=0.0001):
    while True:
        delta = 0
        for state in env.states:
            if env.end_of_game(state):
                continue
            old_value = values[state]
            action = policy[state]
            next_state, reward = env(state, action)
            values[state] = reward + gamma * values[next_state]
            delta = max(delta, abs(old_value - values[state]))
        if delta < accuracy:
            return


def policy_improv(env, policy, values, gamma=0.9):
    stable = True
    for state in env.states:
        if env.end_of_game(state):
            continue
        old_action = policy[state]
        best_action = old_action
        next_state, reward = env(state, old_action)
        best_value = reward + gamma * values[next_state]
        for action in env.get_actions(state):
            next_state, reward = env(state, action)
            candidate = reward + gamma * values[next_state]
            if candidate > best_value + 1e-12:
                best_value = candidate
                best_action = action
        policy[state] = best_action
        if best_action != old_action:
            stable = False
    return stable


def policy_iteration(env, gamma=0.9):
    values = {state: 0.0 for state in env.states}
    policy = initial_policy(env)
    while True:
        policy_eval(env, policy, values, gamma)
        if policy_improv(env, policy, values, gamma):
            return policy, values


if __name__ == '__main__':
    env = GridWorld()
    policy, values = policy_iteration(env)
    for row in range(ROWS):
        print(' '.join(f'{values[row, col]:.3f}' for col in range(COLS)))
