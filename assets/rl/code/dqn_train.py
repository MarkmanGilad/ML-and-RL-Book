"""Ordinary DQN, adapted from the slides and Tic_Tac_Toe_DQN.
Source commit: 659c4c8a635c83865334ee09863c061a94580518.

Target selects AND evaluates next actions, without exploration.
Terminal transitions are processed before stopping the episode.
Target synchronization occurs once per C completed episodes.
Requires PyTorch; runtime validation is listed in the book's gap report.
"""
from pathlib import Path
import random
import torch
from ttt_env import State, TicTacToe
from ttt_training import sample_step
from dqn_replay import ReplayBuffer
from dqn_model import DQN
from dqn_agent import DQNAgent, next_q_values

EPOCHS = 30000
C = 1000
BATCH_SIZE = 64
LEARNING_RATE = 0.1
GAMMA = 0.99
WEIGHTS_PATH = Path(__file__).with_name('dqn_weights.pth')


def train(epochs=EPOCHS, seed=0):
    torch.manual_seed(seed)
    env = TicTacToe()
    Q = DQN()
    agent = DQNAgent(env, Q, seed=seed)
    target = DQN()
    target.load_state_dict(Q.state_dict())
    target.eval()
    target.requires_grad_(False)
    replay = ReplayBuffer(seed=seed + 2)
    opponent_rng = random.Random(seed + 1)
    optimizer = torch.optim.SGD(Q.parameters(), lr=LEARNING_RATE)
    loss_function = torch.nn.MSELoss()
    losses = []
    for epoch in range(epochs):
        state = State()
        while not env.end_of_game(state):
            action = agent.get_action(state, epoch)
            next_state, reward, done = sample_step(
                env, state, action, opponent_rng)
            replay.push(state, action, reward, next_state, done)
            if len(replay) >= BATCH_SIZE:
                states, actions, rewards, next_states, dones = replay.sample(BATCH_SIZE)
                predictions = Q(states, actions)
                future_values = next_q_values(target, next_states, dones)
                targets = rewards + GAMMA * future_values * (~dones).float()
                loss = loss_function(predictions, targets)
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()
                losses.append(loss.item())
            state = next_state
        if (epoch + 1) % C == 0:
            target.load_state_dict(Q.state_dict())
    return env, agent, losses


if __name__ == '__main__':
    env, agent, losses = train()
    torch.save(agent.model.state_dict(), WEIGHTS_PATH)
    print(f'Updates: {len(losses)}')
    print(f'Weights saved to {WEIGHTS_PATH}')
