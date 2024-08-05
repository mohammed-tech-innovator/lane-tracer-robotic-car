from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import torch
from model import model_larg
import torch.nn as nn
import elementry as ele
import numpy as np


#model path
model_path = 'model/mod_larg.stat'
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (512,256)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(512,256))
# allow the camera to warmup
time.sleep(0.1)
# capture frames from the camera

#loop delay
loop_delay = 0.1
#movement duantion
delta_T = 0.15
#loading the model
driver = model_larg.self_driving_model() # model instance 
device = torch.device('cpu') # device in case of raspberry pi cpu 
driver.load_state_dict(torch.load(model_path, map_location=device)) # load model wieghts
#driver = torch.load('model.pth',map_location=device)

def prepare(image):
    image = torch.tensor(np.array(image))
    shape = image.shape
    image = image.view(1,shape[2],shape[0],shape[1])
    image = image/256.0
    return image

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    cv2.imshow("Frame", image)
    image = prepare(image)
    score = driver(image)
    decision = torch.argmax(score)
    print(score)
    
    if decision == 0 : #forward
        ele.forward(delta_T)
    elif decision == 1 : # turn_right
        ele.right_turn(delta_T)
    elif decision == 2 : # backward
        ele.reverse(delta_T)
    elif decision == 3 : # turn_left
        ele.left_turn(delta_T)
    
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    time.sleep(loop_delay)
    if key == ord('q'):
        break # exit loop

    
