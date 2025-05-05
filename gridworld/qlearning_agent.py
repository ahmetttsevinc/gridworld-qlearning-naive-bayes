import random

class QLearningAgent:
    def __init__(self, state_space, action_space, alpha=0.1, gamma=0.9, epsilon=0.2):
        self.state_space = state_space
        self.action_space = action_space
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.q_table = {}

    def get_q(self, state, action):
        return self.q_table.get((state, action), 0.0)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.choice(self.action_space)
        q_values = [self.get_q(state, a) for a in self.action_space]
        max_q = max(q_values)
        actions_with_max_q = [a for a, q in zip(self.action_space, q_values) if q == max_q]
        return random.choice(actions_with_max_q)

    def update(self, state, action, reward, next_state, done):
        max_next_q = max([self.get_q(next_state, a) for a in self.action_space]) if not done else 0.0
        old_q = self.get_q(state, action)
        new_q = old_q + self.alpha * (reward + self.gamma * max_next_q - old_q)
        self.q_table[(state, action)] = new_q 
