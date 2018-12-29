# create expanding window features
from pandas import Series
from pandas import DataFrame
from pandas import concat
series = Series.from_csv('daily-minimum-temperatures-in-me.csv', header=0)
print(series.head(15))
temps = DataFrame(series.values)
# 使用expanding方法，对先前所有值进行统计
window = temps.expanding()
dataframe = concat([window.min(), window.mean(), window.max(), temps.shift(0)], axis=1)
dataframe.columns = ['min', 'mean', 'max', 't+1']
print(dataframe.head(15))