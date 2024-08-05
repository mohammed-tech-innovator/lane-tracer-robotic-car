# Robotic Car Project

This project highlights the Raspberry Pi-based robotic car I developed as part of a larger initiative. The entire project was featured in a report by Al-Arabi TV network and won the best graduation project award.

# Lane Tracing Robotic Car :

The task of lane tracing involves controlling both the speed and the steering angle of the vehicle. Any miscalculation in these parameters can cause the car to derail. Unlike NVidia's end-to-end learning approach, which employs a simple regression model, this project adopts a different methodology:

1. **Data Collection**: A deep-learning model is trained on data collected from a human driving the robotic car. The dataset consists of images and corresponding labels.
2. **Model Training**: The collected images are used to train a deep-learning classification model.
3. **Deployment**: During deployment, the captured images are processed by the trained model, which classifies them into one of four classes:
   - Increase the speed
   - Decrease the speed
   - Increase the steering angle
   - Decrease the steering angle

This approach enables the model to mimic the driving behavior of the human pilot, effectively controlling the vehicle's speed and steering angle.

# The car :
An RC roboic car was constructed, in the heart of it the raspberry pi 4 in which all the control is performed,The raspberry pi receives input from the pi camera only, the distance between the camera lens and the floor is 16 cm , the angle of the camera is 45 degrees , the robot power comes from a 2000mAh power bank, the raspberry pi is connected with L298N (DC motor driver) witch directly controls the DC motors, the car itself has 4 DC motors the two motors in each side are connected to one channel at the L298N driver, that is considered as differential steering . 
<p align="center">
  <img src="https://github.com/user-attachments/assets/31c3104e-09cd-459c-a700-184081e3a018" alt="the car from the front (1)" width="280"/>
  <img src="https://github.com/user-attachments/assets/e7298a66-30e7-4b96-9f62-3c98b5a1744a" alt="the car from the side" width="500" />
</p>

# The track :

The data was collected from a track constructed with black lines representing lanes on a white floor, making it easier and more distinguishable for the AI. A total of 11,137 labeled images were collected, with each image having dimensions of 512x256 pixels.

# The model :

PyTorch was used to construct a deep CNN model with 4 neurons in the final layer. The collected data from the track was divided into training (80%) and testing (20%) sets. The model was trained using the Adam optimizer with a learning rate of 0.001 and a weighted cross-entropy loss function to address class imbalance.

# The data :
Please Find the dataset on this link : https://drive.google.com/file/d/19JuQwtMUgZVSgv0RdXGyCOiej4GEcLxZ/view?usp=sharing

# The acual results :
https://www.youtube.com/watch?v=qhr-C7h5alE&t=70s
