from cgi import test
from pickletools import optimize
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


train_images = train_images / 255.0
test_images = test_images / 255.0


model = keras.Sequential(
  [
    keras.layers.Flatten(input_shape = (28,28)),
    keras.layers.Dense(128, activation = tf.nn.relu), 
    keras.layers.Dense(10, activation = tf.nn.softmax),
    
    ]
)


model.compile(
  optimizer = 'adam',
  loss = 'sparse_categorical_crossentropy',
  metrics = ['accuracy']
  )


model.fit ( train_images, train_labels, epochs = 10)


test_loss, test_acc = model.evaluate(test_images, test_labels)


print("Accuracy (test sample) = ", test_acc)



predictions = model.predict (test_images)
a=0
b=0
c=0
d=0
e=0
f=0
g=0
h=0
j=0
k=0

for i in range(0,10000):
  if np.argmax( predictions[i] ) == 0:
    a=a+1
  if np.argmax( predictions[i] ) == 1:
    b=b+1
  if np.argmax( predictions[i] ) == 2:
    c=c+1
  if np.argmax( predictions[i] ) == 3:
    d=d+1
  if np.argmax( predictions[i] ) == 4:
    e=e+1
  if np.argmax( predictions[i] ) == 5:
    f=f+1
  if np.argmax( predictions[i] ) == 6:
    g=g+1
  if np.argmax( predictions[i] ) == 7:
    h=h+1
  if np.argmax( predictions[i] ) == 8:
    j=j+1
  if np.argmax( predictions[i] ) == 9:
    k=k+1
  

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(j)
print(k)

aa=0
bb=0
cc=0
dd=0
ee=0
ff=0
gg=0
hh=0
jj=0
kk=0


for i in range(0,10000):
  if test_labels[i] == 0:
    aa=aa+1
  if test_labels[i] == 1:
    bb=bb+1
  if test_labels[i] == 2:
    cc=cc+1
  if test_labels[i] == 3:
    dd=dd+1
  if test_labels[i] == 4:
    ee=ee+1
  if test_labels[i] == 5:
    ff=ff+1
  if test_labels[i] == 6:
    gg=gg+1
  if test_labels[i] == 7:
    hh=hh+1
  if test_labels[i] == 8:
    jj=jj+1
  if test_labels[i] == 9:
    kk=kk+1
  

print(aa)
print(bb)
print(cc)
print(dd)
print(ee)
print(ff)
print(gg)
print(hh)
print(jj)
print(kk)

def y(fashion, p):
  return np.zeros(N) + p

p = 10
N = 10

initial_count = np.array([a,b,c,d,e,f,g,h,j,k])

fashion = np.array(["T-shirt/top","Trouser","Pullover","Dress","Coat","Sandal","Shirt","Sneaker","Bag","Ankle boot"])
counts = np.array([abs(aa-a),abs(bb-b),abs(cc-c),abs(dd-d),abs(ee-e),abs(ff-f),abs(gg-g),abs(hh-h),abs(jj-j),abs(kk-k)])
error = np.sqrt(initial_count)

print(counts)

plt.errorbar(fashion, counts, yerr=error, fmt = 'o')
plt.show()