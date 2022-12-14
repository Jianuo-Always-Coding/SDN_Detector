import pandas as pd # 导入另一个包“pandas” 命名为 pd，理解成pandas是在 numpy 基础上的升级包
import numpy as np #导入一个数据分析用的包“numpy” 命名为 np
import matplotlib.pyplot as plt # 导入 matplotlib 命名为 plt，类似 matlab，集成了许多可视化命令

#jupyter 的魔术关键字（magic keywords）
#在文档中显示 matplotlib 包生成的图形
# 设置图形的风格
# matplotlib inline 
# config InlineBackend.figure_format = 'retina'

data = pd.read_csv('../traffic/database_traffic.csv', header=None) #载入数据文件
data.head(5) #查看前5个头部数据

time = data.iloc[:,1] #把数据集中的 time 定义为 time

#mean均值，是正态分布的中心，把 数据集中的均值 定义为 mean
mean = time.mean()

#S.D.标准差，把数据集中的标准差 定义为 std
std = time.std()

#正态分布的概率密度函数。可以理解成 x 是 mu（均值）和 sigma（标准差）的函数
def normfun(x,mu,sigma):
    pdf = np.exp(-((x - mu)**2)/(2*sigma**2)) / (sigma * np.sqrt(2*np.pi))
    return pdf

# 设定 x 轴前两个数字是 X 轴的开始和结束，第三个数字表示步长，或者区间的间隔长度
x = np.arange(0,1000,1) 
#设定 y 轴，载入刚才的正态分布函数
y = normfun(x, mean, std)
plt.plot(x,y)
#画出直方图，最后的“normed”参数，是赋范的意思，数学概念
plt.hist(time, bins=10, rwidth=0.9, normed=True)
plt.title('Traffic value distribution')
plt.xlabel('traffic value')
plt.ylabel('Probability')
#输出
plt.show()

