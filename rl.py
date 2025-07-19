import gymnasium as gym
# Create the environment
env = gym.make('LunarLander-v3')  # continuous: LunarLanderContinuous-v2

# required before you can step the environment
env.reset()

# sample action:
print("sample action shape:", env.action_space.shape)

# observation space shape:
print("observation space shape:", env.observation_space.shape)
env.close()