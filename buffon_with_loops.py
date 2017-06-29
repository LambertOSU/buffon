####################################################
# This script performs a Monte Carlo simulation
# of the Buffon's needle problem.

# https://en.wikipedia.org/wiki/Buffon's_needle

# We examine the so-called "short needle" case in 
# which the length of the needle is equal to the 
# horizontal grid spacing. An estimate for pi can
# be calculated by randomly dropping needles onto 
# a regularly spaced grid and tracking the number
# of needles which cross horizontal grid lines.  

# See the wikipedia page linked above for
# a detailed derivation.

####################################################
# Package Management
import math
import random
import matplotlib.pyplot as plt
import time
####################################################
st = time.time()
####################################################
# Initialize variables

# Counter for the number of needles which cross the grid lines.
cross = 0

# Grid span
span = 10

# Length of needle
needle_len = 1.0

# Grid spacing
grid_spc = 1.0

# Number of needles dropped in the experiment
num_drops = 100
####################################################
# Loop through number of needles (num_drops)
for num in range(num_drops):
    
    # Generate random needle drop                         
    cm_x = random.random()*span   # x-coordinate for center of needle
    cm_y = random.random()*span   # y-coordinate for center of needle
    theta = random.random()*2*math.pi     # angle in radians relative to positive x-axis
    
    # Calculate projection of the needle along x-axis
    x_proj = math.cos(theta)*needle_len/2
    y_proj = math.sin(theta)*needle_len/2

    
    # Calculate list of points representing needle ends.  This is used for plotting.
    x =  [cm_x + x_proj, cm_x - x_proj]
    y =  [cm_y + y_proj, cm_y - y_proj]
    
    # Calculate bounding lines
    closest_line = round(cm_x)

    
    # Test for crossing
    # If the length of the projecting is greater than the distance away from a
    # bounding line, then "cross" is incremented and the needle is plotted red.
    if math.fabs(x_proj) > math.fabs(cm_x - closest_line):
        cross = cross + 1
        plt.plot(x,y, c='r')
    # If not, then the needle is plotted blue.
    else:
        plt.plot(x,y, c='b')
####################################################
# Close loop

####################################################
# Calculate estimate of pi

pi_est = (2*needle_len*num_drops)/(grid_spc*cross)      

# Report estimate
print('\n After dropping %d needles, \n the estimate for pi is: %.5f',(num_drops, pi_est))

# Format and display plot
xgrid = range(span+1)
plt.vlines(xgrid,-1,span+1)
plt.show()

print("\n Runtime:",(time.time() - st)," seconds")






























