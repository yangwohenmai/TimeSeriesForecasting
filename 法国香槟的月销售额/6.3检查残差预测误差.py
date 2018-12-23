from pandas import Series
from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot

# 根据给出的步长interval，创建一个差分序列，间隔12个数字相减
def difference(dataset, interval=1):
	diff = list()
	for i in range(interval, len(dataset)):
		value = dataset[i] - dataset[i - interval]
		diff.append(value)
	return diff

# 还原差分值
def inverse_difference(history, yhat, interval=1):
	return yhat + history[-interval]

# load data
series = Series.from_csv('dataset.csv')
# prepare data
X = series.values
X = X.astype('float32')
train_size = int(len(X) * 0.50)
train, test = X[0:train_size], X[train_size:]
# walk-forward validation
history = [x for x in train]
predictions = list()
for i in range(len(test)):
	# difference data
	months_in_year = 12
	# 获得差分剔除季节性后的新序列
	diff = difference(history, months_in_year)
	# predict
	# 用新序列训练模型
	model = ARIMA(diff, order=(0,0,1))
	# 禁用从模型中自动添加趋势常量
	model_fit = model.fit(trend='nc', disp=0)
	# 获取预测结果
	yhat = model_fit.forecast()[0]
	# 将预测后的结果反差分
	yhat = inverse_difference(history, yhat, months_in_year)
	# 保存预测值
	predictions.append(yhat)
	# observation
	obs = test[i]
	history.append(obs)
# errors
# 所有的  （测试值-预测值），获得残差值，
# 对残差值进行分布观测，看是否符合高斯分布，残差均值mean与0的距离，准备下一步的修正
residuals = [test[i]-predictions[i] for i in range(len(test))]
residuals = DataFrame(residuals)
print(residuals.describe())
# plot
pyplot.figure()
pyplot.subplot(211)
residuals.hist(ax=pyplot.gca())
pyplot.subplot(212)
residuals.plot(kind='kde', ax=pyplot.gca())
pyplot.show()