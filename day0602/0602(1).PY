import tensorflow as tf
from tensorflow import keras


import numpy as np
import matplotlib.pyplot as plt


fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


class_name = ['T-shirt/top',
              'Trouser',
              'Pullover',
              'Dress',
              'Coat',
              'Sandal',
              'Shirt',
              'Sneaker',
              'Bag',
              'Ankle boot']


# print(train_images.shape)
# print(len(train_labels))
# print(train_images[19999])
# print(train_labels[19999])


# print(test_images[9999])
# print(test_labels[9999])


plt.figure()
# plt.imshow(train_images[19999])


for i in range(25) :
  plt.subplot(5,5,i+1)
  plt.imshow(train_images[i])
  plt.xlabel (class_name[train_labels[i]])
# plt.imshow(test_images[9999])
# plt.colorbar()
# plt.grid(False)
plt.show()