# This file provides an example problem for testing the DOT wrapper provided
# in dot.py.  The example problem contained in this file is the first
# example problem from the dot.pdf manual.
#
# Gerhard Venter
# August 21, 2019
#------------------------------------------------------------------------------
import dot as dot
import math as m
import numpy as nm


#------------------------------------------------------------------------------
# Define your own function to evaluate the objective function and constraints
# This function can be name anything, but the arguments must be as shown below.
#
# Input:  x     - The current design variable vector obtained from DOT to 
#               evaluate.  This is a numpy array of length nDvar.
#         obj   - The objective function value that will be evaluated and set 
#               here.
#         g     - The constraint vector that will be evaluated and set here.
#               This is a numpy array of length nCon.
#         param - An optional numpy array with parameter values that the user
#               can specify when setting up the DOT parameters.  These 
#               optional parameters will be passed to this evaluate function
#               unchanged by DOT.
# Return: Nothing
#------------------------------------------------------------------------------
def myEvaluate(x, obj, g, param):

    # Optional step to map the design variable array to local variables that
    # are easier to work with
    h = x[0]
    w = x[1]
    d = x[2]

    # Evaluate the objective function value and use the ".value" notation to
    # update this new value in the calling function, which is DOT in this
    # case
    obj.value = 2.0*(h*w+h*d+2.0*w*d) + 1.25*h/12.0

    # Evaluate the constraints and update the constraint vector.  Since this 
    # is a numpy object, the values will be updated in the calling function
    g[0] = 1.0 - h*w*d/2.

    return


#------------------------------------------------------------------------------
# The main code that setup the optimization problem and calls DOT to solve the
# problem
#------------------------------------------------------------------------------
nDvar = 3  # Number of design variables
nCons = 1  # Number of constraints

# Create numpy arrays for the initial values and lower and upper bounds of the
# design variables
x  = nm.empty(nDvar, float)
xl = nm.empty(nDvar, float)
xu = nm.empty(nDvar, float)

# Set the initial values and upper and lower bounds for the design variables
for i in range(nDvar):
    x[i]  = 1.0
    xl[i] = 0.001
    xu[i] = 100.00

# Initialize the DOT wrapper - this will load the shared library
aDot = dot.dot()

# Set some of the DOT parameters
aDot.nPrint   = 3
aDot.nMethod  = 2

# Set the function to call for evaluating the objective function and constraints
aDot.evaluate = myEvaluate

# Call DOT to perform the optimization
dotRet = aDot.dotcall(x, xl, xu, nCons)

# Print the DOT return values, this will be the final Objective function value,
# the worst constaint value at the optimum and the optimum design variable 
# values.  This is returned as a numpy array.
print( 'Final, optimum results from DOT:' )
print( dotRet )
