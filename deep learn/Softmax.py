# 导入模块
import numpy as np
import matplotlib.pyplot as plt

X=np.arange(-1.0,1.1,0.1)
Y=np.arange(-1.0,1.1,0.1)

input_data=[]
correct_data=[]
for x in X:
    for y in Y:
        input_data.append([x,y])
        if y<np.sin(np.pi*x):
            correct_data.append([0,1])
        else:
            correct_data.append([1,0])

n_data=len(correct_data)
input_data=np.array(input_data)
correct_data=np.array(correct_data)

#输出层
class OutputLayer:
    def __init__(self, n_upper, n):                         # 初始化设置
        self.w = wb_width * np.random.randn(n_upper, n)     # 权重 (矩阵)
        self.b = wb_width * np.random.randn(n)              # 偏置 (向量)

    def forward(self, x):                                   # 正向传播
        self.x = x
        u = np.dot(x, self.w) + self.b
        self.y = u                                          # 恒等函数

    def backward(self, t):                                  # 反向传播
        delta = self.y - t

        self.grad_w = np.dot(self.x.T, delta)
        self.grad_b = np.sum(delta, axis=0)
        
        self.grad_x = np.dot(delta, self.w.T)

    def update(self, eta):                                  # 权重和偏置的更新
        self.w -= eta * self.grad_w
        self.b -= eta * self.grad_b

# --中间层--
class MiddleLayer:
    def __init__ (self,n_upper, n):                             # 初始化设置
        self.w = wb_width * np.random.randn(n_upper, n)         # 权重 (矩阵)
        self.b = wb_width * np.random.randn(n)                  # 偏置 (向量)
    def forward(self,x):                                        # 正向传播
        self.x = x
        u = np.dot(x, self.w) + self.b                          # 中间层的净输入
        self.y = 1 / (1 + np.exp(-u))                           # sigmoid函数
    def backward(self,grad_y):                                  # 反向传播
        delta = grad_y * (1-self.y) * self.y                    # sigmoid函数的微分
        self.grad_w = np.dot(self.x.T, delta)                   # 根据推导公式结果
        self.grad_b = np.sum(delta, axis=0)
        self.grad_x = np.dot(delta, self.w.T)
    def update(self,eta):
        self.w -= eta * self.grad_w
        self.b -= eta * self.grad_b

# 设置参数
wb_width = 0.01     # 权重和偏置的初始范围
epoch = 101        # 迭代次数
#n_data = 100        # 数据点数量
eta = 0.1           # 学习率
interval = 10      # 每隔多少次迭代可视化一次
n_in = 2            # 输入层维度
n_mid = 6           # 中间层维度
n_out = 2           # 输出层维度

# 生成输入数据和正确答案
#input_data = np.linspace(0, 2 * np.pi, n_data)
#correct_data = np.sin(input_data)

# -- 各个网络层的初始化 - -
middle_layer = MiddleLayer(n_in, n_mid)
output_layer = OutputLayer(n_mid, n_out)

# --学习--
sin_data=np.sin(np.pi*X)
for i in range(epoch):
    #随机打乱索引值
    index_random = np.arange(n_data)
    np.random.shuffle(index_random)

    # 用于结果显示
    total_error = 0
    x_1 = []
    y_1 = []
    x_2 = []
    y_2 = []

    for idx in index_random:                # 输入
        x = input_data[idx]           # 正确答案
        t = correct_data[idx]   
        
        #正向传播
        middle_layer.forward(x.reshape(1,2))    # 将输入转换为矩阵
        
        output_layer.forward(middle_layer.y)    # 反向传播
        
        output_layer.backward(t.reshape(1,2))   # 将正确答案转换为矩阵
        middle_layer.backward(output_layer.grad_x)
        
        #权重和偏置的更新
        middle_layer.update(eta)
        output_layer.update(eta)
        if i%interval == 0:
            y = output_layer.y.reshape(-1)
            #将矩阵还原成向量
            #误差的计算
            total_error += -np.sum(t*np.log(y+1e-7)) # 平方和误差
            # 输出记录
            if y[0]>y[1]:
                x_1.append(x[0])
                y_1.append(x[1])
            else:
                x_2.append(x[0])
                y_2.append(x[1])

    if i%interval == 0:
        #用图表显示输出
        plt.plot(X,sin_data, linestyle="dashed")
        plt.scatter(x_1, y_1,marker="+")
        plt.scatter(x_2, y_2,marker="x")
        # plt.show()
        #显示epoch次数和误差
        print("Epoch:" + str(i) + "/" + str(epoch),"Error:" + str(total_error/n_data))