import matplotlib.pyplot as plt

# plt.scatter(2,4)

a = range(1000)
b = [x ** 2 for x in a]
# 点的轮廓颜色去掉
# plt.scatter(a,b,s = 5,c='red',edgecolor = 'none')
plt.scatter(a, b, s=5, c=b, edgecolor='none', cmap=plt.cm.Blues)
plt.ylabel("Y", fontsize=14)
plt.xlabel("X", fontsize=14)
plt.title("use scatter", fontsize=14)

# 设置x轴和y轴的坐标范围
plt.axes([0, 1100, 0, 1100000])

plt.tick_params(axis='both', labelsize=14, which='major')

# plt.show()
plt.savefig('use_scatter.png')
