from pandas import Series
from pandas import DataFrame
from pandas import concat
series = Series.from_csv('daily-minimum-temperatures-in-me.csv', header=0)
temps = DataFrame(series.values)
width = 2
shifted = temps.shift(width - 1)
print(shifted.head(12))
# 向上统计的步长
window = shifted.rolling(window=4)
# 分别取过去四天的最小值，均值，最大值
dataframe = concat([window.min(), window.mean(), window.max(), temps], axis=1)
dataframe.columns = ['min', 'mean', 'max', 't+1']
print(dataframe.head(15))