from ClashOfClansEnv import ClashOfClansEnv, plot_map


def main():
    # 创建游戏环境
    env = ClashOfClansEnv(map_size=(50, 50))

    # 添加大本营
    base_x, base_y = 20, 20
    base_width, base_height = 4, 4
    if env.add_building(base_x, base_y, base_width, base_height, building_type=1):
        print("大本营已添加到地图上")
    else:
        print("添加大本营失败，位置非法或有其他建筑物占据")

        # 添加城墙围起大本营
    wall_x, wall_y = base_x - 1, base_y - 1
    wall_width, wall_height = base_width + 2, base_height + 2
    for i in range(wall_width):
        for j in range(wall_height):
            if (i == 0 or i == wall_width - 1 or j == 0 or j == wall_height - 1) and \
                    env.add_building(wall_x + i, wall_y + j, 1, 1, building_type=2):
                print(f"城墙{i + 1}-{j + 1}已添加到地图上")

    # 打印地图局部区域的信息，包含大本营所在的位置
    plot_map(env.map)


if __name__ == "__main__":
    main()
