from  die import Die
import pygal

# 绘制模拟掷骰子图 直方图

die = Die()
die1 = Die(10)

results = []

for i in range(1000):
    r = die.roll()
    r1 = die1.roll()
    results.append(r + r1)

# print(results)
# 分析每个点数出现的次数
frequencies = {}
max_result = die.num_sides + die1.num_sides
for x in range(2, max_result + 1):
    r = results.count(x)
    frequencies[str(x)] = r

print(frequencies)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [str(x) for x in range(2, max_result + 1)]
hist.x_title = "result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
