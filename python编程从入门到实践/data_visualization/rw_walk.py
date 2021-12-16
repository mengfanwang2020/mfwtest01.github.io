import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态 不断模拟随机漫步
while True:
    # 创建一个RandomWalk实例，绘制其包含的点
    rw = RandomWalk(50000)
    rw.fill_walk()

    # plt.scatter(rw.x_values, rw.y_values, s=10)

    # 设置绘图窗口尺寸
    plt.figure(figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, cmap=plt.cm.Blues, c=point_numbers, edgecolors='none', s=1)

    # 突出起点和重点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴
    # plt.axis('off')
    # 隐藏刻度
    plt.xticks([])
    plt.yticks([])

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break