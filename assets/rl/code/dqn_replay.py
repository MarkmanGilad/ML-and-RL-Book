"""Five-field replay, adapted from Tic_Tac_Toe_DQN/ReplayBuffer.py.
Source commit: 659c4c8a635c83865334ee09863c061a94580518.
"""
from collections import deque
import random
import torch


class ReplayBuffer:
    def __init__(self, capacity=10000, seed=2):
        self.buffer = deque(maxlen=capacity)
        self.rng = random.Random(seed)

    def push(self, state, action, reward, next_state, done):
        self.buffer.append((
            torch.tensor(state.board, dtype=torch.float32).reshape(1, 9),
            torch.tensor(action, dtype=torch.float32).reshape(1, 2),
            torch.tensor([[reward]], dtype=torch.float32),
            torch.tensor(next_state.board, dtype=torch.float32).reshape(1, 9),
            torch.tensor([[done]], dtype=torch.bool)))

    def sample(self, batch_size):
        batch = self.rng.sample(list(self.buffer), batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)
        return (torch.vstack(states), torch.vstack(actions),
                torch.vstack(rewards), torch.vstack(next_states),
                torch.vstack(dones))

    def __len__(self):
        return len(self.buffer)
