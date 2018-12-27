from pandas import Series
from matplotlib import pyplot
series = Series.from_csv('daily-minimum-temperatures-in-me.csv', header=0)
series.hist()
# 看看画出的数据图是否符合高斯钟型分布
pyplot.show()