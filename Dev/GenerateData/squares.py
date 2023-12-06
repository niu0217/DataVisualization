import matplotlib.pyplot as plt


def method1():
    """方法一"""
    input_values = [1, 2, 3, 4, 5]
    suqares = [1, 4, 9, 16, 25]

    plt.style.use('seaborn')  # 设置样式seaborn，可以自己选择
    fig, ax = plt.subplots()
    ax.plot(input_values, suqares, linewidth=3)

    # 设置图标题并给坐标轴加上标签
    ax.set_title("Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)

    # 设置刻度标记的样式
    ax.tick_params(labelsize=14)

    plt.show()


def method2():
    """方法二"""
    x_values = range(1, 1001)
    y_values = [x ** 2 for x in x_values]

    plt.style.use('seaborn')  # 设置样式seaborn，可以自己选择
    fig, ax = plt.subplots()
    ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

    # 设置图标题并给坐标轴加上标签
    ax.set_title("Square Numbers", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Square of Value", fontsize=14)

    # 设置刻度标记的样式
    ax.tick_params(labelsize=14)

    # 设置每个坐标轴的取值范围
    ax.axis([0, 1000, 0, 1_100_000])
    ax.ticklabel_format(style='plain')

    plt.savefig('suqares_plot.png', bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    method2()
