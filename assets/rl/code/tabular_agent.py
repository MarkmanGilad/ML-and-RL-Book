"""Book adaptation of solved/AI_Agent.py; exponential slide epsilon."""
import math
import random


def epsilon_at(epoch, start=1.0, final=0.01, decay=100000):
    return final + (start - final) * math.exp(-epoch / decay)


class TabularAgent:
    def __init__(self, env, seed=0):
        self.env = env
        self.Q = {}
        self.rng = random.Random(seed)

    def get_Q(self, state, action):
        return self.Q.get((state, action), 0.0)

    def set_Q(self, state, action, value):
        self.Q[(state, action)] = value

    def get_action(self, state, epsilon=0.0):
        actions = self.env.get_actions(state)
        if self.rng.random() < epsilon:
            return self.rng.choice(actions)
        return max(actions, key=lambda a: self.get_Q(state, a))
