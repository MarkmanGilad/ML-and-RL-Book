"""Pedagogical implementation of slides 5.1, 9-11; not a GitHub solution.

V(after_state) stores Q(state, action) under the after-state key.
It includes the reward for the X action creating that after-state.
Thus an X-winning after-state can have value 1; it is not the usual
zero continuation value of a terminal state.
"""
from tabular_agent import TabularAgent
from sarsa_tictactoe import train
from ttt_training import evaluate


class AfterStateAgent(TabularAgent):
    def __init__(self, env, seed=0):
        super().__init__(env, seed)
        self.V = {}

    def get_Q(self, state, action):
        after_state, _ = self.env.next_state(state, action)
        return self.V.get(after_state, 0.0)

    def set_Q(self, state, action, value):
        after_state, _ = self.env.next_state(state, action)
        self.V[after_state] = value


if __name__ == '__main__':
    env, agent = train(agent_type=AfterStateAgent)
    print(f'After-state entries: {len(agent.V)}')
    print(evaluate(env, agent.get_action))
