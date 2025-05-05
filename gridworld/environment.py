class GridWorld:
    def __init__(self, size=4, win_state=None, block_states=None):
        self.size = size
        self.win_state = win_state or (size-1, size-1)
        self.block_states = block_states or []
        self.reset()

    def reset(self):
        self.agent_pos = (0, 0)
        return self.agent_pos

    def step(self, action):
        # Hareket: 0=up, 1=down, 2=left, 3=right
        x, y = self.agent_pos
        if action == 0 and x > 0:
            x -= 1
        elif action == 1 and x < self.size - 1:
            x += 1
        elif action == 2 and y > 0:
            y -= 1
        elif action == 3 and y < self.size - 1:
            y += 1
        next_pos = (x, y)
        if next_pos in self.block_states:
            next_pos = self.agent_pos  # Blokluysa hareket etme
        self.agent_pos = next_pos
        reward = 1 if self.agent_pos == self.win_state else 0
        done = self.agent_pos == self.win_state
        return self.agent_pos, reward, done

    def get_state(self):
        return self.agent_pos

    def get_valid_actions(self):
        return [0, 1, 2, 3] 
