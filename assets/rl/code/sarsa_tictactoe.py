"""SARSA based on solved/SARSA_Trainer.py, Tic_Tac_Toe_2.

Source commit 36416a995ce68c40e9799a792ef8c45c348ff451.
Shared interface combines the two game turns into one learner step.
"""
import random
from ttt_env import State, TicTacToe
from tabular_agent import TabularAgent, epsilon_at
from ttt_training import sample_step, evaluate


def train(epochs=100000, seed=0, agent_type=TabularAgent):
    env = TicTacToe()
    agent = agent_type(env, seed)
    opponent_rng = random.Random(seed + 1)
    gamma, alpha = 0.9, 0.1
    for epoch in range(epochs):
        epsilon = epsilon_at(epoch)
        state = State()
        action = agent.get_action(state, epsilon)
        while True:
            next_state, reward, done = sample_step(
                env, state, action, opponent_rng)
            if done:
                target = reward
            else:
                next_action = agent.get_action(next_state, epsilon)
                target = reward + gamma * agent.get_Q(next_state, next_action)
            old_value = agent.get_Q(state, action)
            agent.set_Q(state, action, old_value + alpha * (target - old_value))
            if done:
                break
            state, action = next_state, next_action
    return env, agent


if __name__ == '__main__':
    env, agent = train()
    print(f'Q entries: {len(agent.Q)}')
    print(evaluate(env, agent.get_action))
