# -*- coding: utf-8 -*-
"""Behaviour-Cloning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ceRFGeTcmn4UvMJCdlfnGdkQn13MwAz8
"""

!pip3 install imgaug

!git clone https://github.com/shahanHasan/Autonomous-vehicle-using-open-CV-and-Machine-Learning.git

!ls Autonomous-vehicle-using-open-CV-and-Machine-Learning

# necessary imports
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import keras
from keras.models import Sequential
from keras.optimizers import Adam
from keras.layers import Convolution2D, MaxPooling2D, Dropout, Flatten, Dense
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from imgaug import augmenters as iaa
import cv2
import pandas as pd
import ntpath
import random

# loading data
datadir = 'Autonomous-vehicle-using-open-CV-and-Machine-Learning'
columns = ['center','left','right','steering','throttle','reverse','speed']
data = pd.read_csv(os.path.join(datadir,'driving_log.csv'), names = columns)
pd.set_option('display.max_colwidth', -1)
data.head()

# data normalisation
def path_leaf(path):
  head , tail = ntpath.split(path)
  return tail
data['center'] = data['center'].apply(path_leaf)
data['left'] = data['left'].apply(path_leaf)
data['right'] = data['right'].apply(path_leaf)
data.head()

# visualising the steering angles in a histogram
# number of bars in histogram , must be odd to gain a center value
num_bins = 25
# threshold of 200 in every bin so lowering the bias of going forward and steer angle 0
samples_per_bin = 1000
hist , bins = np.histogram(data['steering'], num_bins)
# centering the values around 0 
center = (bins[:-1]+ bins[1:])* 0.5
print(hist)
print(bins)
plt.bar(center, hist , width=0.05)
plt.plot((np.min(data['steering']), np.max(data['steering'])), (samples_per_bin,samples_per_bin))

print("total data : ", len(data))
# indices of all the steering angles we wanna remove
remove_list = []
for j in range(num_bins):
  list_ = []
  for i in range(len(data['steering'])):
    if data['steering'][i] >= bins[j] and data['steering'][i] <= bins[j+1]:
      #print(data['steering'][i])
      #print(bins[j])
      #print(i)
      #print("---")
      # appends total no of index of steering angles belonging to each bin
      list_.append(i)
  list_ = shuffle(list_)
  list_ = list_[samples_per_bin:]
  remove_list.extend(list_)
  
  
print('removed:' , len(remove_list))
data.drop(data.index[remove_list], inplace=True)
print('remaining', len(data))

hist , _ = np.histogram(data['steering'] , (num_bins))
plt.bar(center, hist , width=0.05)
plt.plot((np.min(data['steering']), np.max(data['steering'])), (samples_per_bin,samples_per_bin))

#print(data.iloc[1])
def load_img_steering(datadir, df):
  image_path = []
  steering = []
  for i in range(len(data)):
    # displays the row from data at the given index
    indexed_data = data.iloc[i]
    center , left , right = indexed_data[0],indexed_data[1],indexed_data[2]
    image_path.append(os.path.join(datadir, center.strip()))
    steering.append(float(indexed_data[3]))
  image_paths = np.asarray(image_path)
  steerings = np.asarray(steering)
  return image_paths , steerings

image_paths , steerings = load_img_steering(datadir + '/IMG' ,data )

# splitting the train validation and test data from the large dataset
X_train , X_valid , y_train , y_valid = train_test_split(image_paths , steerings , test_size = 0.2 , random_state=6)
print('Training samples : {}\nValid samples : {}'.format(len(X_train),len(X_valid)))

# histogram to visualise the train and validation set
fig , axes = plt.subplots(1,2, figsize=(12,4))
axes[0].hist(y_train, bins = num_bins, width=0.05, color='blue')
axes[0].set_title('Training set')
axes[1].hist(y_valid, bins = num_bins , width=0.05 , color='red')
axes[1].set_title('Validation set')

# imgaug / image augmentation 
def zoom(image):
  zoom = iaa.Affine(scale=(1, 1.3))
  image = zoom.augment_image(image)
  return image

# comparing the processed image with the original image
image = image_paths[random.randint(0,1000)]
original_image = mpimg.imread(image)
zoom_image = zoom(original_image)
# displaying the images as plots with 2 columns and 1 row
fig, axes = plt.subplots(1,2, figsize=(15,10))
# proper image format and the axes/images dont overlap
fig.tight_layout()
# plot the images
axes[0].imshow(original_image)
axes[0].set_title('original image')

