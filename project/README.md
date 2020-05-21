# CIFAR-100 Model Analysis

Created by: Luke Steffen

Created on: 05/19/2020

## Project Vision

This project is a Convolutional Neural Network which is used for image analysis and
classification. The CNN is created using the Keras library and the CIFAR-100 dataset.
Once the model is trained, it is used in a python program where the user can give a
filepath to an image for the model to predict. This model is only able to achieve an
accuracy of around 35-40% due to the type of data used for training.

## Code Modules

**from keras.datasets import cifar100**: Cifar-100 dataset used to train the keras model

**import matplotlib.pyplot as plt**: Used to display a test image in the Jupyter Notebook

**from keras import layers**: Used to add layers to a Keras model

**from keras import models**: Used to create a keras model

**from keras.utils import to_categorical**: Used to convert image data to a categorical format

**import numpy as np**: Used to manipulate user's image to prepare it for model prediction

**from PIL import Image**: Used to create an Image object from the user request

**import request**: Used to process a user request/grab the user file given

**from io import BytesIO**: Used to convert file into bytes for processing

**import cv2**: Used to compress input image to match the 32x32 pixel format

**from google.colab.patches import cv2_imshow**: Function used to display compressed image on Jupyter Notebook

## How to run this program

To run this program, you will need all of the libraries stated in the bibliography section of report.ipynb. In 
addition to the libraries, you will also need an evironment that is capable of running Jupyter Notebooks. If you
have a Google account, you can run this program on Google Colab for free with little hassle. Once all of these 
requirements have been met, simply pull this Github repository and run report.ipynb in your Jupyter Notebook 
supported IDE of choice.

## Dataset References

CIFAR-10/100 datasets: https://www.cs.toronto.edu/~kriz/cifar.html


