from pandas import Series
from pandas import DataFrame
from pandas import concat
from matplotlib import pyplot
series = Series.from_csv('daily-minimum-temperatures.csv', header=0)
values = DataFrame(series.values)
dataframe = concat([values.shift(1), values], axis=1)
"""
         0
0     20.7
1     17.9
2     18.8
3     14.6
4     15.8
5     15.8
6     15.8
7     17.4
8     21.8
9     20.0
10    16.2
11    13.3
12    16.7
13    21.5
14    25.0
15    20.7
16    20.6
17    24.8
"""
print(values)
"""
         0
0      NaN
1     20.7
2     17.9
3     18.8
4     14.6
5     15.8
6     15.8
7     15.8
8     17.4
9     21.8
10    20.0
11    16.2
12    13.3
13    16.7
14    21.5
15    25.0
16    20.7
17    20.6
"""
print(values.shift(1))
"""
         0     0
0      NaN  20.7
1     20.7  17.9
2     17.9  18.8
3     18.8  14.6
4     14.6  15.8
5     15.8  15.8
6     15.8  15.8
7     15.8  17.4
8     17.4  21.8
9     21.8  20.0
10    20.0  16.2
11    16.2  13.3
12    13.3  16.7
13    16.7  21.5
14    21.5  25.0
15    25.0  20.7
16    20.7  20.6
17    20.6  24.8
"""
print(dataframe)
dataframe.columns = ['t-1', 't+1']
# -1（负相关）和+1（正相关）之间的相关性，其中小值接近零表示低相关性，高值高于0.5或低于-0.5表示高相关性
result = dataframe.corr()
print(result)