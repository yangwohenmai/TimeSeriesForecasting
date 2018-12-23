from pandas import Series
from sklearn.metrics import mean_squared_error
from statsmodels.tsa.arima_model import ARIMA
from math import sqrt

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
	# 用新序列训练模型
	model = ARIMA(diff, order=(1,1,1))
	# 禁用从模型中自动添加趋势常量
	model_fit = model.fit(trend='nc', disp=0)
	# 获取预测结果
	yhat = model_fit.forecast()[0]
	# 将预测后的结果反差分
	yhat = inverse_difference(history, yhat, months_in_year)
	# 保存预测值
	predictions.append(yhat)
	# 获取真实值
	obs = test[i]
	history.append(obs)
	# 对比预测结果
	print('>Predicted=%.3f, Expected=%3.f' % (yhat, obs))
# 获取误差分析报告
mse = mean_squared_error(test, predictions)
rmse = sqrt(mse)
print('RMSE: %.3f' % rmse)