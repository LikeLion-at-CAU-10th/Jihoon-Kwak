from tensorflow.keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print("DIM  =",train_images.ndim)
print("Shape  =",train_images.shape)
print("Type  =",train_images.dtype)

# digit = train_images[0]
import matplotlib.pyplot as plt

# plt.imshow(digit, cmap=plt.cm.binary)
# plt.show()

plt.figure(figsize=(10,10))
for i in range(100):
  plt.subplot(10, 10, i+1)
  plt.xticks([])
  plt.yticks([])
  plt.grid(False)
  plt.imshow(train_images[i], cmap = plt.cm.binary)
  # plt.xlabel(class_names[train_labels[i]])

plt.show()