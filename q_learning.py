import numpy as np

# Q-learning算法函数
def q_learning(env, num_episodes, learning_rate, discount_factor, epsilon):
    # 初始化Q值表为0
    Q = np.zeros((env.observation_space.n, env.action_space.n))

    for episode in range(num_episodes):
        state = env.reset()
        done = False

        while not done:
            # ε-贪婪策略选择动作
            if np.random.uniform(0, 1) < epsilon:
                action = env.action_space.sample()  # 随机选择动作
            else:
                action = np.argmax(Q[state, :])  # 选择具有最大Q值的动作

            next_state, reward, done, _ = env.step(action)

            # 使用Bellman方程更新Q值表
            Q[state, action] = Q[state, action] + learning_rate * (reward + discount_factor * np.max(Q[next_state, :]) - Q[state, action])

            state = next_state

    return Q
