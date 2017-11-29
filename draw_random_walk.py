from random_walk import RandomWalk
import matplotlib.pyplot as plt

while True:

    rw = RandomWalk(10000)
    rw.fill_walk()

    # 设置屏幕的尺寸
    plt.figure(figsize=(10, 6))

    plt.scatter(rw.x_values, rw.y_values, s=2, c=list(range(rw.num_points)), edgecolors='none', cmap=plt.cm.Blues)

    # 突出起点和终点
    plt.scatter(0, 0, s=20, c='green', edgecolors='none')
    plt.scatter(rw.x_values[-1], rw.y_values[-1], s=20, c='red', edgecolors='none')

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()

    tag = input("continue?y/n:")
    if tag == 'n':
        break
