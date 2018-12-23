from pandas import Series
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf
from matplotlib import pyplot
series = Series.from_csv('stationary.csv')
pyplot.figure()
# 当前子图为两行一列的第一行
pyplot.subplot(211)
# 画出输入序列的ACF图
plot_acf(series, ax=pyplot.gca())
# 当前子图为两行一列的第二行
pyplot.subplot(212)
# 画出输入序列的PACF图
plot_pacf(series, ax=pyplot.gca())
pyplot.show()