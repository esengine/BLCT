import numpy as np
import matplotlib.pyplot as plt


class ClashOfClansEnv:
    def __init__(self, map_size=(50, 50)):
        self.map_size = map_size
        self.map = np.zeros(map_size, dtype=np.int32)

    def is_valid_position(self, x, y, width, height):
        # 检查位置是否合法，没有其他建筑物占据
        for i in range(width):
            for j in range(height):
                if x + i >= self.map_size[0] or y + j >= self.map_size[1] or self.map[x + i, y + j] != 0:
                    return False
        return True

    def add_building(self, x, y, width, height, building_type):
        # 添加建筑物到地图上
        if self.is_valid_position(x, y, width, height):
            for i in range(width):
                for j in range(height):
                    self.map[x + i, y + j] = building_type
            return True
        else:
            return False


def plot_map(map_data):
    # 自定义颜色映射，0表示没有建筑，1表示大本营，2表示城墙
    cmap = plt.cm.colors.ListedColormap(['white', 'red', 'blue'])

    plt.imshow(map_data, cmap=cmap, vmin=0, vmax=2)
    plt.colorbar(ticks=[0, 1, 2], format='%d', label='Building Type')
    plt.title('Clash of Clans Map')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
