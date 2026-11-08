
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# 1. Environment Setup
# -------------------------------

np.random.seed(42)

num_materials = 8
total_steps = 500
num_runs = 30
epsilon = 0.1

# Unknown true performance of each material
true_rewards = np.array([
    2.0, 3.5, 5.0, 4.0,
    7.5, 6.0, 3.0, 8.5
])

# -------------------------------
# 2. Epsilon-Greedy RL Agent
# -------------------------------

def epsilon_greedy():
    Q = np.zeros(num_materials)
    counts = np.zeros(num_materials)

    rewards = []

    for step in range(total_steps):

        # Exploration or exploitation
        if np.random.random() < epsilon:
            action = np.random.randint(num_materials)
        else:
            action = np.argmax(Q)

        # Test selected material
        reward = np.random.normal(
            true_rewards[action], 1.0
        )

        # Update estimated reward
        counts[action] += 1

        Q[action] += (
            reward - Q[action]
        ) / counts[action]

        rewards.append(reward)

    return np.cumsum(rewards)


# -------------------------------
# 3. Random Selection Baseline
# -------------------------------

def random_selection():

    rewards = []

    for step in range(total_steps):

        action = np.random.randint(num_materials)

        reward = np.random.normal(
            true_rewards[action], 1.0
        )

        rewards.append(reward)

    return np.cumsum(rewards)


# -------------------------------
# 4. Run Experiments
# -------------------------------

rl_results = []
random_results = []

for run in range(num_runs):

    rl_results.append(epsilon_greedy())
    random_results.append(random_selection())

rl_results = np.array(rl_results)
random_results = np.array(random_results)

# Average cumulative rewards
avg_rl = np.mean(rl_results, axis=0)
avg_random = np.mean(random_results, axis=0)


# -------------------------------
# 5. Display Results
# -------------------------------

print("Best Material:",
      np.argmax(true_rewards) + 1)

print("Best Material Performance:",
      np.max(true_rewards))

print("RL Average Final Reward:",
      round(np.mean(rl_results[:, -1]), 2))

print("Random Average Final Reward:",
      round(np.mean(random_results[:, -1]), 2))


# -------------------------------
# 6. Plot Learning Curves
# -------------------------------

plt.figure(figsize=(10, 6))

plt.plot(avg_rl, label="Epsilon-Greedy RL")
plt.plot(avg_random, label="Random Selection")

plt.xlabel("Number of Material Tests")
plt.ylabel("Cumulative Reward")

plt.title("RL-Based Material Screening")

plt.legend()
plt.grid(True)

plt.show()
