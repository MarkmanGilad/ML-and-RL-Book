"""Monte Carlo book training example based on solved/MC_Trainer.py.

Tic_Tac_Toe_2 commit 36416a995ce68c40e9799a792ef8c45c348ff451.
Basic random opponent and exponential epsilon match the slides.
"""
import random
from ttt_env import State, TicTacToe
from tabular_agent import TabularAgent, epsilon_at
from ttt_training import sample_step, evaluate


def generate_episode(env, agent, epsilon, opponent_rng):
    episode = []
    state = State()
    while not env.end_of_game(state):
        action = agent.get_action(state, epsilon)
        next_state, reward, done = sample_step(
            env, state, action, opponent_rng)
        episode.append((state, action, reward))
        state = next_state
    return episode


def update_episode(agent, episode, gamma=0.95, alpha=0.01):
    G = 0.0
    for state, action, reward in reversed(episode):
        G = reward + gamma * G
        old_value = agent.get_Q(state, action)
        agent.Q[(state, action)] = old_value + alpha * (G - old_value)


def train(epochs=200000, seed=0):
    env = TicTacToe()
    agent = TabularAgent(env, seed)
    opponent_rng = random.Random(seed + 1)
    for epoch in range(epochs):
        episode = generate_episode(
            env, agent, epsilon_at(epoch), opponent_rng)
        update_episode(agent, episode)
    return env, agent


if __name__ == '__main__':
    env, agent = train()
    print(f'Q entries: {len(agent.Q)}')
    print(evaluate(env, agent.get_action))
