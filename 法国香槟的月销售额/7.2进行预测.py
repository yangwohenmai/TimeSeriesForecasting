from pandas import Series
from statsmodels.tsa.arima_model import ARIMAResults
import numpy

# invert differenced value
def inverse_difference(history, yhat, interval=1):
	return yhat + history[-interval]

series = Series.from_csv('dataset.csv')
months_in_year = 12
# 加载之前保存的模型参数文件
model_fit = ARIMAResults.load('model.pkl')
# 加载误差值
bias = numpy.load('model_bias.npy')
yhat = float(model_fit.forecast()[0])
# 预测结果加上误差值作为新的预测结果
yhat = bias + inverse_difference(series.values, yhat, months_in_year)
print('Predicted: %.3f' % yhat)