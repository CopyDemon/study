import numpy as np


class SimpleNeuron:
    def __init__(self, weights, bias):
        self.weights = np.array(weights)
        self.bias = bias

    def feedforward(self, inputs):
        # 矩阵点积计算：w1*x1 + w2*x2 + ... + wn*xn
        total = np.dot(self.weights, inputs) + self.bias
        return total


# 设置权重和偏置
weights = [10.0, 0.0]  # 两个输入对应的权重
bias = 0.1  # 一个偏置项
neuron = SimpleNeuron(weights, bias)

# 输入数据
inputs = [2.0, 1.0]

# 计算结果
output = neuron.feedforward(inputs)
print(f"神经元的输出结果是: {output}")
