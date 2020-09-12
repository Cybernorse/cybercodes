#!/usr/bin/env python
# coding: utf-8


import tensorflow as tf
from tensorflow.keras.callbacks import TensorBoard

tensorboard = TensorBoard(log_dir="logs/tb_logs")
mnist = tf.keras.datasets.mnist
(x_train,y_train),(x_test,y_test) = mnist.load_data()
x_train=tf.keras.utils.normalize(x_train,axis=1)
x_test=tf.keras.utils.normalize(x_test,axis=1)
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128,activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10,activation=tf.nn.softmax))
model.compile(optimizer='adam' , loss='sparse_categorical_crossentropy' ,metrics=['accuracy'])
model.fit(x_train,y_train,epochs=3,callbacks=[tensorboard])

val_loss,val_acc=model.evaluate(x_test,y_test)

predictions=model.predict(x_test)

import numpy as np
print(np.argmax(predictions[0]))

import matplotlib.pyplot as plt
plt.imshow(x_test[0])
plt.show()







