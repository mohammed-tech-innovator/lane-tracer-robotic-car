from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import elementry as ele
import csv
import os
from pynput import keyboard


time_delta = 0.15
loop_delay = 0.1

# data & refrence path
path1 = "dataset/images/"
path2 = "dataset/ref/"
# count the number of images
frames_counter  = 8916

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (512,256)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(512,256))
# allow the camera to warmup
time.sleep(0.1)

class CSVWriter():

    filename = None
    fp = None
    writer = None

    def __init__(self, filename):
        self.filename = filename
        self.fp = open(self.filename, 'w', encoding='utf8')
        self.writer = csv.writer(self.fp, delimiter=';', quotechar='"', quoting=csv.QUOTE_ALL, lineterminator='\n')

    def close(self):
        self.fp.close()

    def write(self, elems):
        self.writer.writerow(elems)

    def size(self):
        return os.path.getsize(self.filename)

    def fname(self):
        return self.filename


mycsv = CSVWriter(path2 + "ref_1.csv")
print("Written %d bytes to %s" % (mycsv.size(), mycsv.fname()))

def save_image(key,image):
    global frames_counter
    global mycsv
    global camera

    
    
    img_dir = path1 + 'image' + str(frames_counter) + '.jpg'
    cv2.imwrite(img_dir,image)
    
    key_map = {
        'w' : 0,
        'd' : 1,
        's' : 2,
        'a' : 3
        }
    
    line_data = ('image' + str(frames_counter) + '.jpg' , key_map[key])
    mycsv.write((line_data))
    frames_counter = frames_counter + 1



#take action
def on_press(key):
    try:
        if (key == 'w'):
            ele.forward(time_delta)
                     
        if (key == 'd'):
            ele.right_turn(time_delta)
            
        if (key == 's'):
            ele.reverse(time_delta)
            
        if (key == 'a'):
            ele.left_turn(time_delta)
            
    except AttributeError:
        if (key == keyboard.Key.esc):
            return False


for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    image = frame.array
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF
    
    
    
    time.sleep(loop_delay)
    if key == ord('w'):
        save_image('w',image)
        on_press('w')
        time.sleep(loop_delay)
    if key == ord('a'):
        save_image('a',image)
        on_press('a')
        time.sleep(loop_delay)
    if key == ord('s'):
        save_image('s',image)
        on_press('s')
        time.sleep(loop_delay)
    if key == ord('d'):
        save_image('d',image)
        on_press('d')
        time.sleep(loop_delay)
        
    if key == ord('q'):
        mycsv.close()
        break
    rawCapture.truncate(0)
    
