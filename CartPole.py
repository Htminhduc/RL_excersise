import gym
import time

# Initialize the CartPole environment
env = gym.make("CartPole-v1", render_mode="human")

# Reset the environment to the initial state
state = env.reset()

# Number of steps you want to run the environment for
n_steps = 1000

# Loop through the steps
for step in range(n_steps):
    # Render the environment (optional)
    env.render()

    # Take a random action from the action space
    action = env.action_space.sample()

    # Apply the action and get the new state, reward, done, truncated, info
    next_state, reward, done, truncated, info = env.step(action)

    # If the environment returns done or truncated, the episode is finished
    if done or truncated:
        print(f"Episode finished after {step + 1} timesteps")
        break

    # Slow down the rendering to make it visible
    time.sleep(0.05)

# Close the environment
env.close()
