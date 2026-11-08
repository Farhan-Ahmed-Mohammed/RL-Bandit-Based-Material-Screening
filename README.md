# Reinforcement Learning-Based Material Screening

## 📌 Project Overview

This project demonstrates the application of Reinforcement Learning (RL) in material screening using the **Epsilon-Greedy Multi-Armed Bandit algorithm**.

The agent selects from multiple candidate materials, observes their simulated performance, and gradually learns to identify materials with higher expected rewards.

The project also compares the performance of the RL-based approach against a Random Selection strategy.

## 🎯 Objectives

- Implement an Epsilon-Greedy Multi-Armed Bandit algorithm.
- Simulate the performance of different candidate materials.
- Balance exploration and exploitation during material selection.
- Identify promising materials through repeated testing.
- Compare RL performance against random selection.
- Visualize learning performance using cumulative reward curves.

## 🧠 Algorithm Used

**Epsilon-Greedy Multi-Armed Bandit**

The algorithm uses two strategies:

- **Exploration:** Select a random material to discover its performance.
- **Exploitation:** Select the material with the highest estimated reward.

The exploration probability (epsilon) is set to 0.1.

## ⚙️ Project Configuration

| Parameter | Value |
|---|---|
| Number of materials | 8 |
| Algorithm | Epsilon-Greedy |
| Epsilon | 0.1 |
| Tests per run | 500 |
| Experimental runs | 30 |
| Reward distribution | Gaussian |
| Reward standard deviation | 1.0 |
| Baseline | Random Selection |

## 🛠️ Technologies Used

- Python
- NumPy
- Matplotlib
- Reinforcement Learning
- Multi-Armed Bandits

## 📂 Project Structure

```text
RL-Based-Material-Screening/
│
├── material_screening.py
├── README.md
├── requirements.txt
│
├── results/
│   └── learning_curve.png
│
└── presentation/
    └── RL_Based_Material_Screening_Presentation.pptx
```

## 📊 Results and Visualization

The Epsilon-Greedy agent learns to favor materials with higher expected rewards.

The following graph compares the cumulative rewards obtained by the RL agent and the Random Selection baseline over 500 material tests, averaged across 30 runs.

![Learning Curve](results/learning_curve.png)

The RL-based strategy is expected to achieve higher cumulative rewards because it learns from previous material selections and gradually focuses on promising candidates.

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project directory

```bash
cd RL-Based-Material-Screening
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Execute the Python program

```bash
python material_screening.py
```

The program displays the average cumulative reward comparison between the Epsilon-Greedy agent and Random Selection.

## 📌 Conclusion

This project demonstrates how Reinforcement Learning can support sequential decision-making in material screening.

The Epsilon-Greedy algorithm balances exploration and exploitation, allowing the agent to learn which candidate materials are more promising through repeated interactions.

## ⚠️ Limitations

- Material performance values are simulated rather than experimentally measured.
- Only eight candidate materials are considered.
- The experiment uses a simplified reward model.
- Real-world material screening requires actual experimental data and validation.

## 🔮 Future Scope

- Integrate real-world materials datasets.
- Explore contextual bandit algorithms.
- Compare Epsilon-Greedy with Upper Confidence Bound (UCB).
- Investigate Bayesian optimization for material discovery.

## 📚 Project Information

**Domain:** Reinforcement Learning

**Unit:** Unit 5 – Real-World Reinforcement Learning

**Project:** Bandit-Based Material Screening

**Algorithm:** Epsilon-Greedy Multi-Armed Bandit

**Purpose:** Academic and educational demonstration.
