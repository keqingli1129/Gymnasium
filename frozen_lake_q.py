import gymnasium as gym

def run():
    # Create the environment
    env = gym.make('FrozenLake-v1', map_name="8x8", is_slippery=True, render_mode="human")
    state = env.reset()
    terminated = False
    truncated = False
    while not terminated and not truncated:
        action = env.action_space.sample()
        new_state, reward, terminated, truncated, _ = env.step(action)
        state = new_state
        env.render()
    env.close()
    return state

if __name__ == "__main__":
    final_state = run()