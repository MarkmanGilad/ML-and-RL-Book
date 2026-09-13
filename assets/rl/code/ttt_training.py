"""Shared training interface: one X action and then the random opponent.

Adapted from solved/MC_Trainer.py and SARSA_Trainer.py,
Tic_Tac_Toe_2 commit 36416a995ce68c40e9799a792ef8c45c348ff451.
"""
import random
from ttt_env import State


def sample_step(env, state, action, opponent_rng):
    if state.player != 1:
        raise ValueError('The learner is X')
    after_state, reward = env.next_state(state, action)
    if env.end_of_game(after_state):
        return after_state, reward, True
    opponent_action = opponent_rng.choice(env.get_actions(after_state))
    next_state, reward = env.next_state(after_state, opponent_action)
    return next_state, reward, env.end_of_game(next_state)


def evaluate(env, choose_action, games=1000, seed=100):
    opponent_rng = random.Random(seed)
    results = {'wins': 0, 'losses': 0, 'draws': 0}
    for _ in range(games):
        state = State()
        while not env.end_of_game(state):
            action = choose_action(state)
            state, reward, done = sample_step(
                env, state, action, opponent_rng)
        key = 'wins' if reward == 1 else 'losses' if reward == -1 else 'draws'
        results[key] += 1
    return results