axes[1].imshow(zoom_image)
axes[1].set_title('zoomed image')

# image panning : horizontal or vertical panning / translations
def pan(image):
  pan = iaa.Affine(translate_percent= {"x" : (-0.1, 0.1), "y" : (-0.1,0.1)})
  image = pan.augment_image(image)
  return image

# comparing the processed image with the original image
image = image_paths[random.randint(0,1000)]
original_image = mpimg.imread(image)
pan_image = pan(original_image)
# displaying the images as plots with 2 columns and 1 row
fig, axes = plt.subplots(1,2, figsize=(15,10))
# proper image format and the axes/images dont overlap
fig.tight_layout()
# plot the images
axes[0].imshow(original_image)
axes[0].set_title('original image')

axes[1].imshow(pan_image)
axes[1].set_title('panned image')

# altering brightness
def img_random_brightness(image):
  brightness = iaa.Multiply((0.2, 1.2))
  image = brightness.augment_image(image)
  return image

# comparing the processed image with the original image
image = image_paths[random.randint(0,1000)]
original_image = mpimg.imread(image)
brightness_altered_image = img_random_brightness(original_image)
# displaying the images as plots with 2 columns and 1 row
fig, axes = plt.subplots(1,2, figsize=(15,10))
# proper image format and the axes/images dont overlap
fig.tight_layout()
# plot the images
axes[0].imshow(original_image)
axes[0].set_title('original image')

axes[1].imshow(brightness_altered_image)
axes[1].set_title('brightness altered image')

# image flipping : 
def img_random_flip(image , steering_angle):
  image = cv2.flip(image, 1)# 0 H or 1 V or -1(combo of horizontal or vertical)
  steering_angle = -steering_angle
  return image , steering_angle

random_index = random.randint(0,1000)
# comparing the processed image with the original image
image = image_paths[random_index]
steering_angle = steerings[random_index]
original_image = mpimg.imread(image)
flipped_image ,flipped_steering_angle = img_random_flip(original_image , steering_angle )
# displaying the images as plots with 2 columns and 1 row
fig, axes = plt.subplots(1,2, figsize=(15,10))
# proper image format and the axes/images dont overlap
fig.tight_layout()
# plot the images
axes[0].imshow(original_image)
axes[0].set_title('original image - ' + 'steering angle : ' + str(steering_angle))

axes[1].imshow(flipped_image)
axes[1].set_title('flipped image - ' + 'flipped steering angle : ' + str(flipped_steering_angle))

# random augment : only on some images of the dataset to increase generalisation
def random_augment(image , steering_angle):
  image = mpimg.imread(image)
  if np.random.rand() < 0.5:
    image = pan(image)
  if np.random.rand() < 0.5:
    image = zoom(image)
  if np.random.rand() < 0.5:
    image = img_random_brightness(image)
  if np.random.rand() < 0.5:
    image , steering_angle = img_random_flip(image , steering_angle)
  return image , steering_angle

# visualise random augment :
ncol = 2
nrow = 10 
fig ,axs = plt.subplots(nrow , ncol , figsize=(15,50))
fig.tight_layout()
for i in range(10):
  randnum = random.randint(0 , len(image_paths)-1)
  random_image = image_paths[randnum]
  random_steering = steerings[randnum]
  
  original_image = mpimg.imread(random_image)
  augmented_image , steering = random_augment(random_image , random_steering)
  
  # plotting the images
  axs[i][0].imshow(original_image)
  axs[i][0].set_title('original image - \n' + 'steering angle : ' + str(random_steering))
  
  axs[i][1].imshow(augmented_image)
  axs[i][1].set_title('augmented image - \n' + 'steering angle : ' + str(steering))

# a function to pre process all the images of the data set
def img_preprocess(img):
  #img = mpimg.imread(img)
  img = img[60:135,:,:]
  img = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
  img = cv2.GaussianBlur(img, (3,3), 0 )# arg = img , kernal size and deviation
  img = cv2.resize(img , (200,66))
  img = img/255 # normalisation , explained in lane detection
  return img

# comparing the processed image with the original image
image = image_paths[100]
original_image = mpimg.imread(image)
preprocessed_image = img_preprocess(original_image)
# displaying the images as plots with 2 columns and 1 row
fig, axes = plt.subplots(1,2, figsize=(15,10))
# proper image format and the axes/images dont overlap
fig.tight_layout()
# plot the images
axes[0].imshow(original_image)
axes[0].set_title('original image')
axes[1].imshow(preprocessed_image)
axes[1].set_title('preprocessed image')

