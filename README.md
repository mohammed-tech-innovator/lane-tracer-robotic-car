# lane-tracer-robotic-car

The task of lane tracing includes determining the steering angle and the speed of the vehicle; if any of those two is miscalculated it may case the car to derail, NVidia end to end learning uses a simple regression model , another approach that uses very simple CNN classification model , however our approach goes as follows the captured image is passed to a ResNet classification model that maps the input images into the four classes ( increase the speed , decrease the speed , increase the steering angle , decrease the steering angle) .

# The car :

In order to proof the concept we constructed a small RC robotic car, in the heart of it the raspberry pi 4 in which all the control is performed,The raspberry pi receives input from the pi camera only, the distance between the camera lens and the floor is 16 cm , the angle of the camera is 45 degrees , the robot power comes from a 2000mAh power bank, the raspberry pi is connected with L298N (dc motor driver) witch directly controls the dc motors, the car itself has 4 DC motors the two motors in each side are connected to one channel at the L298N driver, that is considered as differential steering . 
<p align="center">
  <img src="https://github.com/user-attachments/assets/31c3104e-09cd-459c-a700-184081e3a018" alt="the car from the front (1)" width="300"/>
  <img src="https://github.com/user-attachments/assets/e7298a66-30e7-4b96-9f62-3c98b5a1744a" alt="the car from the side" width="600" />
</p>

# The trace :

The data was collected from the trace that we build , the trace was constructed from black lines on representing the lanes on a white floor to make it easer and more distinguisable by the AI latter .
A total of 11137 labeled images were collected , the dimentions of the image are 512x256 p

# The model :

We used torchvision resnet18 model with pretraind weights , then we modefied the lengh of the output form 1000 to 4 , we devided the collected data from the trace into training (80%) and testing (20%), the model was trained using adam optimizer with learining rate of 0.001 and crossentropy loss funtion with weights since the classes where not palanced.

# The data :
https://drive.google.com/file/d/19JuQwtMUgZVSgv0RdXGyCOiej4GEcLxZ/view?usp=sharing

# The acual results :
https://www.youtube.com/watch?v=qhr-C7h5alE&t=70s
