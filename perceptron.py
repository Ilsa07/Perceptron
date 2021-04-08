import numpy as np
import matplotlib.pyplot as plt



def perceptrion(x_input: list, y_input: list, number_of_inputs: int, number_of_patters: int, max_iter: int) -> type(list):
    """
    A Perceptron model that learns to respond to only one stimulus, that is linearly separable from the other data
    Input
        x_input: all the inputs to the perceptron
        y_input: the desired output pattern for the perceptron
        number_of_inputs: dimensions of the input
        number_of_patters: the number of possible patterns 
        max_iter: the maximum number of iterations the algorithm will run for
    Output
        The Error for each iteration
    """
    # Model Parameters
    b = 1                   # Threhsold
    alpha = 1               # Learning rate
    tolerance = 10**(-5)    # Tolerance for stopping

    # Initialise the weight, output and error
    w = np.zeros(number_of_inputs)
    y = 0
    error = np.zeros(max_iter)

    # Train the perceptrion
    for t in range(max_iter):
        for mu in range(number_of_patters):
            # Calculate the output, which is a binary value (True if bigger than 1, 0 if not)
            y =  np.subtract(w.dot(x_input[mu]), b)>0

            # Update the weights
            w = np.add(w, np.multiply(alpha, np.multiply(np.subtract(y_input[mu], y), x_input[mu])))

            # Save the error
            error[t] += ((y_input[mu] - y)**2)

            # If the error is sufficiently small stop training
        if error[t] <  tolerance:
            return error

    return error


# OR and XOR Gate Example
# ***********************
n = 2                                   # Dimension of inputs
p = 4                                   # Number of patterns
T = 10                                  # The maximum number of iterations
x = [[0, 0], [0, 1], [1, 0], [1, 1]]    # Inputs
y_OR_gate = [0, 1, 1, 1]                # Desired output for the OR gate
y_XOR_gate = [0, 1, 1, 0]               # Desired output for the XOR gate
error_for_OR_gate = perceptrion(x, y_OR_gate, n, p, T)
error_for_XOR_gate = perceptrion(x, y_XOR_gate, n, p, T)

# Plot The results
plt.plot(error_for_OR_gate, label='OR Error')
plt.plot(error_for_XOR_gate, label='XOR Error')
plt.xlabel('Iterations')
plt.ylabel('Error')
plt.title('Simulation Results')
leg = plt.legend()
plt.show()


# Make the Perceptrion learn a more difficult pattern
# ***************************************************
n = 100                                         # Dimension of inputs
p = 50                                          # Number of patterns
T = 50                                          # The maximum number of iterations
x_difficult =  np.random.randint(2, size=(p,n)) # Random Input Patterns
y_difficult =  np.random.randint(2, size=p)     # Random desired output

# Plot the resuls
error = perceptrion(x_difficult, y_difficult, n, p, T)
plt.plot(error)
plt.xlabel('Iterations')
plt.ylabel('Error')
plt.title('Simulation Results for More Difficult Pattern')
plt.show()