# fit_generator : create images in batches and training on the fly
# training data can be augmented but validation cannot
def batch_generator(image_paths, steering_ang, batch_size, istraining):
  
  while True:
    batch_img = []
    batch_steering = []
    
    for i in range(batch_size):
      random_index = random.randint(0, len(image_paths) - 1)
      
      if istraining:
        im, steering = random_augment(image_paths[random_index], steering_ang[random_index])
     
      else:
        im = mpimg.imread(image_paths[random_index])
        steering = steering_ang[random_index]
      
      im = img_preprocess(im)
      batch_img.append(im)
      batch_steering.append(steering)
    yield (np.asarray(batch_img), np.asarray(batch_steering))

# next(): this function call in an iterator item 
# and retrieves the next item for it

x_train_gen, y_train_gen = next(batch_generator(X_train, y_train, 1, 1))
x_valid_gen, y_valid_gen = next(batch_generator(X_valid, y_valid, 1, 0))

# displaying the images as plots with 2 columns and 1 row
fig, axes = plt.subplots(1,2, figsize=(15,10))
# proper image format and the axes/images dont overlap
fig.tight_layout()
# plot the images
axes[0].imshow(x_train_gen[0])
axes[0].set_title('Training image')
axes[1].imshow(x_valid_gen[0])
axes[1].set_title('Validation image')

# this function iterates through the entire array provided and applies
# the provided function as arguments to the elements of the array
# and return an entirely new array with the output of the function
# passed in as argument in a list 
#### X_train = np.array(list(map(img_preprocess , X_train)))
#### X_valid = np.array(list(map(img_preprocess , X_valid)))
#X_test = np.array(list(map(img_preprocess , X_test)))

#####plt.imshow(X_train[random.randint(0, len(X_train)-1)])
#####plt.axis('off')
#####print(X_train.shape)

# ML model : NVIDIA model (behaviour clonning : regression)
# CNN model : 
# 1 hardcoded image normalisation layer
# 5 convolution layer
# 3 fully connected layers 
# 1 Output layer
# the model learns to detect the line , lane with just 
# steering angle as input , all on its own
def nvidia_model():
  model = Sequential()
  # 1st layer normalisation of image which is done above
  # layer 2 , normalised image is passed to the layer 1 convolve
  # 5 * 5 kernal / 2 * 2 stride in first 3 / 5 * 5 stride in last 2
  model.add(Convolution2D(24,5,5, subsample=(2,2), input_shape=(66,200,3), activation = 'elu'))# 24 filters/ 5 by 5 kernal
  model.add(Convolution2D(36,5,5, subsample=(2,2), activation = 'elu'))
  model.add(Convolution2D(48,5,5, subsample=(2,2), activation = 'elu'))
  model.add(Convolution2D(64,3,3, activation = 'elu'))
  model.add(Convolution2D(64,3,3, activation = 'elu'))
  # avoid over fit by drop out layer
  ###model.add(Dropout(0.5))
  # flatten layer
  model.add(Flatten())
  # drop out
  ###model.add(Dropout(0.5))
  # 1st FC layer with 100 neurons
  model.add(Dense(100 , activation='elu'))
  # avoid over fit by drop out layer (here because the 1st FC layer has too many abstract
  # feature maps)
  ###model.add(Dropout(0.5))
  # 2nd FC layer with 50 neurons
  model.add(Dense(50 , activation='elu'))
  # drop out
  model.add(Dropout(0.5))
  # 3rd FC layer with 10 neurons
  model.add(Dense(10 , activation='elu'))
  # drop out
  ###model.add(Dropout(0.5))
  # output layer , relu activation because it is a regression problem
  # rather than a classification where we continuously predict steering
  # angles . (CONTINUOUS VALUED OUTPUT)
  model.add(Dense(1))
  # compiling the layer with adam optimizer
  optimizer = Adam(lr = 0.005)
  model.compile(loss='mse', optimizer=optimizer)
  return model

model = nvidia_model()
print(model.summary())

# training the model

history = model.fit_generator(batch_generator(X_train ,y_train,300, 1 ), 
                              steps_per_epoch = 300, 
                              epochs = 15, 
                              validation_data = batch_generator(X_valid , y_valid , 100, 0), 
                              validation_steps=200,
                              verbose=1,
                              shuffle=1)

# plotting the loss variance during training

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.legend(['training','validation'])
plt.title('Loss')
plt.xlabel('Epoch')

model.save('model.h5')

#from google.colab import files
#files.download('model.h5')
