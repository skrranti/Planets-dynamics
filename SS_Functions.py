# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 21:04:54 2023

@author: santi
"""

import numpy as np

#%%

## Define the parameters

Ms = 1.99e30 ## Kg
G = 6.67e-11 ## Nm^2/Kg^2

c = 1.496e11 ## m

t_rfactor = np.sqrt(G*Ms/c**3) 

## mass of each planet 

m = np.zeros(10)

m[0] = 0.330   #mercury
m[1] = 4.87    #venus
m[2] = 5.97    #earth
m[3] = 0.642   #mars
m[4] = 1899    #jupyter
m[5] = 568     #saturn
m[6] = 86.8    #uranus
m[7] = 102     #neptune 
m[8] = 0.0125  #pluto
m[9] = Ms*1e-24 #sun

m = m*1e24

m_ = m/Ms ## reescalated mass

## distance to the sun, we will take them as initial conditions por the coordinate x

d = np.zeros(10)

d[0] = 57.9
d[1] = 108.2
d[2] = 149.6
d[3] = 227.9
d[4] = 778.6
d[5] = 1433.5
d[6] = 2872.5
d[7] = 4495.1
d[8] = 5870.0
d[9] = 0

d = d*1e9

d_ = d/c ## distance reescalated

## orbital velocities that will be taken as initial conditions for coordinate y of velocity

ov = np.zeros(10)

ov[0] = 47.9
ov[1] = 35.0
ov[2] = 29.8
ov[3] = 24.1
ov[4] = 13.1
ov[5] = 9.7
ov[6] = 6.8
ov[7] = 5.4
ov[8] = 4.7
ov[9] = 0

ov = ov*1000

ov_ = ov/(c*t_rfactor) ## reescalated velocity



#%%

## functions that are used for the calculus

def distancia(xi,yi,xj,yj):
    f = np.sqrt( (xi-xj)**2 + (yi-yj)**2 )
    return f*f*f

def aceleracion_x(x,y,k): ## m, x and y arrays with same length
    f = 0
    for i in range(len(m_)):
        if (i!=k):
            add = -m_[i]*(x[k]-x[i])/(distancia(x[k],y[k],x[i],y[i]))
            f = f + add
    return f

def aceleracion_y(x,y,k):
    f = 0
    for i in range(len(m_)):
        if (i!=k):
            add = -m_[i]*(y[k]-y[i])/(distancia(x[k],y[k],x[i],y[i]))
            f = f + add
    return f
            


def taylor(r,v,a,dt):
    return r + dt*v + 0.5*a*dt*dt


