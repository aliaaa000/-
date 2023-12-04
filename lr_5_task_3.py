# -*- coding: utf-8 -*-
"""Lr_5_task_3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sSqzcoTIwFkloBt0-5V-5ub1CHN2FLWj
"""

import numpy as np
import matplotlib.pyplot as plt
!pip install neurolab

import neurolab as nl

# Load data from file
text = np.loadtxt('data_perceptron.txt')

# Split data into data points and labels
data = text[:, :2]
labels = text[:, 2].reshape((text.shape[0], 1))

# Plot input data points
plt.figure()
plt.scatter(data[:, 0], data[:, 1])
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.title('Input Data')
dim1_min, dim1_max, dim2_min, dim2_max = 0, 1, 0, 1

# Number of neurons in the output layer
num_output = labels.shape[1]

dim1 = [dim1_min, dim1_max]
dim2 = [dim2_min, dim2_max]
perceptron = nl.net.newp([dim1, dim2], num_output)

# Training the perceptron using our data
error_progress = perceptron.train(data, labels, epochs=100, show=20, lr=0.03)

# Plot the training error progress
plt.figure()
plt.plot(error_progress)
plt.xlabel('Number of epochs')
plt.ylabel('Training error')
plt.title('Change in training error')
plt.grid()
plt.show()