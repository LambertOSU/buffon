import math
import random
import matplotlib.pyplot as plt
import time
span = 10.0

#################################################### 
class needle:



    def __init__(self):
        self.x = random.random()*10.0
        self.y = random.random()*10.0
        self.theta = random.random()*2*math.pi
        self.length = 1.0

    def crosscheck(self):

        close_line = round(self.x)
        x_proj = math.cos(self.theta)*self.length/2

        if math.fabs(x_proj) > math.fabs(self.x - close_line):
            cross = 1
        else:
            cross = 0

        return cross


    def endpoints(self):

        x_proj = math.cos(self.theta)*self.length/2
        y_proj = math.sin(self.theta)*self.length/2
        x =  [self.x + x_proj, self.x - x_proj]
        y =  [self.y + y_proj, self.y - y_proj]
        pts = [x,y]

        return pts



#################################################### 

n = needle()

print(n.endpoints())

f, (ax) = plt.subplots(1,1, figsize = (8,8))

pts = n.endpoints()

ax.plot(pts[0],pts[1], linewidth = 1)

plt.show()


























