from pandas import read_csv
from matplotlib import pyplot
series = read_csv('daily-minimum-temperatures.csv', header=0)
print(series.head())
series.plot()
pyplot.show()