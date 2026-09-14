"""Policy Iteration on the 5x5 maze, then the agent follows the policy."""
from gridworld import Action
from gridworld_maze import COLS, ROWS, START, GridWorld
from policy_iteration import policy_eval, policy_improv

ARROWS = {Action.UP: '^', Action.DOWN: 'v', Action.LEFT: '<', Action.RIGHT: '>'}


def first_action_policy(env):
    return {state: env.get_actions(state)[0]
            for state in env.states if not env.end_of_game(state)}


def solve_policy(env, gamma=0.9):
    values = {state: 0.0 for state in env.states}
    policy = first_action_policy(env)
    while True:
        policy_eval(env, policy, values, gamma)
        if policy_improv(env, policy, values, gamma):
            return policy, values


def run_policy(env, policy, start):
    state = start
    path = [state]
    while not env.end_of_game(state):
        state, reward = env(state, policy[state])
        path.append(state)
    return path


if __name__ == '__main__':
    env = GridWorld()
    policy, values = solve_policy(env)
    for row in range(ROWS):
        print(' '.join(ARROWS.get(policy.get((row, col)), '#')
                       for col in range(COLS)))
    for row in range(ROWS):
        print(' '.join(f'{values[row, col]:.3f}' for col in range(COLS)))
    path = run_policy(env, policy, START)
    print(f'{len(path) - 1} steps: {path}')
