import gym
import random
import numpy as np
import torch

from collections import deque

from ClashOfClansEnv import ClashOfClansEnv, plot_map
from DQN import DQN
from ReplayBuffer import ReplayBuffer
from dqn_train import dqn_train, select_action


def main():
    # 创建游戏环境
    env = ClashOfClansEnv(map_size=(50, 50))

    # 添加大本营
    base_x, base_y = 20, 20
    base_width, base_height = 4, 4
    base_hp = 450
    if env.add_building(base_x, base_y, base_width, base_height, building_type=1):
        print("大本营已添加到地图上")
    else:
        print("添加大本营失败，位置非法或有其他建筑物占据")

    # 打印地图局部区域的信息，包含大本营所在的位置
    plot_map(env.map)


if __name__ == "__main__":
    main()
