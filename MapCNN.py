import torch
import torch.nn as nn

M = 50
N = 50
num_actions = 100

# 定义一个名为MapCNN的神经网络类
class MapCNN(nn.Module):
    def __init__(self, num_channels=16, kernel_size=3):
        super(MapCNN, self).__init__()
        # 第一层卷积层，输入通道数为1，输出通道数为num_channels，卷积核大小为kernel_size，步长为1，填充为1
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=num_channels, kernel_size=kernel_size, stride=1, padding=1)
        # ReLU激活函数
        self.relu = nn.ReLU()
        # 最大池化层，池化核大小为2x2，步长为2
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2)

        # 计算卷积和池化后的输出大小
        self.conv_out_dim = int((M / 2) * (N / 2) * num_channels)

        # 全连接层，用于处理提取的特征
        self.fc1 = nn.Linear(self.conv_out_dim, 128)
        # 最终的全连接层，输出维度为num_actions，即可能的动作数量（例如，不同的攻击策略）
        self.fc2 = nn.Linear(128, num_actions)

    # 神经网络的前向传播函数
    def forward(self, x):
        x = self.conv1(x)
        x = self.relu(x)
        x = self.pool(x)
        x = x.view(-1, self.conv_out_dim)  # 将特征图展开为一维向量
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x
