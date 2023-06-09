# -*- coding: utf-8 -*-
"""pred_autoEncoder.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xI-FA4wpas1QKPJGcuPN224gdeaHAh0q
"""

import numpy as np
from keras. layers import Input, Dense
from keras.models import Model
from keras.datasets import mnist
import matplotlib.pyplot as plt

(x_train,_), (x_test,_)=mnist.load_data()

x_train= x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.


x_train = x_train.reshape((len(x_train), np.prod(x_train. shape [1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))
print(x_train.shape)
print(x_test.shape)

input_size = 784 # compression of factor 24.5, assuming the input is 784 floats 
encoding_dim= 32 #this is the size of our encoded representations
input_img=Input(shape=(input_size,))
# "encoded" is the encoded representation of the input 
encoded= Dense(encoding_dim, activation='relu') (input_img)
# "decoded" is the lossy reconstruction of the input 
decoded = Dense(input_size, activation="sigmoid") (encoded)

autoencoder=Model(input_img, decoded)
autoencoder.compile(optimizer='adam',loss='binary_crossentropy')
autoencoder.fit(x_train,x_train,epochs=5)

def plot_autoencoder_outputs(autoencoder,n,dims):
  decoded_imgs = autoencoder. predict(x_test)
  n = 5 # number of example digits to show
  plt.figure(figsize=(10, 4.5))
  for i in range(n):
    ax = plt.subplot(2, n, i + 1)
    plt.imshow(x_test[i].reshape(*dims))
    ax = plt.subplot(2, n, i + 1 + n) 
    plt.imshow(decoded_imgs [i].reshape(*dims))
  plt.show()

plot_autoencoder_outputs(autoencoder,5,(28,28))