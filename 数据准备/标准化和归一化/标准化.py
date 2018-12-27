# Standardize time series data
from pandas import Series
from sklearn.preprocessing import StandardScaler
from math import sqrt
# load the dataset and print the first 5 rows
series = Series.from_csv('daily-minimum-temperatures-in-me.csv', header=0)
print(series.head())
# 准备数据
values = series.values
values = values.reshape((len(values), 1))
# 定义标准化模型
scaler = StandardScaler()
scaler = scaler.fit(values)
print('Mean: %f, StandardDeviation: %f' % (scaler.mean_, sqrt(scaler.var_)))
# 开始标准化，打印前五行
normalized = scaler.transform(values)
for i in range(5):
	print(normalized[i])
# 逆标准化数据
inversed = scaler.inverse_transform(normalized)
for i in range(5):
	print(inversed[i])