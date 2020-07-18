#loading the necessary packages

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
from tensorflow.keras.models import load_model
import os
import numpy as np
import matplotlib.pyplot as plt


# loading the dataset:


fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


# Loading the names:


class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']


# loading and configuring the training and testing images:


train_images = train_images.reshape((60000, 28, 28, 1))
test_images = test_images.reshape((10000, 28, 28, 1))
train_x = train_images / 255.0
test_y = test_images / 255.0


# creating the model:

model = models.Sequential()

# here the spaces are to add layers in future if the model accuracy is lesser




model.add(layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1) ))
model.add(layers.Conv2D(128, (3,3), activation='relu'))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.MaxPooling2D((2,2)))
model.add(layers.Flatten())
model.add(layers.Dense(128, activation='relu'))
model.add(layers.Dense(10, 'softmax'))
model.summary()
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
fit_model = model.fit(train_x, train_labels, epochs=2, batch_size=512, shuffle=True, validation_split=0.1)
test_loss, test_accuracy = model.evaluate(test_y, test_labels)


# saving the accuracy of the model in accuracy.txt file:


text = fit_model.history
accuracy = text['accuracy'][1] * 100
accuracy = int(accuracy)
f= open("/home/accuracy.txt","w+")
f.write(str(accuracy))
f.close()

print("Accuracy for the model is : " , accuracy ,"%")
