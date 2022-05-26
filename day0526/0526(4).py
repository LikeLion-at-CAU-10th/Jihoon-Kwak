from tensorflow.keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

print("DIM  =",train_images.ndim)
print("Shape  =",train_images.shape)
print("Type  =",train_images.dtype)

# digit = train_images[0]
import matplotlib.pyplot as plt

plt.figure(figsize=(10,10))
plt.subplot(1, 1, 1)
plt.imshow( train_images[500], camp = plt.cm.binary)
plt.show()