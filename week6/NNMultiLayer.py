#!/usr/bin/env python
# coding: utf-8

# Ejemplo de Theano

# 

# In[ ]:


# In[2]:


# Example of TensorFlow library
import tensorflow as tf
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
# declare two symbolic floating-point scalars
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
# create a simple symbolic expression using the add function
add = tf.add(a, b)
# bind 1.5 to 'a', 2.5 to 'b', and evaluate 'c'
sess = tf.Session()
binding = {a: 1.5, b: 2.5}
c = sess.run(add, feed_dict=binding)
print(c)


# In[ ]:


# Example of Theano library
import theano
from theano import tensor
# declare two symbolic floating-point scalars
a = tensor.dscalar()
b = tensor.dscalar()
# create a simple symbolic expression
c = a + b
# convert the expression into a callable object that takes (a,b) and computes c
f = theano.function([a,b], c)
# bind 1.5 to 'a', 2.5 to 'b', and evaluate 'c'
result = f(1.5, 2.5)
print(result)


# DEFINIENDO EL MODELO, ENTRENANDO Y PROBÁNDOLO

# In[ ]:


# first neural network with keras tutorial
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
from google.colab import drive



# load the dataset
drive.mount('/content/drive')
dataset = loadtxt("/content/drive/MyDrive//Colab Notebooks/dataset/pima-indians-diabetes.csv", delimiter=',')


# split into input (X) and output (y) variables
X = dataset[:,0:8]
y = dataset[:,8]
# define the keras model
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu')) # Dense all neurons connected with others, Dense (vector output size, input size, activation function )
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
model.fit(X, y, epochs=100, batch_size=30) # batch is the number of samples inputs used before to compute the error
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))


# HACIENDO PREDICCIONES DEL MODELO AJUSTADO

# In[ ]:




# make class predictions with the model
predictions = model.predict(X)
# summarize the first 5 cases
for i in range(15):
  print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))

