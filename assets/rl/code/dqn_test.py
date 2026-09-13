"""Evaluate saved book DQN weights in 1000 games against random O."""
import torch
from ttt_env import TicTacToe
from ttt_training import evaluate
from dqn_model import DQN
from dqn_agent import DQNAgent
from dqn_train import WEIGHTS_PATH


def test(path=WEIGHTS_PATH, games=1000, seed=100):
    env = TicTacToe()
    model = DQN()
    model.load_state_dict(torch.load(path, map_location='cpu', weights_only=True))
    agent = DQNAgent(env, model, training=False)
    return evaluate(env, agent.get_action, games=games, seed=seed)


if __name__ == '__main__':
    print(test())
