# -*- coding: UTF-8 -*-

import numpy as np
import tensorflow as tf
# 下载并载入 MNIST 手写数字库
from tensorflow.example.tutorials.mnist import input_data

mnist = input_data.read_data_sets('mnist_data',one_hot=True)

# ont_hot 独热码的编码 （encoding) 形式
# 0， 1， 2， 3， 4，5，6，7，8，9 的十位数
# 0： 1000000000
# 1： 0100000000
# 依次移一位

train x = tf.placeholder(tf.float32, [None, 28 * 28]) / 255.
train y = tf.placeholder(tf.int32, [None, 10])
image = tf.reshape(train_x, [-1, 28, 28, 1])

#构建卷积神经网络

tf.layers.conv2d
# 2d表示2维卷积