import matplotlib.pyplot as plt

a = [x**2 for x in range(6)]
plt.plot(a,linewidth = 5)

# 设置标题给坐标轴加标签
plt.title("test",fontsize = 14)
plt.xlabel("Value",fontsize = 24)
plt.ylabel("s of value",fontsize = 14)

# 设置刻度标记的大小
plt.tick_params(axis='both',labelsize = 14)

plt.show()