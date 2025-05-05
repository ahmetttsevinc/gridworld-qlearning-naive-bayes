import random
from environment import GridWorld
from qlearning_agent import QLearningAgent

def main():
    size = 4
    win_state = (size-1, size-1)
    # Bloklu durumları rastgele seç
    all_states = [(i, j) for i in range(size) for j in range(size) if (i, j) not in [(0,0), win_state]]
    block_states = random.sample(all_states, 2)
    env = GridWorld(size=size, win_state=win_state, block_states=block_states)
    agent = QLearningAgent(state_space=None, action_space=env.get_valid_actions())

    episodes = 500
    for ep in range(episodes):
        state = env.reset()
        done = False
        while not done:
            action = agent.choose_action(state)
            next_state, reward, done = env.step(action)
            agent.update(state, action, reward, next_state, done)
            state = next_state
        if (ep+1) % 100 == 0:
            print(f"Episode {ep+1} finished.")
    print("Q-table size:", len(agent.q_table))
    print("Block states:", block_states)

if __name__ == "__main__":
    main() 
