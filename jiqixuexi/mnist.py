import numpy as np
import tensorflow as tf

mnist = tf.learn.datasets.load_dataset("MNIST_data/", one_hot=True)
print(dir(tf))