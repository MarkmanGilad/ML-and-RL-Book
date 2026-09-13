"""Legal-action epsilon-greedy agent, adapted from DQN_Agent.py.
Tic_Tac_Toe_DQN commit: 659c4c8a635c83865334ee09863c061a94580518.
"""
import random
import torch
from tabular_agent import epsilon_at


class DQNAgent:
    def __init__(self, env, model, seed=0, training=True):
        self.env = env
        self.model = model
        self.rng = random.Random(seed)
        self.set_training(training)

    def set_training(self, enabled):
        self.training = enabled
        self.model.train(enabled)

    def get_action(self, state, epoch=0):
        actions = self.env.get_actions(state)
        if not actions:
            raise ValueError('No action in a terminal state')
        epsilon = epsilon_at(epoch, decay=5000) if self.training else 0.0
        if self.rng.random() < epsilon:
            return self.rng.choice(actions)
        states = torch.tensor(state.board, dtype=torch.float32)
        states = states.reshape(1, 9).repeat(len(actions), 1)
        action_tensor = torch.tensor(actions, dtype=torch.float32)
        with torch.no_grad():
            values = self.model(states, action_tensor).flatten()
        return actions[values.argmax().item()]


def next_q_values(target, next_states, dones):
    """Ordinary DQN: target both selects and evaluates legal actions."""
    values = torch.zeros((len(next_states), 1), dtype=torch.float32)
    with torch.no_grad():
        for i, board in enumerate(next_states):
            if dones[i].item():
                continue
            actions = (board.reshape(3, 3) == 0).nonzero().float()
            states = board.reshape(1, 9).repeat(len(actions), 1)
            values[i, 0] = target(states, actions).max()
    return values
