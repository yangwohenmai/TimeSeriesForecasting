# Normalize time series data
from pandas import Series
from sklearn.preprocessing import MinMaxScaler
# load the dataset and print the first 5 rows
series = Series.from_csv('daily-minimum-temperatures-in-me.csv', header=0)
print(series.head())
# 准备归一化数据
values = series.values
values = values.reshape((len(values), 1))
# 定义缩放范围(0,1)
scaler = MinMaxScaler(feature_range=(0, 1))
scaler = scaler.fit(values)
print('Min: %f, Max: %f' % (scaler.data_min_, scaler.data_max_))
# 归一化数据集并打印前5行
normalized = scaler.transform(values)
for i in range(5):
	print(normalized[i])
# 逆变换并打印前5行
inversed = scaler.inverse_transform(normalized)
for i in range(5):
	print(inversed[i])