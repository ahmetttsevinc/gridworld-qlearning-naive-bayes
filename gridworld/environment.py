class GridWorld:
    def __init__(self, size=4, win_state=None, block_states=None):
        """
        Initialize the GridWorld environment.
        :param size: Size of the grid (size x size)
        :param win_state: Tuple for the terminal (goal) state
        :param block_states: List of tuples for blocked states
        """
        self.size = size
        self.win_state = win_state or (size-1, size-1)
        self.block_states = block_states or []
        self.reset()

    def reset(self):
        """
        Reset the agent to the starting position (0, 0).
        :return: Starting state
        """
        self.agent_pos = (0, 0)
        return self.agent_pos

    def step(self, action):
        """
        Take an action in the environment.
        :param action: 0=up, 1=down, 2=left, 3=right
        :return: next_state, reward, done
        """
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
            next_pos = self.agent_pos  # Stay if next position is blocked
        self.agent_pos = next_pos
        reward = 1 if self.agent_pos == self.win_state else 0
        done = self.agent_pos == self.win_state
        return self.agent_pos, reward, done

    def get_state(self):
        """
        Get the current state (agent position).
        """
        return self.agent_pos

    def get_valid_actions(self):
        """
        Return the list of valid actions.
        """
        return [0, 1, 2, 3]
