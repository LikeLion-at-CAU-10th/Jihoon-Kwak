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


print(test_images[5908])
print(test_labels[5908])


plt.figure(figsize=(10,10))
# plt.imshow(train_images[19999])


# for i in range(25) :
#   plt.subplot(5,5,i+1)
#   plt.xticks([]) #remove tick markss
#   plt.yticks([]) #remove tick marks
#   plt.grid(False) #remove grid

#   plt.imshow(train_images[i])
#   plt.xlabel (class_name[train_labels[i]])

plt.imshow(test_images[5908])
plt.colorbar()
plt.grid(False)
plt.show()