import random

import torch
import torch.nn as nn
from torch import optim

def dqn_train(env, q_network, target_network, replay_buffer, num_episodes, batch_size, learning_rate, discount_factor, target_update_frequency):
    optimizer = optim.Adam(q_network.parameters(), lr=learning_rate)
    criterion = nn.MSELoss()

    for episode in range(num_episodes):
        state = env.reset()
        done = False

        while not done:
            # 选择动作
            action = select_action(state, q_network, env.action_space.n)

            next_state, reward, done, _ = env.step(action)

            # 将经验存储在经验回放缓冲区中
            replay_buffer.add((state, action, reward, next_state, done))

            # 从经验回放缓冲区中随机抽取批量数据
            batch = replay_buffer.sample(batch_size)
            states, actions, rewards, next_states, dones = zip(*batch)

            states = torch.tensor(states, dtype=torch.float32)
            actions = torch.tensor(actions, dtype=torch.int64).view(-1, 1)
            rewards = torch.tensor(rewards, dtype=torch.float32).view(-1, 1)
            next_states = torch.tensor(next_states, dtype=torch.float32)
            dones = torch.tensor(dones, dtype=torch.float32).view(-1, 1)

            # 计算Q值和目标Q值
            q_values = q_network(states).gather(1, actions)
            next_q_values = target_network(next_states).detach()
            max_next_q_values = next_q_values.max(1)[0].view(-1, 1)
            target_q_values = rewards + discount_factor * max_next_q_values * (1 - dones)

            # 计算损失并更新网络
            loss = criterion(q_values, target_q_values)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            state = next_state

        # 更新目标网络
        if episode % target_update_frequency == 0:
            target_network.load_state_dict(q_network.state_dict())

def select_action(state, q_network, num_actions, epsilon=0.1):
    if random.random() < epsilon:
        return random.randint(0, num_actions - 1)
    else:
        with torch.no_grad():
            state = torch.tensor(state, dtype=torch.float32)
            q_values = q_network(state)
            return q_values.argmax().item()
