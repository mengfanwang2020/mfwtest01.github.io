import matplotlib.pyplot as plt

# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
#
# # 使用linewidth设置曲线粗细
# plt.plot(input_values, squares, linewidth=5)
#
# # 设置图表标题 并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # 设置刻度标记大小
# plt.tick_params(axis='both', labelsize=14)
#
# plt.show()


# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]
# plt.scatter(input_values, squares, s=100)
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # 设置刻度标记大小
# plt.tick_params(axis='both', which='major', labelsize=14)
# plt.show()


input_values = list(range(1, 101))
squares = [x**2 for x in input_values]
plt.scatter(input_values, squares, c=(0, 0, 0.8), edgecolors='none', s=4)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置每个坐标轴取值范围
plt.axis([0, 110, 0, 11000])

plt.savefig('squares_plot.png', bbox_inches='tight')