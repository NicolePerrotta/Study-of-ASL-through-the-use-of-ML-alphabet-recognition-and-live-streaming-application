import sys
import os
import numpy as np
import copy
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.python.platform import gfile
from tensorflow.core.protobuf import saved_model_pb2
from tensorflow.python.util import compat
import matplotlib.image as mpimg
import string
import PIL

clas = [char for char in string.ascii_uppercase]
classes = np.empty(29, dtype=object) 
for i in range(29):
  if i==26:
    classes[i]='del'
  elif i==27:
    classes[i]='nothing'
  elif i==28: 
    classes[i]='space'
  else:
    classes[i]=clas[i]
#print('Classes: ')
#print(classes, end = " ")
#print('\n')
loaded_model = tf.keras.models.load_model(r"C:\Users\perro\OneDrive\Desktop\model_8_64EfficientNetB0_BW")

def predict(image_data):
    predictions = loaded_model.predict(image_data)
    score = tf.nn.softmax(predictions[0])
    max_score = score[np.argmax(score)]
    res = classes[np.argmax(score)]
    return res, max_score

def doWork():
    c = 0
    cap = cv2.VideoCapture(0)
    res, score = '', 0.0
    i = 0
    mem = ''
    consecutive = 0
    sequence = ''
    while True:
        ret, img = cap.read()
        img = cv2.flip(img, 1)        
        if ret:
            x1, y1, x2, y2 = 100, 100, 300, 300
            img_cropped = img[y1:y2, x1:x2]
            c += 1    
            cv2.imwrite(r'C:\Users\perro\P\fp.jpg', img_cropped)#save the last frame to check it
            img_croppedBW = PIL.Image.open(r"C:\Users\perro\P\fp.jpg").convert("L") #gray scale image converter
            img_croppedBW = np.asarray(img_croppedBW) #becomes an array
            image_data = cv2.resize(img_croppedBW, (64,64))
            image_data = tf.keras.utils.img_to_array(image_data)
            image_data3 = cv2.merge((image_data,image_data,image_data))
            image_data = tf.keras.utils.img_to_array(image_data3)
            image_data = tf.expand_dims(image_data, 0) # from (32, 32, 3) to (None, 32, 32, 3)  
            a = cv2.waitKey(1) # waits to see if `esc` is pressed
            if i == 30: #every 30 frames, 1sec=24 frames
                res_tmp, score = predict(image_data)
                res = res_tmp
                i = 0
                if mem == res:
                    consecutive += 1
                else:
                    consecutive = 0
                if consecutive == 2 and res not in ['nothing']:
                    if res == 'space':
                        sequence += ' '
                    elif res == 'del':
                        sequence = sequence[:-1]
                    else:
                        sequence += res
                    consecutive = 0
            i += 1
            cv2.putText(img, '%s' % (res.upper()), (100,400), cv2.FONT_HERSHEY_SIMPLEX, 4, (255,255,255), 4)
            cv2.putText(img, '(score = %.5f)' % (float(score)), (100,450), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
            mem = res
            cv2.rectangle(img, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.imshow("img", img)
            img_sequence = np.zeros((200,1200,3), np.uint8)
            cv2.putText(img_sequence, '%s' % (sequence.upper()), (30,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
            cv2.imshow('sequence', img_sequence)
            cv2.imshow('gray', img_croppedBW)
            if a == 27: # when `esc` is pressed
                break
doWork()
cv2.destroyAllWindows() 
cv2.VideoCapture(0).release()
