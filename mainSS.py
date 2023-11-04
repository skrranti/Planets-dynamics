# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 01:04:55 2023

@author: santi
"""

import numpy as np 
import SS_Functions as SS


#%% Defining the arrays

## Here we define the 2D arrays for the position, velocity and acceleration of each planet.

t_ini = 0 #ms
t_fin = 1000#ms
dt = 1e-2 #ms

t = np.arange(t_ini,t_fin+dt,dt)

x = np.zeros((len(t),10))
y = np.zeros((len(t),10))

vx = np.zeros((len(t),10))
vy = np.zeros((len(t),10))

ax = np.zeros((len(t),10))
ay = np.zeros((len(t),10))

#%% Initial conditions

x[0] = SS.d_
vy[0] = SS.ov_
## For the y and x velocity we take 0 as initial condition

periods =[[],[],[],[],[],[],[],[],[]] 
beforeperiod = np.zeros(9)

#%% Here we apply the Verlet algorithm

for i in range(10):
    ax[0][i] = SS.aceleracion_x(x[0], y[0], i)
    ay[0][i] = SS.aceleracion_y(x[0], y[0], i)
            

for i in range(len(t)-1):
    print(i)
    for j in range(10):
        x[i+1][j] = SS.taylor(x[i][j], vx[i][j], ax[i][j], dt)
        y[i+1][j] = SS.taylor(y[i][j], vy[i][j], ay[i][j], dt)
        if (y[i][j]<0) and (y[i+1][j]>=0): ## here each time a planet completes a period , we save the period time
            if (j!=9):
                periods[j].append(t[i]-beforeperiod[j])
                beforeperiod[j]=t[i]
        
    for j in range(10):
        ax[i+1][j] = SS.aceleracion_x(x[i+1], y[i+1], j)
        ay[i+1][j] = SS.aceleracion_y(x[i+1], y[i+1], j)
    
    for j in range(10):
        vx[i+1][j] = vx[i][j] + 0.5*dt*(ax[i][j] + ax[i+1][j])
        vy[i+1][j] = vy[i][j] + 0.5*dt*(ay[i][j] + ay[i+1][j])
       


#%% Here we check the period of earth is correct. Taking in account that we have to undo the reescalation. You can check the other periods are also correct.
## Maybe for the farthest planets a period is not completed in the simulation time so you have to make it larger. Also it is possible to change the time reescalation
## factor to make everything faster.


print(periods[2][0]/(t_rfactor*3600*24))





#%% Here we make an animation for the motion of the planets, plotting the position of each planet in each instant of time.



import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

fig, ax =plt.subplots()
ax.axis([-40,40,-40,40]) ## change the axis limits to a closer view of the nearest planets orbits
ax.set_aspect("equal")


p0, = ax.plot(0,1,color='gray', marker='o', label='mercury')
p1, = ax.plot(0,1,color='black', marker='o', label=' venus')
p2, = ax.plot(0,1,color='blue', marker='o', label='earth')
p3, = ax.plot(0,1,color='red', marker='o', label='mars')
p4, = ax.plot(0,1,color='brown', marker='o', label='jupyter')
p5, = ax.plot(0,1,color='purple', marker='o', label='saturn')
p6, = ax.plot(0,1,color='green', marker='o', label='uranus')
p7, = ax.plot(0,1,color='crimson', marker='o', label='neptune')
p8, = ax.plot(0,1,color='springgreen', marker='o', label='pluto')
p9, = ax.plot(0,1,color='orange', marker='o', label='sun')
# fig.set_size_inches(5,5)
ax.legend()
def animate(i):
    p0.set_data(x[i][0], y[i][0]) ## color='gray', marker='o', label='mercury')
    p1.set_data(x[i][1], y[i][1])
    p2.set_data(x[i][2], y[i][2])
    p3.set_data(x[i][3], y[i][3])
    p4.set_data(x[i][4], y[i][4])
    p5.set_data(x[i][5], y[i][5])
    p6.set_data(x[i][6], y[i][6])
    p7.set_data(x[i][7], y[i][7])
    p8.set_data(x[i][8], y[i][8])
    p9.set_data(x[i][9], y[i][9])
   
    

ani = FuncAnimation(fig, animate, frames=len(t), interval=20, repeat=False)
plt.show()

