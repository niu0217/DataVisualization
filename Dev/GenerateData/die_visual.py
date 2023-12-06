import plotly.express as px

from die import Die

# 创建一个die实例
die = Die()

# 掷几次骰子并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequence = results.count(value)
    frequencies.append(frequence)

# 对结果进行可视化
fig = px.bar(x=poss_results, y=frequencies)
fig.show()
