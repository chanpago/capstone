import os
import cv2
### opencv 이미지를 처리하는데 사용되며 컴퓨터 비전에서 매우 편리함
import pickle
### 픽셀 라이브러리는 모델을 저장하는데 사용됨 언제든지 모델을 재사용할 수 있음
import numpy as np
import pandas as pd
### 데이터 조작 도구로 사용됨
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

import keras
import tensorflow
import tempfile
from PIL import ImageFile

from tensorflow.keras.models import Model
from tensorflow.keras.utils import plot_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.applications import VGG19
from tensorflow.keras.callbacks import EarlyStopping
###  모델을 조기중지 시키는데 필요
from tensorflow.keras.preprocessing.image import ImageDataGenerator
### data augmantation 이미지를 증가시키는데 필요
from keras.layers import GlobalAveragePooling2D, Dense, Dropout
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from keras import regularizers
from keras.optimizers import SGD

ImageFile.LOAD_TRUNCATED_IMAGES = True

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

def eachFile(filepath):
	pathDir = os.listdir(filepath)
	out = []
	for allDir in pathDir:
		child = allDir
		out.append(child)
	return out

NUM_CLASSES = 9
TRAIN_PATH = 'C:\\Users\\USER\Desktop\\vgg19\\train'
TEST_PATH = 'C:\\Users\\USER\\Desktop\\vgg19\\test'
VALID_PATH='C:\\Users\\USER\\Desktop\\vgg19\\validation'
FC_NUMS = 4096

FREEZE_LAYERS = 17

IMAGE_SIZE = 224

base_model = VGG19(input_shape=(IMAGE_SIZE, IMAGE_SIZE, 3), include_top=False, weights='imagenet')
x = base_model.output
x = Dropout(0.7)(x)
x = GlobalAveragePooling2D()(x)
x = Dense(4096, activation='relu')(x)
prediction = Dense(NUM_CLASSES, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=prediction)

for layer in model.layers[:FREEZE_LAYERS]:
    layer.trainable = False

    
model.compile(optimizer=SGD(lr=0.00005, momentum=0.9), loss='categorical_crossentropy', metrics=['accuracy'])

train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)


train_generator = train_datagen.flow_from_directory(directory=TRAIN_PATH,
                                                    target_size=(IMAGE_SIZE, IMAGE_SIZE), class_mode = 'categorical', subset='training')
val_generator = val_datagen.flow_from_directory(directory=VALID_PATH, target_size=(IMAGE_SIZE, IMAGE_SIZE), 
                                                class_mode = 'categorical', shuffle=False)

print(val_generator.class_indices)


filepath = 'C:\\Users\\USER\\Desktop\\vgg19\\model\\sewer_weight.h5'
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')

history_ft = model.fit_generator(train_generator, epochs=30, callbacks=[checkpoint], 
                                 validation_data=val_generator, validation_steps=100)
model.save('C:\\Users\\USER\\Desktop\\vgg19\\model\\sewer_weight_final.h5')

