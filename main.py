import numpy as np

from BLCTtensorflow import predict_attack_time, attack_simulation

# 定义兵种属性
barbarian = {"name": "野蛮人", "attack": 160, "health": 65}
archer = {"name": "弓箭手", "attack": 68, "health": 28}

# 建筑信息
buildings = [
    # 大本营
    {"name": "大本营", "damage_per_second": 140, "size": (6, 6), "health": 25000, "attack_range": 15,
     "target": "ground_and_air", "attack_preference": "any"},

    # 巨型加农炮
    {"name": "巨型加农炮", "damage_per_second": 80, "size": (2, 2), "health": 3700, "attack_type": "splash",
     "attack_range": 10, "target": "ground", "attack_preference": "any"},

    # 防空火箭
    {"name": "防空火箭", "damage_per_second": 320, "size": (2, 2), "health": 1600, "attack_range": 10,
     "target": "air", "attack_preference": "any"},

    # 超级特斯拉电磁塔
    {"name": "超级特斯拉电磁塔", "damage_per_second": 175, "size": (2, 2), "health": 2000, "attack_range": 6,
     "attack_type": "single_target", "target": "ground_and_air", "attack_preference": "any"},

    # 火箭炮
    {"name": "火箭炮", "damage_per_second": 140, "size": (3, 3), "health": 2400, "attack_type": "splash",
     "attack_range": (3, 12), "target": "ground_and_air", "attack_preference": "any"},

    # 空中炸弹发射器
    {"name": "空中炸弹发射器", "damage_per_second": 250, "size": (2, 2), "health": 2550, "attack_type": "splash",
     "attack_range": 8.5, "target": "air", "attack_preference": "any"},

    # 投矛器
    {"name": "投矛器", "damage_per_second": 130, "size": (2, 2), "health": 1600, "attack_range": 9,
     "target": "ground_and_air", "attack_preference": "any"},

    # 极速火箭
    {"name": "极速火箭", "damage_per_shot": 165, "shots_per_second": 5, "size": (2, 2), "health": 1500,
     "attack_range": 7, "target": "air", "attack_preference": "any"},

    # 撼地巨石
    {"name": "撼地巨石", "damage_per_second": 175, "size": (2, 2), "health": 2550, "attack_type": "splash",
     "attack_range": 1.7, "target": "ground", "attack_preference": "any"},

    # 多管迫击炮
    {"name": "多管迫击炮", "damage_per_shot": 110, "shots_per_attack": 4, "size": (2, 2), "health": 2100,
     "attack_type": "splash", "attack_range": (3, 10), "target": "ground", "attack_preference": "any"},

    # 加农炮
    {"name": "加农炮", "damage_per_second": 170, "size": (2, 2), "health": 1700, "attack_range": 8,
     "target": "ground", "attack_preference": "single_target"},

    # 多管加农炮
    {"name": "多管加农炮", "damage_per_shot": 100, "shots_per_attack": 8, "size": (2, 2), "health": 2300,
     "attack_range": 6, "target": "ground", "attack_preference": "single_target"},

    # 超级法师塔
    {"name": "超级法师塔", "damage_per_second": 70, "size": (2, 2), "health": 2100, "attack_range": 5.5,
     "max_targets": 5, "target": "ground_and_air", "attack_preference": "any"},

    # 炸弹塔
    {"name": "炸弹塔", "damage_per_second": 95, "size": (2, 2), "health": 2500, "attack_type": "splash",
     "attack_range": 5, "target": "ground", "attack_preference": "any"},

    # 城墙
    {"name": "城墙", "health": 6500, "size": (1, 1)},

    # 营房
    {"name": "营房", "health": 800, "size": (3, 3)}
]

# 陷阱信息
traps = [
    # 地雷
    {"name": "地雷", "damage": 160, "size": (1, 1), "trigger_radius": 1.5, "attack_type": "splash",
     "target": "ground"},

    # 巨型地雷
    {"name": "巨型地雷", "damage": 500, "size": (2, 2), "trigger_radius": 2, "attack_type": "splash",
     "target": "ground"}
]



def monte_carlo_simulation(building, num_simulations=100000):
    troops = [barbarian, archer]
    best_troop = None
    min_avg_time_spent = float("inf")

    for troop in troops:
        total_time_spent = 0
        for _ in range(num_simulations):
            building_copy = building.copy()
            time_spent = attack_simulation(building_copy[0], [troop])
            total_time_spent += time_spent
        avg_time_spent = total_time_spent / num_simulations

        if avg_time_spent < min_avg_time_spent:
            min_avg_time_spent = avg_time_spent
            best_troop = troop["name"]

    return best_troop, min_avg_time_spent  # Return both the best troop and its attack times.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # best_troop, best_troop_attack_times = monte_carlo_simulation(buildings, 10)
    # print("最佳进攻兵种是：", best_troop)
    # print("最佳兵种的攻击次数是：", best_troop_attack_times)

    best_troop = None
    min_avg_time_spent = float("inf")
    troops = [barbarian, archer]
    for troop in troops:
        building_copy = buildings.copy()
        time_spent = predict_attack_time(building_copy[0], troop)
        if time_spent < min_avg_time_spent:
            min_avg_time_spent = time_spent
            best_troop = troop["name"]

    print("最佳进攻兵种是：", best_troop)
