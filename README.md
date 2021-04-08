# Perceptron

### Output
The output of the perceptrion is given by the following equatoin where mu specifies a pattern, Theta is the Heavy Side Function, w is the weights, x is the inout and b is a threshod. The Heavy Side function is necessairy to produce a binary output.

![output](https://latex.codecogs.com/gif.latex?y%5E%5Cmu%20%3D%20%5CTheta%28wx%5E%5Cmu%20-b%29)

### Weight Update
The weight update is given by the following equation, where alpha is the learning rate.

![weight_update](https://latex.codecogs.com/gif.latex?%5CDelta%20w%20%3D%20%5Calpha%20x%5E%5Cmu%20%28y_t%5E%5Cmu%20-%20y%5E%5Cmu%20%29)

### Error
The error for one iteration is calculated as the sum of the squared difference between the expected output and the output of the preceptron.

![error](https://latex.codecogs.com/gif.latex?E%3D%5Csum_%5Cmu%20%28y_t%5E%5Cmu%20-y%5E%5Cmu%29%5E2)

## Getting started
1. Clone the project and create a virtual environment
2. Install the required packages in the virtual environment
   ```
   pip3 install -r requirements.txt
   ```
