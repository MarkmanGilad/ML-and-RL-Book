"""11 -> 128 -> 64 -> 1 as in the DQN TicTacToe slides and DQN.py.
Tic_Tac_Toe_DQN source commit: 659c4c8a635c83865334ee09863c061a94580518.
CPU-only book example; concatenation is inside forward, not __call__.
"""
import torch
from torch import nn


class DQN(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = nn.Linear(11, 128)
        self.linear2 = nn.Linear(128, 64)
        self.output = nn.Linear(64, 1)

    def forward(self, states, actions):
        x = torch.cat((states, actions), dim=1)
        x = torch.relu(self.linear1(x))
        x = torch.relu(self.linear2(x))
        return self.output(x)
